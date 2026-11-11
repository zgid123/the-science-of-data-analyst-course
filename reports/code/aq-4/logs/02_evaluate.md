# Log: aq-4 / 02_evaluate

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:21:55Z |
| Finished (UTC) | 2026-11-11T23:21:57Z |
| Duration | 1.2 s |
| Command | `python aq-4/code/02_evaluate.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output

[saved] aq-4/results/list_quality_by_run.csv  (156 rows x 17 columns)

### AQ4 list quality, pooled over the 13 test runs

| cutoff | per20 | ranking | enrolments | non_completers | list_places | non_completers_on_list | max_attainable | recall | attainable_recall | normalised_recall | precision | base_rate | lift |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 27 | 5 | model | 15,724 | 6,911 | 3,955 | 2870.000 | 3,955 | 0.415 | 0.572 | 0.726 | 0.726 | 0.440 | 1.651 |
| 27 | 5 | random (expected) | 15,724 | 6,911 | 3,955 | 1737.946 | 3,955 | 0.251 | 0.572 | 0.439 | 0.439 | 0.440 | 1.000 |
| 27 | 5 | rule | 15,724 | 6,911 | 3,955 | 2786.000 | 3,955 | 0.403 | 0.572 | 0.704 | 0.704 | 0.440 | 1.603 |
| 27 | 3 | model | 15,724 | 6,911 | 2,373 | 1922.000 | 2,373 | 0.278 | 0.343 | 0.810 | 0.810 | 0.440 | 1.843 |
| 27 | 3 | random (expected) | 15,724 | 6,911 | 2,373 | 1042.768 | 2,373 | 0.151 | 0.343 | 0.439 | 0.439 | 0.440 | 1.000 |
| 27 | 3 | rule | 15,724 | 6,911 | 2,373 | 1846.000 | 2,373 | 0.267 | 0.343 | 0.778 | 0.778 | 0.440 | 1.770 |
| 13 | 5 | model | 15,989 | 7,189 | 4,030 | 2771.000 | 4,030 | 0.385 | 0.561 | 0.688 | 0.688 | 0.450 | 1.529 |
| 13 | 5 | random (expected) | 15,989 | 7,189 | 4,030 | 1811.243 | 4,030 | 0.252 | 0.561 | 0.449 | 0.449 | 0.450 | 1.000 |
| 13 | 5 | rule | 15,989 | 7,189 | 4,030 | 2688.000 | 4,030 | 0.374 | 0.561 | 0.667 | 0.667 | 0.450 | 1.483 |
| 13 | 3 | model | 15,989 | 7,189 | 2,418 | 1795.000 | 2,418 | 0.250 | 0.336 | 0.742 | 0.742 | 0.450 | 1.651 |
| 13 | 3 | random (expected) | 15,989 | 7,189 | 2,418 | 1086.746 | 2,418 | 0.151 | 0.336 | 0.449 | 0.449 | 0.450 | 1.000 |
| 13 | 3 | rule | 15,989 | 7,189 | 2,418 | 1710.000 | 2,418 | 0.238 | 0.336 | 0.707 | 0.707 | 0.450 | 1.573 |
[saved] aq-4/results/list_quality_pooled.csv  (12 rows x 14 columns)

**Per run, day 27, 5 per 20**

| run | n | list_length | non_completers | attainable_recall | base_rate | recall_model | recall_rule | recall_random (expected) | precision_model | precision_rule | precision_random (expected) | lift_model | lift_rule | lift_random (expected) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 348 | 90 | 95 | 0.947 | 0.273 | 0.432 | 0.400 | 0.259 | 0.456 | 0.422 | 0.273 | 1.669 | 1.547 | 1.000 |
| BBB-2014B | 1,280 | 320 | 553 | 0.579 | 0.432 | 0.407 | 0.400 | 0.250 | 0.703 | 0.691 | 0.432 | 1.627 | 1.599 | 1.000 |
| BBB-2014J | 1,786 | 450 | 635 | 0.709 | 0.356 | 0.411 | 0.384 | 0.252 | 0.580 | 0.542 | 0.356 | 1.631 | 1.525 | 1.000 |
| CCC-2014B | 1,500 | 375 | 837 | 0.448 | 0.558 | 0.384 | 0.370 | 0.250 | 0.856 | 0.827 | 0.558 | 1.534 | 1.481 | 1.000 |
| CCC-2014J | 2,021 | 510 | 1,006 | 0.507 | 0.498 | 0.387 | 0.381 | 0.252 | 0.763 | 0.751 | 0.498 | 1.532 | 1.509 | 1.000 |
| DDD-2014B | 1,029 | 260 | 551 | 0.472 | 0.535 | 0.405 | 0.394 | 0.253 | 0.858 | 0.835 | 0.535 | 1.602 | 1.559 | 1.000 |
| DDD-2014J | 1,463 | 370 | 671 | 0.551 | 0.459 | 0.428 | 0.407 | 0.253 | 0.776 | 0.738 | 0.459 | 1.691 | 1.609 | 1.000 |
| EEE-2014B | 605 | 155 | 248 | 0.625 | 0.410 | 0.464 | 0.448 | 0.256 | 0.742 | 0.716 | 0.410 | 1.810 | 1.747 | 1.000 |
| EEE-2014J | 1,020 | 255 | 336 | 0.759 | 0.329 | 0.515 | 0.464 | 0.250 | 0.678 | 0.612 | 0.329 | 2.060 | 1.857 | 1.000 |
| FFF-2014B | 1,299 | 325 | 645 | 0.504 | 0.497 | 0.409 | 0.402 | 0.250 | 0.812 | 0.797 | 0.497 | 1.636 | 1.605 | 1.000 |
| FFF-2014J | 1,859 | 465 | 742 | 0.627 | 0.399 | 0.460 | 0.456 | 0.250 | 0.733 | 0.727 | 0.399 | 1.837 | 1.821 | 1.000 |
| GGG-2014B | 797 | 200 | 319 | 0.627 | 0.400 | 0.389 | 0.401 | 0.251 | 0.620 | 0.640 | 0.400 | 1.549 | 1.599 | 1.000 |
| GGG-2014J | 717 | 180 | 273 | 0.659 | 0.381 | 0.388 | 0.396 | 0.251 | 0.589 | 0.600 | 0.381 | 1.547 | 1.576 | 1.000 |

### Risk tiers at day 27 (tier 1 = top 3 per 20, tier 2 = next 2 per 20; both cut points come from capacity)

| ranking | tier | enrolments | non_completers | non_completion_rate | withdrawn | fail |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| model | tier 2 (next 2 per 20) | 1,582 | 948 | 0.599 | 414 | 534 |
| model | tier 1 (top 3 per 20) | 2,373 | 1,922 | 0.810 | 812 | 1,110 |
| model | not listed | 11,769 | 4,041 | 0.343 | 1,880 | 2,161 |
| rule | tier 2 (next 2 per 20) | 1,582 | 940 | 0.594 | 444 | 496 |
| rule | tier 1 (top 3 per 20) | 2,373 | 1,846 | 0.778 | 747 | 1,099 |
| rule | not listed | 11,769 | 4,125 | 0.350 | 1,915 | 2,210 |
[saved] aq-4/results/tiers.csv  (6 rows x 7 columns)

### Kind of non-completion on the list, day 27, 5 per 20

| ranking | final_result | in_test_runs | on_list | recall |
| :---- | :---- | :---- | :---- | :---- |
| model | Fail | 3,805 | 1,644 | 0.432 |
| model | Withdrawn | 3,106 | 1,226 | 0.395 |
| rule | Fail | 3,805 | 1,595 | 0.419 |
| rule | Withdrawn | 3,106 | 1,191 | 0.383 |
[saved] aq-4/results/outcome_kind_on_list.csv  (4 rows x 5 columns)

### Overlap of the model list with the rule list, day 27, 5 per 20

| run | list_places | on_both | flagged_by_rule | n | overlap_share | share_flagged_by_rule |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 90 | 68 | 143 | 348 | 0.756 | 0.411 |
| BBB-2014B | 320 | 246 | 522 | 1,280 | 0.769 | 0.408 |
| BBB-2014J | 450 | 324 | 594 | 1,786 | 0.720 | 0.333 |
| CCC-2014B | 375 | 287 | 431 | 1,500 | 0.765 | 0.287 |
| CCC-2014J | 510 | 365 | 505 | 2,021 | 0.716 | 0.250 |
| DDD-2014B | 260 | 225 | 241 | 1,029 | 0.865 | 0.234 |
| DDD-2014J | 370 | 290 | 330 | 1,463 | 0.784 | 0.226 |
| EEE-2014B | 155 | 110 | 109 | 605 | 0.710 | 0.180 |
| EEE-2014J | 255 | 188 | 189 | 1,020 | 0.737 | 0.185 |
| FFF-2014B | 325 | 270 | 267 | 1,299 | 0.831 | 0.206 |
| FFF-2014J | 465 | 390 | 333 | 1,859 | 0.839 | 0.179 |
| GGG-2014B | 200 | 142 | 413 | 797 | 0.710 | 0.518 |
| GGG-2014J | 180 | 148 | 345 | 717 | 0.822 | 0.481 |

all runs: 3,053 of 3,955 places shared (77.2%)
[saved] aq-4/results/overlap_by_run.csv  (13 rows x 7 columns)

### Students with no activity at all (every list catches them) apart from active students, day 27, 5 per 20

| ranking | activity | enrolments | non_completers | listed | share_of_all_list_places | recall | precision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| model | no activity since the start | 624 | 513 | 615 | 0.155 | 0.984 | 0.821 |
| model | some activity | 15,100 | 6,398 | 3,340 | 0.845 | 0.370 | 0.708 |
| rule | no activity since the start | 624 | 513 | 624 | 0.158 | 1.000 | 0.822 |
| rule | some activity | 15,100 | 6,398 | 3,331 | 0.842 | 0.355 | 0.682 |
[saved] aq-4/results/active_vs_inactive.csv  (4 rows x 8 columns)
[saved] aq-4/results/s1_reference.csv  (1 rows x 29 columns)  – copied from aq-3/results/s1_gate.csv

Gate S1 (shared with AQ3): model 0.7257 against rule 0.7044, difference +0.0212 [+0.0065, +0.0364], sign-flip p = 0.0032: PASS

