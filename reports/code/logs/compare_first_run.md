# Log: logs / compare_first_run

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:34Z |
| Finished (UTC) | 2026-11-12T16:00:36Z |
| Duration | 1.6 s |
| Command | `python common/compare_first_run.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Result tables of the rerun against the first run (commit 11f4aca)

| aq | status | files |
| :---- | :---- | :---- |
| aq-1 | byte-identical | 24 |
| aq-1 | new in the rerun | 6 |
| aq-1 | structure differs | 1 |
| aq-2 | byte-identical | 2 |
| aq-2 | new in the rerun | 12 |
| aq-2 | only in the first run | 3 |
| aq-2 | structure differs | 16 |
| aq-3 | byte-identical | 28 |
| aq-3 | same values (only time or hash columns differ) | 2 |
| aq-4 | byte-identical | 13 |

**aq-3: 30 result tables** – byte-identical: 28; same values, only time or hash columns differ: 2; other: 0

**aq-4: 13 result tables** – byte-identical: 13; same values, only time or hash columns differ: 0; other: 0

**Every table that is not byte-identical**

| aq | file | status | detail |
| :---- | :---- | :---- | :---- |
| aq-1 | aq-1/results/checks_all.csv | structure differs | first run 5 rows x 4 columns; rerun 7 x 4 |
| aq-1 | aq-1/results/first_missed_by_week4_2013.csv | new in the rerun |  |
| aq-1 | aq-1/results/first_missed_by_week4_all.csv | new in the rerun |  |
| aq-1 | aq-1/results/first_missed_by_week4_year_difference_all.csv | new in the rerun |  |
| aq-1 | aq-1/results/not_registered_d14_by_year_all.csv | new in the rerun |  |
| aq-1 | aq-1/results/rates_module_by_start_month_2013.csv | new in the rerun |  |
| aq-1 | aq-1/results/year_comparison_all.csv | new in the rerun |  |
| aq-2 | aq-2/results/associations_2013.csv | structure differs | first run 5 rows x 22 columns; rerun 5 x 29 |
| aq-2 | aq-2/results/associations_2014.csv | structure differs | first run 5 rows x 22 columns; rerun 5 x 29 |
| aq-2 | aq-2/results/associations_by_module_2013.csv | structure differs | first run 26 rows x 7 columns; rerun 26 x 8 |
| aq-2 | aq-2/results/associations_by_module_2014.csv | structure differs | first run 30 rows x 7 columns; rerun 30 x 8 |
| aq-2 | aq-2/results/binned_residuals_2013.csv | only in the first run |  |
| aq-2 | aq-2/results/binned_residuals_2014.csv | only in the first run |  |
| aq-2 | aq-2/results/binned_residuals_activity5_2013.csv | new in the rerun |  |
| aq-2 | aq-2/results/binned_residuals_activity5_2014.csv | new in the rerun |  |
| aq-2 | aq-2/results/binned_residuals_by_run_2013.csv | new in the rerun |  |
| aq-2 | aq-2/results/binned_residuals_by_run_2014.csv | new in the rerun |  |
| aq-2 | aq-2/results/binned_residuals_decile_2013.csv | new in the rerun |  |
| aq-2 | aq-2/results/binned_residuals_decile_2014.csv | new in the rerun |  |
| aq-2 | aq-2/results/late_tma_average_check.csv | new in the rerun |  |
| aq-2 | aq-2/results/non_completion_by_sign_count_2013.csv | structure differs | first run 5 rows x 3 columns; rerun 10 x 4 |
| aq-2 | aq-2/results/non_completion_by_sign_count_2014.csv | structure differs | first run 5 rows x 3 columns; rerun 10 x 4 |
| aq-2 | aq-2/results/odds_ratios_2013.csv | structure differs | first run 5 rows x 6 columns; rerun 5 x 7 |
| aq-2 | aq-2/results/odds_ratios_2014.csv | structure differs | first run 5 rows x 6 columns; rerun 5 x 7 |
| aq-2 | aq-2/results/replication.csv | structure differs | first run 5 rows x 23 columns; rerun 5 x 39 |
| aq-2 | aq-2/results/replication_by_module.csv | structure differs | first run 30 rows x 14 columns; rerun 30 x 16 |
| aq-2 | aq-2/results/replication_sensitivity.csv | new in the rerun |  |
| aq-2 | aq-2/results/sensitivity_2013.csv | structure differs | first run 35 rows x 6 columns; rerun 45 x 18 |
| aq-2 | aq-2/results/sensitivity_2014.csv | structure differs | first run 35 rows x 6 columns; rerun 45 x 18 |
| aq-2 | aq-2/results/sign_calendar_2013.csv | new in the rerun |  |
| aq-2 | aq-2/results/sign_calendar_2014.csv | new in the rerun |  |
| aq-2 | aq-2/results/sign_correlation_2013.csv | structure differs | first run 5 rows x 6 columns; rerun 10 x 5 |
| aq-2 | aq-2/results/sign_correlation_2014.csv | structure differs | first run 5 rows x 6 columns; rerun 10 x 5 |
| aq-2 | aq-2/results/sign_support_2013.csv | new in the rerun |  |
| aq-2 | aq-2/results/sign_support_2014.csv | new in the rerun |  |
| aq-2 | aq-2/results/small_cells_2014.csv | only in the first run |  |
| aq-2 | aq-2/results/subgroups_2013.csv | structure differs | first run 40 rows x 11 columns; rerun 40 x 11 |
| aq-2 | aq-2/results/subgroups_2014.csv | structure differs | first run 40 rows x 11 columns; rerun 40 x 11 |
| aq-3 | aq-3/results/dev_fold_design.csv | same values (only time or hash columns differ) | seconds: largest absolute difference 21.9 |
| aq-3 | aq-3/results/verification.csv | same values (only time or hash columns differ) | detail: 1 of 8 values differ only in a quoted run time |
[saved] logs/compare_first_run.csv  (107 rows x 4 columns)

**Frozen models**: same hyperparameters in 12 of 12; model file byte-identical (SHA-256) in 12 of 12

| name | cutoff | hyperparameters | same_hyperparameters | same_file_hash |
| :---- | :---- | :---- | :---- | :---- |
| B3 | 27 | {"C": 0.01} | yes | yes |
| M1 | 27 | {"C": 10.0} | yes | yes |
| M2 | 27 | {"C": 10.0} | yes | yes |
| M3 | 27 | {"max_depth": 3, "learning_rate": 0.05, "trees": 100} | yes | yes |
| M4 | 27 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | yes | yes |
| M1_labels_available | 27 | {"C": 0.003} | yes | yes |
| B3 | 13 | {"C": 0.01} | yes | yes |
| M1 | 13 | {"C": 0.01} | yes | yes |
| M2 | 13 | {"C": 0.01} | yes | yes |
| M3 | 13 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | yes | yes |
| M4 | 13 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | yes | yes |
| M1_labels_available | 13 | {"C": 0.003} | yes | yes |

**Headline numbers, first run beside the rerun**

| aq | quantity | first_run | rerun | same | note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| aq-3 | S1: non-completers on the model lists | 2870 | 2870 | yes |  |
| aq-3 | S1: non-completers on the rule lists | 2786 | 2786 | yes |  |
| aq-3 | S1: most attainable | 3955 | 3955 | yes |  |
| aq-3 | S1: pooled normalised recall, model | 0.7257 | 0.7257 | yes |  |
| aq-3 | S1: pooled normalised recall, rule | 0.7044 | 0.7044 | yes |  |
| aq-3 | S1: difference | 0.0212 | 0.0212 | yes |  |
| aq-3 | S1: bootstrap interval, low | 0.0065 | 0.0065 | yes |  |
| aq-3 | S1: bootstrap interval, high | 0.0364 | 0.0364 | yes |  |
| aq-3 | S1: sign-flip p | 0.0032 | 0.0032 | yes |  |
| aq-3 | S1: runs won | 11 | 11 | yes |  |
| aq-3 | S1: runs lost | 2 | 2 | yes |  |
| aq-3 | S1: verdict | PASS | PASS | yes |  |
| aq-3 | chosen configuration | M1 | M1 | yes |  |
| aq-3 | S3: calibration-in-the-large | 0.1240 | 0.1240 | yes |  |
| aq-3 | S3: calibration slope | 0.8726 | 0.8726 | yes |  |
| aq-3 | S3: pooled bounds met | True | True | yes |  |
| aq-4 | FR1 Declared disability: gap | 0.0543 | 0.0543 | yes |  |
| aq-4 | FR1 Declared disability: boot_ci95_low | 0.0038 | 0.0038 | yes |  |
| aq-4 | FR1 Declared disability: boot_ci95_high | 0.0984 | 0.0984 | yes |  |
| aq-4 | FR1 Declared disability: flagged | False | False | yes |  |
| aq-4 | FR1 Deprivation band 0–10%: gap | 0.0117 | 0.0117 | yes |  |
| aq-4 | FR1 Deprivation band 0–10%: boot_ci95_low | -0.0497 | -0.0497 | yes |  |
| aq-4 | FR1 Deprivation band 0–10%: boot_ci95_high | 0.0633 | 0.0633 | yes |  |
| aq-4 | FR1 Deprivation band 0–10%: flagged | False | False | yes |  |
| aq-4 | FR1 Deprivation band missing: gap | -0.0690 | -0.0690 | yes |  |
| aq-4 | FR1 Deprivation band missing: boot_ci95_low | -0.1680 | -0.1680 | yes |  |
| aq-4 | FR1 Deprivation band missing: boot_ci95_high | 0.0238 | 0.0238 | yes |  |
| aq-4 | FR1 Deprivation band missing: flagged | False | False | yes |  |
| aq-4 | FR1 Age 55 or over: gap | -0.1543 | -0.1543 | yes |  |
| aq-4 | FR1 Age 55 or over: boot_ci95_low | -0.3278 | -0.3278 | yes |  |
| aq-4 | FR1 Age 55 or over: boot_ci95_high | 0.0924 | 0.0924 | yes |  |
| aq-4 | FR1 Age 55 or over: flagged | None | None | yes |  |
| aq-4 | list recall, day 27, 5 per 20 | 0.4153 | 0.4153 | yes |  |
| aq-4 | list lift | 1.6510 | 1.6510 | yes |  |
| aq-2 | 2013 sign_task_missed: rows averaged over | 9960 | 9960 | yes |  |
| aq-2 | 2013 sign_task_missed: adjusted risk difference | 0.4067 | 0.4067 | yes |  |
| aq-2 | 2013 sign_task_missed: unadjusted risk difference | 0.5032 | 0.5032 | yes |  |
| aq-2 | 2013 sign_task_missed: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2013 sign_tma_late: rows averaged over | 9960 | 9960 | yes | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2013 sign_tma_late: adjusted risk difference | 0.2166 | 0.2166 | yes | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2013 sign_tma_late: unadjusted risk difference | 0.1854 | 0.1854 | yes | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2013 sign_tma_late: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2013 sign_inactive_last7: rows averaged over | 11811 | 11811 | yes |  |
| aq-2 | 2013 sign_inactive_last7: adjusted risk difference | 0.1348 | 0.1348 | yes |  |
| aq-2 | 2013 sign_inactive_last7: unadjusted risk difference | 0.2526 | 0.2526 | yes |  |
| aq-2 | 2013 sign_inactive_last7: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2013 sign_low_activity: rows averaged over | 11811 | 11811 | yes |  |
| aq-2 | 2013 sign_low_activity: adjusted risk difference | 0.1466 | 0.1466 | yes |  |
| aq-2 | 2013 sign_low_activity: unadjusted risk difference | 0.3205 | 0.3205 | yes |  |
| aq-2 | 2013 sign_low_activity: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2013 sign_no_pre_activity: rows averaged over | 11811 | 11811 | yes |  |
| aq-2 | 2013 sign_no_pre_activity: adjusted risk difference | 0.1126 | 0.1126 | yes |  |
| aq-2 | 2013 sign_no_pre_activity: unadjusted risk difference | 0.2124 | 0.2124 | yes |  |
| aq-2 | 2013 sign_no_pre_activity: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2014 sign_task_missed: rows averaged over | 12585 | 12585 | yes |  |
| aq-2 | 2014 sign_task_missed: adjusted risk difference | 0.3964 | 0.3964 | yes |  |
| aq-2 | 2014 sign_task_missed: unadjusted risk difference | 0.4877 | 0.4877 | yes |  |
| aq-2 | 2014 sign_task_missed: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2014 sign_tma_late: rows averaged over | 12585 | 9064 | no | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2014 sign_tma_late: adjusted risk difference | 0.1623 | 0.2254 | no | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2014 sign_tma_late: unadjusted risk difference | 0.1436 | 0.1732 | no | P16/P17: averaged over the runs with a TMA due only |
| aq-2 | 2014 sign_tma_late: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2014 sign_inactive_last7: rows averaged over | 15724 | 15724 | yes |  |
| aq-2 | 2014 sign_inactive_last7: adjusted risk difference | 0.1541 | 0.1541 | yes |  |
| aq-2 | 2014 sign_inactive_last7: unadjusted risk difference | 0.2653 | 0.2653 | yes |  |
| aq-2 | 2014 sign_inactive_last7: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2014 sign_low_activity: rows averaged over | 15724 | 15724 | yes |  |
| aq-2 | 2014 sign_low_activity: adjusted risk difference | 0.1475 | 0.1475 | yes |  |
| aq-2 | 2014 sign_low_activity: unadjusted risk difference | 0.3024 | 0.3024 | yes |  |
| aq-2 | 2014 sign_low_activity: verdict | consistent association | consistent association | yes |  |
| aq-2 | 2014 sign_no_pre_activity: rows averaged over | 15724 | 15724 | yes |  |
| aq-2 | 2014 sign_no_pre_activity: adjusted risk difference | 0.0915 | 0.0915 | yes |  |
| aq-2 | 2014 sign_no_pre_activity: unadjusted risk difference | 0.1792 | 0.1792 | yes |  |
| aq-2 | 2014 sign_no_pre_activity: verdict | consistent association | consistent association | yes |  |
| aq-1 | non-completion rate, pooled all runs | 0.4526 | 0.4526 | yes |  |
| aq-1 | non-completion rate, year 2013 | 0.4567 | 0.4567 | yes |  |
| aq-1 | non-completion rate, year 2014 | 0.4495 | 0.4495 | yes |  |
| aq-1 | 2014 - 2013, all runs (9 of 2013, 13 of 2014), registered at day 14 (KPI population) | not computed | -0.0072 (-0.0190 to +0.0046) | no | P18: added |
| aq-1 | 2014 - 2013, 6 modules run in both years, registered at day 14 (KPI population) | not computed | -0.0352 (-0.0476 to -0.0227) | no | P18: added |
| aq-1 | 2014 - 2013, 9 module x start-month pairs run in both years, registered at day 14 (KPI population) | not computed | -0.0337 (-0.0465 to -0.0208) | no | P18: added |
| aq-1 | 2014 - 2013, all runs (9 of 2013, 13 of 2014), all enrolments | not computed | +0.0232 (+0.0122 to +0.0342) | no | P18: added |
| aq-1 | 2014 - 2013, 6 modules run in both years, all enrolments | not computed | -0.0022 (-0.0139 to +0.0095) | no | P18: added |
| aq-1 | 2014 - 2013, 9 module x start-month pairs run in both years, all enrolments | not computed | +0.0047 (-0.0073 to +0.0167) | no | P18: added |
[saved] logs/compare_first_run_headlines.csv  (83 rows x 6 columns)

AQ3 and AQ4 headline numbers equal to the first run: 34 of 34
AQ3 and AQ4 result tables whose numbers differ from the first run: 0

RESULT: PASS (AQ3 and AQ4 reproduce the first run)

