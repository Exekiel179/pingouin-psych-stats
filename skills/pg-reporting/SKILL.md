---
name: pg-reporting
description: Convert Pingouin results into compact, polished APA-style or Chinese psychology result sections with tables, assumption notes, and uncertainty caveats.
---

# PG Reporting

Use after a Pingouin result table exists or when the user asks to beautify/statistically polish output.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/apa-output-template.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/archive-contract.md` when the result is part of an analysis run.
- `../../references/pingouin-optimization.md` when inspecting result columns or corrections.
- `../../references/report-output-contract.md` for manuscript or publication-ready output.

## Inputs

Need one of:

- Raw Pingouin result table.
- A dataframe/result object available in the workspace.
- Full numeric values from the user.

If no numeric results are available, generate a fill-in template and refuse to invent numbers.

## Workflow

1. Identify test family and output columns.
2. Verify sample size, statistic, df, p-value, effect size, CI, and correction columns.
3. Create a reader layer: finding summary and polished prose.
4. Create an evidence layer: titled APA table, assumption notes, corrections, effect sizes, and CIs.
5. Create a provenance layer: run id, source result, software versions, code path, and S0-S5 audit.
6. Add explicit limitation notes and separate them from interpretation.
7. Save the report under the active run's `reports/` directory and record its source result file.

## Output Style

For Chinese users, default to Chinese prose with English statistical symbols:

```markdown
**结果。** 独立样本 t 检验显示，A 组得分显著高于 B 组，*t*(38) = 2.41, p = .021, Cohen's d = 0.76, 95% CI [0.12, 1.38]。
```

For English:

```markdown
An independent-samples t test showed that Group A scored higher than Group B, *t*(38) = 2.41, *p* = .021, Cohen's d = 0.76, 95% CI [0.12, 1.38].
```

## Formatting Rules

- Round statistics to 2 decimals unless the user asks otherwise.
- Round p-values to 3 decimals; use `p < .001`.
- Include multiple-comparison correction when present.
- Include effect sizes and CIs when present.
- Separate statistical result from interpretation.
- Mention missing assumption checks if they were not provided.

## Guardrails

- Never convert a non-significant result into evidence of no effect without equivalence/Bayes justification.
- Never overstate clinical/practical significance from p-values alone.
- Do not infer direction from p-value; use group means or coefficients.
- If the Pingouin table lacks necessary values, ask for or compute them.
- End with one compact S0-S5 audit line unless the user requests publication-ready prose only.
- For manuscript output, use the full section contract instead of returning a chat-style paragraph alone.
