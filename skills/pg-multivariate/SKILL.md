---
name: pg-multivariate
description: Run or generate Pingouin code for multivariate comparisons — Hotelling's T-squared test (multivariate_ttest) — plus the multivariate assumption checks box_m (equal covariance) and multivariate_normality, for designs with several dependent variables.
---

# PG Multivariate

Use when several continuous dependent variables are compared together (a mean-vector / profile question), rather than one outcome at a time.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Decision Rules

- Compare one group's mean vector to a reference (one-sample) -> `pg.multivariate_ttest(X)`.
- Compare mean vectors of two independent groups -> `pg.multivariate_ttest(X, Y)`.
- Paired multivariate comparison (same participants) -> `pg.multivariate_ttest(X, Y, paired=True)`.
- Check equal covariance matrices across groups (assumption) -> `pg.box_m(data, dvs, group)`.
- Check multivariate normality (assumption) -> `pg.multivariate_normality(X)`.

## Required Inputs

- Two or more continuous dependent variables (the outcome vector).
- Grouping column for the two-sample test and Box's M.
- Whether the comparison is one-sample, independent, or paired.
- `X`/`Y` are arrays or frames of shape (n, k); drop rows with missing DVs first.

## Code Patterns

Hotelling's T-squared, two independent groups:

```python
X = df.loc[df["group"].eq("A"), ["v1", "v2", "v3"]].to_numpy()
Y = df.loc[df["group"].eq("B"), ["v1", "v2", "v3"]].to_numpy()
res = pg.multivariate_ttest(X, Y).round(3)
pg.print_table(res)
```

One-sample (mean vector vs zero; subtract a reference first if needed):

```python
res = pg.multivariate_ttest(df[["v1", "v2", "v3"]].to_numpy()).round(3)
pg.print_table(res)
```

Assumption checks:

```python
pg.box_m(df, dvs=["v1", "v2", "v3"], group="group")           # equal covariance
pg.multivariate_normality(df[["v1", "v2", "v3"]], alpha=0.05)  # Henze-Zirkler
```

## Output Checks

`multivariate_ttest` returns index `hotelling` with `T2`, `F`, `df1`, `df2`, `pval`. `box_m` returns `Chi2`, `df`, `pval`, `equal_cov` (bool). `multivariate_normality` returns `(hz, pval, normal)`; `normal=False` warns against assuming multivariate normality.

## Guardrails

- Hotelling's T-squared needs n greater than the number of DVs and roughly multivariate-normal data; check `multivariate_normality`.
- A significant Box's M (unequal covariance) undermines the pooled test; report it.
- Pingouin covers Hotelling's T-squared, not full factorial MANOVA — for that recommend statsmodels or R.
- Report T2, F, df, p, and which assumption checks were run.
- End result-bearing answers with one compact S0-S5 audit line.
