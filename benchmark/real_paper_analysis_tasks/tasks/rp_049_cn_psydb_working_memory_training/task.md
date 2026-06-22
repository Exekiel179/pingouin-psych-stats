# rp_049_cn_psydb_working_memory_training: 工作记忆训练迁移效应的边界条件

## Source

- Journal: 心理学报
- Paper URL/DOI: not recorded
- Repository: https://www.scidb.cn/en/psych
- Repository platform: ScienceDB/Psychological Science Data Bank
- Source language: Chinese
- Verification status: `needs_manual_check`
- Task status: `needs_file_verification`

## Research Context

- Research question: 工作记忆训练在什么条件下产生迁移效应？
- Article hypotheses: 提取关于训练组、测量时间和迁移任务类型交互的假设。
- Experimental design: 训练干预设计；需核验组别、前后测、任务类型和随机分配情况。
- Analysis type: pre-post mixed design / training effect
- Variables needed: 组别、时间、任务类型、表现指标、被试 ID。
- Planned Pingouin route: `pg-anova`

## Repository Evidence

- Data evidence: ScienceDB/PsyDB search result indicates possible Acta Psychologica Sinica related dataset; title requires verification.
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
