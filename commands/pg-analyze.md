---
description: Execute the selected Pingouin analysis for the active run after intake and screening.
model: sonnet
---

Continue the active run at the analysis stage through the `pingouin-stat` workflow. Read `references/workflow-contract.md`, load the selected specialist skill, save the exact runnable code to `analysis.py`, and save raw numerical outputs under `results/`. If intake or screening artifacts are missing, route back to `/pg-intake` or `/pg-screen` instead of silently proceeding.
