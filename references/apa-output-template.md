# APA Output Template

Use this file for polished reporting after the analysis code has run.

## Minimal Result Block

```markdown
**Analysis.** <test name> was used to test <hypothesis>. <Design and variables>. Missing data were handled by <method>.

**Assumption checks.** <normality / homogeneity / sphericity / independence summary>. <Correction or robust alternative if needed>.

**Result.** <APA sentence with statistic, df, p, effect size, CI>.

**Interpretation.** The result suggests <plain-language finding>. This does not by itself establish <causal/clinical/generalization claim> unless the study design supports it.
```

## Formatting Rules

- Use italic statistical symbols in Markdown: `*t*`, `*F*`, `*r*`, `*p*`, `M`, `SD`.
- Round most statistics to 2 decimals and p-values to 3 decimals.
- Write `p < .001` instead of `p = .000`.
- Include exact `p` where possible.
- Include effect size: Cohen's d, Hedges g, partial eta squared, odds ratio, r, R-squared, alpha, or ICC as appropriate.
- Include confidence intervals when Pingouin returns them.
- If output is Chinese, keep statistical symbols in English and translate interpretation only.

## Chinese Style

```markdown
**分析方法。** 采用 <test name> 检验 <hypothesis>。因变量为 <dv>，自变量为 <iv>。

**结果。** 结果显示，<condition/group> 在 <dv> 上 <direction>，*t*(df) = value, p = value, Cohen's d = value, 95% CI [low, high]。

**解释。** 这说明 <plain-language interpretation>。需要注意，该结果只能支持 <statistical claim>，不能单独证明 <unsupported claim>。
```

## Table Style

Use compact Markdown tables for user-facing summaries. Put machine-readable full output in a fenced code block only when needed.

Recommended columns:

- Mean tests: comparison, statistic, df, p, adjusted p, effect size, CI, BF10, power.
- ANOVA: source, df, F, p, corrected p, partial eta squared, sphericity note.
- Correlation: variables, n, r, CI, p, BF10, power.
- Regression: predictor, coefficient, SE, statistic, p, CI, model R-squared.
- Reliability: scale or rater model, estimate, CI, F or p if available.

