# Pingouin Psych Stats：面向 AI 编程智能体的可审计心理统计工作流插件

**系统描述预印本 · v0.1.0 implementation snapshot**

## 摘要

心理学统计分析通常需要在研究设计识别、数据形态、假设检查、统计函数选择、结果解释和 APA 报告之间进行多步协调。大语言模型可以生成 Python 代码，但如果这些步骤被压缩在单一提示中，研究者难以判断方法是否适配、结果是否来自真实输出，以及报告是否遗漏效应量、置信区间或多重比较校正。本文介绍 `pingouin-psych-stats`，一个面向 Claude Code、Codex 及其他 AI 编程智能体的 Pingouin 技能插件。插件将心理统计任务拆分为 15 个专门 skill，并通过 `pingouin-stat` 与 `pingouin-stat-router` 将自然语言研究设计路由到最小的分析工作流。为支持可恢复和可复核的研究过程，插件提供 `/pg-intake`、`/pg-screen`、`/pg-analyze`、`/pg-approve`、`/pg-report` 和 `/pg-archive` 六阶段命令链；每次运行将代码、筛查结果、数值输出、报告、图表和 S0–S5 审计记录保存到独立目录。插件还针对 Pingouin 的 API 和设计特点提供版本签名检查、长宽表约束、重复测量球形性、Welch/Games-Howell、多重比较、效应量与置信区间、bootstrap seed 和 ICC/Bayes factor 报告规则。本文说明系统架构、工作流契约、监督关卡、归档设计和当前工程验证结果。当前稿件是软件系统描述；本地质量检查通过不等同于在真实研究场景中已经证明统计正确率或研究效率优势。

**关键词：**Pingouin；心理统计；大语言模型；Claude Code；Codex；可复现分析；统计工作流

## Pingouin Psych Stats: An Auditable Psychology Statistics Workflow Plugin for AI Coding Agents

### Abstract

Psychology statistics workflows require coordinated decisions about study design, data shape, assumptions, test selection, interpretation, and reporting. Large language models can generate Python code, but a single-prompt interaction makes it difficult to verify whether a method fits the design, whether reported values came from executed output, and whether effect sizes, confidence intervals, or multiplicity corrections were preserved. This paper introduces `pingouin-psych-stats`, a Pingouin skill plugin for Claude Code, Codex, and other AI coding agents. The plugin decomposes common psychology analyses into 15 focused skills and routes natural-language study designs to the smallest suitable workflow through `pingouin-stat` and `pingouin-stat-router`. A resumable six-stage command chain—`/pg-intake`, `/pg-screen`, `/pg-analyze`, `/pg-approve`, `/pg-report`, and `/pg-archive`—stores code, screening results, numerical outputs, reports, figures, and S0–S5 audit records in a dedicated run directory. Pingouin-specific guidance covers version and signature checks, long/wide data constraints, repeated-measures sphericity, Welch/Games-Howell follow-ups, multiplicity correction, effect sizes and confidence intervals, bootstrap seeds, and ICC/Bayes-factor reporting. We describe the architecture, workflow contract, supervision gates, archive design, and current engineering checks. This manuscript is a system description; passing local regression checks is not evidence of superior statistical accuracy or research productivity in real studies.

**Keywords:** Pingouin; psychology statistics; large language models; Claude Code; Codex; reproducible analysis; statistical workflow

## Implementation Snapshot

本稿对应插件 manifest 版本 `0.1.0+codex.20260622073355`，以仓库 `main` 分支当前实现为准。当前仓库包含 15 个 skill 和 7 个公开命令：6 个命令组成可恢复主流程，`/pg-method` 作为可选方法分流入口。下文的工程验证、功能描述和文件路径均以本次更新后的实现为准。

## 1 引言

心理学研究中的统计分析很少是单一函数调用。研究者需要先确定研究问题、结果变量尺度、预测变量和分析单位，再判断观测是否独立、是否存在重复测量或嵌套结构。数据进入分析后，还要处理缺失值、长宽表转换、组间不平衡、正态性、方差齐性和球形性等问题。即使统计量已经计算完成，结果报告仍需要保留效应量、置信区间、校正方式和适当的解释边界。

