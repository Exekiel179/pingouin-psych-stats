# Analysis Archive Contract

Use this contract for any run that generates code, tables, figures, or report prose.

## Run Directory

Create one run directory per analysis:

```text
archive/analysis-runs/<YYYYMMDD-HHMMSS>-<short-slug>/
├── analysis.py             # runnable Pingouin code, if code was generated
├── screening.json          # data shape, missingness, assumption checks
├── results/                # raw/result tables exported from Pingouin
├── reports/                # APA/Chinese/English prose and tables
├── figures/                # plotting code and rendered figures
├── audit.md                # S0–S5 approval decision and caveats
└── run-manifest.json       # metadata, input reference, versions, timestamps, state history
```

Use `scripts/init_analysis_run.py` to create the structure and manifest. The run id is the directory name and must not be reused.

## Required Recording

- Record the input path or data-frame identifier, but do not copy raw participant data by default.
- Record Python, Pingouin, and plugin versions when available.
- Keep the manifest state history; use `scripts/workflow_engine.py` for transitions instead of editing status by hand.
- Save the exact generated code before interpretation.
- Save numerical output before writing report prose.
- Save manuscript/report output with a provenance block; use `archive/templates/report-template.md` when starting from an empty report.
- Save the S0–S5 decision, unresolved issues, and approval label.
- Keep reports derived from stored output; never store invented placeholder statistics as final results.

## Naming

- Use lowercase kebab-case for run slugs.
- Use stable names within a run: `analysis.py`, `screening.json`, `audit.md`.
- Use descriptive names under `results/`, `reports/`, and `figures/`.

## Privacy and Reproducibility

The archive is a reproducibility record, not a raw-data warehouse. Do not commit identifiable data, credentials, or unrestricted exports. If a user explicitly requests raw-data archiving, confirm the destination and privacy handling first.
