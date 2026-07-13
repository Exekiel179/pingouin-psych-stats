# Pingouin API Quick Reference

Use this reference only after a skill has selected an analysis family. Keep generated code compact and verify against `help(pg.function)` or `inspect.signature(pg.function)` if Pingouin is installed and a signature is uncertain.

## Imports And Options

```python
import numpy as np
import pandas as pd
import pingouin as pg

pd.set_option("display.max_columns", 120)
pd.set_option("display.width", 160)
```

Preferred output pattern:

```python
res = pg.some_function(...).round(3)
pg.print_table(res)
```

## Data Shape

- Most formula-like Pingouin functions expect a pandas `DataFrame`.
- `anova`, `rm_anova`, `mixed_anova`, `pairwise_tests`, `ancova`, `intraclass_corr`, and `mediation_analysis` are easiest in long format.
- Repeated-measures analyses need a stable subject identifier.
- `cronbach_alpha` usually uses wide item columns, one row per participant.
- For paired data, listwise deletion is typical; report how missing values were handled.

## Mean Tests

```python
pg.ttest(x, y, paired=False, alternative="two-sided", correction="auto", confidence=0.95)
pg.pairwise_tests(data=df, dv="score", between="group", within=None, subject=None,
                  parametric=True, padjust="holm", effsize="hedges")
```

Notes:

- Use `alternative`: `two-sided`, `greater`, or `less`; do not use old `tail`.
- Use `pairwise_tests`, not deprecated `pairwise_ttests`.
- For unequal independent groups, Welch correction is safer; Pingouin can use `correction="auto"` in `ttest`.
- Common output columns include `T`, `dof`, `p-val`, `CI95%`, `cohen-d`, `BF10`, `power`, plus pairwise columns such as `A`, `B`, `Paired`, `Parametric`, `p-corr`, `p-adjust`, and effect-size columns.

## ANOVA

```python
pg.anova(data=df, dv="score", between="group", detailed=True)
pg.welch_anova(data=df, dv="score", between="group")
pg.rm_anova(data=df, dv="score", within="condition", subject="id", detailed=True)
pg.mixed_anova(data=df, dv="score", within="time", between="group", subject="id")
pg.ancova(data=df, dv="score", between="group", covar="baseline")
```

Notes:

- Use `detailed=True` for richer ANOVA tables where available.
- For repeated-measures designs, check sphericity before interpreting uncorrected p-values.
- Typical columns include `Source`, `SS`, `DF`, `MS`, `F`, `p-unc`, `np2`, and sometimes sphericity-related columns such as `eps`, `p-GG-corr`, `W-spher`, `p-spher`, `sphericity`.
- Follow significant omnibus tests with planned or corrected pairwise comparisons using `pg.pairwise_tests`.
- After a Welch ANOVA, use `pg.pairwise_gameshowell`; after a standard ANOVA, `pg.pairwise_tukey` is an option.

## Non-parametric

```python
pg.mwu(x, y, alternative="two-sided")                          # 2 independent groups
pg.wilcoxon(x, y, alternative="two-sided")                     # paired / signed-rank
pg.kruskal(data=df, dv="score", between="group")               # k independent groups
pg.friedman(data=df, dv="score", within="cond", subject="id")  # k repeated conditions
pg.cochran(data=df, dv="passed", within="cond", subject="id")  # binary repeated
```

Notes:

- `mwu`/`wilcoxon` return `U_val`/`W_val`, `p_val`, `RBC` (rank-biserial), `CLES`.
- `kruskal` returns `H`, `p_unc`; `friedman` returns Kendall `W`, `Q`, `p_unc`; `cochran` returns `Q`, `p_unc`.
- Follow a significant omnibus with `pg.pairwise_tests(..., parametric=False, padjust="holm")`.

## Assumption Checks

```python
pg.normality(data=df, dv="score", group="group")
pg.homoscedasticity(data=df, dv="score", group="group")
pg.sphericity(data=df, dv="score", within="condition", subject="id")
pg.madmedianrule(df["score"].to_numpy())          # robust outlier mask (True = outlier)
pg.qqplot(df["score"], dist="norm")               # normality Q-Q plot (needs matplotlib)
```

Use assumption checks as diagnostics, not mechanical pass/fail gates. For large samples, small deviations can be significant.

## Multivariate

