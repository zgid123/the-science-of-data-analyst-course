# Log: aq-1 / 02_analyse_all

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:33:50Z |
| Finished (UTC) | 2026-11-11T23:33:51Z |
| Duration | 0.9 s |
| Command | `python aq-1/code/02_analyse.py --scope all` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Populations, scope = all

| population | enrolments |
| :---- | :---- |
| all enrolments | 32,593 |
| KPI: registered at day 14 | 28,061 |
| KPI without flagged enrolments | 27,962 |
| flagged (missing withdrawal or registration day), all | 138 |
| flagged, in the KPI population | 99 |
[saved] aq-1/results/populations_all.csv  (5 rows x 2 columns)

### Non-completion rate (Fail or Withdrawn) with Wilson 95% intervals, KPI population

**By pooled**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 28,061 | 12,700 | 0.453 | 0.447 | 0.458 |

**By year**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013 | 12,076 | 5,515 | 0.457 | 0.448 | 0.466 |
| 2014 | 15,985 | 7,185 | 0.449 | 0.442 | 0.457 |

**By start_month**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| B | 10,977 | 5,531 | 0.504 | 0.495 | 0.513 |
| J | 17,084 | 7,169 | 0.420 | 0.412 | 0.427 |

**By year_start**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013-B | 4,323 | 2,231 | 0.516 | 0.501 | 0.531 |
| 2013-J | 7,753 | 3,284 | 0.424 | 0.413 | 0.435 |
| 2014-B | 6,654 | 3,300 | 0.496 | 0.484 | 0.508 |
| 2014-J | 9,331 | 3,885 | 0.416 | 0.406 | 0.426 |

**By module**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 720 | 189 | 0.263 | 0.232 | 0.296 |
| BBB | 6,537 | 2,797 | 0.428 | 0.416 | 0.440 |
| CCC | 3,670 | 1,994 | 0.543 | 0.527 | 0.559 |
| DDD | 5,401 | 2,796 | 0.518 | 0.504 | 0.531 |
| EEE | 2,573 | 924 | 0.359 | 0.341 | 0.378 |
| FFF | 6,713 | 3,067 | 0.457 | 0.445 | 0.469 |
| GGG | 2,447 | 933 | 0.381 | 0.362 | 0.401 |

**By run**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 92 | 0.249 | 0.207 | 0.295 |
| AAA-2014J | 350 | 97 | 0.277 | 0.233 | 0.326 |
| BBB-2013B | 1,606 | 804 | 0.501 | 0.476 | 0.525 |
| BBB-2013J | 1,851 | 781 | 0.422 | 0.400 | 0.445 |
| BBB-2014B | 1,289 | 564 | 0.438 | 0.411 | 0.465 |
| BBB-2014J | 1,791 | 648 | 0.362 | 0.340 | 0.384 |
| CCC-2014B | 1,591 | 928 | 0.583 | 0.559 | 0.607 |
| CCC-2014J | 2,079 | 1,066 | 0.513 | 0.491 | 0.534 |
| DDD-2013B | 1,197 | 688 | 0.575 | 0.547 | 0.602 |
| DDD-2013J | 1,675 | 849 | 0.507 | 0.483 | 0.531 |
| DDD-2014B | 1,050 | 572 | 0.545 | 0.515 | 0.575 |
| DDD-2014J | 1,479 | 687 | 0.465 | 0.439 | 0.490 |
| EEE-2013J | 933 | 325 | 0.348 | 0.318 | 0.379 |
| EEE-2014B | 613 | 256 | 0.418 | 0.379 | 0.457 |
| EEE-2014J | 1,027 | 343 | 0.334 | 0.306 | 0.363 |
| FFF-2013B | 1,520 | 739 | 0.486 | 0.461 | 0.511 |
| FFF-2013J | 1,998 | 903 | 0.452 | 0.430 | 0.474 |
| FFF-2014B | 1,309 | 656 | 0.501 | 0.474 | 0.528 |
| FFF-2014J | 1,886 | 769 | 0.408 | 0.386 | 0.430 |
| GGG-2013J | 926 | 334 | 0.361 | 0.330 | 0.392 |
| GGG-2014B | 802 | 324 | 0.404 | 0.371 | 0.438 |
| GGG-2014J | 719 | 275 | 0.382 | 0.348 | 0.419 |

[saved] aq-1/results/rates_all.csv  (38 rows x 7 columns)  – non-completion rate by level, KPI population
**Module by start month (B = February, J = October)**

