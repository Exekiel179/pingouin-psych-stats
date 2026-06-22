# Full-Chain Psychology Benchmark Design

This benchmark should not be limited to "run a statistical test." The unit of evaluation is a research workflow reconstructed from a real paper:

1. research question
2. article hypotheses
3. experimental design
4. data analysis
5. result interpretation

The current candidate pool is in:

- `real_paper_tasks.jsonl`
- `real_paper_tasks.csv`
- `REAL_PAPER_50_TASKS.md`

## Why This Design

Psychology analysis failures often happen before the statistical function call:

- The model misses the real hypothesis and analyzes a convenient but irrelevant variable.
- The model treats repeated-measures data as independent.
- The model ignores experimental factors, covariates, exclusion rules, or preregistered decisions.
- The model reports a significant p value but interprets it against the wrong research question.
- The model overclaims causality from correlational or cross-sectional designs.

So each final benchmark task should start from the paper context, not only from a CSV file.

## Candidate Schema

Each JSONL row contains:

- `research_question`: the focal question to reconstruct from the paper.
- `article_hypotheses`: stated or preregistered predictions.
- `experimental_design`: participants, factors, within/between-subject structure, measures, exclusions.
- `data_analysis_plan`: expected method family and required checks.
- `result_interpretation_target`: what conclusion must be interpreted and bounded.
- `data_evidence`: open data link or file evidence.
- `script_evidence`: analysis script/code evidence.
- `pingouin_route`: expected plugin route.
- `verification_status`: `verified`, `partial`, or `needs_manual_check`.
- `source_language`: English or Chinese.

## Task Types

Use three task levels.

- `T1_design_reconstruction`: Given paper title/abstract/method excerpt, reconstruct research question, hypotheses, variables, and design.
- `T2_analysis_reproduction`: Given data and scripts/codebook, reproduce one target result with Pingouin where appropriate.
- `T3_full_chain`: Given paper context plus data, produce design summary, analysis code, result table, APA/Chinese report, and limitations.

For plugin benchmarking, `T3_full_chain` is the most useful because it tests whether `$pingouin-stat` reduces wrong-method routing and interpretation errors.

## Scoring Rubric

Suggested 100-point scoring:

- Research question and hypothesis extraction: 15
- Experimental design reconstruction: 20
- Variable mapping and preprocessing decisions: 15
- Statistical method choice and assumptions: 20
- Numeric/result reproduction: 15
- Interpretation, caveats, and non-overclaiming: 15

Critical fail conditions:

- Uses an independent test for repeated-measures data without justification.
- Analyzes the wrong dependent variable or wrong contrast.
- Ignores the paper's main hypothesis and substitutes a generic EDA.
- Claims causality from correlational/cross-sectional data.
- Fabricates variables, sample sizes, p values, or citations.

## Source Strategy

English sources:

- Main seed: `Analysis of Open Data and Computational Reproducibility in Registered Reports in Psychology`, an OSF/PsyArXiv project that audits real psychology Registered Reports and records data/script availability.
- Supplement: OSF/Zenodo candidates from higher-impact journals such as `Nature Human Behaviour` and `Journal of Experimental Psychology: General`.

Chinese sources:

- `心理学报` is a top Chinese psychology journal. Its journal page describes it as a major outlet for high-level Chinese psychology research and lists broad indexing/recognition.
- The `心理学开放科学苏州倡议` recommends publishing paper-linked data on FAIR-compatible scientific data platforms and encourages open materials, data coding, observation records, and code.
- The same notice lists `心理科学数据银行` as a psychology open-science data platform: `https://www.scidb.cn/psych`.

Current Chinese candidates are `needs_manual_check` because quick search identified plausible `心理学报`/PsyDB records, but file-level script evidence still needs manual confirmation.

## Conversion Workflow

For each candidate selected for executable benchmark use:

1. Download or record the exact paper PDF/HTML source.
2. Extract the research question and hypotheses into `task_context.md`.
3. Extract Methods fields: sample, design, variables, exclusion rules, and measurement timing.
4. Download the exact dataset and scripts into a frozen task directory.
5. Choose one target result from the paper, preferably one table/figure/statistical paragraph.
6. Write a gold answer with expected method, assumptions, core numeric values, and interpretation.
7. Run both conditions:
   - baseline prompt without plugin guidance
   - plugin-guided prompt requiring `$pingouin-stat`
8. Score with the full-chain rubric and record token/cost/failure data.

## Current Limitations

- The pool has 50 candidates, not 50 fully executable tasks.
- The strongest evidence is for OSF Registered Reports; Chinese ScienceDB/PsyDB entries require manual file-level verification.
- Some original scripts are R, SPSS, JASP, MATLAB, or mixed-effects workflows; Pingouin may only reproduce simplified or subset analyses.
- For psycholinguistic and trial-level data, mixed-effects models may be the correct method; those should be marked as outside full Pingouin scope rather than forced into ANOVA.

