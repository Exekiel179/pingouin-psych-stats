# Supervision Gates

Use these compact gate codes to reduce repeated safety prose while keeping statistical supervision explicit.

## Gate Codes

| Code | Gate | Pass condition |
| --- | --- | --- |
| S0 | Scope | Question, outcome scale, predictors, unit of analysis, and dependency structure are known. |
| S1 | Data | Required columns exist; missingness, group sizes, repeated IDs, and data shape were checked or requested. |
| S2 | API | Pingouin function and signature match the installed/docs version; deprecated functions are avoided. |
| S3 | Assumptions | Relevant assumptions/corrections are checked or explicitly marked unavailable. |
| S4 | Result | Statistics, df, p-values, CIs, effect sizes, and correction labels come from actual output. |
| S5 | Interpretation | Prose separates statistical evidence from causal, clinical, or construct-level claims. |

## Minimal Audit Line

Append one short audit line when reporting conclusions:

```markdown
Audit: S0 pass; S1 checked; S2 pass; S3 partial; S4 output-derived; S5 caveated.
```

## Stop Or Escalate

Stop and ask one clarifying question when S0 fails.

Run `pg-data-screening` when S1 fails and data is available.

Inspect `res.columns`, `help(pg.function)`, or `inspect.signature(pg.function)` when S2 or S4 is uncertain.

Recommend a method outside Pingouin when the design requires mixed-effects models, SEM, multilevel mediation, count models, survival models, or complex survey weights.

## Token Rule

Use gate codes in ordinary answers. Expand the rationale only when the user asks, the result is high-stakes, or a gate fails.

