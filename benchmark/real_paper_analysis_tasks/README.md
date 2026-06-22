# Real-Paper Psychology Analysis Tasks

This dataset contains 50 full-chain psychology benchmark tasks built from real paper candidates.

The task is not only "run a statistical test." Each item asks the model to reconstruct:

1. research question
2. article hypotheses
3. experimental design
4. variable mapping and analysis route
5. Pingouin-compatible analysis or justified out-of-scope note
6. result interpretation and limitations

## Files

- `tasks.jsonl`: machine-readable task metadata.
- `TASKS.md`: human-readable inventory.
- `tasks/<task_id>/task.md`: full task specification.
- `tasks/<task_id>/context.md`: benchmark context and anti-hallucination rule.
- `tasks/<task_id>/gold_rubric.md`: scoring rubric.
- `prompts/baseline/*.md`: baseline prompts.
- `prompts/plugin_guided/*.md`: prompts requiring `$pingouin-stat` and `$pg-analysis-approval`.

## Task Status

- `ready_for_source_linked_run`: data/script availability is verified by source table or repository evidence; can be used for source-linked benchmark runs.
- `needs_result_freezing`: data/script evidence exists but the exact target result/table/figure still needs to be frozen before strict numeric scoring.
- `needs_file_verification`: promising paper/data candidate, but file-level data and script evidence must be checked before formal scoring.

## Run

Smoke test two tasks:

```powershell
benchmark\run_real_paper_benchmark.bat both 2
```

Run plugin-guided only:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_real_paper_benchmark.ps1 -Condition plugin_guided -Limit 5
python benchmark\scripts\score_real_paper_outputs.py --condition plugin_guided
```

Run all:

```powershell
benchmark\run_real_paper_benchmark.bat both
```

## Interpretation

The automatic scorer is a lightweight coverage rubric. It checks whether the answer includes source verification, research question/hypotheses, design reconstruction, variable mapping, method/assumption reasoning, code or reproduction plan, and interpretation/limitations.

It is not a substitute for human scoring. For publication-grade evaluation, freeze a target result for each task and create numeric gold labels.
