---
name: pg-analysis-approval
description: "Review and approve Pingouin psychology analyses before final reporting. Use after data screening or statistical output and before interpretation to catch common problems: wrong test, ignored repeated measures, missing assumption checks, multiple-comparison errors, unsupported causal claims, incomplete reporting, or output-format mismatches."
---

# PG Analysis Approval

Use as the final statistical checkpoint before writing conclusions or deliverables.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/workflow-index.md`
- `../../references/apa-output-template.md` if checking report prose.

Read `../../references/pingouin-api-quickref.md` only if an API/function choice is questionable.

## Inputs

Review whatever is available:

- User request and research question.
- Dataset screening summary.
- Pingouin code.
- Pingouin result tables.
- Draft interpretation/report.
- Requested output format and figure/table requirements.

## Approval Checklist

Check:

- S0 Scope: design, outcome scale, unit of analysis, dependency structure.
- S1 Data: columns, missingness, group sizes, repeated IDs, long/wide shape.
- S2 API: current Pingouin function signature, no deprecated function, correct parameters.
- S3 Assumptions: normality/homogeneity/sphericity/linearity/independence as relevant.
- S4 Result: values come from output; df, p, CI, effect size, correction are present when needed.
- S5 Interpretation: no unsupported causal, clinical, or construct-level overclaim.
- Deliverable: requested format, language, tables, figures, and reproducibility needs are addressed.

## Decision Labels

Use one label:

- `APPROVED`: ready to report.
- `APPROVED_WITH_NOTES`: acceptable but caveats must be included.
- `REVISE`: fixable issue before reporting.
- `BLOCKED`: missing data/design information or wrong model family.

## Output Format

```markdown
Decision: <APPROVED / APPROVED_WITH_NOTES / REVISE / BLOCKED>
Critical issues: <none or concise list>
Required fixes: <none or exact actions>
Reporting notes: <effect size, CI, correction, caveat, format>
Audit: S0 <status>; S1 <status>; S2 <status>; S3 <status>; S4 <status>; S5 <status>.
```

## Hard Stops

Return `BLOCKED` if:

- Outcome scale or dependency structure makes the selected test invalid.
- Repeated/nested data were analyzed as independent rows.
- A causal mediation/causal conclusion is requested from unsuitable data without caveat.
- Required numerical output is absent but the user asks for final result prose.
- The correct method is outside Pingouin's scope.
