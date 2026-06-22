# rp_045_cn_psydb_sentence_production_eye_tracking: 中文句子产生中语义和音韵编码的时间进程及交互作用

## Source

- Journal: 心理学报
- Paper URL/DOI: not recorded
- Repository: https://www.scidb.cn/en/psych
- Repository platform: ScienceDB/Psychological Science Data Bank
- Source language: Chinese
- Verification status: `needs_manual_check`
- Task status: `needs_file_verification`

## Research Context

- Research question: 中文句子产生中语义编码与音韵编码的时间进程如何展开，二者是否交互？
- Article hypotheses: 提取关于语义效应、音韵效应及其时间进程/交互的假设。
- Experimental design: 心理语言学实验；需核验项目/被试双随机结构、时间窗、条件和重复测量因素。
- Analysis type: psycholinguistic repeated-measures analysis
- Variables needed: 语义条件、音韵条件、时间窗、眼动/反应指标、被试 ID、项目 ID。
- Planned Pingouin route: `pingouin-stat-router`

## Repository Evidence

- Data evidence: ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related eye-movement dataset.
- Script evidence: Analysis script not confirmed; inspect dataset files.

## Benchmark Task

Starting from the research question, reconstruct the study design, identify the target hypothesis and variables, then produce a defensible analysis plan and result interpretation. Use the repository data/scripts when available. If file-level evidence is incomplete, explicitly state what must be verified before numeric reproduction.

## Expected Deliverables

- Repository verification note: identify what data/script evidence is present and what remains missing.
- Research question reconstructed from the paper context.
- Article hypotheses or a clear statement that the hypothesis must be extracted from the paper.
- Experimental design summary: sample, factors, within/between-subject structure, measures, exclusions.
- Variable mapping from repository data/scripts to outcome, predictors, covariates, and participant IDs.
- Statistical method choice with assumptions and a note on whether Pingouin is in scope.
- Executable Python/Pingouin analysis code or a precise reason why the original method is outside Pingouin scope.
- APA-style or Chinese psychology-style result report.
- Interpretation tied back to the research question, with caveats and no unsupported causal claims.

## Known Failure Modes

- Analyzing a convenient variable instead of the paper's focal dependent variable.
- Ignoring repeated-measures, participant IDs, item IDs, or nested trial structure.
- Using an independent-samples test for paired/repeated observations.
- Omitting assumption checks, effect sizes, confidence intervals, or multiple-comparison correction.
- Reporting numeric results that were not computed from the referenced data/script.
- Interpreting a significant p value without linking it to the hypothesis.
- Making causal claims from correlational or cross-sectional data.
- Misreading Chinese variable names, paper hypotheses, or psychology reporting conventions.
- Forcing the task into Pingouin when the original model may require mixed-effects or specialized software.
