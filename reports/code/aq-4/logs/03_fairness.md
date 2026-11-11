# Log: aq-4 / 03_fairness

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:22:46Z |
| Finished (UTC) | 2026-11-11T23:23:37Z |
| Duration | 50.9 s |
| Command | `python aq-4/code/03_fairness.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Confirmatory fairness check FR1: recall at capacity by group, day 27, 5 per 20

| ranking | group | test_enrolments | group_non_completers | group_base_rate | recall_group | recall_others | gap | boot_ci95_low | boot_ci95_high | p_one_sided | p_holm | holm_upper_bound | status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| model | Declared disability | 1,488 | 803 | 0.540 | 0.463 | 0.409 | 0.054 | 0.004 | 0.098 | 0.983 | 1.000 | 0.091 | not flagged |
| model | Deprivation band 0–10% | 1,486 | 787 | 0.530 | 0.426 | 0.414 | 0.012 | -0.050 | 0.063 | 0.643 | 1.000 | 0.063 | not flagged |
| model | Deprivation band missing | 610 | 181 | 0.297 | 0.348 | 0.417 | -0.069 | -0.168 | 0.024 | 0.066 | 0.199 | 0.034 | not flagged |
| model | Age 55 or over | 118 | 42 | 0.356 | 0.262 | 0.416 | -0.154 | -0.328 | 0.092 | 0.091 |  |  | insufficient data, not cleared (point gap only) |
| rule | Declared disability | 1,488 | 803 | 0.540 | 0.413 | 0.402 | 0.012 | -0.043 | 0.066 | 0.675 | 1.000 | 0.056 | not flagged |
| rule | Deprivation band 0–10% | 1,486 | 787 | 0.530 | 0.412 | 0.402 | 0.010 | -0.046 | 0.065 | 0.639 | 1.000 | 0.065 | not flagged |
| rule | Deprivation band missing | 610 | 181 | 0.297 | 0.337 | 0.405 | -0.068 | -0.161 | 0.021 | 0.063 | 0.190 | 0.030 | not flagged |
| rule | Age 55 or over | 118 | 42 | 0.356 | 0.238 | 0.404 | -0.166 | -0.304 | 0.091 | 0.085 |  |  | insufficient data, not cleared (point gap only) |
[saved] aq-4/results/fairness_confirmatory.csv  (8 rows x 18 columns)

**FR1 verdict for the model list: 0 of 3 confirmatory groups flagged.** A group is flagged only when its recall is more than 10 points below the others AND the Holm-adjusted interval lies below 0.

### Descriptive: selection rate, recall and precision by audit group (model list and rule list)

| attribute | group | enrolments | non_completers | base_rate | share_of_all_non_completers | model_selection_rate | model_share_of_list | model_recall | model_precision | rule_selection_rate | rule_share_of_list | rule_recall | rule_precision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | 6,666 | 2,750 | 0.413 | 0.398 | 0.239 | 0.403 | 0.387 | 0.668 | 0.239 | 0.403 | 0.379 | 0.654 |
| gender | M | 9,058 | 4,161 | 0.459 | 0.602 | 0.261 | 0.597 | 0.434 | 0.765 | 0.261 | 0.597 | 0.419 | 0.739 |
| disability | N | 14,236 | 6,108 | 0.429 | 0.884 | 0.244 | 0.878 | 0.409 | 0.719 | 0.247 | 0.890 | 0.402 | 0.697 |
| disability | Y | 1,488 | 803 | 0.540 | 0.116 | 0.325 | 0.122 | 0.463 | 0.770 | 0.292 | 0.110 | 0.413 | 0.763 |
| age_band | 0-35 | 10,942 | 5,017 | 0.459 | 0.726 | 0.275 | 0.760 | 0.436 | 0.728 | 0.272 | 0.753 | 0.418 | 0.704 |
| age_band | 35-55 | 4,664 | 1,852 | 0.397 | 0.268 | 0.201 | 0.237 | 0.363 | 0.717 | 0.206 | 0.242 | 0.367 | 0.708 |
| age_band | 55<= | 118 | 42 | 0.356 | 0.006 | 0.119 | 0.004 | 0.262 | 0.786 | 0.153 | 0.005 | 0.238 | 0.556 |
| imd_band | 0-10% | 1,486 | 787 | 0.530 | 0.114 | 0.295 | 0.111 | 0.426 | 0.763 | 0.289 | 0.108 | 0.412 | 0.755 |
| imd_band | 10-20% | 1,582 | 811 | 0.513 | 0.117 | 0.297 | 0.119 | 0.449 | 0.774 | 0.286 | 0.114 | 0.414 | 0.743 |
| imd_band | 20-30% | 1,701 | 853 | 0.501 | 0.123 | 0.280 | 0.120 | 0.424 | 0.761 | 0.278 | 0.120 | 0.414 | 0.746 |
| imd_band | 30-40% | 1,691 | 752 | 0.445 | 0.109 | 0.265 | 0.113 | 0.438 | 0.734 | 0.260 | 0.111 | 0.434 | 0.743 |
| imd_band | 40-50% | 1,543 | 678 | 0.439 | 0.098 | 0.257 | 0.100 | 0.426 | 0.730 | 0.264 | 0.103 | 0.406 | 0.676 |
| imd_band | 50-60% | 1,529 | 674 | 0.441 | 0.098 | 0.266 | 0.103 | 0.430 | 0.713 | 0.264 | 0.102 | 0.424 | 0.708 |
| imd_band | 60-70% | 1,464 | 597 | 0.408 | 0.086 | 0.227 | 0.084 | 0.380 | 0.684 | 0.221 | 0.082 | 0.370 | 0.682 |
| imd_band | 70-80% | 1,435 | 602 | 0.420 | 0.087 | 0.229 | 0.083 | 0.389 | 0.713 | 0.237 | 0.086 | 0.394 | 0.697 |
| imd_band | 80-90% | 1,401 | 525 | 0.375 | 0.076 | 0.218 | 0.077 | 0.381 | 0.654 | 0.225 | 0.080 | 0.375 | 0.625 |
| imd_band | 90-100% | 1,282 | 451 | 0.352 | 0.065 | 0.200 | 0.065 | 0.392 | 0.689 | 0.208 | 0.068 | 0.377 | 0.637 |
| imd_band | Missing | 610 | 181 | 0.297 | 0.026 | 0.157 | 0.024 | 0.348 | 0.656 | 0.172 | 0.027 | 0.337 | 0.581 |
[saved] aq-4/results/fairness_descriptive.csv  (18 rows x 14 columns)

### Descriptive: calibration by group (frozen model, no recalibration)

| group | enrolments | events | non_events | observed_rate | mean_predicted | citl | citl_ci_low | citl_ci_high | slope | slope_ci_low | slope_ci_high | enough_for_a_curve |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Declared disability | 1,488 | 803 | 685 | 0.540 | 0.462 | 0.386 | 0.273 | 0.499 | 0.881 | 0.753 | 1.008 | yes |
| Deprivation band 0–10% | 1,486 | 787 | 699 | 0.530 | 0.457 | 0.363 | 0.250 | 0.475 | 0.840 | 0.713 | 0.967 | yes |
| Deprivation band missing | 610 | 181 | 429 | 0.297 | 0.343 | -0.266 | -0.460 | -0.072 | 0.582 | 0.412 | 0.752 | no |
| Age 55 or over | 118 | 42 | 76 | 0.356 | 0.268 | 0.493 | 0.080 | 0.905 | 0.885 | 0.408 | 1.363 | no |
| Female | 6,666 | 2,750 | 3,916 | 0.413 | 0.407 | 0.026 | -0.028 | 0.080 | 0.862 | 0.800 | 0.924 | yes |
| Male | 9,058 | 4,161 | 4,897 | 0.459 | 0.421 | 0.197 | 0.151 | 0.243 | 0.879 | 0.828 | 0.930 | yes |
| All test enrolments | 15,724 | 6,911 | 8,813 | 0.440 | 0.415 | 0.124 | 0.089 | 0.159 | 0.873 | 0.834 | 0.912 | yes |
[saved] aq-4/results/fairness_calibration.csv  (7 rows x 13 columns)

### Descriptive: ABROCA within run (area between the group's ROC curve and the others'), with a shuffled-label reference

| group | abroca | auc_group_minus_others | shuffled_mean | shuffled_p95 | above_chance_reference |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Declared disability | 0.0434 | -0.0065 | 0.0518 | 0.0617 | no |
| Deprivation band 0–10% | 0.0523 | -0.0142 | 0.0520 | 0.0620 | no |
| Deprivation band missing | 0.0659 | -0.0480 | 0.0607 | 0.0758 | no |
| Female (against male) | 0.0631 | 0.0023 | 0.0432 | 0.0541 | yes |
[saved] aq-4/results/fairness_abroca.csv  (4 rows x 6 columns)

### Proxy check: mean score and predictor values by group (which predictors carry group information)

| group | enrolments | mean_risk_score | median_clicks_0c | median_activity_ratio | share_repeat_attempt | share_flagged_by_rule | share_task_missed | share_inactive_last7 | observed_non_completion |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Declared disability | 1,488 | 0.462 | 138.000 | 0.917 | 0.176 | 0.337 | 0.114 | 0.237 | 0.540 |
| Deprivation band 0–10% | 1,486 | 0.457 | 139.000 | 0.874 | 0.139 | 0.351 | 0.110 | 0.271 | 0.530 |
| Deprivation band missing | 610 | 0.343 | 288.500 | 1.296 | 0.082 | 0.172 | 0.066 | 0.121 | 0.297 |
| Age 55 or over | 118 | 0.268 | 311.000 | 1.733 | 0.076 | 0.169 | 0.034 | 0.136 | 0.356 |
| Female | 6,666 | 0.407 | 117.000 | 1.061 | 0.120 | 0.328 | 0.067 | 0.276 | 0.413 |
| All test enrolments | 15,724 | 0.415 | 167.500 | 1.000 | 0.118 | 0.281 | 0.087 | 0.219 | 0.440 |
[saved] aq-4/results/fairness_proxy.csv  (6 rows x 10 columns)

