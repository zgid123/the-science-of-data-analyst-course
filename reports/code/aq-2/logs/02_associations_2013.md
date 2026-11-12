# Log: aq-2 / 02_associations_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:48:13Z |
| Finished (UTC) | 2026-11-12T15:48:16Z |
| Duration | 2.8 s |
| Command | `python aq-2/code/02_associations.py --scope 2013` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 associations at day 27, scope = 2013: 11,811 enrolments, 9 runs, 5,245 non-completers (44.4%)

**Risk difference per sign (percentage points = value x 100); n = rows of the support, the only rows averaged over**

| sign | n | support_modules | rows_defined_outside_support | with_sign | rate_with_sign | rate_without_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 9,960 | 4 | 0 | 1,285 | 0.900 | 0.396 | 0.503 | 0.483 | 0.522 | 0.407 | 0.375 | 0.438 |
| sign_tma_late | 9,960 | 4 | 0 | 577 | 0.636 | 0.451 | 0.185 | 0.144 | 0.225 | 0.217 | 0.174 | 0.259 |
| sign_inactive_last7 | 11,811 | 6 | 0 | 2,444 | 0.644 | 0.392 | 0.253 | 0.231 | 0.274 | 0.135 | 0.101 | 0.168 |
| sign_low_activity | 11,811 | 6 | 0 | 3,175 | 0.678 | 0.358 | 0.321 | 0.301 | 0.339 | 0.147 | 0.123 | 0.170 |
| sign_no_pre_activity | 11,811 | 6 | 0 | 2,297 | 0.615 | 0.403 | 0.212 | 0.190 | 0.234 | 0.113 | 0.085 | 0.140 |

**Verdict against the Level 1 criterion (verdict = direction of the module point estimates, as Level 1 words it; verdict_strict = only modules whose own interval excludes 0)**

| sign | adjusted_rd | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | modules_same_direction_interval_excludes_0 | modules_interval_includes_0 | two_thirds_same_direction | verdict | verdict_strict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 0.407 | yes | yes | 4 | 4 | 4 | none | yes | consistent association | consistent association |
| sign_tma_late | 0.217 | yes | yes | 4 | 4 | 4 | none | yes | consistent association | consistent association |
| sign_inactive_last7 | 0.135 | yes | yes | 6 | 6 | 4 | AAA, GGG | yes | consistent association | consistent association |
| sign_low_activity | 0.147 | yes | yes | 6 | 6 | 6 | none | yes | consistent association | consistent association |
| sign_no_pre_activity | 0.113 | yes | yes | 6 | 6 | 4 | AAA, GGG | yes | consistent association | consistent association |
[saved] aq-2/results/associations_2013.csv  (5 rows x 29 columns)

