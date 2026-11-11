# Log: aq-2 / 02_associations_2014

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:23:53Z |
| Finished (UTC) | 2026-11-11T23:23:56Z |
| Duration | 3.3 s |
| Command | `python aq-2/code/02_associations.py --scope 2014` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 associations at day 27, scope = 2014: 15,724 enrolments, 13 runs, 6,911 non-completers (44.0%)

**Risk difference per sign (percentage points = value x 100)**

| sign | enrolments_defined | with_sign | rate_with_sign | rate_without_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 12,585 | 1,368 | 0.890 | 0.403 | 0.488 | 0.468 | 0.506 | 0.396 | 0.368 | 0.425 |
| sign_tma_late | 12,585 | 429 | 0.594 | 0.451 | 0.144 | 0.096 | 0.190 | 0.162 | 0.129 | 0.196 |
| sign_inactive_last7 | 15,724 | 3,440 | 0.647 | 0.381 | 0.265 | 0.247 | 0.283 | 0.154 | 0.128 | 0.181 |
| sign_low_activity | 15,724 | 4,099 | 0.663 | 0.361 | 0.302 | 0.285 | 0.319 | 0.148 | 0.127 | 0.168 |
| sign_no_pre_activity | 15,724 | 3,161 | 0.583 | 0.403 | 0.179 | 0.160 | 0.198 | 0.092 | 0.069 | 0.114 |

**Verdict against the Level 1 criterion**

| sign | adjusted_rd | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | two_thirds_same_direction | verdict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 0.396 | yes | yes | 5 | 5 | yes | consistent association |
| sign_tma_late | 0.162 | yes | yes | 4 | 4 | yes | consistent association |
| sign_inactive_last7 | 0.154 | yes | yes | 7 | 7 | yes | consistent association |
| sign_low_activity | 0.148 | yes | yes | 7 | 7 | yes | consistent association |
| sign_no_pre_activity | 0.092 | yes | yes | 7 | 7 | yes | consistent association |
[saved] aq-2/results/associations_2014.csv  (5 rows x 22 columns)

**Adjusted risk difference by module (modules with at least 20 enrolments with and without the sign)**

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 348 | 28 | 0.415 | 0.235 | 0.594 |
| sign_task_missed | BBB | 3,066 | 220 | 0.534 | 0.480 | 0.588 |
| sign_task_missed | CCC | 3,521 | 402 | 0.353 | 0.302 | 0.404 |
| sign_task_missed | DDD | 2,492 | 302 | 0.367 | 0.305 | 0.428 |
| sign_task_missed | FFF | 3,158 | 416 | 0.332 | 0.269 | 0.395 |
| sign_tma_late | AAA | 348 | 53 | 0.002 | -0.132 | 0.135 |
| sign_tma_late | BBB | 3,066 | 191 | 0.257 | 0.189 | 0.326 |
| sign_tma_late | DDD | 2,492 | 99 | 0.208 | 0.122 | 0.293 |
| sign_tma_late | FFF | 3,158 | 86 | 0.233 | 0.139 | 0.327 |
| sign_inactive_last7 | AAA | 348 | 71 | 0.165 | 0.032 | 0.298 |
| sign_inactive_last7 | BBB | 3,066 | 937 | 0.122 | 0.079 | 0.166 |
| sign_inactive_last7 | CCC | 3,521 | 755 | 0.189 | 0.147 | 0.231 |
| sign_inactive_last7 | DDD | 2,492 | 328 | 0.142 | 0.068 | 0.216 |
| sign_inactive_last7 | EEE | 1,625 | 298 | 0.136 | 0.064 | 0.208 |
| sign_inactive_last7 | FFF | 3,158 | 293 | 0.168 | 0.081 | 0.255 |
| sign_inactive_last7 | GGG | 1,514 | 758 | 0.146 | 0.091 | 0.202 |
| sign_low_activity | AAA | 348 | 91 | 0.008 | -0.098 | 0.113 |
| sign_low_activity | BBB | 3,066 | 916 | 0.074 | 0.031 | 0.117 |
| sign_low_activity | CCC | 3,521 | 804 | 0.086 | 0.040 | 0.132 |
| sign_low_activity | DDD | 2,492 | 626 | 0.176 | 0.125 | 0.227 |
| sign_low_activity | EEE | 1,625 | 347 | 0.290 | 0.220 | 0.360 |
| sign_low_activity | FFF | 3,158 | 818 | 0.205 | 0.160 | 0.251 |
| sign_low_activity | GGG | 1,514 | 497 | 0.153 | 0.093 | 0.213 |
| sign_no_pre_activity | AAA | 348 | 21 | 0.097 | -0.091 | 0.286 |
| sign_no_pre_activity | BBB | 3,066 | 901 | 0.013 | -0.024 | 0.050 |
| sign_no_pre_activity | CCC | 3,521 | 532 | 0.130 | 0.080 | 0.179 |
| sign_no_pre_activity | DDD | 2,492 | 255 | 0.060 | -0.013 | 0.132 |
| sign_no_pre_activity | EEE | 1,625 | 327 | 0.225 | 0.163 | 0.287 |
| sign_no_pre_activity | FFF | 3,158 | 433 | 0.089 | 0.035 | 0.144 |
| sign_no_pre_activity | GGG | 1,514 | 692 | 0.074 | 0.024 | 0.123 |
[saved] aq-2/results/associations_by_module_2014.csv  (30 rows x 7 columns)

