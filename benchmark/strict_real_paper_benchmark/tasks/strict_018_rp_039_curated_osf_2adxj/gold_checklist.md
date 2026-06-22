# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_018_rp_039_curated_osf_2adxj/sources/doc/Output_Reproducibility_and_Robustness_Study_3_PDF_Export.pdf` (doc, 450617 bytes)
- `tasks/strict_018_rp_039_curated_osf_2adxj/sources/doc/R_codes_v3_Newsonetal.2025.html` (doc, 117673 bytes)
- `tasks/strict_018_rp_039_curated_osf_2adxj/sources/script/R_codes_v3_Newsonetal.2025.qmd` (script, 10301 bytes)
- `tasks/strict_018_rp_039_curated_osf_2adxj/sources/data/Correlation_BonfCorrected.xlsx` (data, 22299 bytes)
- `tasks/strict_018_rp_039_curated_osf_2adxj/sources/script/Syntax-Reproducibility-Robustness.sps` (script, 10293 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, correlation, regression, mediation, reliability
- Candidate variables: SDS_17, SES, USA, age, criminal_att_final, employed_yes, fusion_7, fusion_8, good_job, kids, male, no_trouble, relationship_yes

Snippets:

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

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
