# Report Output Contract

Use this contract when the user asks for a manuscript section, APA report, thesis result, or publication-ready output.

## Output Layers

Produce three layers in this order:

1. **Reader layer:** a short finding summary and polished prose.
2. **Evidence layer:** compact APA table(s), assumption notes, corrections, effect sizes, and CIs.
3. **Provenance layer:** run id, source result files, software versions, analysis code path, and S0–S5 audit.

Do not mix raw Python logs into the reader layer. Put full machine output in `results/` and link it from the provenance layer.

## Manuscript Section Contract

Use only sections that fit the request, in this order:

```markdown
# <Analysis title>

## Analysis Summary
## Data and Assumptions
## Results
## Interpretation
## Limitations
## Reproducibility
## Audit
```

For a multi-analysis manuscript, repeat `Results` subsections per test family and finish with one integrated interpretation. Never merge incompatible statistics into one paragraph.

## Table Standards

- Give every table a descriptive title and a one-sentence note.
- Use stable column order: comparison/source, estimate, uncertainty, test statistic, df, p, correction, effect size.
- Preserve raw values in `results/`; round only the display table.
- Use `p < .001`, never `p = .000`.
- Include the correction method and effect-size definition when applicable.
- Do not present a p-value without the direction or estimate it belongs to.

## Prose Standards

- Begin with the design and test, not a generic introduction.
- State missing-data and assumption handling in one compact paragraph.
- Report estimate, uncertainty, test statistic, df, p, correction, and effect size when available.
- Separate statistical evidence from causal, clinical, and construct claims.
- Use `Interpretation` for meaning and `Limitations` for caveats; do not bury caveats in parentheses.

## Provenance Block

```markdown
## Reproducibility

- Run: `<run-id>`
- Code: `analysis.py`
- Results: `results/<file>`
- Python / Pingouin: `<versions>`
- Missing data: `<rule>`
- Multiple-comparison correction: `<method or not applicable>`

## Audit

Decision: <APPROVED / APPROVED_WITH_NOTES / REVISE / BLOCKED>
Audit: S0 <status>; S1 <status>; S2 <status>; S3 <status>; S4 <status>; S5 <status>.
```

If any provenance field is unavailable, write `not recorded` rather than guessing.