**Sign x module cells below the minimum size**

| sign | module | with_sign | without_sign | handling |
| :---- | :---- | :---- | :---- | :---- |
| sign_tma_late | CCC | 0 | 3,521 | not defined (cell below 20); pooled slope |
[saved] aq-2/results/small_cells_2014.csv  (1 rows x 5 columns)

model: 45 coefficients, converged = True, log-likelihood = -9375.8, deviance = 18751.6
[saved] aq-2/results/model_coefficients_2014.csv  (45 rows x 4 columns)

**Odds ratios, model without sign x module terms (they read larger than risk ratios at a 44% base rate)**

| term | odds_ratio | or_ci_low | or_ci_high | p_value | adjusted_rd_no_interactions |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 6.559 | 5.453 | 7.889 | 0.000 | 0.381 |
| sign_tma_late | 2.673 | 2.165 | 3.301 | 0.000 | 0.206 |
| sign_inactive_last7 | 1.991 | 1.801 | 2.201 | 0.000 | 0.150 |
| sign_low_activity | 1.932 | 1.765 | 2.116 | 0.000 | 0.144 |
| sign_no_pre_activity | 1.505 | 1.368 | 1.656 | 0.000 | 0.087 |
[saved] aq-2/results/odds_ratios_2014.csv  (5 rows x 6 columns)

**Phi correlation between signs (all enrolments)**

| sign | sign_task_missed | sign_tma_late | sign_inactive_last7 | sign_low_activity | sign_no_pre_activity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 1.000 | -0.052 | 0.250 | 0.344 | 0.151 |
| sign_tma_late | -0.052 | 1.000 | -0.034 | 0.029 | 0.033 |
| sign_inactive_last7 | 0.250 | -0.034 | 1.000 | 0.444 | 0.288 |
| sign_low_activity | 0.344 | 0.029 | 0.444 | 1.000 | 0.271 |
| sign_no_pre_activity | 0.151 | 0.033 | 0.288 | 0.271 | 1.000 |
[saved] aq-2/results/sign_correlation_2014.csv  (5 rows x 6 columns)

**Non-completion by number of signs present**

| signs_present | enrolments | non_completion_rate |
| :---- | :---- | :---- |
| 0 | 8,701 | 0.313 |
| 1 | 3,516 | 0.501 |
| 2 | 1,927 | 0.593 |
| 3 | 1,193 | 0.764 |
| 4 | 387 | 0.953 |
[saved] aq-2/results/non_completion_by_sign_count_2014.csv  (5 rows x 3 columns)

