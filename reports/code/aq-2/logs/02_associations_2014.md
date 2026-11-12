# Log: aq-2 / 02_associations_2014

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:24Z |
| Finished (UTC) | 2026-11-12T16:00:27Z |
| Duration | 3.4 s |
| Command | `python aq-2/code/02_associations.py --scope 2014` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 associations at day 27, scope = 2014: 15,724 enrolments, 13 runs, 6,911 non-completers (44.0%)

**Risk difference per sign (percentage points = value x 100); n = rows of the support, the only rows averaged over**

| sign | n | support_modules | rows_defined_outside_support | with_sign | rate_with_sign | rate_without_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 12,585 | 5 | 0 | 1,368 | 0.890 | 0.403 | 0.488 | 0.468 | 0.506 | 0.396 | 0.368 | 0.425 |
| sign_tma_late | 9,064 | 4 | 0 | 429 | 0.594 | 0.421 | 0.173 | 0.125 | 0.220 | 0.225 | 0.179 | 0.272 |
| sign_inactive_last7 | 15,724 | 7 | 0 | 3,440 | 0.647 | 0.381 | 0.265 | 0.247 | 0.283 | 0.154 | 0.128 | 0.181 |
| sign_low_activity | 15,724 | 7 | 0 | 4,099 | 0.663 | 0.361 | 0.302 | 0.285 | 0.319 | 0.148 | 0.127 | 0.168 |
| sign_no_pre_activity | 15,724 | 7 | 0 | 3,161 | 0.583 | 0.403 | 0.179 | 0.160 | 0.198 | 0.092 | 0.069 | 0.114 |

**Verdict against the Level 1 criterion (verdict = direction of the module point estimates, as Level 1 words it; verdict_strict = only modules whose own interval excludes 0)**

| sign | adjusted_rd | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | modules_same_direction_interval_excludes_0 | modules_interval_includes_0 | two_thirds_same_direction | verdict | verdict_strict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 0.396 | yes | yes | 5 | 5 | 5 | none | yes | consistent association | consistent association |
| sign_tma_late | 0.225 | yes | yes | 4 | 4 | 3 | AAA | yes | consistent association | consistent association |
| sign_inactive_last7 | 0.154 | yes | yes | 7 | 7 | 7 | none | yes | consistent association | consistent association |
| sign_low_activity | 0.148 | yes | yes | 7 | 7 | 6 | AAA | yes | consistent association | consistent association |
| sign_no_pre_activity | 0.092 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | yes | consistent association | weak or inconsistent |
[saved] aq-2/results/associations_2014.csv  (5 rows x 29 columns)

**Adjusted risk difference by module (modules with their own slope: at least 20 enrolments with and 20 without the sign)**

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 348 | 28 | 0.415 | 0.235 | 0.594 | yes |
| sign_task_missed | BBB | 3,066 | 220 | 0.534 | 0.480 | 0.588 | yes |
| sign_task_missed | CCC | 3,521 | 402 | 0.353 | 0.302 | 0.404 | yes |
| sign_task_missed | DDD | 2,492 | 302 | 0.367 | 0.305 | 0.428 | yes |
| sign_task_missed | FFF | 3,158 | 416 | 0.332 | 0.269 | 0.395 | yes |
| sign_tma_late | AAA | 348 | 53 | 0.002 | -0.132 | 0.135 | no |
| sign_tma_late | BBB | 3,066 | 191 | 0.257 | 0.189 | 0.326 | yes |
| sign_tma_late | DDD | 2,492 | 99 | 0.208 | 0.122 | 0.293 | yes |
| sign_tma_late | FFF | 3,158 | 86 | 0.233 | 0.139 | 0.327 | yes |
| sign_inactive_last7 | AAA | 348 | 71 | 0.165 | 0.032 | 0.298 | yes |
| sign_inactive_last7 | BBB | 3,066 | 937 | 0.122 | 0.079 | 0.166 | yes |
| sign_inactive_last7 | CCC | 3,521 | 755 | 0.189 | 0.147 | 0.231 | yes |
| sign_inactive_last7 | DDD | 2,492 | 328 | 0.142 | 0.068 | 0.216 | yes |
| sign_inactive_last7 | EEE | 1,625 | 298 | 0.136 | 0.064 | 0.208 | yes |
| sign_inactive_last7 | FFF | 3,158 | 293 | 0.168 | 0.081 | 0.255 | yes |
| sign_inactive_last7 | GGG | 1,514 | 758 | 0.146 | 0.091 | 0.202 | yes |
| sign_low_activity | AAA | 348 | 91 | 0.008 | -0.098 | 0.113 | no |
| sign_low_activity | BBB | 3,066 | 916 | 0.074 | 0.031 | 0.117 | yes |
| sign_low_activity | CCC | 3,521 | 804 | 0.086 | 0.040 | 0.132 | yes |
| sign_low_activity | DDD | 2,492 | 626 | 0.176 | 0.125 | 0.227 | yes |
| sign_low_activity | EEE | 1,625 | 347 | 0.290 | 0.220 | 0.360 | yes |
| sign_low_activity | FFF | 3,158 | 818 | 0.205 | 0.160 | 0.251 | yes |
| sign_low_activity | GGG | 1,514 | 497 | 0.153 | 0.093 | 0.213 | yes |
| sign_no_pre_activity | AAA | 348 | 21 | 0.097 | -0.091 | 0.286 | no |
| sign_no_pre_activity | BBB | 3,066 | 901 | 0.013 | -0.024 | 0.050 | no |
| sign_no_pre_activity | CCC | 3,521 | 532 | 0.130 | 0.080 | 0.179 | yes |
| sign_no_pre_activity | DDD | 2,492 | 255 | 0.060 | -0.013 | 0.132 | no |
| sign_no_pre_activity | EEE | 1,625 | 327 | 0.225 | 0.163 | 0.287 | yes |
| sign_no_pre_activity | FFF | 3,158 | 433 | 0.089 | 0.035 | 0.144 | yes |
| sign_no_pre_activity | GGG | 1,514 | 692 | 0.074 | 0.024 | 0.123 | yes |
[saved] aq-2/results/associations_by_module_2014.csv  (30 rows x 8 columns)

