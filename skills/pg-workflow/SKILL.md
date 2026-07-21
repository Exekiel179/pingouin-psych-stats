---
name: pg-workflow
description: Run and resume the stateful Pingouin psychology statistics workflow. Use when the user wants an end-to-end, auditable analysis from intake through screening, analysis, approval, reporting, and archive, or asks to continue an existing analysis run.
---

# PG Workflow

Use this skill as the cross-platform orchestration entry point. Claude Code users may use the `/pg-*` commands; Codex and other agents should invoke this skill directly.

## Load

Read these references in order:

1. `../../references/workflow-contract.md`
2. `../../references/archive-contract.md`
3. `../../references/intake-checklist.md` when starting a new run
4. `../../references/supervision-gates.md` before approval
5. `../../references/pingouin-optimization.md` before generating Pingouin code

Use `../../scripts/workflow_engine.py` for every state transition. Never edit `run-manifest.json` status by hand.

## Dispatch

1. Find the active run under `archive/analysis-runs/`, or initialize one with `scripts/init_analysis_run.py`.
2. Read the manifest status.
3. Execute only the next allowed stage from `workflow-contract.md`.
4. Save the stage artifacts before advancing the state.
5. If approval returns `REVISE`, repair and return to `analyzed`; if `BLOCKED`, stop and explain the missing decision or data.
6. Finish only after `workflow_engine.py check <run>` passes at `complete`.

## Required Handoff Block

Before each stage, return:

```markdown
Run: <run-id>
State: <current>
Next: <target state and stage>
Inputs: <files/data available>
Outputs: <files this stage will create>
Guardrail: <highest-risk issue>
```

## Hard Rules

- Do not run inferential analysis before screening artifacts exist.
- Do not report conclusions before an `approved` or `approved_with_notes` state.
- Do not claim results from code that has not produced stored numerical output.
- Do not copy raw participant data into an archive unless the user explicitly confirms the privacy handling.
- Keep the S0-S5 audit line in the final handoff.
