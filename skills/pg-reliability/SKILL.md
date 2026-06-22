---
name: pg-reliability
description: Run or generate Pingouin code for Cronbach alpha, item-scale reliability checks, and intraclass correlation for psychological ratings.
---

# PG Reliability

Use for internal consistency and inter-rater/test-retest reliability.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Function Choice

- Internal consistency of multiple scale items -> `pg.cronbach_alpha`.
- Inter-rater, test-retest, or target-by-rater reliability -> `pg.intraclass_corr`.

## Required Inputs

- Item columns and reverse-coded item list for alpha.
- Whether items are all intended to measure one construct.
- Long-format ICC columns: target, rater, rating.
- ICC model decision: single vs average, consistency vs agreement, one-way vs two-way.

## Code Patterns

Cronbach alpha:

```python
items = df[["item1", "item2", "item3", "item4"]]
alpha, ci = pg.cronbach_alpha(data=items)
print({"alpha": round(alpha, 3), "ci95": ci})
```

Item-total screening:

```python
for col in items.columns:
    alpha_drop, ci_drop = pg.cronbach_alpha(data=items.drop(columns=col))
    print(col, round(alpha_drop, 3), ci_drop)
```

ICC:

```python
icc = pg.intraclass_corr(data=df, targets="target",
                         raters="rater", ratings="rating").round(3)
pg.print_table(icc)
```

## Reporting

- Alpha: number of items, alpha, CI, and whether any reverse coding was applied.
- ICC: exact row/type from Pingouin output, ICC value, CI, F, df, p if available, and model interpretation.

## Guardrails

- Alpha does not prove unidimensionality; mention factor structure if relevant.
- Low alpha can reflect few items, multidimensionality, poor items, or restricted range.
- Do not choose ICC row after seeing the most favorable value; pick model from design first.
- Make sure each target-rater pair is valid; duplicated ratings can corrupt ICC.
- End result-bearing answers with one compact S0-S5 audit line.
