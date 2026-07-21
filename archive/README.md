# Analysis Archive

This directory stores reproducible analysis runs created by `pingouin-psych-stats`.

Each run lives in its own timestamped folder. Use:

```bash
python scripts/init_analysis_run.py --slug my-study
```

The initializer creates `analysis.py`, `screening.json`, `results/`, `reports/`, `figures/`, `audit.md`, and `run-manifest.json`. Replace placeholders with real output as the workflow progresses. Raw participant data is not copied into the archive by default.

The archive is intentionally separate from `benchmark/outputs/`, which contains evaluation-only artifacts.