大语言模型为这些步骤提供了自然语言接口，但“生成可运行代码”与“生成可审计的研究分析”并不是同一个目标。模型可能选择错误的函数、忽略被试 ID、使用过时 API、把未执行的代码写成结果，或把相关性写成因果性。研究者因此需要的不只是一个代码生成器，而是一套把方法决策、数据检查、数值输出和报告交付连接起来的工作流。

`pingouin-psych-stats` 针对这一需求，将 Pingouin 的心理统计能力拆分为小型 skill，并把每次分析组织为一个有状态的 run。本文的贡献是工程化的：提供面向 AI 编程智能体的路由层、Pingouin 专项约束、S0–S5 审批关卡和文件归档契约。本文不主张插件替代统计学家、伦理审查或研究者对数据与结论的责任。

## 2 系统架构

### 2.1 插件组成

插件包含 Claude Code 与 Codex manifest、15 个 skill、references 规则库、Python scripts、命令入口和 benchmark 目录。skill 分为四层：入口与路由（`pingouin-stat`、`pingouin-stat-router`），数据与基础检验（`pg-data-screening`、`pg-mean-tests`、`pg-anova`、`pg-correlations`），扩展分析（回归/中介、非参数、分类、贝叶斯、多元、信度、效能），以及审批与报告（`pg-analysis-approval`、`pg-reporting`）。

每个 skill 的 frontmatter 只承担触发与发现功能；具体流程在 `SKILL.md` 中定义，API 速查、APA 模板、监督关卡和 Pingouin 优化规则则按需从 references 加载。这个分层减少了无关上下文进入普通分析，并把 benchmark 和测试脚本排除在用户分析上下文之外。

### 2.2 方法路由

`pingouin-stat-router` 先解析结果变量类型、因素结构、被试 ID、依赖关系、比较数量、缺失值规则和计划/探索性状态，再选择最小下游 skill。例如，两个独立组的连续结果进入 `pg-mean-tests`；重复测量的多水平因子进入 `pg-anova`；多个分类变量进入 `pg-categorical`；需要 Bayes factor 时进入 `pg-bayesian`。如果单位、依赖结构或变量列名不明确，路由器先提出最小澄清问题，而不是生成带有虚构列名的代码。

## 3 顺序工作流

### 3.1 六阶段命令链

插件将主要命令组织成可恢复的六阶段流程：

| 阶段 | 命令 | 主要产物 |
|---|---|---|
| 1. Intake | `/pg-intake` | 研究设计、数据引用和 run manifest |
| 2. Screen | `/pg-screen` | 数据形态、缺失值、组样本量、假设检查 |
| 3. Analyze | `/pg-analyze` | 可运行 `analysis.py` 与 Pingouin 数值输出 |
| 4. Approve | `/pg-approve` | S0–S5 审批决定与修订项 |
| 5. Report | `/pg-report` | APA 表格、中文/英文结果和图表 |
| 6. Archive | `/pg-archive` | 完整性检查后的可复核 run |

`/pg-method` 是可选的分流帮助，不改变六阶段状态。若审批结果为 `REVISE` 或 `BLOCKED`，流程返回分析阶段或筛查阶段；未经审批通过，不生成最终解释性报告。

### 3.2 S0–S5 监督关卡

每次结果性输出均可附带一行审计状态：

```text
Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.
```

S0 检查研究范围和分析单位；S1 检查数据列、缺失、组大小、重复 ID 和数据形态；S2 检查 Pingouin 函数签名与版本兼容；S3 检查相关假设和校正；S4 确认统计量来自实际结果对象；S5 区分统计证据与因果、临床或构念层面的主张。关卡不是自动批准机制，而是把分析中最容易被忽略的证据链显式化。

## 4 Pingouin 专项优化

### 4.1 API 与版本

插件要求在版本不确定时检查 `pingouin.__version__` 和 `inspect.signature(pg.function)`，避免依据旧版记忆生成参数。当前仓库的质量检查在 Pingouin 0.6.1 环境中运行，并优先使用 `pairwise_tests` 而不是已弃用的 `pairwise_ttests`。生成代码时保留原始结果对象，四舍五入只发生在报告层。

### 4.2 设计与假设