**Binned residuals: observed minus predicted non-completion by run and activity level**

| run | activity_level | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | low | 89 | 0.348 | 0.349 | -0.001 | 0.101 | no |
| AAA-2014J | none | 2 | 0.500 | 0.451 | 0.049 | 0.704 | no |
| AAA-2014J | normal | 257 | 0.245 | 0.245 | -0.000 | 0.054 | no |
| BBB-2014B | low | 340 | 0.553 | 0.553 | -0.000 | 0.054 | no |
| BBB-2014B | none | 85 | 0.859 | 0.839 | 0.020 | 0.080 | no |
| BBB-2014B | normal | 855 | 0.342 | 0.343 | -0.002 | 0.032 | no |
| BBB-2014J | low | 430 | 0.463 | 0.464 | -0.001 | 0.048 | no |
| BBB-2014J | none | 61 | 0.787 | 0.808 | -0.021 | 0.101 | no |
| BBB-2014J | normal | 1,295 | 0.300 | 0.298 | 0.001 | 0.025 | no |
| CCC-2014B | low | 308 | 0.760 | 0.760 | -0.001 | 0.049 | no |
| CCC-2014B | none | 45 | 1.000 | 0.964 | 0.036 | 0.056 | no |
| CCC-2014B | normal | 1,147 | 0.486 | 0.488 | -0.001 | 0.030 | no |
| CCC-2014J | low | 411 | 0.696 | 0.694 | 0.002 | 0.045 | no |
| CCC-2014J | none | 40 | 0.875 | 0.935 | -0.060 | 0.078 | no |
| CCC-2014J | normal | 1,570 | 0.436 | 0.435 | 0.001 | 0.025 | no |
| DDD-2014B | low | 244 | 0.787 | 0.765 | 0.021 | 0.054 | no |
| DDD-2014B | none | 30 | 0.900 | 0.939 | -0.039 | 0.087 | no |
| DDD-2014B | normal | 755 | 0.440 | 0.445 | -0.005 | 0.036 | no |
| DDD-2014J | low | 316 | 0.680 | 0.694 | -0.014 | 0.052 | no |
| DDD-2014J | none | 36 | 0.889 | 0.882 | 0.007 | 0.108 | no |
| DDD-2014J | normal | 1,111 | 0.382 | 0.378 | 0.004 | 0.029 | no |
| EEE-2014B | low | 102 | 0.706 | 0.739 | -0.033 | 0.087 | no |
| EEE-2014B | none | 22 | 0.955 | 0.875 | 0.079 | 0.141 | no |
| EEE-2014B | normal | 481 | 0.322 | 0.319 | 0.003 | 0.042 | no |
| EEE-2014J | low | 193 | 0.642 | 0.638 | 0.005 | 0.069 | no |
| EEE-2014J | none | 30 | 0.833 | 0.810 | 0.024 | 0.143 | no |
| EEE-2014J | normal | 797 | 0.235 | 0.237 | -0.002 | 0.030 | no |
| FFF-2014B | low | 306 | 0.732 | 0.760 | -0.028 | 0.049 | no |
| FFF-2014B | none | 32 | 0.906 | 0.952 | -0.046 | 0.075 | no |
| FFF-2014B | normal | 961 | 0.408 | 0.398 | 0.010 | 0.032 | no |
| FFF-2014J | low | 434 | 0.680 | 0.661 | 0.019 | 0.045 | no |
| FFF-2014J | none | 46 | 0.935 | 0.900 | 0.035 | 0.089 | no |
| FFF-2014J | normal | 1,379 | 0.293 | 0.300 | -0.007 | 0.025 | no |
| GGG-2014B | low | 159 | 0.497 | 0.553 | -0.056 | 0.079 | no |
| GGG-2014B | none | 98 | 0.704 | 0.611 | 0.093 | 0.098 | no |
| GGG-2014B | normal | 540 | 0.317 | 0.317 | -0.000 | 0.040 | no |
| GGG-2014J | low | 143 | 0.462 | 0.515 | -0.054 | 0.084 | no |
| GGG-2014J | none | 97 | 0.670 | 0.593 | 0.077 | 0.100 | no |
| GGG-2014J | normal | 477 | 0.298 | 0.297 | 0.000 | 0.042 | no |