| code_module | enrolments_J | enrolments_B | rate_J | rate_B | february_minus_october |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 720 |  | 0.263 |  |  |
| BBB | 3,642 | 2,895 | 0.392 | 0.473 | 0.080 |
| CCC | 2,079 | 1,591 | 0.513 | 0.583 | 0.071 |
| DDD | 3,154 | 2,247 | 0.487 | 0.561 | 0.074 |
| EEE | 1,960 | 613 | 0.341 | 0.418 | 0.077 |
| FFF | 3,884 | 2,829 | 0.430 | 0.493 | 0.063 |
| GGG | 1,645 | 802 | 0.370 | 0.404 | 0.034 |

modules with both start months: 6; February rate higher in 6 of them (gap 0.034 to 0.080)

[saved] aq-1/results/rates_module_by_start_month_all.csv  (7 rows x 6 columns)

### Three denominators per run: KPI population, all enrolments, KPI without flagged enrolments

| run | n_kpi | rate_kpi | ci_low | ci_high | n_all | rate_all | n_unflagged | rate_unflagged | shift_all_minus_kpi | all_outside_kpi_interval | shift_unflagged_minus_kpi | unflagged_outside_kpi_interval |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 0.249 | 0.207 | 0.295 | 383 | 0.274 | 370 | 0.249 | 0.026 | no | 0.000 | no |
| AAA-2014J | 350 | 0.277 | 0.233 | 0.326 | 365 | 0.307 | 350 | 0.277 | 0.030 | no | 0.000 | no |
| BBB-2013B | 1,606 | 0.501 | 0.476 | 0.525 | 1,767 | 0.546 | 1,605 | 0.500 | 0.045 | yes | -0.000 | no |
| BBB-2013J | 1,851 | 0.422 | 0.400 | 0.445 | 2,237 | 0.521 | 1,851 | 0.422 | 0.099 | yes | 0.000 | no |
| BBB-2014B | 1,289 | 0.438 | 0.411 | 0.465 | 1,613 | 0.549 | 1,288 | 0.437 | 0.112 | yes | -0.000 | no |
| BBB-2014J | 1,791 | 0.362 | 0.340 | 0.384 | 2,292 | 0.497 | 1,779 | 0.358 | 0.136 | yes | -0.004 | no |
| CCC-2014B | 1,591 | 0.583 | 0.559 | 0.607 | 1,936 | 0.658 | 1,591 | 0.583 | 0.074 | yes | 0.000 | no |
| CCC-2014J | 2,079 | 0.513 | 0.491 | 0.534 | 2,498 | 0.594 | 2,050 | 0.506 | 0.081 | yes | -0.006 | no |
| DDD-2013B | 1,197 | 0.575 | 0.547 | 0.602 | 1,303 | 0.609 | 1,194 | 0.574 | 0.034 | yes | -0.001 | no |
| DDD-2013J | 1,675 | 0.507 | 0.483 | 0.531 | 1,938 | 0.572 | 1,675 | 0.507 | 0.065 | yes | 0.000 | no |
| DDD-2014B | 1,050 | 0.545 | 0.515 | 0.575 | 1,228 | 0.610 | 1,048 | 0.544 | 0.065 | yes | -0.001 | no |
| DDD-2014J | 1,479 | 0.465 | 0.439 | 0.490 | 1,803 | 0.561 | 1,463 | 0.459 | 0.096 | yes | -0.006 | no |
| EEE-2013J | 933 | 0.348 | 0.318 | 0.379 | 1,052 | 0.421 | 932 | 0.348 | 0.073 | yes | -0.001 | no |
| EEE-2014B | 613 | 0.418 | 0.379 | 0.457 | 694 | 0.486 | 613 | 0.418 | 0.068 | yes | 0.000 | no |
| EEE-2014J | 1,027 | 0.334 | 0.306 | 0.363 | 1,188 | 0.424 | 1,023 | 0.331 | 0.090 | yes | -0.003 | no |
| FFF-2013B | 1,520 | 0.486 | 0.461 | 0.511 | 1,614 | 0.515 | 1,519 | 0.486 | 0.029 | yes | -0.000 | no |
| FFF-2013J | 1,998 | 0.452 | 0.430 | 0.474 | 2,283 | 0.520 | 1,997 | 0.452 | 0.068 | yes | -0.000 | no |
| FFF-2014B | 1,309 | 0.501 | 0.474 | 0.528 | 1,500 | 0.564 | 1,308 | 0.501 | 0.063 | yes | -0.000 | no |
| FFF-2014J | 1,886 | 0.408 | 0.386 | 0.430 | 2,365 | 0.528 | 1,862 | 0.400 | 0.120 | yes | -0.008 | no |
| GGG-2013J | 926 | 0.361 | 0.330 | 0.392 | 952 | 0.378 | 925 | 0.360 | 0.017 | no | -0.001 | no |
| GGG-2014B | 802 | 0.404 | 0.371 | 0.438 | 833 | 0.426 | 802 | 0.404 | 0.022 | no | 0.000 | no |
| GGG-2014J | 719 | 0.382 | 0.348 | 0.419 | 749 | 0.407 | 717 | 0.381 | 0.025 | no | -0.002 | no |
[saved] aq-1/results/denominators_by_run_all.csv  (22 rows x 13 columns)

