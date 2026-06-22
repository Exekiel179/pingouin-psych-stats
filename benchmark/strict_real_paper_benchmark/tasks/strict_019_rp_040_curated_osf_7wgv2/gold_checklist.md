# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/REP_supps-rev.Rmd` (script, 35307 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1-rev2.pdf` (doc, 172925 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/Fig1-rev2.R` (script, 8157 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1-rev.pdf` (doc, 70654 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/data/CR.csv` (data, 10388608 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/REP_supps-rev.pdf` (doc, 14849901 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/data/CR.csv` (data, 10388608 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/REP_supps.pdf` (doc, 2681634 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/REP_supps.Rmd` (script, 12694 bytes)
- `tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1.pdf` (doc, 118119 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: reliability
- Candidate variables: Condition, Country, Truth, value

Snippets:

- `ggdist::stat_halfeye(alpha = 0.7) + ylab(NULL) + theme_bw() +`
- `size = 6, alpha = 0.8) +`
- `width = 0.15, alpha = 0.8) +`
- `alpha = 0.8,`
- `boxplot.args = list(color = "black", outlier.shape = NA, show_guide = FALSE, alpha = 0.8),`
- `violin.args = list(color = "black", outlier.shape = NA, alpha = 0.7),`
- `point.args = list(show_guide = FALSE, alpha = 0)`
- `show_guide = FALSE, alpha = 0.8,`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
