# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Final_ms.Rmd` (script, 49553 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP.R` (script, 11445 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP_power_analysis.R` (script, 1394 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/other/heat-aggression_AMP_power_analysis.bmp` (other, 319670 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/data/heat-aggression_AMP_pilot_data.csv` (data, 39702 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Power_Analysis.R` (script, 1394 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP_pilot.R` (script, 9227 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/other/Heat-Aggression_AMP_Power_Analysis.bmp` (other, 319670 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Pre-registration.R` (script, 5736 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/doc/Heat-Aggression_AMP_Pilot_Study_Preregistration.pdf` (doc, 125655 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/data/heat-aggression_AMP_data.csv` (data, 51563 bytes)
- `tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP-predata-IPA_ms.Rmd` (script, 33873 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova
- Candidate variables: ampRating, ampTrial, ampTrialDummy, perceived.prime

Snippets:

- `anova(trialType, trialTypePrime)`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
