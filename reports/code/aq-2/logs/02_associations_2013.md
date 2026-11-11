# Log: aq-2 / 02_associations_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:00:27Z |
| Finished (UTC) | 2026-11-11T23:00:30Z |
| Duration | 2.4 s |
| Command | `python aq-2/code/02_associations.py --scope 2013` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 associations at day 27, scope = 2013: 11,811 enrolments, 9 runs, 5,245 non-completers (44.4%)

**Risk difference per sign (percentage points = value x 100)**

| sign | enrolments_defined | with_sign | rate_with_sign | rate_without_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 9,960 | 1,285 | 0.900 | 0.396 | 0.503 | 0.483 | 0.522 | 0.407 | 0.375 | 0.438 |
| sign_tma_late | 9,960 | 577 | 0.636 | 0.451 | 0.185 | 0.144 | 0.225 | 0.217 | 0.174 | 0.259 |
| sign_inactive_last7 | 11,811 | 2,444 | 0.644 | 0.392 | 0.253 | 0.231 | 0.274 | 0.135 | 0.101 | 0.168 |
| sign_low_activity | 11,811 | 3,175 | 0.678 | 0.358 | 0.321 | 0.301 | 0.339 | 0.147 | 0.123 | 0.170 |
| sign_no_pre_activity | 11,811 | 2,297 | 0.615 | 0.403 | 0.212 | 0.190 | 0.234 | 0.113 | 0.085 | 0.140 |

**Verdict against the Level 1 criterion**

| sign | adjusted_rd | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | two_thirds_same_direction | verdict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 0.407 | yes | yes | 4 | 4 | yes | consistent association |
| sign_tma_late | 0.217 | yes | yes | 4 | 4 | yes | consistent association |
| sign_inactive_last7 | 0.135 | yes | yes | 6 | 6 | yes | consistent association |
| sign_low_activity | 0.147 | yes | yes | 6 | 6 | yes | consistent association |
| sign_no_pre_activity | 0.113 | yes | yes | 6 | 6 | yes | consistent association |
[saved] aq-2/results/associations_2013.csv  (5 rows x 22 columns)

**Adjusted risk difference by module (modules with at least 20 enrolments with and without the sign)**

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 369 | 23 | 0.436 | 0.219 | 0.653 |
| sign_task_missed | BBB | 3,364 | 421 | 0.448 | 0.398 | 0.497 |
| sign_task_missed | DDD | 2,790 | 533 | 0.352 | 0.304 | 0.401 |
| sign_task_missed | FFF | 3,437 | 308 | 0.408 | 0.347 | 0.469 |
| sign_tma_late | AAA | 369 | 52 | 0.198 | 0.063 | 0.333 |
| sign_tma_late | BBB | 3,364 | 254 | 0.224 | 0.167 | 0.281 |
| sign_tma_late | DDD | 2,790 | 62 | 0.171 | 0.063 | 0.280 |
| sign_tma_late | FFF | 3,437 | 209 | 0.248 | 0.186 | 0.310 |
| sign_inactive_last7 | AAA | 369 | 65 | 0.049 | -0.082 | 0.179 |
| sign_inactive_last7 | BBB | 3,364 | 968 | 0.088 | 0.044 | 0.132 |
| sign_inactive_last7 | DDD | 2,790 | 248 | 0.193 | 0.092 | 0.294 |
| sign_inactive_last7 | EEE | 927 | 171 | 0.193 | 0.096 | 0.291 |
| sign_inactive_last7 | FFF | 3,437 | 486 | 0.153 | 0.093 | 0.212 |
| sign_inactive_last7 | GGG | 924 | 506 | 0.039 | -0.033 | 0.111 |
| sign_low_activity | AAA | 369 | 79 | 0.141 | 0.010 | 0.272 |
| sign_low_activity | BBB | 3,364 | 1,040 | 0.108 | 0.065 | 0.151 |
| sign_low_activity | DDD | 2,790 | 735 | 0.161 | 0.115 | 0.208 |
| sign_low_activity | EEE | 927 | 170 | 0.346 | 0.249 | 0.444 |
| sign_low_activity | FFF | 3,437 | 842 | 0.124 | 0.077 | 0.170 |
| sign_low_activity | GGG | 924 | 309 | 0.129 | 0.050 | 0.207 |
| sign_no_pre_activity | AAA | 369 | 25 | 0.093 | -0.088 | 0.274 |
| sign_no_pre_activity | BBB | 3,364 | 1,033 | 0.082 | 0.045 | 0.119 |
| sign_no_pre_activity | DDD | 2,790 | 306 | 0.136 | 0.071 | 0.200 |
| sign_no_pre_activity | EEE | 927 | 211 | 0.162 | 0.084 | 0.240 |
| sign_no_pre_activity | FFF | 3,437 | 364 | 0.131 | 0.069 | 0.193 |
| sign_no_pre_activity | GGG | 924 | 358 | 0.047 | -0.020 | 0.114 |
[saved] aq-2/results/associations_by_module_2013.csv  (26 rows x 7 columns)

