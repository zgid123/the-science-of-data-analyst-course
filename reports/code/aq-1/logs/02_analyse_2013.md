# Log: aq-1 / 02_analyse_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T22:58:40Z |
| Finished (UTC) | 2026-11-11T22:58:41Z |
| Duration | 0.7 s |
| Command | `python aq-1/code/02_analyse.py --scope 2013` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Populations, scope = 2013

| population | enrolments |
| :---- | :---- |
| all enrolments | 13,529 |
| KPI: registered at day 14 | 12,076 |
| KPI without flagged enrolments | 12,068 |
| flagged (missing withdrawal or registration day), all | 21 |
| flagged, in the KPI population | 8 |
[saved] aq-1/results/populations_2013.csv  (5 rows x 2 columns)

### Non-completion rate (Fail or Withdrawn) with Wilson 95% intervals, KPI population

**By pooled**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 12,076 | 5,515 | 0.457 | 0.448 | 0.466 |

**By year**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013 | 12,076 | 5,515 | 0.457 | 0.448 | 0.466 |

**By start_month**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| B | 4,323 | 2,231 | 0.516 | 0.501 | 0.531 |
| J | 7,753 | 3,284 | 0.424 | 0.413 | 0.435 |

**By year_start**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013-B | 4,323 | 2,231 | 0.516 | 0.501 | 0.531 |
| 2013-J | 7,753 | 3,284 | 0.424 | 0.413 | 0.435 |

**By module**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 370 | 92 | 0.249 | 0.207 | 0.295 |
| BBB | 3,457 | 1,585 | 0.458 | 0.442 | 0.475 |
| DDD | 2,872 | 1,537 | 0.535 | 0.517 | 0.553 |
| EEE | 933 | 325 | 0.348 | 0.318 | 0.379 |
| FFF | 3,518 | 1,642 | 0.467 | 0.450 | 0.483 |
| GGG | 926 | 334 | 0.361 | 0.330 | 0.392 |

**By run**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 92 | 0.249 | 0.207 | 0.295 |
| BBB-2013B | 1,606 | 804 | 0.501 | 0.476 | 0.525 |
| BBB-2013J | 1,851 | 781 | 0.422 | 0.400 | 0.445 |
| DDD-2013B | 1,197 | 688 | 0.575 | 0.547 | 0.602 |
| DDD-2013J | 1,675 | 849 | 0.507 | 0.483 | 0.531 |
| EEE-2013J | 933 | 325 | 0.348 | 0.318 | 0.379 |
| FFF-2013B | 1,520 | 739 | 0.486 | 0.461 | 0.511 |
| FFF-2013J | 1,998 | 903 | 0.452 | 0.430 | 0.474 |
| GGG-2013J | 926 | 334 | 0.361 | 0.330 | 0.392 |

[saved] aq-1/results/rates_2013.csv  (21 rows x 7 columns)  – non-completion rate by level, KPI population

### Three denominators per run: KPI population, all enrolments, KPI without flagged enrolments

