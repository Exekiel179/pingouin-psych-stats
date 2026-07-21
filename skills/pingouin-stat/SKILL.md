---
name: pingouin-stat
description: "Main Pingouin statistics workflow for psychology research. Use when the user says pingouin-stat or asks to analyze psychology data with Pingouin end-to-end: first clarify research question, variables, assumptions, output format such as Word/PDF/LaTeX, table/figure requirements, then route to analysis skills, run approval checks, and organize final results."
---

# Pingouin Stat

This is the main entry point. Use it instead of asking users to choose individual sub-skills.

## Load

Read in order:

1. `../../references/intake-checklist.md`
2. `../../references/workflow-index.md`
3. `../../references/supervision-gates.md`

Read `../../references/archive-contract.md` before generating code or a deliverable that must be reproducible.
Read `../../references/workflow-contract.md` for a resumable multi-command run.
Read `../../references/pingouin-optimization.md` before generating concrete Pingouin code.

Read `../../references/pingouin-api-quickref.md` only when generating code. Read `../../references/apa-output-template.md` only when writing final prose or tables.

## Workflow

1. Intake: clarify only missing items that affect the analysis.
2. Route: choose one or more downstream skills from `workflow-index.md`.
3. Screen: use `pg-data-screening` when data shape, missingness, or assumptions are unknown.
4. Analyze: call the selected analysis workflow or generate the relevant Pingouin code.
5. Approve: run `pg-analysis-approval` before final interpretation.
6. Organize: use `pg-reporting` to produce the requested deliverable shape.
7. Archive: initialize a run under `archive/analysis-runs/`, save the exact code and numerical outputs, then write the report and S0–S5 audit record.

## Intake Contract

If key information is missing, ask a compact question set covering:

- Research hypothesis.
- Data path or available columns.
- Outcome, predictor, subject ID, covariates/mediators/raters/items.
- Between/within/repeated/nested structure.
- Planned or exploratory tests.
- Output format: Markdown, Word/docx, PDF, LaTeX, CSV tables, notebook/script.
- Figure/table requirements.
- Language and reporting standard.

If the user says "你先决定" or provides enough context, proceed with explicit assumptions.

## Routing Output

Before analysis, produce this short plan:

```markdown
Intake: <known + missing/assumed>.
Route: <skill(s)> -> <Pingouin function(s)>.
Approval gates: S0-S5 will be checked before interpretation.
Deliverable: <format/language/tables/figures>.
Next: <ask question / run screening / generate code>.
```

## Result Assembly

Final result should include only the sections that fit the user's requested format:

- Analysis plan.
- Data screening summary.
- Main statistical result.
- Follow-up comparisons.
- Figure/table code or rendered table.
- APA/Chinese prose.
- Approval findings.
- Reproducible Python code.

## Guardrails

- Do not skip approval when producing conclusions.
- Do not invent results when no data/output exists.
- Do not force Pingouin onto designs requiring mixed-effects models, SEM, count models, survival analysis, or complex survey models.
- Use short S0-S5 audit codes by default; expand only failed gates or user-requested rationale.
- Do not finish a code-generating run without saving the code, output references, and audit record under one archive run directory.
