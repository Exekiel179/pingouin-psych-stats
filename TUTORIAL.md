# Pingouin Psych Stats Tutorial

这是一份从安装到完成一次可归档心理统计分析的简明教程。

## 1. 安装

先安装 Pingouin：

```bash
pip install pingouin pandas numpy
```

在 Claude Code 中安装插件：

```text
/plugin marketplace add Exekiel179/pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

Codex 或其他智能体可以直接指向仓库目录；它们会读取 `.codex-plugin/plugin.json` 和 `skills/`。

## 2. 一键运行

Claude Code 使用：

```text
/pg-workflow
```

Codex 或其他支持 skills 的智能体使用：

```text
Use pg-workflow to analyze my psychology dataset.
```

建议同时提供：数据路径、研究问题、因变量、组别/时间变量、被试 ID、协变量和期望输出格式。

## 3. 工作流会做什么

```text
Intake → Screen → Analyze → Approve → Report → Archive
```

插件会先澄清设计，再检查数据形态和假设，选择 Pingouin 函数，保存可运行代码和数值结果，执行 S0–S5 审批，最后生成报告并归档。

## 4. 分阶段使用

需要手动控制时，按下面顺序执行：

```text
/pg-intake
/pg-screen
/pg-analyze
/pg-approve
/pg-report
/pg-archive
```

常用单项命令：

```text
/pg-method
我有三个独立组，比较抑郁得分，应该用什么检验？
```

```text
/pg-screen
请检查 data/study.csv 的缺失值、异常值、重复 ID 和长宽表结构。
```

```text
/pg-report
把当前 Pingouin 结果写成 APA 中文结果，并保留效应量和置信区间。
```

## 5. 直接调用专业 skill

当研究设计已经明确时，可以直接调用：

```text
$pg-anova
$pg-correlations
$pg-regression-mediation
$pg-reliability
$pg-power
$pg-bayesian
$pg-multivariate
$pg-nonparametric
$pg-categorical
```

不确定方法时，使用 `$pingouin-stat-router`；需要完整、可恢复流程时，使用 `$pg-workflow`。

## 6. 归档位置

每次分析保存在：

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

状态和产物由 `scripts/workflow_engine.py` 管理，不要手动修改 manifest 状态。原始受试者数据默认不会被复制到归档目录。

## 7. 运行模板和检查

打印一个 Pingouin 代码模板：

```bash
python scripts/pingouin_template.py rm-anova
```

检查插件和 Pingouin API：

```bash
python scripts/run_skill_quality_checks.py
```

当前检查包含函数签名、分析调用、路由、插件表面、状态机和静态预算检查。

## 8. 升级

Claude Code：

```text
/plugin marketplace update pingouin-stats
/plugin update pingouin-psych-stats@pingouin-stats
```

Codex 本地仓库：

```bash
cd F:/plugins/pingouin-psych-stats
git pull origin main
```

升级后重启智能体或重新开启会话。

## 9. 不适用的设计

当任务需要随机斜率混合效应模型、SEM、多层中介、计数模型、生存分析或复杂抽样权重时，插件会建议使用 statsmodels、R/lme4 或其他专门工具，而不会强行套用 Pingouin。