model: 37 coefficients, converged = True, log-likelihood = -6956.1, deviance = 13912.2
[saved] aq-2/results/model_coefficients_2013.csv  (37 rows x 4 columns)

**Odds ratios, model without sign x module terms (they read larger than risk ratios at a 44% base rate)**

| term | odds_ratio | or_ci_low | or_ci_high | p_value | adjusted_rd_no_interactions |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 7.490 | 6.140 | 9.137 | 0.000 | 0.403 |
| sign_tma_late | 2.894 | 2.398 | 3.492 | 0.000 | 0.220 |
| sign_inactive_last7 | 1.667 | 1.467 | 1.894 | 0.000 | 0.108 |
| sign_low_activity | 1.949 | 1.751 | 2.169 | 0.000 | 0.144 |
| sign_no_pre_activity | 1.618 | 1.444 | 1.813 | 0.000 | 0.101 |
[saved] aq-2/results/odds_ratios_2013.csv  (5 rows x 6 columns)

**Phi correlation between signs (all enrolments)**

| sign | sign_task_missed | sign_tma_late | sign_inactive_last7 | sign_low_activity | sign_no_pre_activity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 1.000 | -0.079 | 0.315 | 0.377 | 0.192 |
| sign_tma_late | -0.079 | 1.000 | -0.058 | 0.035 | 0.041 |
| sign_inactive_last7 | 0.315 | -0.058 | 1.000 | 0.496 | 0.315 |
| sign_low_activity | 0.377 | 0.035 | 0.496 | 1.000 | 0.300 |
| sign_no_pre_activity | 0.192 | 0.041 | 0.315 | 0.300 | 1.000 |
[saved] aq-2/results/sign_correlation_2013.csv  (5 rows x 6 columns)

**Non-completion by number of signs present**

| signs_present | enrolments | non_completion_rate |
| :---- | :---- | :---- |
| 0 | 6,554 | 0.306 |
| 1 | 2,477 | 0.508 |
| 2 | 1,430 | 0.631 |
| 3 | 959 | 0.739 |
| 4 | 391 | 0.944 |
[saved] aq-2/results/non_completion_by_sign_count_2013.csv  (5 rows x 3 columns)

**Binned residuals: observed minus predicted non-completion by run and activity level**