**Adjusted risk difference by module (modules with their own slope: at least 20 enrolments with and 20 without the sign)**

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 369 | 23 | 0.436 | 0.219 | 0.653 | yes |
| sign_task_missed | BBB | 3,364 | 421 | 0.448 | 0.398 | 0.497 | yes |
| sign_task_missed | DDD | 2,790 | 533 | 0.352 | 0.304 | 0.401 | yes |
| sign_task_missed | FFF | 3,437 | 308 | 0.408 | 0.347 | 0.469 | yes |
| sign_tma_late | AAA | 369 | 52 | 0.198 | 0.063 | 0.333 | yes |
| sign_tma_late | BBB | 3,364 | 254 | 0.224 | 0.167 | 0.281 | yes |
| sign_tma_late | DDD | 2,790 | 62 | 0.171 | 0.063 | 0.280 | yes |
| sign_tma_late | FFF | 3,437 | 209 | 0.248 | 0.186 | 0.310 | yes |
| sign_inactive_last7 | AAA | 369 | 65 | 0.049 | -0.082 | 0.179 | no |
| sign_inactive_last7 | BBB | 3,364 | 968 | 0.088 | 0.044 | 0.132 | yes |
| sign_inactive_last7 | DDD | 2,790 | 248 | 0.193 | 0.092 | 0.294 | yes |
| sign_inactive_last7 | EEE | 927 | 171 | 0.193 | 0.096 | 0.291 | yes |
| sign_inactive_last7 | FFF | 3,437 | 486 | 0.153 | 0.093 | 0.212 | yes |
| sign_inactive_last7 | GGG | 924 | 506 | 0.039 | -0.033 | 0.111 | no |
| sign_low_activity | AAA | 369 | 79 | 0.141 | 0.010 | 0.272 | yes |
| sign_low_activity | BBB | 3,364 | 1,040 | 0.108 | 0.065 | 0.151 | yes |
| sign_low_activity | DDD | 2,790 | 735 | 0.161 | 0.115 | 0.208 | yes |
| sign_low_activity | EEE | 927 | 170 | 0.346 | 0.249 | 0.444 | yes |
| sign_low_activity | FFF | 3,437 | 842 | 0.124 | 0.077 | 0.170 | yes |
| sign_low_activity | GGG | 924 | 309 | 0.129 | 0.050 | 0.207 | yes |
| sign_no_pre_activity | AAA | 369 | 25 | 0.093 | -0.088 | 0.274 | no |
| sign_no_pre_activity | BBB | 3,364 | 1,033 | 0.082 | 0.045 | 0.119 | yes |
| sign_no_pre_activity | DDD | 2,790 | 306 | 0.136 | 0.071 | 0.200 | yes |
| sign_no_pre_activity | EEE | 927 | 211 | 0.162 | 0.084 | 0.240 | yes |
| sign_no_pre_activity | FFF | 3,437 | 364 | 0.131 | 0.069 | 0.193 | yes |
| sign_no_pre_activity | GGG | 924 | 358 | 0.047 | -0.020 | 0.114 | no |
[saved] aq-2/results/associations_by_module_2013.csv  (26 rows x 8 columns)

module estimates whose 95% interval includes 0 (no detectable association in that module): 4 of 26

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_inactive_last7 | AAA | 369 | 65 | 0.049 | -0.082 | 0.179 |
| sign_inactive_last7 | GGG | 924 | 506 | 0.039 | -0.033 | 0.111 |
| sign_no_pre_activity | AAA | 369 | 25 | 0.093 | -0.088 | 0.274 |
| sign_no_pre_activity | GGG | 924 | 358 | 0.047 | -0.020 | 0.114 |

**Support of each sign: rows of each module where the sign is defined, and how the module is handled**

| sign | code_module | rows_defined | with_sign | without_sign | handling |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 369 | 23 | 346 | own slope |
| sign_task_missed | BBB | 3,364 | 421 | 2,943 | own slope |
| sign_task_missed | DDD | 2,790 | 533 | 2,257 | own slope |
| sign_task_missed | EEE | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_task_missed | FFF | 3,437 | 308 | 3,129 | own slope |
| sign_task_missed | GGG | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_tma_late | AAA | 369 | 52 | 317 | own slope |
| sign_tma_late | BBB | 3,364 | 254 | 3,110 | own slope |
| sign_tma_late | DDD | 2,790 | 62 | 2,728 | own slope |
| sign_tma_late | EEE | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_tma_late | FFF | 3,437 | 209 | 3,228 | own slope |
| sign_tma_late | GGG | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_inactive_last7 | AAA | 369 | 65 | 304 | own slope |
| sign_inactive_last7 | BBB | 3,364 | 968 | 2,396 | own slope |
| sign_inactive_last7 | DDD | 2,790 | 248 | 2,542 | own slope |
| sign_inactive_last7 | EEE | 927 | 171 | 756 | own slope |
| sign_inactive_last7 | FFF | 3,437 | 486 | 2,951 | own slope |
| sign_inactive_last7 | GGG | 924 | 506 | 418 | own slope |
| sign_low_activity | AAA | 369 | 79 | 290 | own slope |
| sign_low_activity | BBB | 3,364 | 1,040 | 2,324 | own slope |
| sign_low_activity | DDD | 2,790 | 735 | 2,055 | own slope |
| sign_low_activity | EEE | 927 | 170 | 757 | own slope |
| sign_low_activity | FFF | 3,437 | 842 | 2,595 | own slope |
| sign_low_activity | GGG | 924 | 309 | 615 | own slope |
| sign_no_pre_activity | AAA | 369 | 25 | 344 | own slope |
| sign_no_pre_activity | BBB | 3,364 | 1,033 | 2,331 | own slope |
| sign_no_pre_activity | DDD | 2,790 | 306 | 2,484 | own slope |
| sign_no_pre_activity | EEE | 927 | 211 | 716 | own slope |
| sign_no_pre_activity | FFF | 3,437 | 364 | 3,073 | own slope |
| sign_no_pre_activity | GGG | 924 | 358 | 566 | own slope |
[saved] aq-2/results/sign_support_2013.csv  (30 rows x 6 columns)