cells outside two standard errors: 0 of 39; largest |residual| = 0.093
[saved] aq-2/results/binned_residuals_2014.csv  (39 rows x 8 columns)

**Sensitivity of the adjusted risk differences**

| variant | enrolments | sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| main | 15,724 | sign_task_missed | 0.396 | 0.368 | 0.425 |
| main | 15,724 | sign_tma_late | 0.162 | 0.129 | 0.196 |
| main | 15,724 | sign_inactive_last7 | 0.154 | 0.128 | 0.181 |
| main | 15,724 | sign_low_activity | 0.148 | 0.127 | 0.168 |
| main | 15,724 | sign_no_pre_activity | 0.092 | 0.069 | 0.114 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 15,724 | sign_task_missed | 0.398 | 0.369 | 0.426 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 15,724 | sign_tma_late | 0.163 | 0.129 | 0.197 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 15,724 | sign_inactive_last7 | 0.155 | 0.128 | 0.181 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 15,724 | sign_low_activity_dedup | 0.146 | 0.125 | 0.166 |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | 15,724 | sign_no_pre_activity | 0.091 | 0.069 | 0.114 |
| late CMAs also count as late | 15,724 | sign_task_missed | 0.409 | 0.372 | 0.445 |
| late CMAs also count as late | 15,724 | sign_any_task_late | 0.183 | 0.128 | 0.238 |
| late CMAs also count as late | 15,724 | sign_inactive_last7 | 0.154 | 0.128 | 0.181 |
| late CMAs also count as late | 15,724 | sign_low_activity | 0.148 | 0.128 | 0.169 |
| late CMAs also count as late | 15,724 | sign_no_pre_activity | 0.092 | 0.069 | 0.114 |
| without flagged enrolments | 15,632 | sign_task_missed | 0.393 | 0.364 | 0.422 |
| without flagged enrolments | 15,632 | sign_tma_late | 0.163 | 0.129 | 0.197 |
| without flagged enrolments | 15,632 | sign_inactive_last7 | 0.151 | 0.124 | 0.178 |
| without flagged enrolments | 15,632 | sign_low_activity | 0.148 | 0.128 | 0.169 |
| without flagged enrolments | 15,632 | sign_no_pre_activity | 0.092 | 0.070 | 0.115 |
| only runs with a task due by day 27 | 12,585 | sign_task_missed | 0.397 | 0.368 | 0.425 |
| only runs with a task due by day 27 | 12,585 | sign_tma_late | 0.162 | 0.129 | 0.196 |
| only runs with a task due by day 27 | 12,585 | sign_inactive_last7 | 0.157 | 0.126 | 0.188 |
| only runs with a task due by day 27 | 12,585 | sign_low_activity | 0.127 | 0.104 | 0.150 |
| only runs with a task due by day 27 | 12,585 | sign_no_pre_activity | 0.076 | 0.050 | 0.102 |
| low activity = below a quarter of the run median | 15,724 | sign_task_missed | 0.404 | 0.375 | 0.432 |
| low activity = below a quarter of the run median | 15,724 | sign_tma_late | 0.171 | 0.138 | 0.204 |
| low activity = below a quarter of the run median | 15,724 | sign_inactive_last7 | 0.170 | 0.144 | 0.196 |
| low activity = below a quarter of the run median | 15,724 | sign_low_activity_q25 | 0.152 | 0.120 | 0.184 |
| low activity = below a quarter of the run median | 15,724 | sign_no_pre_activity | 0.099 | 0.076 | 0.121 |
| low activity = below the run median | 15,724 | sign_task_missed | 0.393 | 0.365 | 0.421 |
| low activity = below the run median | 15,724 | sign_tma_late | 0.157 | 0.123 | 0.191 |
| low activity = below the run median | 15,724 | sign_inactive_last7 | 0.157 | 0.132 | 0.183 |
| low activity = below the run median | 15,724 | sign_low_activity_median | 0.146 | 0.130 | 0.162 |
| low activity = below the run median | 15,724 | sign_no_pre_activity | 0.086 | 0.064 | 0.108 |
[saved] aq-2/results/sensitivity_2014.csv  (35 rows x 6 columns)

