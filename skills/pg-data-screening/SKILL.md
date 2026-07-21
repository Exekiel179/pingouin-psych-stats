---
name: pg-data-screening
description: "Screen psychology datasets before Pingouin analysis: variable types, missingness, duplicates, long/wide shape, assumption checks, and safer preprocessing."
---

# PG Data Screening

Use before analysis when data has not been inspected in the current thread, or when a test fails because of missing values, shape, categories, or assumptions.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/pingouin-optimization.md`
- `../../references/archive-contract.md` when running inside an archive.

## Workflow

1. Inspect data columns, dtypes, sample size, missingness, duplicates, and group sizes.
2. Confirm long versus wide format for the target analysis.
3. Confirm repeated-measures identifiers are unique enough for the design.
4. Run only relevant assumption checks.
5. Produce a short analysis-readiness summary and minimal corrective code.

## Standard Code Skeleton

```python
import pandas as pd
import pingouin as pg

df = pd.read_csv("data.csv")
print(df.info())
print(df.describe(include="all"))
print(df.isna().mean().sort_values(ascending=False).head(20))
print(df.duplicated().sum())
```

For group balance:

```python
print(df.groupby("group", dropna=False).size())
```

For normality by group:

```python
pg.normality(data=df, dv="score", group="group")
```

For homogeneity:

```python
pg.homoscedasticity(data=df, dv="score", group="group")
```

For repeated-measures sphericity:

```python
pg.sphericity(data=df, dv="score", within="condition", subject="id")
```

For robust outliers (MAD-median rule) and a normality Q-Q plot:

```python
mask = pg.madmedianrule(df["score"].to_numpy())   # True = flagged outlier
print({"n_outliers": int(mask.sum())})

import matplotlib.pyplot as plt                    # qqplot needs matplotlib
pg.qqplot(df["score"], dist="norm")
plt.savefig("qqplot.png", dpi=150, bbox_inches="tight")
```

## Reporting

Report:

- Number of rows and unique participants.
- Missingness by required variable.
- Any impossible values or suspicious categories.
- Whether the data shape matches the intended Pingouin function.
- Assumption diagnostics and practical implication.
- Exact rows removed if listwise deletion is used.

## Guardrails

- Assumption tests are diagnostic; do not mechanically switch tests solely from a significant normality test in a large sample.
- If repeated measures exist, never analyze rows as independent.
- If IDs repeat unexpectedly within a condition, stop and flag the design/data issue.
- If transformations or exclusions are proposed, state whether they were planned or post hoc.
- Flag outliers with a rule chosen in advance (e.g. MAD-median); never delete points silently.
- End with a compact audit line using S0-S5 gate codes.
