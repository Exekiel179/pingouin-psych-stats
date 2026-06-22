---
name: pg-correlations
description: Run or generate Pingouin code for Pearson, Spearman, Kendall, partial, repeated-measures, distance, and pairwise correlations with APA-style reporting.
---

# PG Correlations

Use for association analyses between continuous or ordinal variables.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Function Choice

- Two continuous variables, linear association -> `pg.corr(..., method="pearson")`.
- Ordinal or monotonic/non-normal association -> `method="spearman"` or `method="kendall"`.
- Association controlling covariates -> `pg.partial_corr`.
- Many variables -> `pg.pairwise_corr` with `padjust`.
- Repeated observations per participant -> `pg.rm_corr`.
- Nonlinear dependence screening -> `pg.distance_corr` if appropriate.

## Required Inputs

- Variables to correlate.
- Whether observations are independent.
- Covariates, if partial correlation is requested.
- Multiple-comparison family and correction.
- Hypothesis direction; default to two-sided.

## Code Patterns

Basic correlation:

```python
res = pg.corr(x=df["x"], y=df["y"], method="pearson",
              alternative="two-sided").round(3)
pg.print_table(res)
```

Partial correlation:

```python
res = pg.partial_corr(data=df, x="x", y="y",
                      covar=["age", "baseline"],
                      method="pearson").round(3)
```

Pairwise correlations:

```python
res = pg.pairwise_corr(data=df, columns=["x", "y", "z"],
                       method="spearman", padjust="holm").round(3)
```

Repeated-measures correlation:

```python
res = pg.rm_corr(data=df, x="x", y="y", subject="id").round(3)
```

## Reporting

Report `n`, `r`, CI, p-value, Bayes factor if returned, and method. Include a scatterplot recommendation when interpretation depends on linearity or outliers.

## Guardrails

- Correlation is not causation.
- Do not use ordinary `pg.corr` when observations repeat within participants.
- If outliers drive the effect, report sensitivity analysis or robust alternative.
- If many correlations are explored, use and report p-value adjustment.
- Do not interpret partial correlation as causal control.
- End result-bearing answers with one compact S0-S5 audit line.
