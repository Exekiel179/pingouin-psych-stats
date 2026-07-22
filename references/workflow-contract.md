# Sequential Workflow Contract

The primary user workflow is a stateful sequence. Commands operate on one active run directory under `archive/analysis-runs/`.

The executable state machine is `scripts/workflow_engine.py`. A command must advance the manifest through that engine after its required artifacts are present.

| Stage | Command | Reads | Must produce | Next |
|---|---|---|---|---|
| 1 Intake | internal stage | User design and data reference | `run-manifest.json` with `status=intake_complete` | screen |
| 2 Screen | internal stage | Data and manifest | `screening.json` with shape, missingness, assumptions | analyze |
| 3 Analyze | internal stage | Screening and design | `analysis.py`, raw result tables under `results/` | approve |
| 4 Approve | internal stage | Code, screening, results | `audit.md` with APPROVED/APPROVED_WITH_NOTES/REVISE/BLOCKED | report only if approved |
| 5 Report | `/pg-report` or internal stage | Approved results and audit | Tables/prose under `reports/`, figures under `figures/` | archive |
| 6 Archive | internal stage | Entire run directory | Complete manifest and artifact checklist | complete |

## Continuation Rules

- If no active run exists, invoke `/pg-workflow`.
- `/pg-method` is an auxiliary router; it may be used before `/pg-workflow`.
- A failed approval returns to the internal analyze stage; do not write final reporting prose while status is `REVISE` or `BLOCKED`.
- A report may be generated only from stored numerical output, not from an unexecuted code sketch.
- `blocked` is terminal until a user starts a new run; `revise` is the only repair path back to `analyzed`.