modules where a sign is defined by the calendar but does not vary (rows left out of that sign's average): 0

model: 37 coefficients, converged = True, log-likelihood = -6956.1, deviance = 13912.2
[saved] aq-2/results/model_coefficients_2013.csv  (37 rows x 4 columns)

**Odds ratios, model without sign x module terms (they read larger than risk ratios at a 44% base rate)**

| term | n_support | odds_ratio | or_ci_low | or_ci_high | p_value | adjusted_rd_no_interactions |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 9,960 | 7.490 | 6.140 | 9.137 | 0.000 | 0.403 |
| sign_tma_late | 9,960 | 2.894 | 2.398 | 3.492 | 0.000 | 0.220 |
| sign_inactive_last7 | 11,811 | 1.667 | 1.467 | 1.894 | 0.000 | 0.108 |
| sign_low_activity | 11,811 | 1.949 | 1.751 | 2.169 | 0.000 | 0.144 |
| sign_no_pre_activity | 11,811 | 1.618 | 1.444 | 1.813 | 0.000 | 0.101 |
[saved] aq-2/results/odds_ratios_2013.csv  (5 rows x 7 columns)

**Phi correlation between signs, on the rows where both are defined**

| sign_a | sign_b | enrolments_both_defined | phi | with_both |
| :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | sign_tma_late | 9,960 | -0.095 | 0 |
| sign_task_missed | sign_inactive_last7 | 9,960 | 0.398 | 735 |
| sign_task_missed | sign_low_activity | 9,960 | 0.413 | 960 |
| sign_task_missed | sign_no_pre_activity | 9,960 | 0.242 | 529 |
| sign_tma_late | sign_inactive_last7 | 9,960 | -0.048 | 60 |
| sign_tma_late | sign_low_activity | 9,960 | 0.038 | 195 |
| sign_tma_late | sign_no_pre_activity | 9,960 | 0.061 | 154 |
| sign_inactive_last7 | sign_low_activity | 11,811 | 0.496 | 1,710 |
| sign_inactive_last7 | sign_no_pre_activity | 11,811 | 0.315 | 1,071 |
| sign_low_activity | sign_no_pre_activity | 11,811 | 0.300 | 1,239 |
[saved] aq-2/results/sign_correlation_2013.csv  (10 rows x 5 columns)

**Non-completion by number of signs present**

| population | signs_present | enrolments | non_completion_rate |
| :---- | :---- | :---- | :---- |
| all enrolments (task signs cannot occur in runs without a task due) | 0 | 6,554 | 0.306 |
| all enrolments (task signs cannot occur in runs without a task due) | 1 | 2,477 | 0.508 |
| all enrolments (task signs cannot occur in runs without a task due) | 2 | 1,430 | 0.631 |
| all enrolments (task signs cannot occur in runs without a task due) | 3 | 959 | 0.739 |
| all enrolments (task signs cannot occur in runs without a task due) | 4 | 391 | 0.944 |
| runs where all five signs are defined | 0 | 5,674 | 0.320 |
| runs where all five signs are defined | 1 | 2,031 | 0.531 |
| runs where all five signs are defined | 2 | 1,134 | 0.669 |
| runs where all five signs are defined | 3 | 730 | 0.788 |
| runs where all five signs are defined | 4 | 391 | 0.944 |
[saved] aq-2/results/non_completion_by_sign_count_2013.csv  (10 rows x 4 columns)

**(a) Binned residuals by run and three activity levels (the check named in the Level 1 card). The levels are cut at the low-activity sign's own threshold, so the model fits them almost by construction.**

| run | activity_level | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | none | 1 | 1.000 | 0.854 | 0.146 | 0.705 | no |
| AAA-2013J | low | 78 | 0.449 | 0.451 | -0.002 | 0.103 | no |
| AAA-2013J | normal | 290 | 0.190 | 0.190 | -0.000 | 0.045 | no |
| BBB-2013B | none | 97 | 0.948 | 0.919 | 0.029 | 0.053 | no |
| BBB-2013B | low | 341 | 0.660 | 0.670 | -0.010 | 0.047 | no |
| BBB-2013B | normal | 1,092 | 0.376 | 0.376 | 0.000 | 0.028 | no |
| BBB-2013J | none | 145 | 0.779 | 0.792 | -0.012 | 0.061 | no |
| BBB-2013J | low | 457 | 0.562 | 0.557 | 0.005 | 0.043 | no |
| BBB-2013J | normal | 1,232 | 0.319 | 0.319 | -0.000 | 0.026 | no |
| DDD-2013B | none | 39 | 0.974 | 0.968 | 0.006 | 0.056 | no |
| DDD-2013B | low | 257 | 0.786 | 0.793 | -0.007 | 0.047 | no |
| DDD-2013B | normal | 847 | 0.465 | 0.463 | 0.002 | 0.033 | no |
| DDD-2013J | none | 44 | 0.909 | 0.933 | -0.024 | 0.073 | no |
| DDD-2013J | low | 395 | 0.739 | 0.733 | 0.007 | 0.041 | no |
| DDD-2013J | normal | 1,208 | 0.403 | 0.404 | -0.001 | 0.027 | no |
| EEE-2013J | none | 39 | 0.897 | 0.850 | 0.048 | 0.113 | no |
| EEE-2013J | low | 131 | 0.702 | 0.716 | -0.014 | 0.076 | no |
| EEE-2013J | normal | 757 | 0.252 | 0.252 | -0.000 | 0.031 | no |
| FFF-2013B | none | 36 | 0.972 | 0.957 | 0.015 | 0.067 | no |
| FFF-2013B | low | 314 | 0.656 | 0.672 | -0.016 | 0.049 | no |
| FFF-2013B | normal | 1,104 | 0.390 | 0.386 | 0.004 | 0.028 | no |
| FFF-2013J | none | 47 | 0.979 | 0.904 | 0.075 | 0.083 | no |
| FFF-2013J | low | 445 | 0.674 | 0.672 | 0.002 | 0.041 | no |
| FFF-2013J | normal | 1,491 | 0.364 | 0.366 | -0.003 | 0.024 | no |
| GGG-2013J | none | 159 | 0.579 | 0.481 | 0.098 | 0.079 | yes |
| GGG-2013J | low | 150 | 0.353 | 0.457 | -0.104 | 0.081 | yes |
| GGG-2013J | normal | 615 | 0.304 | 0.304 | 0.000 | 0.037 | no |

cells outside two standard errors: 2 of 27; largest |residual| = 0.146
[saved] aq-2/results/binned_residuals_by_run_2013.csv  (27 rows x 8 columns)

**(b) Binned residuals by five activity levels on days 0-27**

| model | activity_level5 | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main model (low activity = below half the run median) | 1 no click on days 0-27 | 607 | 0.811 | 0.775 | 0.036 | 0.029 | yes |
| main model (low activity = below half the run median) | 2 below half the run median | 2,568 | 0.647 | 0.656 | -0.009 | 0.017 | no |
| main model (low activity = below half the run median) | 3 half the median to the median | 2,714 | 0.467 | 0.396 | 0.070 | 0.018 | yes |
| main model (low activity = below half the run median) | 4 median to twice the median | 3,447 | 0.334 | 0.349 | -0.015 | 0.016 | no |
| main model (low activity = below half the run median) | 5 twice the median or more | 2,475 | 0.272 | 0.328 | -0.057 | 0.018 | yes |
| main model, low activity = below the run median | 1 no click on days 0-27 | 607 | 0.811 | 0.755 | 0.056 | 0.030 | yes |
| main model, low activity = below the run median | 2 below half the run median | 2,568 | 0.647 | 0.622 | 0.025 | 0.017 | yes |
| main model, low activity = below the run median | 3 half the median to the median | 2,714 | 0.467 | 0.503 | -0.037 | 0.018 | yes |
| main model, low activity = below the run median | 4 median to twice the median | 3,447 | 0.334 | 0.315 | 0.019 | 0.015 | yes |
| main model, low activity = below the run median | 5 twice the median or more | 2,475 | 0.272 | 0.298 | -0.026 | 0.018 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 1 no click on days 0-27 | 607 | 0.811 | 0.828 | -0.018 | 0.027 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 2 below half the run median | 2,568 | 0.647 | 0.643 | 0.004 | 0.017 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 3 half the median to the median | 2,714 | 0.467 | 0.435 | 0.032 | 0.018 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 4 median to twice the median | 3,447 | 0.334 | 0.351 | -0.016 | 0.016 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 5 twice the median or more | 2,475 | 0.272 | 0.284 | -0.013 | 0.018 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 1 no click on days 0-27 | 607 | 0.811 | 0.817 | -0.007 | 0.027 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 2 below half the run median | 2,568 | 0.647 | 0.637 | 0.010 | 0.017 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 3 half the median to the median | 2,714 | 0.467 | 0.475 | -0.008 | 0.018 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 4 median to twice the median | 3,447 | 0.334 | 0.330 | 0.004 | 0.016 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 5 twice the median or more | 2,475 | 0.272 | 0.277 | -0.005 | 0.018 | no |

**(c) Binned residuals by tenth of the predicted risk**

| model | risk_decile | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main model (low activity = below half the run median) | 01 | 1,182 | 0.186 | 0.205 | -0.019 | 0.023 | no |
| main model (low activity = below half the run median) | 02 | 1,181 | 0.275 | 0.275 | 0.001 | 0.026 | no |
| main model (low activity = below half the run median) | 03 | 1,181 | 0.306 | 0.307 | -0.001 | 0.027 | no |
| main model (low activity = below half the run median) | 04 | 1,181 | 0.294 | 0.323 | -0.030 | 0.027 | yes |
| main model (low activity = below half the run median) | 05 | 1,181 | 0.381 | 0.348 | 0.033 | 0.028 | yes |
| main model (low activity = below half the run median) | 06 | 1,181 | 0.399 | 0.382 | 0.016 | 0.028 | no |
| main model (low activity = below half the run median) | 07 | 1,181 | 0.442 | 0.445 | -0.003 | 0.029 | no |
| main model (low activity = below half the run median) | 08 | 1,181 | 0.552 | 0.533 | 0.020 | 0.029 | no |
| main model (low activity = below half the run median) | 09 | 1,181 | 0.693 | 0.703 | -0.011 | 0.026 | no |
| main model (low activity = below half the run median) | 10 | 1,181 | 0.914 | 0.919 | -0.006 | 0.016 | no |
| main model, low activity = below the run median | 01 | 1,182 | 0.178 | 0.197 | -0.020 | 0.023 | no |
| main model, low activity = below the run median | 02 | 1,181 | 0.251 | 0.259 | -0.007 | 0.025 | no |
| main model, low activity = below the run median | 03 | 1,181 | 0.285 | 0.283 | 0.001 | 0.026 | no |
| main model, low activity = below the run median | 04 | 1,181 | 0.339 | 0.313 | 0.026 | 0.027 | no |
| main model, low activity = below the run median | 05 | 1,181 | 0.356 | 0.355 | 0.001 | 0.028 | no |
| main model, low activity = below the run median | 06 | 1,181 | 0.417 | 0.418 | -0.001 | 0.029 | no |
| main model, low activity = below the run median | 07 | 1,181 | 0.486 | 0.465 | 0.021 | 0.029 | no |
| main model, low activity = below the run median | 08 | 1,181 | 0.533 | 0.538 | -0.005 | 0.029 | no |
| main model, low activity = below the run median | 09 | 1,181 | 0.686 | 0.699 | -0.013 | 0.026 | no |
| main model, low activity = below the run median | 10 | 1,181 | 0.912 | 0.914 | -0.002 | 0.016 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 01 | 1,182 | 0.179 | 0.193 | -0.015 | 0.023 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 02 | 1,181 | 0.228 | 0.263 | -0.035 | 0.026 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 03 | 1,181 | 0.298 | 0.299 | -0.001 | 0.027 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 04 | 1,181 | 0.330 | 0.327 | 0.003 | 0.027 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 05 | 1,181 | 0.354 | 0.356 | -0.002 | 0.028 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 06 | 1,181 | 0.415 | 0.390 | 0.025 | 0.028 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 07 | 1,181 | 0.470 | 0.445 | 0.025 | 0.029 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 08 | 1,181 | 0.561 | 0.537 | 0.023 | 0.029 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 09 | 1,181 | 0.691 | 0.705 | -0.014 | 0.026 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 10 | 1,181 | 0.916 | 0.925 | -0.009 | 0.015 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 01 | 1,182 | 0.173 | 0.190 | -0.018 | 0.023 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 02 | 1,181 | 0.234 | 0.258 | -0.024 | 0.025 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 03 | 1,181 | 0.304 | 0.287 | 0.017 | 0.026 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 04 | 1,181 | 0.314 | 0.315 | -0.000 | 0.027 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 05 | 1,181 | 0.378 | 0.352 | 0.027 | 0.028 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 06 | 1,181 | 0.403 | 0.407 | -0.004 | 0.029 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 07 | 1,181 | 0.483 | 0.467 | 0.017 | 0.029 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 08 | 1,181 | 0.550 | 0.542 | 0.008 | 0.029 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 09 | 1,181 | 0.684 | 0.703 | -0.019 | 0.026 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 10 | 1,181 | 0.917 | 0.921 | -0.004 | 0.016 | no |
- main model (low activity = below half the run median): activity levels outside two standard errors: 3 of 5 (largest |residual| 0.070); risk tenths outside: 2 of 10 (largest 0.033)
- main model, low activity = below the run median: activity levels outside two standard errors: 5 of 5 (largest |residual| 0.056); risk tenths outside: 0 of 10 (largest 0.026)
- post hoc: main model + log(1 + clicks on days 0-27): activity levels outside two standard errors: 2 of 5 (largest |residual| 0.032); risk tenths outside: 1 of 10 (largest 0.035)
- post hoc: low activity = below the run median, + log(1 + clicks on days 0-27): activity levels outside two standard errors: 0 of 5 (largest |residual| 0.010); risk tenths outside: 0 of 10 (largest 0.027)
[saved] aq-2/results/binned_residuals_activity5_2013.csv  (20 rows x 8 columns)
[saved] aq-2/results/binned_residuals_decile_2013.csv  (40 rows x 8 columns)

continuous activity term: coefficient -0.3088 per unit of log(1 + clicks) (robust SE 0.0312), odds ratio 0.734; deviance 13803.0 against 13912.2 for the main model

**Sensitivity of the adjusted risk differences (n = rows of the sign's support in that variant)**

| variant | status | rows_in_model | sign | n | n_with_sign | support_modules | adjusted_rd | adj_ci_low | adj_ci_high | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | modules_same_direction_interval_excludes_0 | modules_interval_includes_0 | verdict | verdict_strict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main | planned | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.407 | 0.375 | 0.438 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| main | planned | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.217 | 0.174 | 0.259 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| main | planned | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.135 | 0.101 | 0.168 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| main | planned | 11,811 | sign_low_activity | 11,811 | 3,175 | 6 | 0.147 | 0.123 | 0.170 | yes | yes | 6 | 6 | 6 | none | consistent association | consistent association |
| main | planned | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.113 | 0.085 | 0.140 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.406 | 0.375 | 0.437 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.216 | 0.174 | 0.258 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.135 | 0.101 | 0.169 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 11,811 | sign_low_activity_dedup | 11,811 | 3,188 | 6 | 0.148 | 0.124 | 0.172 | yes | yes | 6 | 6 | 6 | none | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.112 | 0.084 | 0.140 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| late CMAs also count as late | planned | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.406 | 0.374 | 0.437 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| late CMAs also count as late | planned | 11,811 | sign_any_task_late | 9,960 | 1,533 | 4 | 0.167 | 0.128 | 0.206 | yes | yes | 4 | 3 | 3 | DDD | consistent association | consistent association |
| late CMAs also count as late | planned | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.134 | 0.100 | 0.168 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| late CMAs also count as late | planned | 11,811 | sign_low_activity | 11,811 | 3,175 | 6 | 0.147 | 0.123 | 0.171 | yes | yes | 6 | 6 | 6 | none | consistent association | consistent association |
| late CMAs also count as late | planned | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.113 | 0.085 | 0.141 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| without flagged enrolments | planned | 11,803 | sign_task_missed | 9,954 | 1,280 | 4 | 0.407 | 0.375 | 0.438 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| without flagged enrolments | planned | 11,803 | sign_tma_late | 9,954 | 577 | 4 | 0.217 | 0.175 | 0.259 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| without flagged enrolments | planned | 11,803 | sign_inactive_last7 | 11,803 | 2,437 | 6 | 0.135 | 0.101 | 0.168 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| without flagged enrolments | planned | 11,803 | sign_low_activity | 11,803 | 3,168 | 6 | 0.146 | 0.123 | 0.170 | yes | yes | 6 | 6 | 6 | none | consistent association | consistent association |
| without flagged enrolments | planned | 11,803 | sign_no_pre_activity | 11,803 | 2,291 | 6 | 0.113 | 0.085 | 0.140 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 9,960 | sign_task_missed | 9,960 | 1,285 | 4 | 0.406 | 0.375 | 0.438 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 9,960 | sign_tma_late | 9,960 | 577 | 4 | 0.216 | 0.174 | 0.259 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 9,960 | sign_inactive_last7 | 9,960 | 1,767 | 4 | 0.138 | 0.100 | 0.177 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 9,960 | sign_low_activity | 9,960 | 2,696 | 4 | 0.129 | 0.104 | 0.155 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 9,960 | sign_no_pre_activity | 9,960 | 1,728 | 4 | 0.114 | 0.083 | 0.145 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.414 | 0.382 | 0.445 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.224 | 0.183 | 0.266 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.154 | 0.121 | 0.188 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 11,811 | sign_low_activity_q25 | 11,811 | 1,792 | 6 | 0.144 | 0.110 | 0.178 | yes | yes | 6 | 6 | 5 | AAA | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.120 | 0.093 | 0.148 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| low activity = below the run median | planned | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.409 | 0.378 | 0.440 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| low activity = below the run median | planned | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.203 | 0.160 | 0.246 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| low activity = below the run median | planned | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.143 | 0.112 | 0.175 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| low activity = below the run median | planned | 11,811 | sign_low_activity_median | 11,811 | 5,889 | 6 | 0.134 | 0.115 | 0.152 | yes | yes | 6 | 6 | 5 | AAA | consistent association | consistent association |
| low activity = below the run median | planned | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.106 | 0.078 | 0.133 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.373 | 0.338 | 0.408 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.204 | 0.161 | 0.246 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.087 | 0.051 | 0.122 | yes | yes | 6 | 5 | 4 | AAA, GGG | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_low_activity | 11,811 | 3,175 | 6 | 0.029 | -0.002 | 0.060 | no | no | 6 | 4 | 2 | AAA, BBB, FFF, GGG | weak or inconsistent | weak or inconsistent |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.091 | 0.063 | 0.119 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_task_missed | 9,960 | 1,285 | 4 | 0.374 | 0.339 | 0.409 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_tma_late | 9,960 | 577 | 4 | 0.196 | 0.153 | 0.239 | yes | yes | 4 | 4 | 4 | none | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_inactive_last7 | 11,811 | 2,444 | 6 | 0.092 | 0.058 | 0.127 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_low_activity_median | 11,811 | 5,889 | 6 | 0.059 | 0.034 | 0.083 | yes | yes | 6 | 5 | 3 | AAA, BBB, GGG | consistent association | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 11,811 | sign_no_pre_activity | 11,811 | 2,297 | 6 | 0.089 | 0.061 | 0.116 | yes | yes | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association |

sign x variant rows that do not meet the Level 1 criterion: 1 of 45

| variant | sign | n | adjusted_rd | adj_ci_low | adj_ci_high | modules_defined | modules_same_direction | verdict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| post hoc: + log(1 + clicks on days 0-27) | sign_low_activity | 11,811 | 0.029 | -0.002 | 0.060 | 6 | 4 | weak or inconsistent |
[saved] aq-2/results/sensitivity_2013.csv  (45 rows x 18 columns)

**Risk differences by audit group (description; the groups are not model inputs; n = rows of the support in the group)**

| attribute | group | sign | n | with_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
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

labels of the sensitivity signs: sign_low_activity_q25 = Clicks below a quarter of the run median; sign_low_activity_median = Clicks below the run median; sign_low_activity_dedup = De-duplicated clicks below half the run median; sign_any_task_late = TMA or CMA submitted late