| run | n_kpi | rate_kpi | ci_low | ci_high | n_all | rate_all | n_unflagged | rate_unflagged | shift_all_minus_kpi | all_outside_kpi_interval | shift_unflagged_minus_kpi | unflagged_outside_kpi_interval |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 0.249 | 0.207 | 0.295 | 383 | 0.274 | 370 | 0.249 | 0.026 | no | 0.000 | no |
| BBB-2013B | 1,606 | 0.501 | 0.476 | 0.525 | 1,767 | 0.546 | 1,605 | 0.500 | 0.045 | yes | -0.000 | no |
| BBB-2013J | 1,851 | 0.422 | 0.400 | 0.445 | 2,237 | 0.521 | 1,851 | 0.422 | 0.099 | yes | 0.000 | no |
| DDD-2013B | 1,197 | 0.575 | 0.547 | 0.602 | 1,303 | 0.609 | 1,194 | 0.574 | 0.034 | yes | -0.001 | no |
| DDD-2013J | 1,675 | 0.507 | 0.483 | 0.531 | 1,938 | 0.572 | 1,675 | 0.507 | 0.065 | yes | 0.000 | no |
| EEE-2013J | 933 | 0.348 | 0.318 | 0.379 | 1,052 | 0.421 | 932 | 0.348 | 0.073 | yes | -0.001 | no |
| FFF-2013B | 1,520 | 0.486 | 0.461 | 0.511 | 1,614 | 0.515 | 1,519 | 0.486 | 0.029 | yes | -0.000 | no |
| FFF-2013J | 1,998 | 0.452 | 0.430 | 0.474 | 2,283 | 0.520 | 1,997 | 0.452 | 0.068 | yes | -0.000 | no |
| GGG-2013J | 926 | 0.361 | 0.330 | 0.392 | 952 | 0.378 | 925 | 0.360 | 0.017 | no | -0.001 | no |
[saved] aq-1/results/denominators_by_run_2013.csv  (9 rows x 13 columns)

**Pooled**

| denominator | enrolments | non_completers | rate |
| :---- | :---- | :---- | :---- |
| KPI (registered at day 14) | 12,076 | 5,515 | 0.457 |
| all enrolments | 13,529 | 6,959 | 0.514 |
| KPI without flagged | 12,068 | 5,507 | 0.456 |
[saved] aq-1/results/denominators_pooled_2013.csv  (3 rows x 4 columns)

### Outcome shares (Pass, Distinction, Fail, Withdrawn), KPI population

[saved] aq-1/results/outcome_shares_2013.csv  (76 rows x 8 columns)
| level | group | enrolments | Distinction | Pass | Fail | Withdrawn |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| pooled | all runs | 12,076 | 0.089 | 0.454 | 0.267 | 0.189 |
| module | AAA | 370 | 0.054 | 0.697 | 0.116 | 0.132 |
| module | BBB | 3,457 | 0.095 | 0.446 | 0.283 | 0.176 |
| module | DDD | 2,872 | 0.053 | 0.412 | 0.273 | 0.262 |
| module | EEE | 933 | 0.136 | 0.516 | 0.214 | 0.134 |
| module | FFF | 3,518 | 0.087 | 0.447 | 0.265 | 0.202 |
| module | GGG | 926 | 0.152 | 0.487 | 0.317 | 0.043 |

### Non-completion by audit attribute (description only; no model reads these columns)

| attribute | group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | 5,826 | 2,620 | 0.450 | 0.437 | 0.463 |
| gender | M | 6,250 | 2,895 | 0.463 | 0.451 | 0.476 |
| disability | N | 10,919 | 4,879 | 0.447 | 0.438 | 0.456 |
| disability | Y | 1,157 | 636 | 0.550 | 0.521 | 0.578 |
| imd_band | 0-10% | 1,196 | 732 | 0.612 | 0.584 | 0.639 |
| imd_band | 10-20% | 1,279 | 692 | 0.541 | 0.514 | 0.568 |
| imd_band | 20-30% | 1,317 | 677 | 0.514 | 0.487 | 0.541 |
| imd_band | 30-40% | 1,337 | 618 | 0.462 | 0.436 | 0.489 |
| imd_band | 40-50% | 1,203 | 551 | 0.458 | 0.430 | 0.486 |
| imd_band | 50-60% | 1,190 | 521 | 0.438 | 0.410 | 0.466 |
| imd_band | 60-70% | 1,068 | 428 | 0.401 | 0.372 | 0.430 |
| imd_band | 70-80% | 1,099 | 452 | 0.411 | 0.383 | 0.441 |
| imd_band | 80-90% | 998 | 382 | 0.383 | 0.353 | 0.413 |
| imd_band | 90-100% | 969 | 341 | 0.352 | 0.322 | 0.383 |
| imd_band | Missing | 420 | 121 | 0.288 | 0.247 | 0.333 |
| age_band | 0-35 | 8,441 | 4,042 | 0.479 | 0.468 | 0.490 |
| age_band | 35-55 | 3,559 | 1,454 | 0.409 | 0.392 | 0.425 |
| age_band | 55<= | 76 | 19 | 0.250 | 0.166 | 0.358 |
[saved] aq-1/results/rates_by_audit_group_2013.csv  (18 rows x 7 columns)

