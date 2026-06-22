---
name: pingouin-stat-router
description: Route psychology statistics requests to the smallest Pingouin workflow. Use when the user asks what analysis to run, gives a psychology design, asks to analyze data with Pingouin, or needs lower-token guidance before code generation.
---

# Pingouin Stat Router

Compatibility entry point. For end-to-end work, prefer `pingouin-stat`, which adds intake, approval, and deliverable planning before and after routing.

Use this skill first when the requested statistical analysis is unclear or broad.

## Load

Read only these references unless another skill requires more:

- `../../references/workflow-index.md`
- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md` only when generating concrete code.
- `../../references/apa-output-template.md` only if the user asks for report text or formatted output.

## Goal

Select the smallest downstream skill and analysis plan that fits the study design. Do not run a statistical test until the design, variables, and data shape are clear enough to avoid an obvious wrong test.

## Required Questions To Resolve

Resolve from the user's text or data before choosing the test:

- Outcome variable: continuous, ordinal, binary, count, or categorical.
- Predictors: between-subjects, within-subjects, covariates, mediators, or raters/items.
- Unit of analysis: participant, trial, item, dyad, classroom, or other cluster.
- Dependency: independent observations, repeated measures, paired samples, nested observations, or multiple raters.
- Number of levels per factor.
- Hypothesis direction: two-sided by default unless explicitly directional and preregistered.
- Planned comparisons versus exploratory post hoc tests.
- Missing-data handling.

If these cannot be inferred, ask the minimum necessary clarifying question. If a reasonable default is safe, state it explicitly.

## Routing

- Data quality, missingness, assumptions, reshape, or column inspection -> `pg-data-screening`.
- One-sample, independent, paired, Welch, or pairwise group comparisons -> `pg-mean-tests`.
- One-way/factorial ANOVA, repeated-measures ANOVA, mixed ANOVA, Welch ANOVA, ANCOVA -> `pg-anova`.
- Pearson/Spearman/Kendall, partial correlation, pairwise correlation, repeated-measures correlation -> `pg-correlations`.
- Linear regression, logistic regression, mediation -> `pg-regression-mediation`.
- Cronbach alpha, ICC, inter-rater reliability -> `pg-reliability`.
- Sample size, achieved power, detectable effect -> `pg-power`.
- APA/Chinese result prose, polished tables, result interpretation -> `pg-reporting`.

## Output Format

Return this compact block:

```markdown
Recommended: <skill> using <function(s)>.
Why: <design-to-test mapping>.
Need: <columns/data shape/missing item>.
Guardrail: <one highest-risk assumption or correction>.
Next: <code / run screening / one clarifying question>.
Audit: <S0-S5 compact gate status>.
```

## Hard Rules

- Do not invent column names; use placeholders only in code templates and mark them clearly.
- Do not claim causality from correlational or cross-sectional data.
- Do not treat Likert single items as interval without noting the assumption.
- Do not ignore repeated measures or clustering.
- Prefer `pairwise_tests`, not deprecated `pairwise_ttests`.
- Prefer `alternative="two-sided"` unless the user gives a directional hypothesis.
