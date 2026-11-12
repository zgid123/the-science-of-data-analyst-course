# Log: aq-3 / 07_error_analysis

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:59:19Z |
| Finished (UTC) | 2026-11-12T15:59:20Z |
| Duration | 1.7 s |
| Command | `python aq-3/code/07_error_analysis.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Errors by run – day 27, 5 per 20, model M1 and rule-ranked list

| run | n | non_completers | list_length | model_hits | model_listed_completers | model_missed | rule_hits | rule_missed | model_minus_rule_hits | share_of_list_completers | missed_even_by_a_perfect_list |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 348 | 95 | 90 | 41 | 49 | 54 | 38 | 57 | 3 | 0.544 | 5 |
| BBB-2014B | 1,280 | 553 | 320 | 225 | 95 | 328 | 221 | 332 | 4 | 0.297 | 233 |
| BBB-2014J | 1,786 | 635 | 450 | 261 | 189 | 374 | 244 | 391 | 17 | 0.420 | 185 |
| CCC-2014B | 1,500 | 837 | 375 | 321 | 54 | 516 | 310 | 527 | 11 | 0.144 | 462 |
| CCC-2014J | 2,021 | 1,006 | 510 | 389 | 121 | 617 | 383 | 623 | 6 | 0.237 | 496 |
| DDD-2014B | 1,029 | 551 | 260 | 223 | 37 | 328 | 217 | 334 | 6 | 0.142 | 291 |
| DDD-2014J | 1,463 | 671 | 370 | 287 | 83 | 384 | 273 | 398 | 14 | 0.224 | 301 |
| EEE-2014B | 605 | 248 | 155 | 115 | 40 | 133 | 111 | 137 | 4 | 0.258 | 93 |
| EEE-2014J | 1,020 | 336 | 255 | 173 | 82 | 163 | 156 | 180 | 17 | 0.322 | 81 |
| FFF-2014B | 1,299 | 645 | 325 | 264 | 61 | 381 | 259 | 386 | 5 | 0.188 | 320 |
| FFF-2014J | 1,859 | 742 | 465 | 341 | 124 | 401 | 338 | 404 | 3 | 0.267 | 277 |
| GGG-2014B | 797 | 319 | 200 | 124 | 76 | 195 | 128 | 191 | -4 | 0.380 | 119 |
| GGG-2014J | 717 | 273 | 180 | 106 | 74 | 167 | 108 | 165 | -2 | 0.411 | 93 |
[saved] aq-3/results/errors_by_run.csv  (13 rows x 12 columns)

All runs: 6,911 non-completers; the lists hold 3,955 places; the model lists 2,870 of them and misses 4,041, of whom 2,956 could not be listed by any ranking because their run has more non-completers than places. 1,085 listed students completed.

### Errors by slice: share of each slice's non-completers on the list (recall) and share of the slice's listed students who did not complete (precision)

| slice | group | enrolments | non_completers | base_rate | model_listed | model_selection_rate | model_recall | model_precision | rule_listed | rule_selection_rate | rule_recall | rule_precision | recall_model_minus_rule |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| activity_level | low | 3,475 | 2,205 | 0.635 | 2,112 | 0.608 | 0.709 | 0.741 | 2,303 | 0.663 | 0.733 | 0.702 | -0.024 |
| activity_level | none | 624 | 513 | 0.822 | 615 | 0.986 | 0.984 | 0.821 | 624 | 1.000 | 1.000 | 0.822 | -0.016 |
| activity_level | normal | 11,625 | 4,193 | 0.361 | 1,228 | 0.106 | 0.191 | 0.652 | 1,028 | 0.088 | 0.156 | 0.638 | 0.035 |
| attempts | first attempt | 13,865 | 5,801 | 0.418 | 2,961 | 0.214 | 0.370 | 0.724 | 3,186 | 0.230 | 0.379 | 0.690 | -0.009 |
| attempts | repeat attempt | 1,859 | 1,110 | 0.597 | 994 | 0.535 | 0.653 | 0.729 | 769 | 0.414 | 0.530 | 0.765 | 0.123 |
| final_result | Fail | 3,805 | 3,805 | 1.000 | 1,644 | 0.432 | 0.432 | 1.000 | 1,595 | 0.419 | 0.419 | 1.000 | 0.013 |
| final_result | Withdrawn | 3,106 | 3,106 | 1.000 | 1,226 | 0.395 | 0.395 | 1.000 | 1,191 | 0.383 | 0.383 | 1.000 | 0.011 |
| module | AAA | 348 | 95 | 0.273 | 90 | 0.259 | 0.432 | 0.456 | 90 | 0.259 | 0.400 | 0.422 | 0.032 |
| module | BBB | 3,066 | 1,188 | 0.387 | 770 | 0.251 | 0.409 | 0.631 | 770 | 0.251 | 0.391 | 0.604 | 0.018 |
| module | CCC | 3,521 | 1,843 | 0.523 | 885 | 0.251 | 0.385 | 0.802 | 885 | 0.251 | 0.376 | 0.783 | 0.009 |
| module | DDD | 2,492 | 1,222 | 0.490 | 630 | 0.253 | 0.417 | 0.810 | 630 | 0.253 | 0.401 | 0.778 | 0.016 |
| module | EEE | 1,625 | 584 | 0.359 | 410 | 0.252 | 0.493 | 0.702 | 410 | 0.252 | 0.457 | 0.651 | 0.036 |
| module | FFF | 3,158 | 1,387 | 0.439 | 790 | 0.250 | 0.436 | 0.766 | 790 | 0.250 | 0.430 | 0.756 | 0.006 |
| module | GGG | 1,514 | 592 | 0.391 | 380 | 0.251 | 0.389 | 0.605 | 380 | 0.251 | 0.399 | 0.621 | -0.010 |
| paired_run | False | 4,923 | 2,410 | 0.490 | 1,240 | 0.252 | 0.394 | 0.765 | 1,240 | 0.252 | 0.387 | 0.752 | 0.007 |
| paired_run | True | 10,801 | 4,501 | 0.417 | 2,715 | 0.251 | 0.427 | 0.708 | 2,715 | 0.251 | 0.412 | 0.683 | 0.015 |
| reach | left within 7 days of the cut-off | 205 | 205 | 1.000 | 110 | 0.537 | 0.537 | 1.000 | 109 | 0.532 | 0.532 | 1.000 | 0.005 |
| reach | reachable | 15,519 | 6,706 | 0.432 | 3,845 | 0.248 | 0.412 | 0.718 | 3,846 | 0.248 | 0.399 | 0.696 | 0.012 |
| registration | registered after the start | 152 | 65 | 0.428 | 73 | 0.480 | 0.738 | 0.658 | 51 | 0.336 | 0.538 | 0.686 | 0.200 |
| registration | registered before the start | 15,570 | 6,845 | 0.440 | 3,880 | 0.249 | 0.412 | 0.727 | 3,902 | 0.251 | 0.402 | 0.705 | 0.010 |
| registration | registration day missing | 2 | 1 | 0.500 | 2 | 1.000 | 1.000 | 0.500 | 2 | 1.000 | 1.000 | 0.500 | 0.000 |
| student_in_training_runs | False | 14,138 | 5,957 | 0.421 | 3,289 | 0.233 | 0.395 | 0.715 | 3,367 | 0.238 | 0.389 | 0.689 | 0.005 |
| student_in_training_runs | True | 1,586 | 954 | 0.602 | 666 | 0.420 | 0.544 | 0.779 | 588 | 0.371 | 0.490 | 0.794 | 0.055 |
[saved] aq-3/results/errors_by_slice.csv  (23 rows x 14 columns)

### Who is on which list

| membership | enrolments | non_completion_rate | share_withdrawn | share_fail | share_no_activity | share_flagged_by_rule | median_activity_ratio |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| both lists | 3,053 | 0.763 | 0.322 | 0.441 | 0.201 | 0.926 | 0.168 |
| model list only | 902 | 0.600 | 0.269 | 0.330 | 0.000 | 0.211 | 0.667 |
| neither list | 10,867 | 0.330 | 0.154 | 0.176 | 0.000 | 0.059 | 1.361 |
| rule list only | 902 | 0.507 | 0.231 | 0.276 | 0.010 | 0.846 | 0.436 |
[saved] aq-3/results/list_overlap.csv  (4 rows x 8 columns)

Overlap: 3,053 of 3,955 places (77.2%) are the same enrolments on both lists.

### List stability near rank k (within-run bootstrap of enrolments, 500 replicates)

| band | enrolments | mean_share_of_resamples_on_list | min | max |
| :---- | :---- | :---- | :---- | :---- |
| more than 10% inside | 2,389 | 1.000 | 1.000 | 1.000 |
| 5–10% inside | 785 | 1.000 | 0.980 | 1.000 |
| 0–5% inside (last places) | 781 | 0.903 | 0.476 | 1.000 |
| 0–5% outside (first not listed) | 791 | 0.098 | 0.000 | 0.522 |
| 5–10% outside | 785 | 0.000 | 0.000 | 0.016 |
| more than 10% outside | 10,193 | 0.000 | 0.000 | 0.000 |
[saved] aq-3/results/list_stability.csv  (6 rows x 5 columns)

