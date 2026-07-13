---
name: pg-categorical
description: Run or generate Pingouin code for categorical / contingency-table analyses — chi-square test of independence, McNemar's paired test, 2x2 crosstabs, and chi-square power — for psychology data with nominal variables.
---

# PG Categorical

Use when both variables are categorical (nominal) and the question is association or change in proportions.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Decision Rules

- Association between two independent categorical variables (any R x C) -> `pg.chi2_independence(data, x, y)`.
- Change in a binary outcome for the same participants (paired 2x2) -> `pg.chi2_mcnemar(data, x, y)`.
- Just the 2x2 table from two binary columns -> `pg.dichotomous_crosstab(data, x, y)`.
- Sample size / power for a chi-square test -> `pg.power_chi2(dof, w, n, power, alpha)`.

## Required Inputs

- Two categorical columns (row and column variables).
- Whether observations are independent (chi-square) or paired within participants (McNemar).
- For McNemar/crosstab: columns must be dichotomous (0/1 or two levels).
- For power: effect size `w` (Cohen), degrees of freedom, and the unknown to solve (set to `None`).

## Code Patterns

Chi-square test of independence (returns a 3-tuple):

```python
expected, observed, stats = pg.chi2_independence(data=df, x="group", y="response")
pg.print_table(stats.round(3))          # read the "pearson" row
```

McNemar paired test (binary 0/1 columns; returns observed table + stats):

```python
observed, stats = pg.chi2_mcnemar(data=df, x="before", y="after")
pg.print_table(stats.round(3))
```

2x2 crosstab:

```python
ct = pg.dichotomous_crosstab(data=df, x="cond_a", y="cond_b")
print(ct)
```

Chi-square power / sample size:

```python
power = pg.power_chi2(dof=1, w=0.3, n=100, alpha=0.05)   # solve n via n=None, power=0.8
print({"power": round(float(power), 3)})
```

## Output Checks

`chi2_independence` stats rows include `pearson`; columns are `test`, `lambda`, `chi2`, `dof`, `pval`, `cramer` (effect size), `power`. Report Cramér's V, not just chi-square. `chi2_mcnemar` stats give `chi2`, `dof`, `p_approx`, `p_exact`; prefer `p_exact` for small discordant counts.

## Guardrails

- Chi-square needs adequate expected counts; if many cells < 5, note it and consider Fisher's exact (outside Pingouin).
- McNemar requires paired dichotomous data, not two independent groups.
- Report the contingency table and Cramér's V / effect size, not only the p-value.
- Chi-square shows association, not causation or direction.
- End result-bearing answers with one compact S0-S5 audit line.
