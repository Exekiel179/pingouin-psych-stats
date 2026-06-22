Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Evers 2014 registered report
Journal: Frontiers in Psychology
Paper URL/DOI: https://doi.org/10.3389/fpsyg.2014.00875
Original repository: https://osf.io/e6cr3/

Local data files:
- tasks/strict_016_rp_026_rr_026/sources/data/ALL_DATA.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/Classroom_Data_Faces_2012_and_2013.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/tversky_faces_eindhoven_SIMILARITY.sav
- tasks/strict_016_rp_026_rr_026/sources/data/tversky_faces_tilburg_CATEGORIZATION.sav
- tasks/strict_016_rp_026_rr_026/sources/data/faces_sad_eindhoven_SIMILARITY.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/faces_happy_eindhoven_SIMILARITY.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_faces_SIMILARITY_cleaned.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_faces_CATEGORIZATION_cleaned.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_faces_SIMILARITY_raw.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_faces_CATEGORIZATION_raw.sav
- tasks/strict_016_rp_026_rr_026/sources/data/tversky_landen_tilburg_SIMILARITY.sav
- tasks/strict_016_rp_026_rr_026/sources/data/Countries_eindhoven_B_India_CATEGORIZATION.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/Countries_eindhoven_A_Hongarije_CATEGORIZATION.xlsx
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_landen_SIMILARITY_cleaned.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_countries_CATEGORIZATION_cleaned.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_countries_SIMILARITY_raw.sav
- tasks/strict_016_rp_026_rr_026/sources/data/mturk_tversky_countries_CATEGORIZATION_raw.sav
- tasks/strict_016_rp_026_rr_026/sources/data/Meta-Analysis_Calculation_Cohens_d.xlsx

Local script files:
- tasks/strict_016_rp_026_rr_026/sources/script/meta_analysis.R

Local document/readme files:
- tasks/strict_016_rp_026_rr_026/sources/doc/Pre-registration.pdf

Detected analysis families from scripts: not detected
Candidate variables from scripts: not extracted
Script analysis snippets:
- no statistical snippets detected

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