| run | activity_level | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | low | 78 | 0.449 | 0.451 | -0.002 | 0.113 | no |
| AAA-2013J | none | 1 | 1.000 | 0.854 | 0.146 | 0.705 | no |
| AAA-2013J | normal | 290 | 0.190 | 0.190 | -0.000 | 0.046 | no |
| BBB-2013B | low | 341 | 0.660 | 0.670 | -0.010 | 0.051 | no |
| BBB-2013B | none | 97 | 0.948 | 0.919 | 0.029 | 0.055 | no |
| BBB-2013B | normal | 1,092 | 0.376 | 0.376 | 0.000 | 0.029 | no |
| BBB-2013J | low | 457 | 0.562 | 0.557 | 0.005 | 0.046 | no |
| BBB-2013J | none | 145 | 0.779 | 0.792 | -0.012 | 0.067 | no |
| BBB-2013J | normal | 1,232 | 0.319 | 0.319 | -0.000 | 0.027 | no |
| DDD-2013B | low | 257 | 0.786 | 0.793 | -0.007 | 0.051 | no |
| DDD-2013B | none | 39 | 0.974 | 0.968 | 0.006 | 0.056 | no |
| DDD-2013B | normal | 847 | 0.465 | 0.463 | 0.002 | 0.034 | no |
| DDD-2013J | low | 395 | 0.739 | 0.733 | 0.007 | 0.045 | no |
| DDD-2013J | none | 44 | 0.909 | 0.933 | -0.024 | 0.075 | no |
| DDD-2013J | normal | 1,208 | 0.403 | 0.404 | -0.001 | 0.028 | no |
| EEE-2013J | low | 131 | 0.702 | 0.716 | -0.014 | 0.079 | no |
| EEE-2013J | none | 39 | 0.897 | 0.850 | 0.048 | 0.114 | no |
| EEE-2013J | normal | 757 | 0.252 | 0.252 | -0.000 | 0.032 | no |
| FFF-2013B | low | 314 | 0.656 | 0.672 | -0.016 | 0.053 | no |
| FFF-2013B | none | 36 | 0.972 | 0.957 | 0.015 | 0.068 | no |
| FFF-2013B | normal | 1,104 | 0.390 | 0.386 | 0.004 | 0.029 | no |
| FFF-2013J | low | 445 | 0.674 | 0.672 | 0.002 | 0.045 | no |
| FFF-2013J | none | 47 | 0.979 | 0.904 | 0.075 | 0.086 | no |
| FFF-2013J | normal | 1,491 | 0.364 | 0.366 | -0.003 | 0.025 | no |
| GGG-2013J | low | 150 | 0.353 | 0.457 | -0.104 | 0.081 | yes |
| GGG-2013J | none | 159 | 0.579 | 0.481 | 0.098 | 0.079 | yes |
| GGG-2013J | normal | 615 | 0.304 | 0.304 | 0.000 | 0.037 | no |

cells outside two standard errors: 2 of 27; largest |residual| = 0.146
[saved] aq-2/results/binned_residuals_2013.csv  (27 rows x 8 columns)

**Sensitivity of the adjusted risk differences**

| variant | enrolments | sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| main | 11,811 | sign_task_missed | 0.407 | 0.375 | 0.438 |
| main | 11,811 | sign_tma_late | 0.217 | 0.174 | 0.259 |
| main | 11,811 | sign_inactive_last7 | 0.135 | 0.101 | 0.168 |
| main | 11,811 | sign_low_activity | 0.147 | 0.123 | 0.170 |
| main | 11,811 | sign_no_pre_activity | 0.113 | 0.085 | 0.140 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 11,811 | sign_task_missed | 0.406 | 0.375 | 0.437 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 11,811 | sign_tma_late | 0.216 | 0.174 | 0.258 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 11,811 | sign_inactive_last7 | 0.135 | 0.101 | 0.169 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 11,811 | sign_low_activity_dedup | 0.148 | 0.124 | 0.172 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 11,811 | sign_no_pre_activity | 0.112 | 0.084 | 0.140 |
| late CMAs also count as late | 11,811 | sign_task_missed | 0.406 | 0.374 | 0.437 |
| late CMAs also count as late | 11,811 | sign_any_task_late | 0.167 | 0.128 | 0.206 |
| late CMAs also count as late | 11,811 | sign_inactive_last7 | 0.134 | 0.100 | 0.168 |
| late CMAs also count as late | 11,811 | sign_low_activity | 0.147 | 0.123 | 0.171 |
| late CMAs also count as late | 11,811 | sign_no_pre_activity | 0.113 | 0.085 | 0.141 |
| without flagged enrolments | 11,803 | sign_task_missed | 0.407 | 0.375 | 0.438 |
| without flagged enrolments | 11,803 | sign_tma_late | 0.217 | 0.175 | 0.259 |
| without flagged enrolments | 11,803 | sign_inactive_last7 | 0.135 | 0.101 | 0.168 |
| without flagged enrolments | 11,803 | sign_low_activity | 0.146 | 0.123 | 0.170 |
| without flagged enrolments | 11,803 | sign_no_pre_activity | 0.113 | 0.085 | 0.140 |
| only runs with a task due by day 27 | 9,960 | sign_task_missed | 0.406 | 0.375 | 0.438 |
| only runs with a task due by day 27 | 9,960 | sign_tma_late | 0.216 | 0.174 | 0.259 |
| only runs with a task due by day 27 | 9,960 | sign_inactive_last7 | 0.138 | 0.100 | 0.177 |
| only runs with a task due by day 27 | 9,960 | sign_low_activity | 0.129 | 0.104 | 0.155 |
| only runs with a task due by day 27 | 9,960 | sign_no_pre_activity | 0.114 | 0.083 | 0.145 |
| low activity = below a quarter of the run median | 11,811 | sign_task_missed | 0.414 | 0.382 | 0.445 |
| low activity = below a quarter of the run median | 11,811 | sign_tma_late | 0.224 | 0.183 | 0.266 |
| low activity = below a quarter of the run median | 11,811 | sign_inactive_last7 | 0.154 | 0.121 | 0.188 |
| low activity = below a quarter of the run median | 11,811 | sign_low_activity_q25 | 0.144 | 0.110 | 0.178 |
| low activity = below a quarter of the run median | 11,811 | sign_no_pre_activity | 0.120 | 0.093 | 0.148 |
| low activity = below the run median | 11,811 | sign_task_missed | 0.409 | 0.378 | 0.440 |
| low activity = below the run median | 11,811 | sign_tma_late | 0.203 | 0.160 | 0.246 |
| low activity = below the run median | 11,811 | sign_inactive_last7 | 0.143 | 0.112 | 0.175 |
| low activity = below the run median | 11,811 | sign_low_activity_median | 0.134 | 0.115 | 0.152 |
| low activity = below the run median | 11,811 | sign_no_pre_activity | 0.106 | 0.078 | 0.133 |
[saved] aq-2/results/sensitivity_2013.csv  (35 rows x 6 columns)

