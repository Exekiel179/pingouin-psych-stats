---
description: Review a Pingouin analysis against the S0–S5 gates before final interpretation or reporting.
model: sonnet
---

Trigger `pg-analysis-approval`. Return a gate-by-gate decision, identify the highest-risk unresolved issue, and use APPROVED, APPROVED_WITH_NOTES, REVISE, or BLOCKED. Do not rewrite the analysis silently.

After writing `audit.md`, advance the run to `approved`, `approved_with_notes`, `revise`, or `blocked` through `scripts/workflow_engine.py`; do not edit the manifest status manually.