重复测量、混合 ANOVA、重复相关、Friedman 和 Cochran Q 等分析要求稳定的被试 ID 与适配的长表结构；重复测量 ANOVA 需要检查球形性并报告必要的校正。单因素设计中若方差不齐，工作流会考虑 Welch ANOVA 及 Games-Howell 后续比较。多重比较默认显式指定校正方式，通常使用 Holm，除非研究的预注册计划规定了其他方案。

### 4.3 结果与报告

统计报告优先保存样本量、效应量、置信区间、校正标签和原始输出列，而非只保存 p 值。中介分析记录 bootstrap 次数和 seed；ICC 报告具体模型而不是只给出最大系数；Bayes factor 报告 prior scale 并区分 BF10 与 BF01。`pg-reporting` 只有在存在真实结果表或完整数值时才生成正式结果段落，否则输出待填模板并明确缺失项。

### 4.4 适用边界

Pingouin 并不覆盖所有心理统计设计。涉及随机斜率的混合效应模型、结构方程模型、多层中介、计数模型、生存分析或复杂抽样权重时，插件会拒绝强行套用，并建议转向 statsmodels、R/lme4 或专门的结构方程工具。该拒绝路径是方法安全的一部分，而不是功能缺失的掩盖。

## 5 可复现归档

每个 run 使用时间戳和短 slug 命名，结构如下：

```text
archive/analysis-runs/<run-id>/
├── analysis.py
├── screening.json
├── results/
├── reports/
├── figures/
├── audit.md
└── run-manifest.json
```

manifest 记录输入路径或 dataframe 引用、插件和 Pingouin 版本、时间戳、状态及原始数据是否复制。默认不复制受试者数据，因此该归档是可复核记录而不是原始数据仓库。`analysis.py` 必须在解释前保存，数值输出必须先于报告文本保存，报告必须能回指到对应的结果文件。

## 6 工程验证

仓库包含函数签名、主要分析调用、路由矩阵、主入口契约、静态预算和插件表面一致性检查。当前本地环境为 Pingouin 0.6.1，14 项检查全部通过。检查覆盖 API 可用性与插件结构完整性，不是对真实心理学研究准确率的估计。

## 7 局限与未来工作

第一，当前验证以确定性回归检查和小规模合成数据为主，尚未完成跨数据集、跨模型和跨研究者的盲评。第二，S0–S5 依赖用户提供的信息和实际输出，不能替代独立统计审查。第三，归档契约能提高可追溯性，但不能修复原始数据质量或研究设计中的识别问题。第四，Pingouin 版本升级可能改变函数签名或返回列，必须重新运行兼容性检查。

未来工作包括：建立真实匿名心理学数据集上的基线对照评估；比较普通提示与插件引导在方法选择、假设检查和过度解释方面的差异；增加跨版本 API 快照；以及评估归档记录是否降低研究者的返工和复核成本。

## 8 结论

`pingouin-psych-stats` 将 Pingouin 的统计函数包装为面向 AI 编程智能体的可路由、可审批和可归档工作流。其主要设计不是让模型自动替研究者作出所有统计判断，而是把设计识别、数据筛查、版本兼容、结果来源和解释边界安排在连续的阶段中。六阶段命令链和独立 run 归档使一次分析能够暂停、复核、修订和重建，为后续的真实研究评估提供了工程基础。

## 声明

**数据可用性：**本文为软件系统描述，不使用人类受试者数据。源代码和工作流资源见 GitHub 仓库。

**伦理声明：**本文不涉及人类受试者、动物实验或个人敏感数据。

**作者贡献：**待作者依据实际贡献填写 CRediT 角色。

**利益冲突：**待作者确认。

**资金：**待作者确认；如无外部资助，应明确声明未获得专门资助。

**AI 使用声明：**投稿前应由作者核验所有技术事实、版本信息和引用，并依据目标预印本平台政策填写正式 AI 使用声明。AI 工具不应列为作者，也不替代作者对稿件内容的责任。

## 参考资料

Exekiel179. (2026). *pingouin-psych-stats* [Computer software]. GitHub. https://github.com/Exekiel179/pingouin-psych-stats

Pingouin documentation. (n.d.). *Pingouin: Statistics in Python*. https://pingouin-stats.org/

Vallat, R. (2018). Pingouin: statistics in Python. *Journal of Open Source Software, 3*(31), 1026. https://doi.org/10.21105/joss.01026
