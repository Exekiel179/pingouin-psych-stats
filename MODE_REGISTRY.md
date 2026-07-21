# Pingouin Psych Stats Mode Registry

Single source of truth for the plugin's public entry points and loading boundaries.
Update this file before adding a command, changing a trigger, or changing the default workflow.

## Public Entry Points

| Entry | Mode | Trigger examples | Output |
|---|---|---|---|
| `pingouin-stat` | `full` | `pingouin-stat`, "分析这份心理学数据" | Full workflow; use sequential commands for resumable runs |
| `pg-workflow` | `orchestrate` | "运行完整 Pingouin 工作流", "继续上次分析" | Cross-platform stateful orchestration |
| `pingouin-stat-router` | `route` | `/pg-method`, "该用什么统计方法", "选择 Pingouin 分析" | Recommended skill, required inputs, one guardrail, audit status |
| `pg-data-screening` | `screen` | "先筛查数据", "检查缺失和假设" | Data shape, missingness, assumptions, reshape advice |
| `pg-reporting` | `report` | "写成 APA 结果", "把表格转成中文结果" | APA table/prose from existing output |
| `pg-analysis-approval` | `approve` | "检查分析能不能报告", "审批统计结果" | S0–S5 gate review and decision |

## Specialist Skills

These remain available for explicit routing when the design is known:

`pg-mean-tests`, `pg-anova`, `pg-correlations`, `pg-regression-mediation`,
`pg-nonparametric`, `pg-categorical`, `pg-bayesian`, `pg-multivariate`,
`pg-reliability`, and `pg-power`.

## Command Map

| Command | Dispatch |
|---|---|
| `/pg-intake` | Start run and resolve design inputs |
| `/pg-method` | `pingouin-stat-router` method selection |
| `/pg-screen` | `pg-data-screening` |
| `/pg-analyze` | Execute selected Pingouin analysis |
| `/pg-report` | `pg-reporting` |
| `/pg-approve` | `pg-analysis-approval` |
| `/pg-archive` | Finalize run artifact checklist |

## Loading Policy

- Metadata and command descriptions are public discovery surface.
- The selected `SKILL.md` is loaded only after an entry point is triggered.
- References are loaded conditionally according to the selected skill's `Load` section.
- Scripts are executed for deterministic checks or templates; do not load benchmark prompts into ordinary analysis context.
- Benchmark fixtures are evaluation-only and never evidence for a user's analysis.

## Routing Precedence

1. Explicit command or named skill wins.
2. For a new/resumable run, follow `/pg-intake` → `/pg-screen` → `/pg-analyze` → `/pg-approve` → `/pg-report` → `/pg-archive`.
3. Method-selection uncertainty routes to `pingouin-stat-router` via `/pg-method`.
4. Known design routes to the smallest specialist skill.
5. If unit, dependency, outcome scale, or required columns remain unclear, ask one compact clarification before code generation.

For resumable work, follow `references/workflow-contract.md` in order.
