---
description: Convert existing Pingouin output into APA-style tables or concise Chinese/English result prose.
model: sonnet
---

Trigger `pg-reporting`. Use actual result objects or user-provided output only. If statistics are missing, state what is unavailable instead of inventing values. Append the compact S0–S5 audit line when reporting conclusions.

Require an `approved` or `approved_with_notes` run state, save deliverables under `reports/` and `figures/`, then advance the run to `reported` with `scripts/workflow_engine.py`.