**Pooled**

| denominator | enrolments | non_completers | rate |
| :---- | :---- | :---- | :---- |
| KPI (registered at day 14) | 28,061 | 12,700 | 0.453 |
| all enrolments | 32,593 | 17,208 | 0.528 |
| KPI without flagged | 27,962 | 12,602 | 0.451 |
[saved] aq-1/results/denominators_pooled_all.csv  (3 rows x 4 columns)

### Outcome shares (Pass, Distinction, Fail, Withdrawn), KPI population

[saved] aq-1/results/outcome_shares_all.csv  (136 rows x 8 columns)
| level | group | enrolments | Distinction | Pass | Fail | Withdrawn |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| pooled | all runs | 28,061 | 0.108 | 0.440 | 0.250 | 0.202 |
| module | AAA | 720 | 0.061 | 0.676 | 0.124 | 0.139 |
| module | BBB | 6,537 | 0.103 | 0.469 | 0.269 | 0.159 |
| module | CCC | 3,670 | 0.136 | 0.321 | 0.213 | 0.331 |
| module | DDD | 5,401 | 0.071 | 0.411 | 0.261 | 0.257 |
| module | EEE | 2,573 | 0.138 | 0.503 | 0.218 | 0.141 |
| module | FFF | 6,713 | 0.100 | 0.443 | 0.254 | 0.203 |
| module | GGG | 2,447 | 0.162 | 0.457 | 0.297 | 0.084 |

### Non-completion by audit attribute (description only; no model reads these columns)

| attribute | group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | 12,573 | 5,462 | 0.434 | 0.426 | 0.443 |
| gender | M | 15,488 | 7,238 | 0.467 | 0.459 | 0.475 |
| disability | N | 25,385 | 11,230 | 0.442 | 0.436 | 0.449 |
| disability | Y | 2,676 | 1,470 | 0.549 | 0.530 | 0.568 |
| imd_band | 0-10% | 2,708 | 1,546 | 0.571 | 0.552 | 0.589 |
| imd_band | 10-20% | 2,890 | 1,533 | 0.530 | 0.512 | 0.549 |
| imd_band | 20-30% | 3,060 | 1,574 | 0.514 | 0.497 | 0.532 |
| imd_band | 30-40% | 3,055 | 1,398 | 0.458 | 0.440 | 0.475 |
| imd_band | 40-50% | 2,773 | 1,257 | 0.453 | 0.435 | 0.472 |
| imd_band | 50-60% | 2,740 | 1,217 | 0.444 | 0.426 | 0.463 |
| imd_band | 60-70% | 2,561 | 1,057 | 0.413 | 0.394 | 0.432 |
| imd_band | 70-80% | 2,550 | 1,071 | 0.420 | 0.401 | 0.439 |
| imd_band | 80-90% | 2,419 | 928 | 0.384 | 0.364 | 0.403 |
| imd_band | 90-100% | 2,268 | 809 | 0.357 | 0.337 | 0.377 |
| imd_band | Missing | 1,037 | 310 | 0.299 | 0.272 | 0.328 |
| age_band | 0-35 | 19,580 | 9,261 | 0.473 | 0.466 | 0.480 |
| age_band | 35-55 | 8,283 | 3,374 | 0.407 | 0.397 | 0.418 |
| age_band | 55<= | 198 | 65 | 0.328 | 0.267 | 0.396 |
[saved] aq-1/results/rates_by_audit_group_all.csv  (18 rows x 7 columns)

