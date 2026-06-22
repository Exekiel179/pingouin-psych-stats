# Pingouin Plugin Mini Benchmark

This benchmark compares two conditions in opencode:

- `baseline`: the model receives only the task, data description, and dataset path.
- `plugin_guided`: the model is instructed to use the local `$pingouin-stat` plugin guidance files.

The purpose is to estimate differences in:

- Output correctness.
- Failure rate.
- Token/cost usage from `opencode stats`.
- Statistical safety, including method choice, assumptions, and overclaiming.

## Existing Sources Used

This benchmark intentionally starts from existing public benchmark material:

- **StatLLM**: statistical analysis tasks, data descriptions, CSV datasets, and human-verified SAS solutions. Used as the main source for statistical task prompts.
- **InfiAgent DA-Agent / DAEval**: closed-form CSV data-analysis tasks with answer tags. Used for automatically scored tasks and output-format design.
- **DataSciBench**: used as a design reference for agentic data-science evaluation, error lists, cost tracking, and multi-step task reporting.

The selected task pool is created by `scripts/build_existing_task_pool.py`. It copies only selected CSV files and task metadata into `benchmark/tasks/`.

The default curated pool currently contains 49 tasks:

- 37 from StatLLM.
- 12 from InfiAgent DA-Agent / DAEval.
- Main covered families: ANOVA, t tests, correlation, regression/logistic regression, normality/data screening, descriptive statistics, and chi-square.

The pool is intentionally source-first: prompts remain close to the original benchmark wording, with only wrapper instructions added for opencode conditions.

## Setup

From the plugin root:

```powershell
python benchmark\scripts\build_existing_task_pool.py
```

Optional: inspect generated tasks:

```powershell
Get-Content benchmark\tasks\tasks.jsonl -TotalCount 3
```

## Run With opencode

Run a small smoke test:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_opencode_benchmark.ps1 -Condition both -Limit 2
```

Or via batch:

```bat
benchmark\run_benchmark.bat both 2
```

Run all selected tasks:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_opencode_benchmark.ps1 -Condition both
```

Or:

```bat
benchmark\run_benchmark.bat both
```

Run with an explicit model:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_opencode_benchmark.ps1 -Model "provider/model" -Condition both
```

## Score

```powershell
python benchmark\scripts\score_outputs.py --condition both
```

Closed-form DAEval tasks are tag-scored against existing labels when labels are present. StatLLM tasks are scored by a lightweight rubric because the original gold solutions are SAS code rather than direct Python/Pingouin answer labels.

Outputs:

- `benchmark/results/run_log.jsonl`: exit code and wall-clock time.
- `benchmark/results/scores.csv`: per-task scores and failure flags.
- `benchmark/results/summary.json`: average score and failure rate by condition.

## Token/Cost Comparison

Use opencode's own accounting:

```powershell
opencode stats
```

If you need per-run isolation, run baseline and plugin-guided conditions separately and export sessions:

```powershell
opencode session
opencode export <sessionID> > benchmark\results\<sessionID>.json
```

## Interpretation

This is a small benchmark, not a publication-grade evaluation. Treat it as a regression and usability test:

- `plugin_guided` should reduce wrong-method failures and missing assumption checks.
- `plugin_guided` may spend more prompt tokens because it reads guidance files.
- Net token efficiency should be judged by total completion attempts, failures, and revisions, not prompt size alone.
