# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_017_rp_029_rr_029/sources/doc/SF_3_Measures.pdf` (doc, 91102 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/data/SPI_Items_used.xlsx` (data, 53621 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/doc/SF_1_Analyses.pdf` (doc, 256720 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/doc/SF_2_Exploratory.pdf` (doc, 215113 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/other/mediation_table.tex` (other, 4268 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/script/extra_analyses.R` (script, 27172 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/other/mediation_table.Rnw` (other, 4890 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/script/vigilance.R` (script, 50887 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/data/Neuroticism_26_Vigilance_-_Final_Version_August_21_2C_2017_12.21_skip23.csv` (data, 80920 bytes)
- `tasks/strict_017_rp_029_rr_029/sources/doc/Pre-registration_revised.pdf` (doc, 214559 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, correlation, regression, mediation, reliability
- Candidate variables: outcome, stat

Snippets:

- `(alpha.c <- psych::alpha(vigdata[, con.items], check.keys = T))`
- `c.keys <- alpha.c$keys`
- `(alpha.ax <- psych::alpha(vigdata[, anxiety.items], check.keys = T))`
- `ax.keys <- alpha.ax$keys`
- `(alpha.es <- psych::alpha(vigdata[, emotionalstability.items], check.keys = T))`
- `es.keys <- alpha.es$keys`
- `(alpha.in <- psych::alpha(vigdata[, industry.items], check.keys = T))`
- `in.keys <- alpha.in$keys*-1`
- `(alpha.ir <- psych::alpha(vigdata[, irritability.items], check.keys = T))`
- `ir.keys <- alpha.ir$keys*-1`
- `(alpha.or <- psych::alpha(vigdata[, order.items], check.keys = T))`
- `or.keys <- alpha.or$keys*-1`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
