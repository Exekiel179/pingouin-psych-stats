You are completing a strict real-paper psychology benchmark task.

Paper: Steegen 2014 registered report
Journal: Frontiers in Psychology
Paper URL/DOI: https://doi.org/10.3389/fpsyg.2014.00786
Original repository: https://osf.io/ivfu6/

Local data files:
- tasks/strict_006_rp_009_rr_009/sources/data/readme.txt
- tasks/strict_006_rp_009_rr_009/sources/data/rawdata_delayed_session1.txt
- tasks/strict_006_rp_009_rr_009/sources/data/rawdata_immediate.txt
- tasks/strict_006_rp_009_rr_009/sources/data/rawdata_delayed_session2.txt

Local script files:
- tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_confirmatoryanalyses.m
- tasks/strict_006_rp_009_rr_009/sources/script/crowdwithin_analysis.m
- tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_posthocanalyses.m
- tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_postprocessing.m
- tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_samplesize.m
- tasks/strict_006_rp_009_rr_009/sources/script/RPP_ivfu6.R

Local document/readme files:
- tasks/strict_006_rp_009_rr_009/sources/doc/steegenetal2014_report.pdf
- tasks/strict_006_rp_009_rr_009/sources/doc/pre_data_collection_steegenetal2014.pdf

Detected analysis families from scripts: t_test, correlation, reliability
Candidate variables from scripts: not extracted
Script analysis snippets:
- `grp(set).corr{g}=corr(grp(set).d{g}, grp(set).d{3});`
- `alpha=.05;`
- `% ttest`
- `[h p ci stats] = ttest(grp(set).d{g} - grp(set).d{3});`
- `ncp_low = fzero(@(delta) tnonct(delta, df, 1-alpha/2, grp(set).t{g}), [-20,20]);`
- `ncp_high = fzero(@(delta) tnonct(delta, df, alpha/2, grp(set).t{g}), [-20,20]);`
- `[h p ci stats] = ttest(grp(set).d{1} - grp(set).d{2});`
- `ncp_low = fzero(@(delta) tnonct(delta, df, 1-alpha/2, grp(set).t{3}), [-20,20]);`
- `ncp_high = fzero(@(delta) tnonct(delta, df, alpha/2, grp(set).t{3}), [-20,20]);`
- `ncp_low = fzero(@(delta) tnonct(delta, df, 1-alpha/2, grpcmp.t{1}), [-20,20]);`
- `ncp_high = fzero(@(delta) tnonct(delta, df, alpha/2, grpcmp.t{1}), [-20,20]);`
- `[h3 p3 ci3 stats3] = ttest(grp(set).d{1} - grp(set).d{2});`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
