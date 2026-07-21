# Sequential Workflow Contract

The primary user workflow is a stateful sequence. Commands operate on one active run directory under `archive/analysis-runs/`.

The executable state machine is `scripts/workflow_engine.py`. A command must advance the manifest through that engine after its required artifacts are present.

| Stage | Command | Reads | Must produce | Next |
|---|---|---|---|---|
| 1 Intake | `/pg-intake` | User design and data reference | `run-manifest.json` with `status=intake_complete` | `/pg-screen` |
| 2 Screen | `/pg-screen` | Data and manifest | `screening.json` with shape, missingness, assumptions | `/pg-analyze` |
| 3 Analyze | `/pg-analyze` | Screening and design | `analysis.py`, raw result tables under `results/` | `/pg-approve` |
| 4 Approve | `/pg-approve` | Code, screening, results | `audit.md` with APPROVED/APPROVED_WITH_NOTES/REVISE/BLOCKED | `/pg-report` only if approved |
| 5 Report | `/pg-report` | Approved results and audit | Tables/prose under `reports/`, figures under `figures/` | `/pg-archive` |
| 6 Archive | `/pg-archive` | Entire run directory | Complete manifest and artifact checklist | complete |

## Continuation Rules

- If no active run exists, start `/pg-intake`.
- `/pg-method` is an auxiliary router; it may be used before `/pg-intake` but is not a replacement for intake.
- A failed approval returns to `/pg-analyze`; do not write final reporting prose while status is `REVISE` or `BLOCKED`.
- A report may be generated only from stored numerical output, not from an unexecuted code sketch.
- `blocked` is terminal until a user starts a new run; `revise` is the only repair path back to `analyzed`.
