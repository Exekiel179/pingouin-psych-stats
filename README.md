# Pingouin Psych Stats

> A small, safety-first plugin that routes psychology-statistics requests into compact [Pingouin](https://pingouin-stats.org/) workflows — with assumption checks, correct function selection, reproducible Python, and APA-style reporting.
>
> 一个安全优先的小型插件，把心理学统计需求路由到精简的 [Pingouin](https://pingouin-stats.org/) 工作流 —— 内置假设检验、正确函数选择、可复现 Python 代码与 APA 规范报告。

**License:** MIT · **Plugin type:** Skill plugin for Claude Code, Codex & other AI agents · **Source of truth:** https://pingouin-stats.org/

## Plugin surface and loading

The plugin follows progressive disclosure so the default context stays small:

- **Public discovery:** plugin manifests, skill descriptions, and `/pg-*` commands.
- **Selected workflow:** only the triggered `SKILL.md` is loaded.
- **Conditional guidance:** intake, routing, API, APA, and S0-S5 references are loaded only when needed.
- **Execution-only resources:** scripts and benchmark fixtures are not ordinary analysis context.

The public entry points and command-to-skill mapping are maintained in [`MODE_REGISTRY.md`](MODE_REGISTRY.md). The detailed policy is in [`references/exposure-policy.md`](references/exposure-policy.md).

Available Claude Code commands:

| Command | Purpose |
| --- | --- |
| `/pg-intake` | Start a run and clarify design inputs |
| `/pg-method` | Choose the smallest valid method workflow |
| `/pg-screen` | Data screening before analysis |
| `/pg-analyze` | Execute the selected Pingouin analysis |
| `/pg-approve` | S0-S5 analysis approval |
| `/pg-report` | APA table or result prose from existing output |
| `/pg-archive` | Finalize the run archive |

For a resumable analysis, use them in this order: `/pg-intake` → `/pg-screen` → `/pg-analyze` → `/pg-approve` → `/pg-report` → `/pg-archive`. `/pg-method` is an optional method-selection helper before intake.

The sequence is enforced by `scripts/workflow_engine.py`, which validates artifact prerequisites, records state history, and captures Python/Pingouin/plugin environment metadata in each run manifest.

---

## English

### What this is

`pingouin-psych-stats` is a skill plugin for AI coding agents (Claude Code, Codex, and others), aimed at psychology researchers who analyze data with [Pingouin](https://pingouin-stats.org/). Instead of one large prompt, it is deliberately split into **small skills** so the agent loads only the workflow it actually needs. This keeps token usage low and makes the statistical supervision explicit and auditable.

The plugin emphasizes:

- **Correct function selection** — map the study design to the right test before writing code.
- **Assumption checks** — normality, homoscedasticity, sphericity, missingness, repeated/clustered structure.
- **Reproducible Python** — clean, runnable Pingouin snippets instead of ad-hoc prose.
- **Explicit uncertainty** — separate statistical evidence from causal / clinical / construct-level claims.
- **APA-style reporting** — polished tables and concise Chinese or English result text.

### Skills

| Skill | Purpose | Key Pingouin functions |
| --- | --- | --- |
| `pingouin-stat` | **Main entry point.** End-to-end: intake → routing → screening → analysis → approval → reporting. | routes to the functions below |
| `pingouin-stat-router` | Lightweight router: pick the smallest workflow and required variables. | — |
| `pg-data-screening` | Inspect data shape, missingness, assumptions, reshape. | `normality`, `homoscedasticity`, `sphericity` |
| `pg-mean-tests` | One-sample, independent, paired, Welch, and pairwise tests. | `ttest`, `pairwise_tests` |
| `pg-anova` | One-way, factorial, repeated-measures, mixed, Welch ANOVA, ANCOVA. | `anova`, `welch_anova`, `rm_anova`, `mixed_anova`, `ancova` |
| `pg-correlations` | Pearson / Spearman / Kendall, partial, repeated-measures, pairwise. | `corr`, `partial_corr`, `pairwise_corr`, `rm_corr` |
| `pg-regression-mediation` | OLS, logistic regression, mediation analysis. | `linear_regression`, `logistic_regression`, `mediation_analysis` |
| `pg-nonparametric` | Mann-Whitney, Wilcoxon, Kruskal-Wallis, Friedman, Cochran Q rank tests. | `mwu`, `wilcoxon`, `kruskal`, `friedman`, `cochran` |
| `pg-categorical` | Chi-square independence, McNemar, 2x2 crosstabs, chi-square power. | `chi2_independence`, `chi2_mcnemar`, `dichotomous_crosstab`, `power_chi2` |
| `pg-bayesian` | Bayes factors for t tests, correlations, and proportions. | `bayesfactor_ttest`, `bayesfactor_pearson`, `bayesfactor_binom` |
| `pg-multivariate` | Hotelling's T² for several DVs, with Box's M and multivariate-normality checks. | `multivariate_ttest`, `box_m`, `multivariate_normality` |
| `pg-reliability` | Internal consistency and rater reliability. | `cronbach_alpha`, `intraclass_corr` |
| `pg-power` | Sample-size, achieved-power, detectable-effect planning. | `power_ttest`, `power_anova`, `power_corr`, … |
| `pg-reporting` | APA-style tables and concise CN/EN result prose. | `print_table` + result objects |
| `pg-analysis-approval` | Review the analysis against the S0–S5 gates before final interpretation. | reviews selected functions/output |

### Supervision gates (S0–S5)

Conclusions carry a short, auditable gate line instead of repeated safety prose:

| Code | Gate | Pass condition |
| --- | --- | --- |
| **S0** | Scope | Question, outcome scale, predictors, unit of analysis, and dependency structure are known. |
| **S1** | Data | Required columns exist; missingness, group sizes, repeated IDs, and shape were checked. |
| **S2** | API | Function and signature match the installed Pingouin version; deprecated functions avoided. |
| **S3** | Assumptions | Relevant assumptions/corrections are checked or explicitly marked unavailable. |
| **S4** | Result | Statistics, df, p-values, CIs, effect sizes, and corrections come from actual output. |
| **S5** | Interpretation | Prose separates statistical evidence from causal/clinical/construct claims. |

Example audit line: `Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.`

### Repository layout

```
pingouin-psych-stats/
├── .claude-plugin/plugin.json      # Claude Code plugin manifest
├── .claude-plugin/marketplace.json # Claude Code marketplace entry (installable via /plugin)
├── .codex-plugin/plugin.json       # Codex plugin manifest (name, skills path, interface)
├── skills/                     # The 15 skills above (each a SKILL.md + agents/openai.yaml)
├── references/                 # Routing index, supervision gates, API quickref, APA template
├── scripts/                    # pingouin_template.py + skill quality checks
└── benchmark/                  # Mini benchmark comparing baseline vs. plugin-guided runs
```

> **Note:** large third-party benchmark datasets (raw `sources/` data, PDFs, `.sav`/`.xls` files, ~180MB) are **not** committed. They are excluded via `.gitignore` and regenerated locally with the benchmark build scripts. Task metadata, prompts, and scripts are tracked.

### Quick start

This is a skill plugin for AI coding agents (Claude Code, Codex, and others).

**Install in Claude Code** — straight from GitHub:

```bash
/plugin marketplace add Exekiel179/pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

To try it before pushing, run `/plugin marketplace add ./` from a local checkout of this repo, then the same install line. The 15 skills load automatically and Claude invokes them by task (or name).

**Codex / other agents** — point your agent environment at this directory so it discovers the `skills/` folder (Codex additionally reads the `.codex-plugin/plugin.json` manifest).

Then drive it with prompts such as:

- "Use `pingouin-stat-router` to choose the right analysis."
- "Run `pg-anova` for my repeated-measures design."
- "Use `pg-reporting` to write APA-style results."

For a full run, start with `pingouin-stat`; it handles intake, routing, the S0–S5 approval gates, and the final deliverable.

### Benchmark

`benchmark/` contains a small evaluation comparing two conditions in [opencode](https://opencode.ai/):

- **baseline** — the model receives only the task, data description, and dataset path.
- **plugin_guided** — the model is instructed to use this plugin's guidance files.

It estimates differences in correctness, failure rate, token/cost usage, and statistical safety (method choice, assumptions, overclaiming). See [`benchmark/BENCHMARK.md`](benchmark/BENCHMARK.md) for setup, running, and scoring. The task pool draws on existing public material (StatLLM, InfiAgent DA-Agent / DAEval, DataSciBench) — treat it as a regression and usability check, **not** a publication-grade evaluation.

### Scope and limits

Pingouin is the right tool for many psychology designs, but **not all**. The plugin will recommend a method outside Pingouin (and refuse to force a fit) when the design requires mixed-effects models, SEM, multilevel mediation, count models, survival analysis, or complex survey weights.

---

## 中文

### 这是什么

`pingouin-psych-stats` 是一个面向心理学研究者的技能插件，支持 Claude Code、Codex 等 AI 编程智能体，用于通过 [Pingouin](https://pingouin-stats.org/) 进行数据分析。它没有把所有逻辑塞进一个大提示词，而是刻意拆分成**多个小技能（skills）**，让智能体只加载当前真正需要的工作流。这样既能降低 token 消耗，也让统计监督变得显式、可审计。

插件强调：

- **正确的函数选择** —— 在写代码之前，先把研究设计映射到正确的检验方法。
- **假设检验** —— 正态性、方差齐性、球形性、缺失值、重复测量 / 嵌套结构。
- **可复现的 Python** —— 给出干净、可直接运行的 Pingouin 代码，而非含糊的文字描述。
- **显式的不确定性** —— 把统计证据与因果 / 临床 / 构念层面的主张区分开。
- **APA 规范报告** —— 输出规整的表格与简洁的中英文结果文字。

### 技能列表

| 技能 | 用途 | 主要 Pingouin 函数 |
| --- | --- | --- |
| `pingouin-stat` | **主入口。** 端到端流程：信息采集 → 路由 → 数据筛查 → 分析 → 审批 → 报告。 | 路由到下列函数 |
| `pingouin-stat-router` | 轻量路由：选出最小的工作流与所需变量。 | — |
| `pg-data-screening` | 检查数据形态、缺失值、假设，并整形。 | `normality`、`homoscedasticity`、`sphericity` |
| `pg-mean-tests` | 单样本、独立样本、配对、Welch 及两两比较。 | `ttest`、`pairwise_tests` |
| `pg-anova` | 单因素、析因、重复测量、混合、Welch ANOVA、ANCOVA。 | `anova`、`welch_anova`、`rm_anova`、`mixed_anova`、`ancova` |
| `pg-correlations` | Pearson / Spearman / Kendall、偏相关、重复测量、两两相关。 | `corr`、`partial_corr`、`pairwise_corr`、`rm_corr` |
| `pg-regression-mediation` | OLS、逻辑回归、中介分析。 | `linear_regression`、`logistic_regression`、`mediation_analysis` |
| `pg-nonparametric` | Mann-Whitney、Wilcoxon、Kruskal-Wallis、Friedman、Cochran Q 等秩检验。 | `mwu`、`wilcoxon`、`kruskal`、`friedman`、`cochran` |
| `pg-categorical` | 卡方独立性、McNemar、2x2 列联表、卡方效能。 | `chi2_independence`、`chi2_mcnemar`、`dichotomous_crosstab`、`power_chi2` |
| `pg-bayesian` | t 检验、相关、比例的贝叶斯因子。 | `bayesfactor_ttest`、`bayesfactor_pearson`、`bayesfactor_binom` |
| `pg-multivariate` | 多个因变量的 Hotelling T²，含 Box's M 与多元正态检验。 | `multivariate_ttest`、`box_m`、`multivariate_normality` |
| `pg-reliability` | 内部一致性与评分者信度。 | `cronbach_alpha`、`intraclass_corr` |
| `pg-power` | 样本量、已达成效能、可检测效应量的规划。 | `power_ttest`、`power_anova`、`power_corr` …… |
| `pg-reporting` | APA 风格表格与简洁的中英文结果文字。 | `print_table` + 结果对象 |
| `pg-analysis-approval` | 在最终解释前，按 S0–S5 关卡复核分析。 | 复核所选函数与输出 |

### 监督关卡（S0–S5）

结论会附带一行简短、可审计的关卡说明，取代反复出现的安全提示文字：

| 代码 | 关卡 | 通过条件 |
| --- | --- | --- |
| **S0** | 范围 | 研究问题、结果变量尺度、预测变量、分析单位与依赖结构均已明确。 |
| **S1** | 数据 | 所需列存在；缺失值、组样本量、重复 ID 与数据形态均已检查。 |
| **S2** | API | 函数与签名匹配已安装的 Pingouin 版本；避免使用已弃用函数。 |
| **S3** | 假设 | 相关假设 / 校正已检查，或明确标注为不可用。 |
| **S4** | 结果 | 统计量、自由度、p 值、置信区间、效应量与校正均来自真实输出。 |
| **S5** | 解释 | 文字将统计证据与因果 / 临床 / 构念层面的主张区分开。 |

示例审计行：`Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.`

### 目录结构

```
pingouin-psych-stats/
├── .claude-plugin/plugin.json      # Claude Code 插件清单
├── .claude-plugin/marketplace.json # Claude Code marketplace 条目（可用 /plugin 安装）
├── .codex-plugin/plugin.json       # Codex 插件清单（名称、技能路径、界面信息）
├── skills/                     # 上述 15 个技能（每个含 SKILL.md + agents/openai.yaml）
├── references/                 # 路由索引、监督关卡、API 速查、APA 模板
├── scripts/                    # pingouin_template.py + 技能质量检查脚本
└── benchmark/                  # 对比「无插件」与「插件引导」运行的小型基准测试
```

> **说明：** 体量较大的第三方基准数据（原始 `sources/` 数据、PDF、`.sav`/`.xls` 文件，约 180MB）**未**纳入版本库。它们通过 `.gitignore` 排除，可用基准构建脚本在本地重新生成；任务元数据、提示词与脚本则保留在版本库中。

### 快速开始

这是一个面向 AI 编程智能体（Claude Code、Codex 等）的技能插件。

**在 Claude Code 中安装** —— 直接从 GitHub 装：

```bash
/plugin marketplace add Exekiel179/pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

想在推送前先试用，可在本仓库的本地副本根目录运行 `/plugin marketplace add ./`，再执行同样的 install 命令。15 个技能会自动加载，Claude 按任务（或名称）调用它们。

**Codex / 其他智能体** —— 让你的智能体环境指向本目录，使其能发现 `skills/` 文件夹（Codex 会额外读取 `.codex-plugin/plugin.json` 清单）。

然后用如下提示词驱动它：

- "用 `pingouin-stat-router` 选择合适的分析方法。"
- "为我的重复测量设计运行 `pg-anova`。"
- "用 `pg-reporting` 写出 APA 风格的结果。"

若要完整跑一遍，从 `pingouin-stat` 开始：它会处理信息采集、路由、S0–S5 审批关卡以及最终交付物。

### 基准测试

`benchmark/` 目录包含一个在 [opencode](https://opencode.ai/) 中对比两种条件的小型评估：

- **baseline（基线）** —— 模型只拿到任务、数据描述与数据集路径。
- **plugin_guided（插件引导）** —— 指示模型使用本插件的引导文件。

它用于估计在正确性、失败率、token / 成本消耗，以及统计安全性（方法选择、假设、过度主张）上的差异。安装、运行与评分见 [`benchmark/BENCHMARK.md`](benchmark/BENCHMARK.md)。任务池基于已有公开素材（StatLLM、InfiAgent DA-Agent / DAEval、DataSciBench）—— 请将其视为回归与可用性测试，**而非**出版级评估。

### 适用范围与边界

Pingouin 适用于许多心理学设计，但**并非全部**。当设计需要混合效应模型、结构方程模型（SEM）、多层中介、计数模型、生存分析或复杂抽样权重时，插件会推荐 Pingouin 之外的方法，并拒绝强行套用。

---

## License

[MIT](LICENSE) © Local Research Tools
