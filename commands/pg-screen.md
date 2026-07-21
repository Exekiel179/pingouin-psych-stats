---
description: Screen a psychology dataset for shape, missingness, outliers, and statistical assumptions before analysis.
model: sonnet
---

Trigger `pg-data-screening`. Return the data shape, missingness, relevant assumption checks, and one recommended next step. Save `screening.json`, then advance the active run to `screened` with `scripts/workflow_engine.py`. Do not select a final inferential test until the unit of analysis and dependency structure are clear.