module estimates whose 95% interval includes 0 (no detectable association in that module): 5 of 30

| sign | code_module | enrolments | with_sign | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_tma_late | AAA | 348 | 53 | 0.002 | -0.132 | 0.135 |
| sign_low_activity | AAA | 348 | 91 | 0.008 | -0.098 | 0.113 |
| sign_no_pre_activity | AAA | 348 | 21 | 0.097 | -0.091 | 0.286 |
| sign_no_pre_activity | BBB | 3,066 | 901 | 0.013 | -0.024 | 0.050 |
| sign_no_pre_activity | DDD | 2,492 | 255 | 0.060 | -0.013 | 0.132 |

**Support of each sign: rows of each module where the sign is defined, and how the module is handled**

| sign | code_module | rows_defined | with_sign | without_sign | handling |
| :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | AAA | 348 | 28 | 320 | own slope |
| sign_task_missed | BBB | 3,066 | 220 | 2,846 | own slope |
| sign_task_missed | CCC | 3,521 | 402 | 3,119 | own slope |
| sign_task_missed | DDD | 2,492 | 302 | 2,190 | own slope |
| sign_task_missed | EEE | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_task_missed | FFF | 3,158 | 416 | 2,742 | own slope |
| sign_task_missed | GGG | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_tma_late | AAA | 348 | 53 | 295 | own slope |
| sign_tma_late | BBB | 3,066 | 191 | 2,875 | own slope |
| sign_tma_late | CCC | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_tma_late | DDD | 2,492 | 99 | 2,393 | own slope |
| sign_tma_late | EEE | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_tma_late | FFF | 3,158 | 86 | 3,072 | own slope |
| sign_tma_late | GGG | 0 | 0 | 0 | sign not defined in this module's runs: no term, outside the support |
| sign_inactive_last7 | AAA | 348 | 71 | 277 | own slope |
| sign_inactive_last7 | BBB | 3,066 | 937 | 2,129 | own slope |
| sign_inactive_last7 | CCC | 3,521 | 755 | 2,766 | own slope |
| sign_inactive_last7 | DDD | 2,492 | 328 | 2,164 | own slope |
| sign_inactive_last7 | EEE | 1,625 | 298 | 1,327 | own slope |
| sign_inactive_last7 | FFF | 3,158 | 293 | 2,865 | own slope |
| sign_inactive_last7 | GGG | 1,514 | 758 | 756 | own slope |
| sign_low_activity | AAA | 348 | 91 | 257 | own slope |
| sign_low_activity | BBB | 3,066 | 916 | 2,150 | own slope |
| sign_low_activity | CCC | 3,521 | 804 | 2,717 | own slope |
| sign_low_activity | DDD | 2,492 | 626 | 1,866 | own slope |
| sign_low_activity | EEE | 1,625 | 347 | 1,278 | own slope |
| sign_low_activity | FFF | 3,158 | 818 | 2,340 | own slope |
| sign_low_activity | GGG | 1,514 | 497 | 1,017 | own slope |
| sign_no_pre_activity | AAA | 348 | 21 | 327 | own slope |
| sign_no_pre_activity | BBB | 3,066 | 901 | 2,165 | own slope |
| sign_no_pre_activity | CCC | 3,521 | 532 | 2,989 | own slope |
| sign_no_pre_activity | DDD | 2,492 | 255 | 2,237 | own slope |
| sign_no_pre_activity | EEE | 1,625 | 327 | 1,298 | own slope |
| sign_no_pre_activity | FFF | 3,158 | 433 | 2,725 | own slope |
| sign_no_pre_activity | GGG | 1,514 | 692 | 822 | own slope |
[saved] aq-2/results/sign_support_2014.csv  (35 rows x 6 columns)