**Risk differences by audit group (description; the groups are not model inputs)**

| attribute | group | sign | enrolments | with_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | sign_task_missed | 5,254 | 446 | 0.520 | 0.485 | 0.548 | 0.450 | 0.418 | 0.483 |
| gender | F | sign_tma_late | 5,254 | 238 | 0.184 | 0.119 | 0.246 | 0.197 | 0.157 | 0.237 |
| gender | F | sign_inactive_last7 | 6,666 | 1,837 | 0.231 | 0.204 | 0.257 | 0.144 | 0.119 | 0.170 |
| gender | F | sign_low_activity | 6,666 | 1,753 | 0.257 | 0.230 | 0.283 | 0.121 | 0.098 | 0.145 |
| gender | F | sign_no_pre_activity | 6,666 | 1,631 | 0.136 | 0.108 | 0.163 | 0.061 | 0.039 | 0.084 |
| gender | M | sign_task_missed | 7,331 | 922 | 0.465 | 0.440 | 0.488 | 0.358 | 0.326 | 0.390 |
| gender | M | sign_tma_late | 7,331 | 191 | 0.114 | 0.042 | 0.182 | 0.137 | 0.100 | 0.175 |
| gender | M | sign_inactive_last7 | 9,058 | 1,603 | 0.321 | 0.296 | 0.345 | 0.161 | 0.129 | 0.194 |
| gender | M | sign_low_activity | 9,058 | 2,346 | 0.337 | 0.315 | 0.358 | 0.167 | 0.143 | 0.191 |
| gender | M | sign_no_pre_activity | 9,058 | 1,530 | 0.235 | 0.209 | 0.261 | 0.114 | 0.087 | 0.140 |
| disability | N | sign_task_missed | 11,416 | 1,198 | 0.497 | 0.476 | 0.516 | 0.398 | 0.370 | 0.426 |
| disability | N | sign_tma_late | 11,416 | 368 | 0.139 | 0.087 | 0.189 | 0.162 | 0.128 | 0.195 |
| disability | N | sign_inactive_last7 | 14,236 | 3,087 | 0.273 | 0.254 | 0.292 | 0.155 | 0.128 | 0.181 |
| disability | N | sign_low_activity | 14,236 | 3,665 | 0.305 | 0.287 | 0.323 | 0.148 | 0.127 | 0.168 |
| disability | N | sign_no_pre_activity | 14,236 | 2,830 | 0.182 | 0.162 | 0.202 | 0.092 | 0.070 | 0.115 |
| disability | Y | sign_task_missed | 1,169 | 170 | 0.388 | 0.324 | 0.437 | 0.380 | 0.352 | 0.408 |
| disability | Y | sign_tma_late | 1,169 | 61 | 0.133 | 0.005 | 0.239 | 0.168 | 0.133 | 0.203 |
| disability | Y | sign_inactive_last7 | 1,488 | 353 | 0.184 | 0.126 | 0.239 | 0.150 | 0.123 | 0.177 |
| disability | Y | sign_low_activity | 1,488 | 434 | 0.266 | 0.213 | 0.316 | 0.146 | 0.126 | 0.167 |
| disability | Y | sign_no_pre_activity | 1,488 | 331 | 0.141 | 0.081 | 0.199 | 0.082 | 0.060 | 0.105 |
| imd_group | 0-30% (most deprived) | sign_task_missed | 3,760 | 476 | 0.454 | 0.422 | 0.481 | 0.398 | 0.370 | 0.426 |
| imd_group | 0-30% (most deprived) | sign_tma_late | 3,760 | 166 | 0.179 | 0.104 | 0.246 | 0.172 | 0.137 | 0.206 |
| imd_group | 0-30% (most deprived) | sign_inactive_last7 | 4,769 | 1,215 | 0.246 | 0.215 | 0.276 | 0.150 | 0.124 | 0.176 |
| imd_group | 0-30% (most deprived) | sign_low_activity | 4,769 | 1,371 | 0.291 | 0.262 | 0.320 | 0.144 | 0.124 | 0.164 |
| imd_group | 0-30% (most deprived) | sign_no_pre_activity | 4,769 | 1,080 | 0.176 | 0.143 | 0.208 | 0.084 | 0.063 | 0.106 |
| imd_group | 30-70% | sign_task_missed | 4,943 | 554 | 0.493 | 0.461 | 0.520 | 0.399 | 0.370 | 0.427 |
| imd_group | 30-70% | sign_tma_late | 4,943 | 163 | 0.087 | 0.009 | 0.163 | 0.164 | 0.130 | 0.198 |
| imd_group | 30-70% | sign_inactive_last7 | 6,227 | 1,337 | 0.271 | 0.241 | 0.299 | 0.153 | 0.127 | 0.179 |
| imd_group | 30-70% | sign_low_activity | 6,227 | 1,623 | 0.300 | 0.273 | 0.327 | 0.147 | 0.127 | 0.168 |
| imd_group | 30-70% | sign_no_pre_activity | 6,227 | 1,282 | 0.185 | 0.154 | 0.215 | 0.091 | 0.069 | 0.113 |
| imd_group | 70-100% (least deprived) | sign_task_missed | 3,338 | 298 | 0.500 | 0.453 | 0.540 | 0.395 | 0.366 | 0.424 |
| imd_group | 70-100% (least deprived) | sign_tma_late | 3,338 | 91 | 0.120 | 0.017 | 0.221 | 0.154 | 0.121 | 0.188 |
| imd_group | 70-100% (least deprived) | sign_inactive_last7 | 4,118 | 814 | 0.242 | 0.204 | 0.279 | 0.158 | 0.131 | 0.185 |
| imd_group | 70-100% (least deprived) | sign_low_activity | 4,118 | 1,005 | 0.295 | 0.260 | 0.328 | 0.150 | 0.129 | 0.171 |
| imd_group | 70-100% (least deprived) | sign_no_pre_activity | 4,118 | 731 | 0.136 | 0.097 | 0.176 | 0.098 | 0.074 | 0.122 |
| imd_group | Missing | sign_task_missed | 544 | 40 | 0.434 | 0.275 | 0.559 | 0.373 | 0.340 | 0.407 |
| imd_group | Missing | sign_tma_late | 544 | 9 | 0.149 | -0.110 | 0.440 | 0.134 | 0.098 | 0.170 |
| imd_group | Missing | sign_inactive_last7 | 610 | 74 | 0.339 | 0.219 | 0.449 | 0.171 | 0.137 | 0.205 |
| imd_group | Missing | sign_low_activity | 610 | 100 | 0.315 | 0.210 | 0.415 | 0.160 | 0.134 | 0.185 |
| imd_group | Missing | sign_no_pre_activity | 610 | 68 | 0.229 | 0.107 | 0.350 | 0.112 | 0.082 | 0.142 |
[saved] aq-2/results/subgroups_2014.csv  (40 rows x 11 columns)

