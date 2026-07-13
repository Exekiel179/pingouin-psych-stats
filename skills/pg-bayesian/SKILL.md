---
name: pg-bayesian
description: Compute or generate Pingouin Bayes factors for t tests, correlations, and proportions (bayesfactor_ttest, bayesfactor_pearson, bayesfactor_binom), and read the BF10 already returned by pg.ttest and pg.corr.
---

# PG Bayesian

Use when the user wants Bayesian evidence (Bayes factors) alongside or instead of p-values, e.g. to quantify support for the null.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Decision Rules

- t test already run -> read the `BF10` column from `pg.ttest(...)`; no extra call needed.
- Correlation already run -> read `BF10` from `pg.corr(...)`.
- From a t statistic -> `pg.bayesfactor_ttest(t, nx, ny=None, paired=False)`.
- From a correlation r and n -> `pg.bayesfactor_pearson(r, n)`.
- Proportion vs a chance value -> `pg.bayesfactor_binom(k, n, p)`.

## Required Inputs

- For t: the t value, group sizes (nx, ny), paired flag, prior scale r (default 0.707).
- For pearson: r and n.
- For binom: successes k, trials n, null probability p (default 0.5).

## Code Patterns

Bayes factor from a t test (BF10 is also already in the ttest table):

```python
tt = pg.ttest(x, y, paired=False)
print({"BF10_from_table": float(tt["BF10"].iloc[0])})
bf = pg.bayesfactor_ttest(float(tt["T"].iloc[0]), nx=len(x), ny=len(y))
print({"BF10": round(float(bf), 3)})
```

Bayes factor for a correlation:

```python
bf = pg.bayesfactor_pearson(r=0.30, n=60)
print({"BF10": round(float(bf), 3)})
```

Bayes factor for a proportion:

```python
bf = pg.bayesfactor_binom(k=55, n=100, p=0.5)
print({"BF10": round(float(bf), 3)})
```

## Interpretation

BF10 > 1 favors the alternative; BF10 < 1 favors the null. Rough labels: 1-3 anecdotal, 3-10 moderate, 10-30 strong, >30 very strong. BF01 = 1 / BF10.

## Guardrails

- State the prior scale (`r`) used; the Bayes factor depends on it.
- A Bayes factor is relative evidence between two models, not the probability a hypothesis is true.
- Do not equate a Bayes factor with a p-value threshold; report it as graded evidence.
- Pair BF10 (or BF01) with the effect size and CI.
- End result-bearing answers with one compact S0-S5 audit line.
