You are completing a strict real-paper psychology benchmark task.

Paper: Nature Human Behaviour Repro - Newson et al. (2025)
Journal: Nature Human Behaviour
Paper URL/DOI: not recorded
Original repository: https://osf.io/2adxj/

Local data files:
- tasks/strict_018_rp_039_curated_osf_2adxj/sources/data/Correlation_BonfCorrected.xlsx

Local script files:
- tasks/strict_018_rp_039_curated_osf_2adxj/sources/script/R_codes_v3_Newsonetal.2025.qmd
- tasks/strict_018_rp_039_curated_osf_2adxj/sources/script/Syntax-Reproducibility-Robustness.sps

Local document/readme files:
- tasks/strict_018_rp_039_curated_osf_2adxj/sources/doc/Output_Reproducibility_and_Robustness_Study_3_PDF_Export.pdf
- tasks/strict_018_rp_039_curated_osf_2adxj/sources/doc/R_codes_v3_Newsonetal.2025.html

Detected analysis families from scripts: anova, correlation, regression, mediation, reliability
Candidate variables from scripts: SDS_17, SES, USA, age, criminal_att_final, employed_yes, fusion_7, fusion_8, good_job, kids, male, no_trouble, relationship_yes
Script analysis snippets:
- `# Compute Cronbach's alpha criminal_behav`
- `alpha(S3_Data[, c(`
- `# Compute Cronbach's alpha SDS`
- `result_fusion <- corr.test(`
- `method = "pearson",   # same as SPSS default`
- `result <- corr.test(`
- `method = "pearson",    # same as SPSS default`
- `PARTIAL CORR /VARIABLES=criminal_att_final fusion_1 fusion_2 fusion_3 fusion_4 fusion_5 fusion_6 fusion_8 fusion_7 BY age relationship_yes /SIGNIFICANCE=TWOTAIL /MISSING=ANALYSIS.`
- `PARTIAL CORR /VARIABLES=criminal_behav fusion_1 fusion_2 fusion_3 fusion_4 fusion_5 fusion_6 fusion_8 fusion_7 BY age white relationship_yes SDS_17 /SIGNIFICANCE=TWOTAIL /MISSING=ANALYSIS.`
- `PARTIAL CORR /VARIABLES=arrested fusion_1 fusion_2 fusion_3 fusion_4 fusion_5 fusion_6 fusion_8 fusion_7 BY white relationship_yes SES /SIGNIFICANCE=TWOTAIL /MISSING=ANALYSIS.`
- `PARTIAL CORR /VARIABLES=convicted fusion_1 fusion_2 fusion_3 fusion_4 fusion_5 fusion_6 fusion_8 fusion_7 BY SES white /SIGNIFICANCE=TWOTAIL /MISSING=ANALYSIS.`
- `PARTIAL CORR /VARIABLES=good_job fusion_1 fusion_2 fusion_3 fusion_4 fusion_5 fusion_6 fusion_8 fusion_7 BY SES relationship_yes employed_yes SDS_17 /SIGNIFICANCE=TWOTAIL /MISSING=ANALYSIS.`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
