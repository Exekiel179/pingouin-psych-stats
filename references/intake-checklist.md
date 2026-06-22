# Psychology Statistics Intake Checklist

Use this checklist before routing a broad request. Ask only the missing items that materially affect the analysis; do not interrogate the user when the answer is already in the prompt or data.

## Minimum Intake

1. Research question and hypothesis.
2. Data file/path or dataframe name.
3. Outcome variable(s) and scale: continuous, ordinal/Likert item, binary, count, categorical.
4. Predictor(s): between-subject factor, within-subject factor, covariate, mediator, rater, item.
5. Unit of analysis: participant, trial, item, dyad, clinician rating, group/class.
6. Dependency structure: independent, paired, repeated measures, nested, multiple raters.
7. Missing-data rule: listwise deletion, pairwise deletion, imputation already done, or ask for screening.
8. Planned versus exploratory comparisons.
9. Output language: Chinese, English, or bilingual.
10. Deliverable format: Markdown, Word/docx, PDF, LaTeX, CSV tables, or Python notebook/script.
11. Figure/table requirements: APA table, descriptive table, raincloud/box/violin/scatter/interaction plot, publication size.
12. Reporting standard: APA, journal style, thesis, preregistration, supplementary material.

## Ask Strategy

If many items are missing, ask a compact form:

```markdown
请补充这些最关键的信息：
1. 数据在哪里，或列名有哪些？
2. 因变量、自变量/组别/时间点、被试 ID 分别是什么？
3. 你要输出什么格式：Markdown / Word / PDF / LaTeX / 只要 Python 代码？
4. 需要哪些图表：描述统计表 / APA 表 / 箱线图 / 散点图 / 交互图？
5. 这是计划检验还是探索性分析？
```

If enough information exists, proceed and state assumptions in one line.

## Deliverable Routing

- Markdown or chat summary -> `pg-reporting`.
- Word/docx -> produce Markdown first and note conversion path; use a document skill only if available/requested.
- PDF -> produce LaTeX/Markdown source first unless a PDF toolchain is present.
- LaTeX -> produce table/prose snippets and code blocks.
- Figures -> generate Python plotting code; prefer seaborn/matplotlib unless the repo has a plotting standard.

