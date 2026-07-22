# Usage Guide · 使用说明

> A skill plugin that routes psychology-statistics requests into [Pingouin](https://pingouin-stats.org/) workflows — for Claude Code, Codex, and other AI agents.
>
> 一个把心理学统计需求路由到 [Pingouin](https://pingouin-stats.org/) 工作流的技能插件，支持 Claude Code、Codex 等。

For the current step-by-step tutorial, see [`TUTORIAL.md`](TUTORIAL.md). The canonical one-click entry is `/pg-workflow` in Claude Code or `$pg-workflow` in Codex.

---

## English

### 1. Install

**Option A — Remote (from GitHub, recommended)**

```
/plugin marketplace add Exekiel179/pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

**Option B — Local (from a cloned / downloaded copy)**

```
git clone https://github.com/Exekiel179/pingouin-psych-stats.git
```

Then, in Claude Code, add the local folder as a marketplace and install:

```
/plugin marketplace add ./pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

`/plugin marketplace add` also accepts an absolute path (e.g. `F:/plugins/pingouin-psych-stats`). Use the local method when you want to try local edits before pushing.

**Codex / other agents**: point your agent environment at the repo directory — Codex reads `.codex-plugin/plugin.json`; other agents read the `SKILL.md` files under `skills/`.

**Prerequisite**: Pingouin installed in the Python you run analyses with — `pip install pingouin`.

### 2. Two ways to use

- **Just describe the task** (easiest) — the plugin auto-routes: *"I have pre/post anxiety scores from the same participants — which test?"*
- **Name the main entry** `pingouin-stat` — end-to-end (intake → route → screen → analyze → approve → report): *"Use pingouin-stat to analyze this dataset."*

### 3. Scenario map

| You want to… | Just say |
| --- | --- |
| Full analysis / not sure where to start | "Use pingouin-stat to analyze" |
| Screen data (missing, outliers, assumptions) | "Screen the data first" |
| Two-group / paired mean comparison | "Compare groups A and B" |
| 3+ groups / repeated-measures ANOVA | "Run a repeated-measures ANOVA" |
| Assumptions fail → non-parametric | "It's non-normal, use a rank test" |
| Categorical / chi-square | "Is therapy type linked to relapse?" |
| Correlation / partial correlation | "Stress vs sleep, controlling age" |
| Regression / logistic / mediation | "Predict dropout from motivation" |
| Several DVs together (Hotelling) | "Compare two groups on three subscales" |
| Reliability α / ICC | "Cronbach's alpha for this scale" |
| Power / sample size | "N for r = .30 at 80% power" |
| Bayes factor | "Give me the Bayes factor" |
| Write results | "Write this as APA prose" |

### 4. What you get

Reproducible Pingouin code, assumption checks, effect sizes and CIs (not just p-values), and a one-line **S0–S5 audit** on conclusions, e.g. `Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.`

### 5. Where it won't force a fit

For designs needing mixed-effects models, SEM, multilevel mediation, count models, survival analysis, or full factorial MANOVA, it says Pingouin isn't the right tool and points you to statsmodels / R (lme4) instead.

### 6. Local dev / tests

```
python scripts/run_skill_quality_checks.py     # run quality checks (15 checks)
python scripts/pingouin_template.py anova       # print a code template for one analysis
```

---

## 中文

### 1. 安装

**方式 A —— 远程安装（从 GitHub，推荐）**

```
/plugin marketplace add Exekiel179/pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

**方式 B —— 本地安装（从克隆 / 下载的副本）**

```
git clone https://github.com/Exekiel179/pingouin-psych-stats.git
```

然后在 Claude Code 里，把本地文件夹当作 marketplace 加进来再安装：

```
/plugin marketplace add ./pingouin-psych-stats
/plugin install pingouin-psych-stats@pingouin-stats
```

`/plugin marketplace add` 也接受绝对路径（如 `F:/plugins/pingouin-psych-stats`）。想在推送前试用本地改动时用这种方式。

**Codex / 其他智能体**：把智能体环境指向本仓库目录即可 —— Codex 读 `.codex-plugin/plugin.json`，其他读 `skills/` 里的 `SKILL.md`。

**前置**：跑分析的 Python 环境需装 Pingouin —— `pip install pingouin`。

### 2. 两种用法

- **直接说需求**（最省事）—— 插件自动路由：*"我有同一批被试的前后测焦虑分数，该用什么检验？"*
- **点名主入口** `pingouin-stat` —— 端到端跑（采集 → 路由 → 筛查 → 分析 → 审批 → 报告）：*"用 pingouin-stat 帮我完整分析这份数据。"*

### 3. 场景对照

| 你要做的 | 说一句就行 |
| --- | --- |
| 完整分析 / 不知从哪开始 | "用 pingouin-stat 分析" |
| 查数据（缺失、离群、假设） | "先筛查一下数据" |
| 两组 / 配对比较均值 | "比较 A、B 两组的分数" |
| 三组以上 / 重复测量 ANOVA | "做重复测量方差分析" |
| 假设不满足 → 非参数 | "数据不正态，用非参数检验" |
| 分类变量 / 卡方 | "看治疗方式和复发是否相关" |
| 相关 / 偏相关 | "控制年龄后，压力和睡眠的相关" |
| 回归 / 逻辑回归 / 中介 | "用动机预测是否退出" |
| 多个因变量一起比（Hotelling） | "两组在三个子量表上一起比" |
| 信度 α / ICC | "算这个量表的克伦巴赫 α" |
| 效能 / 样本量 | "r=.30、80% 效能要多少人" |
| 贝叶斯因子 | "给我这个差异的贝叶斯因子" |
| 写结果 | "把这个表写成 APA 中文结果" |

### 4. 你会得到什么

可复现的 Pingouin 代码、假设检查、效应量与置信区间（不只 p 值），以及结论末尾一行 **S0–S5 审计**，例如 `Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.`

### 5. 它不会硬来

当设计需要**混合效应模型、SEM、多层中介、计数模型、生存分析、完整析因 MANOVA**时，插件会明说 Pingouin 不适合，并建议改用 statsmodels / R（lme4）等，而不是强行套用。

### 6. 本地改代码 / 跑测试

```
python scripts/run_skill_quality_checks.py     # 跑质量检查（15 项）
python scripts/pingouin_template.py anova       # 打印某分析的代码模板
```
