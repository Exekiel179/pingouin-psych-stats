---
description: Start a Pingouin analysis run, clarify the minimum design inputs, and create its archive directory.
model: sonnet
---

Start a run with `pingouin-stat` intake. Resolve the research question, outcome scale, predictors/factors, subject ID, dependency structure, data reference, planned versus exploratory status, and deliverable. Then initialize `archive/analysis-runs/<run-id>/` with `scripts/init_analysis_run.py` and advance the manifest to `intake_complete` with `scripts/workflow_engine.py advance <run> intake_complete`. Do not run an inferential test in this stage.