**Risk differences by audit group (description; the groups are not model inputs)**

| attribute | group | sign | enrolments | with_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | sign_task_missed | 4,852 | 604 | 0.524 | 0.494 | 0.549 | 0.423 | 0.389 | 0.457 |
| gender | F | sign_tma_late | 4,852 | 311 | 0.180 | 0.123 | 0.234 | 0.216 | 0.172 | 0.260 |
| gender | F | sign_inactive_last7 | 5,697 | 1,454 | 0.217 | 0.188 | 0.246 | 0.111 | 0.078 | 0.143 |
| gender | F | sign_low_activity | 5,697 | 1,553 | 0.298 | 0.270 | 0.325 | 0.128 | 0.101 | 0.156 |
| gender | F | sign_no_pre_activity | 5,697 | 1,342 | 0.190 | 0.160 | 0.220 | 0.095 | 0.069 | 0.121 |
| gender | M | sign_task_missed | 5,108 | 681 | 0.484 | 0.455 | 0.510 | 0.391 | 0.353 | 0.430 |
| gender | M | sign_tma_late | 5,108 | 266 | 0.194 | 0.134 | 0.251 | 0.217 | 0.168 | 0.267 |
| gender | M | sign_inactive_last7 | 6,114 | 990 | 0.312 | 0.280 | 0.342 | 0.157 | 0.116 | 0.199 |
| gender | M | sign_low_activity | 6,114 | 1,622 | 0.342 | 0.315 | 0.368 | 0.163 | 0.135 | 0.192 |
| gender | M | sign_no_pre_activity | 6,114 | 955 | 0.250 | 0.216 | 0.282 | 0.129 | 0.093 | 0.165 |
| disability | N | sign_task_missed | 9,004 | 1,112 | 0.508 | 0.486 | 0.528 | 0.407 | 0.376 | 0.439 |
| disability | N | sign_tma_late | 9,004 | 517 | 0.183 | 0.139 | 0.225 | 0.218 | 0.175 | 0.260 |
| disability | N | sign_inactive_last7 | 10,688 | 2,206 | 0.257 | 0.235 | 0.280 | 0.135 | 0.102 | 0.169 |
| disability | N | sign_low_activity | 10,688 | 2,861 | 0.323 | 0.303 | 0.343 | 0.148 | 0.124 | 0.171 |
| disability | N | sign_no_pre_activity | 10,688 | 2,081 | 0.217 | 0.194 | 0.240 | 0.113 | 0.086 | 0.141 |
| disability | Y | sign_task_missed | 956 | 173 | 0.440 | 0.379 | 0.486 | 0.400 | 0.371 | 0.430 |
| disability | Y | sign_tma_late | 956 | 60 | 0.198 | 0.071 | 0.295 | 0.207 | 0.165 | 0.249 |
| disability | Y | sign_inactive_last7 | 1,123 | 238 | 0.205 | 0.135 | 0.269 | 0.129 | 0.095 | 0.163 |
| disability | Y | sign_low_activity | 1,123 | 314 | 0.290 | 0.229 | 0.347 | 0.138 | 0.114 | 0.161 |
| disability | Y | sign_no_pre_activity | 1,123 | 216 | 0.167 | 0.095 | 0.235 | 0.107 | 0.080 | 0.134 |
| imd_group | 0-30% (most deprived) | sign_task_missed | 3,132 | 511 | 0.442 | 0.410 | 0.469 | 0.402 | 0.371 | 0.432 |
| imd_group | 0-30% (most deprived) | sign_tma_late | 3,132 | 223 | 0.165 | 0.100 | 0.223 | 0.212 | 0.173 | 0.251 |
| imd_group | 0-30% (most deprived) | sign_inactive_last7 | 3,690 | 886 | 0.247 | 0.211 | 0.280 | 0.127 | 0.095 | 0.158 |
| imd_group | 0-30% (most deprived) | sign_low_activity | 3,690 | 1,116 | 0.313 | 0.280 | 0.343 | 0.138 | 0.115 | 0.162 |
| imd_group | 0-30% (most deprived) | sign_no_pre_activity | 3,690 | 861 | 0.207 | 0.170 | 0.242 | 0.107 | 0.081 | 0.133 |
| imd_group | 30-70% | sign_task_missed | 3,936 | 493 | 0.516 | 0.481 | 0.545 | 0.408 | 0.377 | 0.439 |
| imd_group | 30-70% | sign_tma_late | 3,936 | 219 | 0.183 | 0.115 | 0.247 | 0.217 | 0.175 | 0.259 |
| imd_group | 30-70% | sign_inactive_last7 | 4,684 | 981 | 0.237 | 0.202 | 0.271 | 0.134 | 0.101 | 0.168 |
| imd_group | 30-70% | sign_low_activity | 4,684 | 1,274 | 0.310 | 0.279 | 0.340 | 0.147 | 0.123 | 0.170 |
| imd_group | 30-70% | sign_no_pre_activity | 4,684 | 921 | 0.187 | 0.151 | 0.222 | 0.112 | 0.085 | 0.139 |
| imd_group | 70-100% (least deprived) | sign_task_missed | 2,527 | 249 | 0.550 | 0.501 | 0.589 | 0.411 | 0.378 | 0.444 |
| imd_group | 70-100% (least deprived) | sign_tma_late | 2,527 | 115 | 0.155 | 0.062 | 0.245 | 0.221 | 0.176 | 0.265 |
| imd_group | 70-100% (least deprived) | sign_inactive_last7 | 3,019 | 546 | 0.238 | 0.192 | 0.283 | 0.141 | 0.105 | 0.177 |
| imd_group | 70-100% (least deprived) | sign_low_activity | 3,019 | 719 | 0.308 | 0.267 | 0.348 | 0.154 | 0.129 | 0.179 |
| imd_group | 70-100% (least deprived) | sign_no_pre_activity | 3,019 | 480 | 0.198 | 0.150 | 0.246 | 0.118 | 0.088 | 0.147 |
| imd_group | Missing | sign_task_missed | 365 | 32 | 0.329 | 0.151 | 0.487 | 0.409 | 0.370 | 0.447 |
| imd_group | Missing | sign_tma_late | 365 | 20 | 0.272 | 0.058 | 0.469 | 0.228 | 0.173 | 0.284 |
| imd_group | Missing | sign_inactive_last7 | 418 | 31 | 0.253 | 0.079 | 0.422 | 0.166 | 0.120 | 0.213 |
| imd_group | Missing | sign_low_activity | 418 | 66 | 0.330 | 0.202 | 0.451 | 0.166 | 0.136 | 0.195 |
| imd_group | Missing | sign_no_pre_activity | 418 | 35 | 0.284 | 0.117 | 0.442 | 0.135 | 0.097 | 0.172 |
[saved] aq-2/results/subgroups_2013.csv  (40 rows x 11 columns)

