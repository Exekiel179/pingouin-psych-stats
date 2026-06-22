# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_006_rp_009_rr_009/sources/doc/steegenetal2014_report.pdf` (doc, 692114 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/doc/pre_data_collection_steegenetal2014.pdf` (doc, 124278 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_confirmatoryanalyses.m` (script, 5967 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/data/readme.txt` (data, 1057 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/crowdwithin_analysis.m` (script, 2581 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_posthocanalyses.m` (script, 1146 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_postprocessing.m` (script, 3925 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/data/rawdata_delayed_session1.txt` (data, 34998 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/data/rawdata_immediate.txt` (data, 95468 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/data/rawdata_delayed_session2.txt` (data, 20847 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/other/data_steegenetal2014.mat` (other, 7151 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/steegenetal2014_samplesize.m` (script, 1217 bytes)
- `tasks/strict_006_rp_009_rr_009/sources/script/RPP_ivfu6.R` (script, 6119 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: t_test, correlation, reliability
- Candidate variables: not extracted

Snippets:

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

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
