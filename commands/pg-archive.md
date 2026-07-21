---
description: Finalize a Pingouin analysis run by checking that code, outputs, report, and S0-S5 audit are archived together.
model: sonnet
---

Read `references/archive-contract.md`. Use `scripts/workflow_engine.py check <run>` to validate the active state, then advance `reported` to `complete`. Report missing artifacts instead of changing the manifest by hand. Never copy raw participant data automatically.