```python
pg.multivariate_ttest(X, Y=None, paired=False)       # Hotelling's T-squared; X, Y are (n, k)
pg.box_m(df, dvs=["v1", "v2", "v3"], group="group")   # equality of covariance matrices
pg.multivariate_normality(df[["v1", "v2", "v3"]], alpha=0.05)   # Henze-Zirkler
```

Notes:

- `multivariate_ttest` returns index `hotelling` with `T2`, `F`, `df1`, `df2`, `pval`.
- `box_m` returns `Chi2`, `df`, `pval`, `equal_cov`; `multivariate_normality` returns `(hz, pval, normal)`.
- Needs n greater than the number of DVs; Pingouin does not cover full factorial MANOVA.

## Correlations

```python
pg.corr(x=df["x"], y=df["y"], method="pearson", alternative="two-sided")
pg.partial_corr(data=df, x="x", y="y", covar=["age", "baseline"], method="pearson")
pg.pairwise_corr(data=df, columns=["x", "y", "z"], method="spearman", padjust="holm")
pg.rm_corr(data=df, x="x", y="y", subject="id")
pg.distance_corr(df["x"], df["y"])   # nonlinear dependence screening (0 = independent)
```

Common output columns include `n`, `r`, `CI95%`, `p-val`, `BF10`, and `power`.

## Categorical / Contingency

```python
expected, observed, stats = pg.chi2_independence(data=df, x="group", y="response")
observed2, mcnemar = pg.chi2_mcnemar(data=df, x="before", y="after")   # paired 0/1
ct = pg.dichotomous_crosstab(data=df, x="cond_a", y="cond_b")
pg.power_chi2(dof=1, w=0.3, n=100, alpha=0.05)                          # n=None to solve n
```

Notes:

- `chi2_independence` returns `(expected, observed, stats)`; read the `pearson` row of `stats` (`chi2`, `dof`, `pval`, `cramer`, `power`).
- `chi2_mcnemar` needs paired dichotomous columns; returns `(observed, stats)` with `chi2`, `dof`, `p_approx`, `p_exact`.
- Report Cramér's V (effect size) and the contingency table, not only the p-value.

## Regression And Mediation

```python
X = df[["x1", "x2"]]
y = df["outcome"]
pg.linear_regression(X, y, add_intercept=True)

pg.logistic_regression(df[["x1", "x2"]], df["binary_outcome"], remove_na=True)

pg.mediation_analysis(data=df, x="x", m="mediator", y="outcome",
                      covar=["age"], seed=42, n_boot=5000)
```

For Pingouin 0.6.1, `logistic_regression` uses `X, y`, not `data/dv/pred_vars`.
Mediation bootstrap p-values and intervals depend on seed and number of bootstraps; report both.

## Reliability

```python
pg.cronbach_alpha(data=df_items)
pg.intraclass_corr(data=df, targets="target", raters="rater", ratings="rating")
```

For ICC, report the exact ICC type and whether the design is one-way/two-way, single/average, consistency/agreement.

## Bayesian

```python
tt = pg.ttest(x, y); tt["BF10"]                      # BF10 already in ttest / corr output
pg.bayesfactor_ttest(t, nx, ny=None, paired=False, r=0.707)
pg.bayesfactor_pearson(r=0.30, n=60)
pg.bayesfactor_binom(k=55, n=100, p=0.5)
```

Notes:

- BF10 > 1 favors the alternative, < 1 favors the null; BF01 = 1 / BF10.
- State the prior scale `r`; the Bayes factor depends on it.

## Power

```python
pg.power_ttest(d=0.5, n=None, power=0.8, alpha=0.05, contrast="two-samples")
pg.power_ttest2n(nx=30, ny=35, d=0.5, alpha=0.05)
pg.power_anova(eta_squared=0.06, k=3, n=None, power=0.8, alpha=0.05)
pg.power_rm_anova(eta_squared=0.06, m=3, n=None, power=0.8, alpha=0.05)
pg.power_corr(r=0.3, n=None, power=0.8, alpha=0.05)
```

Exactly one of sample size, power, alpha, or effect size is usually solved by setting it to `None`.

## Reporting Guardrails

- Never invent significance, sample size, degrees of freedom, or confidence intervals.
- If a required column is absent, say so and inspect `res.columns`.
- Always state whether tests were planned or post hoc.
- Always state multiple-comparison correction for families of tests.
- Prefer effect sizes and confidence intervals over p-values alone.
- For psychological interpretation, distinguish statistical result from construct-level inference.
