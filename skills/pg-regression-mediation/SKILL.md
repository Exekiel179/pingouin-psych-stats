---
name: pg-regression-mediation
description: Run or generate Pingouin code for linear regression, binary logistic regression, and mediation analysis with reproducible reporting.
---

# PG Regression Mediation

Use for regression-style questions that Pingouin supports directly.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Function Choice

- Continuous outcome, additive linear predictors -> `pg.linear_regression`.
- Binary outcome -> `pg.logistic_regression` with `X, y`.
- Single or multiple mediator path model -> `pg.mediation_analysis`.

## Required Inputs

- Outcome variable and scale.
- Predictor list.
- Covariates and whether they are theoretical controls.
- Binary coding for logistic regression.
- Mediation paths: `x`, `m`, `y`.
- Bootstrap count and seed for mediation.

## Code Patterns

Linear regression:

```python
vars_needed = ["outcome", "x1", "x2"]
tmp = df.dropna(subset=vars_needed)
res = pg.linear_regression(tmp[["x1", "x2"]], tmp["outcome"],
                           add_intercept=True).round(3)
pg.print_table(res)
```

Logistic regression:

```python
vars_needed = ["binary_outcome", "x1", "x2"]
tmp = df.dropna(subset=vars_needed)
res = pg.logistic_regression(tmp[["x1", "x2"]], tmp["binary_outcome"],
                             remove_na=False).round(3)
pg.print_table(res)
```

Mediation:

```python
res = pg.mediation_analysis(data=df, x="x", m="mediator", y="outcome",
                            covar=["age"], n_boot=5000,
                            seed=42).round(3)
pg.print_table(res)
```

## Reporting

- Regression: report coefficient, SE, statistic, p, CI, and model R-squared/adjusted R-squared if returned.
- Logistic: report coefficient and convert to odds ratio when useful with `np.exp(coef)`.
- Mediation: report total, direct, indirect paths, bootstrap CI, seed, and bootstrap count.

## Guardrails

- Pingouin linear regression is OLS; it is not a mixed model or SEM package.
- For Pingouin 0.6.1, `logistic_regression` takes `X, y`; verify the signature before using examples from older wrappers.
- Check residual assumptions and influential cases when substantive conclusions depend on them.
- Do not present mediation as causal unless temporal order, design, and assumptions support it.
- Do not hide automatic missing-data removal; report effective n.
- Mediation bootstrap p-values vary with seed and bootstrap count.
- End result-bearing answers with one compact S0-S5 audit line.