### Week of the first assessed task (TMA or CMA) due while enrolled and not submitted, KPI population

**Task calendar per run**

| run | first_task_due_day | first_task_due_week | tasks_due_by_day27 | tasks_in_run |
| :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 19 | 3 | 1 | 5 |
| BBB-2013B | 19 | 3 | 1 | 11 |
| BBB-2013J | 19 | 3 | 1 | 11 |
| DDD-2013B | 23 | 4 | 2 | 13 |
| DDD-2013J | 25 | 4 | 1 | 6 |
| EEE-2013J | 33 | 5 | 0 | 4 |
| FFF-2013B | 19 | 3 | 1 | 12 |
| FFF-2013J | 19 | 3 | 1 | 12 |
| GGG-2013J | 61 | 9 | 0 | 9 |
[saved] aq-1/results/task_calendar_by_run_2013.csv  (9 rows x 5 columns)

Runs with no task due by day 27: 2 of 9: EEE-2013J, GGG-2013J

**First missed task by outcome**

| group | enrolments | ever_missed | share_ever_missed | median_first_missed_week | p25_week | p75_week | share_missed_by_week_4 | share_missed_by_week_8 | share_missed_by_week_12 | share_missed_by_week_16 | share_missed_by_week_20 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completers (Pass or Distinction) | 6,561 | 1,439 | 0.219 | 24.000 | 18.000 | 30.000 | 0.005 | 0.019 | 0.023 | 0.041 | 0.071 |
| Distinction | 1,075 | 111 | 0.103 | 30.000 | 23.000 | 33.000 | 0.001 | 0.003 | 0.004 | 0.011 | 0.019 |
| Fail | 3,230 | 2,733 | 0.846 | 13.000 | 7.000 | 19.000 | 0.164 | 0.350 | 0.411 | 0.538 | 0.659 |
| Non-completers (Fail or Withdrawn) | 5,515 | 4,307 | 0.781 | 9.000 | 4.000 | 18.000 | 0.196 | 0.374 | 0.418 | 0.543 | 0.650 |
| Pass | 5,486 | 1,328 | 0.242 | 24.000 | 18.000 | 30.000 | 0.005 | 0.022 | 0.027 | 0.047 | 0.081 |
| Withdrawn | 2,285 | 1,574 | 0.689 | 8.000 | 4.000 | 14.000 | 0.241 | 0.406 | 0.430 | 0.549 | 0.638 |
[saved] aq-1/results/first_missed_task_by_outcome_2013.csv  (6 rows x 12 columns)
[saved] aq-1/results/first_missed_task_cumulative_2013.csv  (68 rows x 5 columns)

**Non-completers: first missed task by module**

| code_module | non_completers | share_ever_missed | median_first_missed_week | share_missed_by_week_4 | share_missed_by_week_8 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 92 | 0.641 | 17.000 | 0.120 | 0.293 |
| BBB | 1,585 | 0.839 | 8.000 | 0.247 | 0.471 |
| DDD | 1,537 | 0.746 | 8.000 | 0.255 | 0.412 |
| EEE | 325 | 0.772 | 10.000 | 0.000 | 0.295 |
| FFF | 1,642 | 0.755 | 13.000 | 0.174 | 0.339 |
| GGG | 334 | 0.844 | 18.000 | 0.000 | 0.000 |
[saved] aq-1/results/first_missed_task_by_module_2013.csv  (6 rows x 6 columns)