### Week of the first assessed task (TMA or CMA) due while enrolled and not submitted, KPI population

**Task calendar per run**

| run | first_task_due_day | first_task_due_week | tasks_due_by_day27 | tasks_in_run |
| :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 19 | 3 | 1 | 5 |
| AAA-2014J | 19 | 3 | 1 | 5 |
| BBB-2013B | 19 | 3 | 1 | 11 |
| BBB-2013J | 19 | 3 | 1 | 11 |
| BBB-2014B | 12 | 2 | 1 | 11 |
| BBB-2014J | 19 | 3 | 1 | 5 |
| CCC-2014B | 18 | 3 | 1 | 8 |
| CCC-2014J | 18 | 3 | 1 | 8 |
| DDD-2013B | 23 | 4 | 2 | 13 |
| DDD-2013J | 25 | 4 | 1 | 6 |
| DDD-2014B | 25 | 4 | 1 | 6 |
| DDD-2014J | 20 | 3 | 1 | 6 |
| EEE-2013J | 33 | 5 | 0 | 4 |
| EEE-2014B | 33 | 5 | 0 | 4 |
| EEE-2014J | 33 | 5 | 0 | 4 |
| FFF-2013B | 19 | 3 | 1 | 12 |
| FFF-2013J | 19 | 3 | 1 | 12 |
| FFF-2014B | 24 | 4 | 1 | 12 |
| FFF-2014J | 24 | 4 | 1 | 12 |
| GGG-2013J | 61 | 9 | 0 | 9 |
| GGG-2014B | 61 | 9 | 0 | 9 |
| GGG-2014J | 61 | 9 | 0 | 9 |
[saved] aq-1/results/task_calendar_by_run_all.csv  (22 rows x 5 columns)

Runs with no task due by day 27: 6 of 22: EEE-2013J, EEE-2014B, EEE-2014J, GGG-2013J, GGG-2014B, GGG-2014J

**First missed task by outcome**

| group | enrolments | ever_missed | share_ever_missed | median_first_missed_week | p25_week | p75_week | share_missed_by_week_4 | share_missed_by_week_8 | share_missed_by_week_12 | share_missed_by_week_16 | share_missed_by_week_20 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completers (Pass or Distinction) | 15,361 | 3,150 | 0.205 | 24.000 | 14.000 | 30.000 | 0.005 | 0.038 | 0.047 | 0.060 | 0.081 |
| Distinction | 3,022 | 393 | 0.130 | 23.000 | 5.000 | 32.000 | 0.001 | 0.043 | 0.046 | 0.054 | 0.060 |
| Fail | 7,027 | 5,816 | 0.828 | 12.000 | 6.000 | 19.000 | 0.150 | 0.335 | 0.424 | 0.529 | 0.636 |
| Non-completers (Fail or Withdrawn) | 12,700 | 9,532 | 0.751 | 9.000 | 5.000 | 18.000 | 0.168 | 0.351 | 0.430 | 0.532 | 0.619 |
| Pass | 12,339 | 2,757 | 0.223 | 24.000 | 14.000 | 29.000 | 0.006 | 0.036 | 0.047 | 0.062 | 0.086 |
| Withdrawn | 5,673 | 3,716 | 0.655 | 8.000 | 4.000 | 14.000 | 0.190 | 0.371 | 0.436 | 0.535 | 0.598 |
[saved] aq-1/results/first_missed_task_by_outcome_all.csv  (6 rows x 12 columns)
[saved] aq-1/results/first_missed_task_cumulative_all.csv  (70 rows x 5 columns)

**Non-completers: first missed task by module**

| code_module | non_completers | share_ever_missed | median_first_missed_week | share_missed_by_week_4 | share_missed_by_week_8 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 189 | 0.603 | 12.500 | 0.122 | 0.302 |
| BBB | 2,797 | 0.795 | 8.000 | 0.212 | 0.423 |
| CCC | 1,994 | 0.725 | 5.000 | 0.204 | 0.447 |
| DDD | 2,796 | 0.712 | 8.000 | 0.212 | 0.366 |
| EEE | 924 | 0.753 | 10.000 | 0.000 | 0.281 |
| FFF | 3,067 | 0.753 | 13.000 | 0.169 | 0.340 |
| GGG | 933 | 0.807 | 17.000 | 0.000 | 0.000 |
[saved] aq-1/results/first_missed_task_by_module_all.csv  (7 rows x 6 columns)