modules where a sign is defined by the calendar but does not vary (rows left out of that sign's average): 0

model: 45 coefficients, converged = True, log-likelihood = -9375.8, deviance = 18751.6
[saved] aq-2/results/model_coefficients_2014.csv  (45 rows x 4 columns)

**Odds ratios, model without sign x module terms (they read larger than risk ratios at a 44% base rate)**

| term | n_support | odds_ratio | or_ci_low | or_ci_high | p_value | adjusted_rd_no_interactions |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | 12,585 | 6.559 | 5.453 | 7.889 | 0.000 | 0.381 |
| sign_tma_late | 9,064 | 2.673 | 2.165 | 3.301 | 0.000 | 0.207 |
| sign_inactive_last7 | 15,724 | 1.991 | 1.801 | 2.201 | 0.000 | 0.150 |
| sign_low_activity | 15,724 | 1.932 | 1.765 | 2.116 | 0.000 | 0.144 |
| sign_no_pre_activity | 15,724 | 1.505 | 1.368 | 1.656 | 0.000 | 0.087 |
[saved] aq-2/results/odds_ratios_2014.csv  (5 rows x 7 columns)

**Phi correlation between signs, on the rows where both are defined**

| sign_a | sign_b | enrolments_both_defined | phi | with_both |
| :---- | :---- | :---- | :---- | :---- |
| sign_task_missed | sign_tma_late | 9,064 | -0.077 | 0 |
| sign_task_missed | sign_inactive_last7 | 12,585 | 0.324 | 757 |
| sign_task_missed | sign_low_activity | 12,585 | 0.391 | 1,025 |
| sign_task_missed | sign_no_pre_activity | 12,585 | 0.211 | 543 |
| sign_tma_late | sign_inactive_last7 | 9,064 | -0.026 | 58 |
| sign_tma_late | sign_low_activity | 9,064 | 0.034 | 145 |
| sign_tma_late | sign_no_pre_activity | 9,064 | 0.060 | 120 |
| sign_inactive_last7 | sign_low_activity | 15,724 | 0.444 | 2,163 |
| sign_inactive_last7 | sign_no_pre_activity | 15,724 | 0.288 | 1,442 |
| sign_low_activity | sign_no_pre_activity | 15,724 | 0.271 | 1,575 |
[saved] aq-2/results/sign_correlation_2014.csv  (10 rows x 5 columns)

**Non-completion by number of signs present**

| population | signs_present | enrolments | non_completion_rate |
| :---- | :---- | :---- | :---- |
| all enrolments (task signs cannot occur in runs without a task due) | 0 | 8,701 | 0.313 |
| all enrolments (task signs cannot occur in runs without a task due) | 1 | 3,516 | 0.501 |
| all enrolments (task signs cannot occur in runs without a task due) | 2 | 1,927 | 0.593 |
| all enrolments (task signs cannot occur in runs without a task due) | 3 | 1,193 | 0.764 |
| all enrolments (task signs cannot occur in runs without a task due) | 4 | 387 | 0.953 |
| runs where all five signs are defined | 0 | 5,113 | 0.302 |
| runs where all five signs are defined | 1 | 1,994 | 0.501 |
| runs where all five signs are defined | 2 | 1,054 | 0.583 |
| runs where all five signs are defined | 3 | 629 | 0.754 |
| runs where all five signs are defined | 4 | 274 | 0.953 |
[saved] aq-2/results/non_completion_by_sign_count_2014.csv  (10 rows x 4 columns)

**(a) Binned residuals by run and three activity levels (the check named in the Level 1 card). The levels are cut at the low-activity sign's own threshold, so the model fits them almost by construction.**

| run | activity_level | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | none | 2 | 0.500 | 0.451 | 0.049 | 0.704 | no |
| AAA-2014J | low | 89 | 0.348 | 0.349 | -0.001 | 0.095 | no |
| AAA-2014J | normal | 257 | 0.245 | 0.245 | -0.000 | 0.051 | no |
| BBB-2014B | none | 85 | 0.859 | 0.839 | 0.020 | 0.071 | no |
| BBB-2014B | low | 340 | 0.553 | 0.553 | -0.000 | 0.050 | no |
| BBB-2014B | normal | 855 | 0.342 | 0.343 | -0.002 | 0.031 | no |
| BBB-2014J | none | 61 | 0.787 | 0.808 | -0.021 | 0.086 | no |
| BBB-2014J | low | 430 | 0.463 | 0.464 | -0.001 | 0.045 | no |
| BBB-2014J | normal | 1,295 | 0.300 | 0.298 | 0.001 | 0.025 | no |
| CCC-2014B | none | 45 | 1.000 | 0.964 | 0.036 | 0.055 | no |
| CCC-2014B | low | 308 | 0.760 | 0.760 | -0.001 | 0.045 | no |
| CCC-2014B | normal | 1,147 | 0.486 | 0.488 | -0.001 | 0.029 | no |
| CCC-2014J | none | 40 | 0.875 | 0.935 | -0.060 | 0.077 | no |
| CCC-2014J | low | 411 | 0.696 | 0.694 | 0.002 | 0.042 | no |
| CCC-2014J | normal | 1,570 | 0.436 | 0.435 | 0.001 | 0.024 | no |
| DDD-2014B | none | 30 | 0.900 | 0.939 | -0.039 | 0.086 | no |
| DDD-2014B | low | 244 | 0.787 | 0.765 | 0.021 | 0.050 | no |
| DDD-2014B | normal | 755 | 0.440 | 0.445 | -0.005 | 0.035 | no |
| DDD-2014J | none | 36 | 0.889 | 0.882 | 0.007 | 0.105 | no |
| DDD-2014J | low | 316 | 0.680 | 0.694 | -0.014 | 0.049 | no |
| DDD-2014J | normal | 1,111 | 0.382 | 0.378 | 0.004 | 0.028 | no |
| EEE-2014B | none | 22 | 0.955 | 0.875 | 0.079 | 0.139 | no |
| EEE-2014B | low | 102 | 0.706 | 0.739 | -0.033 | 0.084 | no |
| EEE-2014B | normal | 481 | 0.322 | 0.319 | 0.003 | 0.042 | no |
| EEE-2014J | none | 30 | 0.833 | 0.810 | 0.024 | 0.140 | no |
| EEE-2014J | low | 193 | 0.642 | 0.638 | 0.005 | 0.066 | no |
| EEE-2014J | normal | 797 | 0.235 | 0.237 | -0.002 | 0.029 | no |
| FFF-2014B | none | 32 | 0.906 | 0.952 | -0.046 | 0.075 | no |
| FFF-2014B | low | 306 | 0.732 | 0.760 | -0.028 | 0.046 | no |
| FFF-2014B | normal | 961 | 0.408 | 0.398 | 0.010 | 0.031 | no |
| FFF-2014J | none | 46 | 0.935 | 0.900 | 0.035 | 0.087 | no |
| FFF-2014J | low | 434 | 0.680 | 0.661 | 0.019 | 0.042 | no |
| FFF-2014J | normal | 1,379 | 0.293 | 0.300 | -0.007 | 0.024 | no |
| GGG-2014B | none | 98 | 0.704 | 0.611 | 0.093 | 0.098 | no |
| GGG-2014B | low | 159 | 0.497 | 0.553 | -0.056 | 0.078 | no |
| GGG-2014B | normal | 540 | 0.317 | 0.317 | -0.000 | 0.039 | no |
| GGG-2014J | none | 97 | 0.670 | 0.593 | 0.077 | 0.099 | no |
| GGG-2014J | low | 143 | 0.462 | 0.515 | -0.054 | 0.082 | no |
| GGG-2014J | normal | 477 | 0.298 | 0.297 | 0.000 | 0.041 | no |

cells outside two standard errors: 0 of 39; largest |residual| = 0.093
[saved] aq-2/results/binned_residuals_by_run_2014.csv  (39 rows x 8 columns)

**(b) Binned residuals by five activity levels on days 0-27**

| model | activity_level5 | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main model (low activity = below half the run median) | 1 no click on days 0-27 | 624 | 0.822 | 0.793 | 0.029 | 0.029 | no |
| main model (low activity = below half the run median) | 2 below half the run median | 3,475 | 0.635 | 0.640 | -0.005 | 0.015 | no |
| main model (low activity = below half the run median) | 3 half the median to the median | 3,734 | 0.478 | 0.399 | 0.079 | 0.015 | yes |
| main model (low activity = below half the run median) | 4 median to twice the median | 4,660 | 0.349 | 0.351 | -0.002 | 0.014 | no |
| main model (low activity = below half the run median) | 5 twice the median or more | 3,231 | 0.242 | 0.330 | -0.088 | 0.016 | yes |
| main model, low activity = below the run median | 1 no click on days 0-27 | 624 | 0.822 | 0.771 | 0.051 | 0.030 | yes |
| main model, low activity = below the run median | 2 below half the run median | 3,475 | 0.635 | 0.607 | 0.027 | 0.015 | yes |
| main model, low activity = below the run median | 3 half the median to the median | 3,734 | 0.478 | 0.512 | -0.034 | 0.016 | yes |
| main model, low activity = below the run median | 4 median to twice the median | 4,660 | 0.349 | 0.312 | 0.037 | 0.013 | yes |
| main model, low activity = below the run median | 5 twice the median or more | 3,231 | 0.242 | 0.295 | -0.053 | 0.016 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 1 no click on days 0-27 | 624 | 0.822 | 0.868 | -0.046 | 0.025 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 2 below half the run median | 3,475 | 0.635 | 0.626 | 0.008 | 0.015 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 3 half the median to the median | 3,734 | 0.478 | 0.446 | 0.032 | 0.016 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 4 median to twice the median | 4,660 | 0.349 | 0.352 | -0.003 | 0.014 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 5 twice the median or more | 3,231 | 0.242 | 0.275 | -0.033 | 0.015 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 1 no click on days 0-27 | 624 | 0.822 | 0.851 | -0.029 | 0.026 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 2 below half the run median | 3,475 | 0.635 | 0.628 | 0.006 | 0.015 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 3 half the median to the median | 3,734 | 0.478 | 0.479 | -0.001 | 0.016 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 4 median to twice the median | 4,660 | 0.349 | 0.329 | 0.019 | 0.013 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 5 twice the median or more | 3,231 | 0.242 | 0.270 | -0.028 | 0.015 | yes |

**(c) Binned residuals by tenth of the predicted risk**

| model | risk_decile | enrolments | observed | predicted | residual | two_se | outside_2se |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main model (low activity = below half the run median) | 01 | 1,573 | 0.199 | 0.210 | -0.011 | 0.021 | no |
| main model (low activity = below half the run median) | 02 | 1,572 | 0.242 | 0.252 | -0.010 | 0.022 | no |
| main model (low activity = below half the run median) | 03 | 1,573 | 0.299 | 0.285 | 0.015 | 0.023 | no |
| main model (low activity = below half the run median) | 04 | 1,572 | 0.331 | 0.333 | -0.003 | 0.024 | no |
| main model (low activity = below half the run median) | 05 | 1,572 | 0.359 | 0.365 | -0.006 | 0.024 | no |
| main model (low activity = below half the run median) | 06 | 1,573 | 0.398 | 0.400 | -0.002 | 0.025 | no |
| main model (low activity = below half the run median) | 07 | 1,572 | 0.465 | 0.451 | 0.014 | 0.025 | no |
| main model (low activity = below half the run median) | 08 | 1,573 | 0.558 | 0.537 | 0.021 | 0.025 | no |
| main model (low activity = below half the run median) | 09 | 1,572 | 0.657 | 0.667 | -0.010 | 0.024 | no |
| main model (low activity = below half the run median) | 10 | 1,572 | 0.887 | 0.895 | -0.008 | 0.015 | no |
| main model, low activity = below the run median | 01 | 1,573 | 0.184 | 0.194 | -0.009 | 0.020 | no |
| main model, low activity = below the run median | 02 | 1,572 | 0.238 | 0.233 | 0.005 | 0.021 | no |
| main model, low activity = below the run median | 03 | 1,573 | 0.284 | 0.286 | -0.002 | 0.023 | no |
| main model, low activity = below the run median | 04 | 1,572 | 0.317 | 0.321 | -0.003 | 0.024 | no |
| main model, low activity = below the run median | 05 | 1,572 | 0.354 | 0.364 | -0.010 | 0.024 | no |
| main model, low activity = below the run median | 06 | 1,573 | 0.435 | 0.416 | 0.019 | 0.025 | no |
| main model, low activity = below the run median | 07 | 1,572 | 0.495 | 0.481 | 0.014 | 0.025 | no |
| main model, low activity = below the run median | 08 | 1,573 | 0.554 | 0.547 | 0.008 | 0.025 | no |
| main model, low activity = below the run median | 09 | 1,572 | 0.643 | 0.667 | -0.024 | 0.024 | yes |
| main model, low activity = below the run median | 10 | 1,572 | 0.891 | 0.888 | 0.003 | 0.016 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 01 | 1,573 | 0.177 | 0.191 | -0.014 | 0.020 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 02 | 1,572 | 0.223 | 0.247 | -0.024 | 0.022 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 03 | 1,573 | 0.282 | 0.287 | -0.005 | 0.023 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 04 | 1,572 | 0.319 | 0.325 | -0.005 | 0.024 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 05 | 1,572 | 0.373 | 0.364 | 0.009 | 0.024 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 06 | 1,573 | 0.415 | 0.406 | 0.010 | 0.025 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 07 | 1,572 | 0.490 | 0.457 | 0.033 | 0.025 | yes |
| post hoc: main model + log(1 + clicks on days 0-27) | 08 | 1,573 | 0.557 | 0.537 | 0.020 | 0.025 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 09 | 1,572 | 0.673 | 0.677 | -0.004 | 0.023 | no |
| post hoc: main model + log(1 + clicks on days 0-27) | 10 | 1,572 | 0.885 | 0.905 | -0.019 | 0.014 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 01 | 1,573 | 0.163 | 0.186 | -0.023 | 0.020 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 02 | 1,572 | 0.246 | 0.241 | 0.005 | 0.022 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 03 | 1,573 | 0.268 | 0.281 | -0.013 | 0.023 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 04 | 1,572 | 0.328 | 0.319 | 0.009 | 0.024 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 05 | 1,572 | 0.351 | 0.360 | -0.008 | 0.024 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 06 | 1,573 | 0.438 | 0.411 | 0.027 | 0.025 | yes |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 07 | 1,572 | 0.485 | 0.474 | 0.011 | 0.025 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 08 | 1,573 | 0.558 | 0.548 | 0.010 | 0.025 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 09 | 1,572 | 0.669 | 0.677 | -0.008 | 0.023 | no |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | 10 | 1,572 | 0.888 | 0.899 | -0.011 | 0.015 | no |
- main model (low activity = below half the run median): activity levels outside two standard errors: 2 of 5 (largest |residual| 0.088); risk tenths outside: 0 of 10 (largest 0.021)
- main model, low activity = below the run median: activity levels outside two standard errors: 5 of 5 (largest |residual| 0.053); risk tenths outside: 1 of 10 (largest 0.024)
- post hoc: main model + log(1 + clicks on days 0-27): activity levels outside two standard errors: 3 of 5 (largest |residual| 0.046); risk tenths outside: 3 of 10 (largest 0.033)
- post hoc: low activity = below the run median, + log(1 + clicks on days 0-27): activity levels outside two standard errors: 3 of 5 (largest |residual| 0.029); risk tenths outside: 2 of 10 (largest 0.027)
[saved] aq-2/results/binned_residuals_activity5_2014.csv  (20 rows x 8 columns)
[saved] aq-2/results/binned_residuals_decile_2014.csv  (40 rows x 8 columns)

continuous activity term: coefficient -0.3712 per unit of log(1 + clicks) (robust SE 0.0281), odds ratio 0.690; deviance 18538.1 against 18751.6 for the main model

**Sensitivity of the adjusted risk differences (n = rows of the sign's support in that variant)**

| variant | status | rows_in_model | sign | n | n_with_sign | support_modules | adjusted_rd | adj_ci_low | adj_ci_high | at_least_5_points | interval_excludes_0 | modules_defined | modules_same_direction | modules_same_direction_interval_excludes_0 | modules_interval_includes_0 | verdict | verdict_strict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main | planned | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.396 | 0.368 | 0.425 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| main | planned | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.225 | 0.179 | 0.272 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| main | planned | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.154 | 0.128 | 0.181 | yes | yes | 7 | 7 | 7 | none | consistent association | consistent association |
| main | planned | 15,724 | sign_low_activity | 15,724 | 4,099 | 7 | 0.148 | 0.127 | 0.168 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| main | planned | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.092 | 0.069 | 0.114 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.398 | 0.369 | 0.426 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.226 | 0.179 | 0.273 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.155 | 0.128 | 0.181 | yes | yes | 7 | 7 | 7 | none | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 15,724 | sign_low_activity_dedup | 15,724 | 4,129 | 7 | 0.146 | 0.125 | 0.166 | yes | yes | 7 | 6 | 6 | AAA | consistent association | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | planned | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.091 | 0.069 | 0.114 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| late CMAs also count as late | planned | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.409 | 0.372 | 0.445 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| late CMAs also count as late | planned | 15,724 | sign_any_task_late | 12,585 | 3,508 | 5 | 0.183 | 0.128 | 0.238 | yes | yes | 5 | 5 | 3 | AAA, CCC | consistent association | weak or inconsistent |
| late CMAs also count as late | planned | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.154 | 0.128 | 0.181 | yes | yes | 7 | 7 | 7 | none | consistent association | consistent association |
| late CMAs also count as late | planned | 15,724 | sign_low_activity | 15,724 | 4,099 | 7 | 0.148 | 0.128 | 0.169 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| late CMAs also count as late | planned | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.092 | 0.069 | 0.114 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| without flagged enrolments | planned | 15,632 | sign_task_missed | 12,499 | 1,301 | 5 | 0.393 | 0.364 | 0.422 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| without flagged enrolments | planned | 15,632 | sign_tma_late | 9,007 | 428 | 4 | 0.226 | 0.179 | 0.274 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| without flagged enrolments | planned | 15,632 | sign_inactive_last7 | 15,632 | 3,364 | 7 | 0.151 | 0.124 | 0.178 | yes | yes | 7 | 7 | 7 | none | consistent association | consistent association |
| without flagged enrolments | planned | 15,632 | sign_low_activity | 15,632 | 4,031 | 7 | 0.148 | 0.128 | 0.169 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| without flagged enrolments | planned | 15,632 | sign_no_pre_activity | 15,632 | 3,125 | 7 | 0.092 | 0.070 | 0.115 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| only runs with a task due by day 27 | planned | 12,585 | sign_task_missed | 12,585 | 1,368 | 5 | 0.397 | 0.368 | 0.425 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 12,585 | sign_tma_late | 9,064 | 429 | 4 | 0.225 | 0.179 | 0.272 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 12,585 | sign_inactive_last7 | 12,585 | 2,384 | 5 | 0.157 | 0.126 | 0.188 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 12,585 | sign_low_activity | 12,585 | 3,255 | 5 | 0.127 | 0.104 | 0.150 | yes | yes | 5 | 5 | 4 | AAA | consistent association | consistent association |
| only runs with a task due by day 27 | planned | 12,585 | sign_no_pre_activity | 12,585 | 2,142 | 5 | 0.076 | 0.050 | 0.102 | yes | yes | 5 | 5 | 2 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| low activity = below a quarter of the run median | planned | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.404 | 0.375 | 0.432 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.238 | 0.192 | 0.284 | yes | yes | 4 | 4 | 3 | AAA | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.170 | 0.144 | 0.196 | yes | yes | 7 | 7 | 7 | none | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 15,724 | sign_low_activity_q25 | 15,724 | 2,231 | 7 | 0.152 | 0.120 | 0.184 | yes | yes | 7 | 7 | 5 | AAA, CCC | consistent association | consistent association |
| low activity = below a quarter of the run median | planned | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.099 | 0.076 | 0.121 | yes | yes | 7 | 7 | 5 | AAA, BBB | consistent association | consistent association |
| low activity = below the run median | planned | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.393 | 0.365 | 0.421 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| low activity = below the run median | planned | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.218 | 0.171 | 0.266 | yes | yes | 4 | 3 | 3 | AAA | consistent association | consistent association |
| low activity = below the run median | planned | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.157 | 0.132 | 0.183 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| low activity = below the run median | planned | 15,724 | sign_low_activity_median | 15,724 | 7,833 | 7 | 0.146 | 0.130 | 0.162 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| low activity = below the run median | planned | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.086 | 0.064 | 0.108 | yes | yes | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.358 | 0.327 | 0.390 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.212 | 0.165 | 0.260 | yes | yes | 4 | 3 | 3 | AAA | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.102 | 0.075 | 0.130 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_low_activity | 15,724 | 4,099 | 7 | 0.008 | -0.019 | 0.034 | no | no | 7 | 3 | 2 | CCC, DDD, GGG | weak or inconsistent | weak or inconsistent |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.065 | 0.043 | 0.088 | yes | yes | 7 | 6 | 3 | AAA, BBB, DDD, GGG | consistent association | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_task_missed | 12,585 | 1,368 | 5 | 0.357 | 0.325 | 0.389 | yes | yes | 5 | 5 | 5 | none | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_tma_late | 9,064 | 429 | 4 | 0.210 | 0.162 | 0.258 | yes | yes | 4 | 3 | 3 | AAA | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_inactive_last7 | 15,724 | 3,440 | 7 | 0.107 | 0.080 | 0.133 | yes | yes | 7 | 7 | 6 | AAA | consistent association | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_low_activity_median | 15,724 | 7,833 | 7 | 0.059 | 0.038 | 0.081 | yes | yes | 7 | 4 | 4 | AAA, BBB, GGG | weak or inconsistent | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | 15,724 | sign_no_pre_activity | 15,724 | 3,161 | 7 | 0.065 | 0.042 | 0.087 | yes | yes | 7 | 6 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |

sign x variant rows that do not meet the Level 1 criterion: 2 of 45

| variant | sign | n | adjusted_rd | adj_ci_low | adj_ci_high | modules_defined | modules_same_direction | verdict |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| post hoc: + log(1 + clicks on days 0-27) | sign_low_activity | 15,724 | 0.008 | -0.019 | 0.034 | 7 | 3 | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | sign_low_activity_median | 15,724 | 0.059 | 0.038 | 0.081 | 7 | 4 | weak or inconsistent |
[saved] aq-2/results/sensitivity_2014.csv  (45 rows x 18 columns)

**Risk differences by audit group (description; the groups are not model inputs; n = rows of the support in the group)**

| attribute | group | sign | n | with_sign | unadjusted_rd | unadj_ci_low | unadj_ci_high | adjusted_rd | adj_ci_low | adj_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | sign_task_missed | 5,254 | 446 | 0.520 | 0.485 | 0.548 | 0.450 | 0.418 | 0.483 |
| gender | F | sign_tma_late | 4,403 | 238 | 0.195 | 0.130 | 0.257 | 0.235 | 0.187 | 0.283 |
| gender | F | sign_inactive_last7 | 6,666 | 1,837 | 0.231 | 0.204 | 0.257 | 0.144 | 0.119 | 0.170 |
| gender | F | sign_low_activity | 6,666 | 1,753 | 0.257 | 0.230 | 0.283 | 0.121 | 0.098 | 0.145 |
| gender | F | sign_no_pre_activity | 6,666 | 1,631 | 0.136 | 0.108 | 0.163 | 0.061 | 0.039 | 0.084 |
| gender | M | sign_task_missed | 7,331 | 922 | 0.465 | 0.440 | 0.488 | 0.358 | 0.326 | 0.390 |
| gender | M | sign_tma_late | 4,661 | 191 | 0.152 | 0.080 | 0.221 | 0.216 | 0.157 | 0.276 |
| gender | M | sign_inactive_last7 | 9,058 | 1,603 | 0.321 | 0.296 | 0.345 | 0.161 | 0.129 | 0.194 |
| gender | M | sign_low_activity | 9,058 | 2,346 | 0.337 | 0.315 | 0.358 | 0.167 | 0.143 | 0.191 |
| gender | M | sign_no_pre_activity | 9,058 | 1,530 | 0.235 | 0.209 | 0.261 | 0.114 | 0.087 | 0.140 |
| disability | N | sign_task_missed | 11,416 | 1,198 | 0.497 | 0.476 | 0.516 | 0.398 | 0.370 | 0.426 |
| disability | N | sign_tma_late | 8,172 | 368 | 0.172 | 0.120 | 0.223 | 0.226 | 0.179 | 0.273 |
| disability | N | sign_inactive_last7 | 14,236 | 3,087 | 0.273 | 0.254 | 0.292 | 0.155 | 0.128 | 0.181 |
| disability | N | sign_low_activity | 14,236 | 3,665 | 0.305 | 0.287 | 0.323 | 0.148 | 0.127 | 0.168 |
| disability | N | sign_no_pre_activity | 14,236 | 2,830 | 0.182 | 0.162 | 0.202 | 0.092 | 0.070 | 0.115 |
| disability | Y | sign_task_missed | 1,169 | 170 | 0.388 | 0.324 | 0.437 | 0.380 | 0.352 | 0.408 |
| disability | Y | sign_tma_late | 892 | 61 | 0.130 | 0.001 | 0.238 | 0.220 | 0.175 | 0.266 |
| disability | Y | sign_inactive_last7 | 1,488 | 353 | 0.184 | 0.126 | 0.239 | 0.150 | 0.123 | 0.177 |
| disability | Y | sign_low_activity | 1,488 | 434 | 0.266 | 0.213 | 0.316 | 0.146 | 0.126 | 0.167 |
| disability | Y | sign_no_pre_activity | 1,488 | 331 | 0.141 | 0.081 | 0.199 | 0.082 | 0.060 | 0.105 |
| imd_group | 0-30% (most deprived) | sign_task_missed | 3,760 | 476 | 0.454 | 0.422 | 0.481 | 0.398 | 0.370 | 0.426 |
| imd_group | 0-30% (most deprived) | sign_tma_late | 2,847 | 166 | 0.208 | 0.132 | 0.275 | 0.227 | 0.181 | 0.272 |
| imd_group | 0-30% (most deprived) | sign_inactive_last7 | 4,769 | 1,215 | 0.246 | 0.215 | 0.276 | 0.150 | 0.124 | 0.176 |
| imd_group | 0-30% (most deprived) | sign_low_activity | 4,769 | 1,371 | 0.291 | 0.262 | 0.320 | 0.144 | 0.124 | 0.164 |
| imd_group | 0-30% (most deprived) | sign_no_pre_activity | 4,769 | 1,080 | 0.176 | 0.143 | 0.208 | 0.084 | 0.063 | 0.106 |
| imd_group | 30-70% | sign_task_missed | 4,943 | 554 | 0.493 | 0.461 | 0.520 | 0.399 | 0.370 | 0.427 |
| imd_group | 30-70% | sign_tma_late | 3,587 | 163 | 0.117 | 0.039 | 0.194 | 0.226 | 0.179 | 0.272 |
| imd_group | 30-70% | sign_inactive_last7 | 6,227 | 1,337 | 0.271 | 0.241 | 0.299 | 0.153 | 0.127 | 0.179 |
| imd_group | 30-70% | sign_low_activity | 6,227 | 1,623 | 0.300 | 0.273 | 0.327 | 0.147 | 0.127 | 0.168 |
| imd_group | 30-70% | sign_no_pre_activity | 6,227 | 1,282 | 0.185 | 0.154 | 0.215 | 0.091 | 0.069 | 0.113 |
| imd_group | 70-100% (least deprived) | sign_task_missed | 3,338 | 298 | 0.500 | 0.453 | 0.540 | 0.395 | 0.366 | 0.424 |
| imd_group | 70-100% (least deprived) | sign_tma_late | 2,312 | 91 | 0.159 | 0.056 | 0.261 | 0.223 | 0.175 | 0.271 |
| imd_group | 70-100% (least deprived) | sign_inactive_last7 | 4,118 | 814 | 0.242 | 0.204 | 0.279 | 0.158 | 0.131 | 0.185 |
| imd_group | 70-100% (least deprived) | sign_low_activity | 4,118 | 1,005 | 0.295 | 0.260 | 0.328 | 0.150 | 0.129 | 0.171 |
| imd_group | 70-100% (least deprived) | sign_no_pre_activity | 4,118 | 731 | 0.136 | 0.097 | 0.176 | 0.098 | 0.074 | 0.122 |
| imd_group | Missing | sign_task_missed | 544 | 40 | 0.434 | 0.275 | 0.559 | 0.373 | 0.340 | 0.407 |
| imd_group | Missing | sign_tma_late | 318 | 9 | 0.186 | -0.075 | 0.478 | 0.229 | 0.167 | 0.291 |
| imd_group | Missing | sign_inactive_last7 | 610 | 74 | 0.339 | 0.219 | 0.449 | 0.171 | 0.137 | 0.205 |
| imd_group | Missing | sign_low_activity | 610 | 100 | 0.315 | 0.210 | 0.415 | 0.160 | 0.134 | 0.185 |
| imd_group | Missing | sign_no_pre_activity | 610 | 68 | 0.229 | 0.107 | 0.350 | 0.112 | 0.082 | 0.142 |
[saved] aq-2/results/subgroups_2014.csv  (40 rows x 11 columns)

labels of the sensitivity signs: sign_low_activity_q25 = Clicks below a quarter of the run median; sign_low_activity_median = Clicks below the run median; sign_low_activity_dedup = De-duplicated clicks below half the run median; sign_any_task_late = TMA or CMA submitted late

