# Log: aq-3 / 05_test

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:18:58Z |
| Finished (UTC) | 2026-11-11T23:19:33Z |
| Duration | 35.5 s |
| Command | `python aq-3/code/05_test.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ3 single test – frozen 2026-11-11T23:18:16Z, chosen configuration M1

12 frozen model files match their SHA-256 at the freeze: PASS
[saved] aq-3/extracted-datasets/aq3_test_scores_blind_d27.csv  (15,724 rows x 16 columns)  – scores written before any 2014 outcome is read
[saved] aq-3/extracted-datasets/aq3_test_scores_blind_d13.csv  (15,989 rows x 16 columns)  – scores written before any 2014 outcome is read
[saved] aq-3/extracted-datasets/aq3_test_scored_d27.csv  (15,724 rows x 37 columns)  – test scores with outcomes
[saved] aq-3/extracted-datasets/aq3_test_scored_d13.csv  (15,989 rows x 37 columns)  – test scores with outcomes
[saved] aq-3/results/test_runs.csv  (312 rows x 17 columns)
[saved] aq-3/results/test_pooled.csv  (24 rows x 17 columns)

**Test, pooled over the 13 runs of 2014**

| cutoff | per20 | ranking | enrolments | non_completers | list_length | non_completers_on_list | max_attainable | pooled_normalised_recall | random_list_normalised_recall | pooled_recall | pooled_precision | base_rate | max_attainable_precision | pooled_lift |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 13 | 3 | B2_rule | 15,989 | 7,189 | 2,418 | 1,710 | 2,418 | 0.707 | 0.449 | 0.238 | 0.707 | 0.450 | 1.000 | 1.573 |
| 13 | 3 | B3 | 15,989 | 7,189 | 2,418 | 1,473 | 2,418 | 0.609 | 0.449 | 0.205 | 0.609 | 0.450 | 1.000 | 1.355 |
| 13 | 3 | M1 | 15,989 | 7,189 | 2,418 | 1,795 | 2,418 | 0.742 | 0.449 | 0.250 | 0.742 | 0.450 | 1.000 | 1.651 |
| 13 | 3 | M2 | 15,989 | 7,189 | 2,418 | 1,810 | 2,418 | 0.749 | 0.449 | 0.252 | 0.749 | 0.450 | 1.000 | 1.665 |
| 13 | 3 | M3 | 15,989 | 7,189 | 2,418 | 1,809 | 2,418 | 0.748 | 0.449 | 0.252 | 0.748 | 0.450 | 1.000 | 1.664 |
| 13 | 3 | M4 | 15,989 | 7,189 | 2,418 | 1,802 | 2,418 | 0.745 | 0.449 | 0.251 | 0.745 | 0.450 | 1.000 | 1.657 |
| 13 | 5 | B2_rule | 15,989 | 7,189 | 4,030 | 2,688 | 4,030 | 0.667 | 0.449 | 0.374 | 0.667 | 0.450 | 1.000 | 1.483 |
| 13 | 5 | B3 | 15,989 | 7,189 | 4,030 | 2,328 | 4,030 | 0.578 | 0.449 | 0.324 | 0.578 | 0.450 | 1.000 | 1.285 |
| 13 | 5 | M1 | 15,989 | 7,189 | 4,030 | 2,771 | 4,030 | 0.688 | 0.449 | 0.385 | 0.688 | 0.450 | 1.000 | 1.529 |
| 13 | 5 | M2 | 15,989 | 7,189 | 4,030 | 2,771 | 4,030 | 0.688 | 0.449 | 0.385 | 0.688 | 0.450 | 1.000 | 1.529 |
| 13 | 5 | M3 | 15,989 | 7,189 | 4,030 | 2,768 | 4,030 | 0.687 | 0.449 | 0.385 | 0.687 | 0.450 | 1.000 | 1.528 |
| 13 | 5 | M4 | 15,989 | 7,189 | 4,030 | 2,779 | 4,030 | 0.690 | 0.449 | 0.387 | 0.690 | 0.450 | 1.000 | 1.534 |
| 27 | 3 | B2_rule | 15,724 | 6,911 | 2,373 | 1,846 | 2,373 | 0.778 | 0.439 | 0.267 | 0.778 | 0.440 | 1.000 | 1.770 |
| 27 | 3 | B3 | 15,724 | 6,911 | 2,373 | 1,421 | 2,373 | 0.599 | 0.439 | 0.206 | 0.599 | 0.440 | 1.000 | 1.362 |
| 27 | 3 | M1 | 15,724 | 6,911 | 2,373 | 1,922 | 2,373 | 0.810 | 0.439 | 0.278 | 0.810 | 0.440 | 1.000 | 1.843 |
| 27 | 3 | M2 | 15,724 | 6,911 | 2,373 | 1,925 | 2,373 | 0.811 | 0.439 | 0.279 | 0.811 | 0.440 | 1.000 | 1.846 |
| 27 | 3 | M3 | 15,724 | 6,911 | 2,373 | 1,929 | 2,373 | 0.813 | 0.439 | 0.279 | 0.813 | 0.440 | 1.000 | 1.850 |
| 27 | 3 | M4 | 15,724 | 6,911 | 2,373 | 1,926 | 2,373 | 0.812 | 0.439 | 0.279 | 0.812 | 0.440 | 1.000 | 1.847 |
| 27 | 5 | B2_rule | 15,724 | 6,911 | 3,955 | 2,786 | 3,955 | 0.704 | 0.439 | 0.403 | 0.704 | 0.440 | 1.000 | 1.603 |
| 27 | 5 | B3 | 15,724 | 6,911 | 3,955 | 2,244 | 3,955 | 0.567 | 0.439 | 0.325 | 0.567 | 0.440 | 1.000 | 1.291 |
| 27 | 5 | M1 | 15,724 | 6,911 | 3,955 | 2,870 | 3,955 | 0.726 | 0.439 | 0.415 | 0.726 | 0.440 | 1.000 | 1.651 |
| 27 | 5 | M2 | 15,724 | 6,911 | 3,955 | 2,872 | 3,955 | 0.726 | 0.439 | 0.416 | 0.726 | 0.440 | 1.000 | 1.652 |
| 27 | 5 | M3 | 15,724 | 6,911 | 3,955 | 2,860 | 3,955 | 0.723 | 0.439 | 0.414 | 0.723 | 0.440 | 1.000 | 1.645 |
| 27 | 5 | M4 | 15,724 | 6,911 | 3,955 | 2,880 | 3,955 | 0.728 | 0.439 | 0.417 | 0.728 | 0.440 | 1.000 | 1.657 |

### S1 gate: chosen model against the rule-ranked list, all 13 test runs, all eligible enrolments, day 27, 5 per 20

| run | n | list_length | non_completers | max_attainable | model_on_list | rule_on_list | model_nr | rule_nr | difference |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 348 | 90 | 95 | 90 | 41 | 38 | 0.456 | 0.422 | 0.033 |
| BBB-2014B | 1,280 | 320 | 553 | 320 | 225 | 221 | 0.703 | 0.691 | 0.012 |
| BBB-2014J | 1,786 | 450 | 635 | 450 | 261 | 244 | 0.580 | 0.542 | 0.038 |
| CCC-2014B | 1,500 | 375 | 837 | 375 | 321 | 310 | 0.856 | 0.827 | 0.029 |
| CCC-2014J | 2,021 | 510 | 1,006 | 510 | 389 | 383 | 0.763 | 0.751 | 0.012 |
| DDD-2014B | 1,029 | 260 | 551 | 260 | 223 | 217 | 0.858 | 0.835 | 0.023 |
| DDD-2014J | 1,463 | 370 | 671 | 370 | 287 | 273 | 0.776 | 0.738 | 0.038 |
| EEE-2014B | 605 | 155 | 248 | 155 | 115 | 111 | 0.742 | 0.716 | 0.026 |
| EEE-2014J | 1,020 | 255 | 336 | 255 | 173 | 156 | 0.678 | 0.612 | 0.067 |
| FFF-2014B | 1,299 | 325 | 645 | 325 | 264 | 259 | 0.812 | 0.797 | 0.015 |
| FFF-2014J | 1,859 | 465 | 742 | 465 | 341 | 338 | 0.733 | 0.727 | 0.006 |
| GGG-2014B | 797 | 200 | 319 | 200 | 124 | 128 | 0.620 | 0.640 | -0.020 |
| GGG-2014J | 717 | 180 | 273 | 180 | 106 | 108 | 0.589 | 0.600 | -0.011 |

| Quantity | Value |
| :---- | :---- |
| Pooled normalised recall, model (M1) | 0.7257 (2,870 of 3,955); bootstrap 95% interval 0.6663 to 0.7752 |
| Pooled normalised recall, rule-ranked list | 0.7044 (2,786 of 3,955); bootstrap 95% interval 0.6405 to 0.7547 |
| Difference (model − rule) | +0.0212 = +84 non-completers on lists of 3,955 places |
| 95% paired two-level bootstrap interval of the difference | +0.0065 to +0.0364 (2,000 replicates; share of replicates ≤ 0: 0.0015) |
| Sign-flip test on the 13 per-run differences, one-sided | p = 0.0032 (26 of 8,192 sign assignments) |
| Wins / ties / losses of the model over runs | 11 / 0 / 2 |
| Unweighted mean of per-run differences | +0.0207 |
| Same point estimates with exact ties broken in expectation | model 0.7257, rule 0.7045 |
| **S1 verdict** | **PASS** (needs difference > 0, interval above 0 and p < 0.05) |

[saved] aq-3/results/s1_gate.csv  (1 rows x 29 columns)
[saved] aq-3/results/s1_gate_per_run.csv  (13 rows x 12 columns)
[saved] aq-3/results/s1_bootstrap.csv  (2,000 rows x 3 columns)

### Context only (cannot change the verdict): other rankings against the rule, day 27, 5 per 20

| ranking_a | ranking_b | pooled_nr_a | pooled_nr_b | difference | boot_ci_low | boot_ci_high | signflip_p | wins | ties | losses |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| B3 | B2_rule | 0.5674 | 0.7044 | -0.1370 | -0.1665 | -0.1079 | 1.0000 | 0 | 0 | 13 |
| M2 | B2_rule | 0.7262 | 0.7044 | 0.0217 | 0.0046 | 0.0384 | 0.0219 | 11 | 0 | 2 |
| M3 | B2_rule | 0.7231 | 0.7044 | 0.0187 | 0.0030 | 0.0372 | 0.0125 | 10 | 1 | 2 |
| M4 | B2_rule | 0.7282 | 0.7044 | 0.0238 | 0.0077 | 0.0412 | 0.0106 | 11 | 0 | 2 |
| M1 | B3 | 0.7257 | 0.5674 | 0.1583 | 0.1321 | 0.1864 | 0.0001 | 13 | 0 | 0 |
| M3 | M1 | 0.7231 | 0.7257 | -0.0025 | -0.0122 | 0.0101 | 0.5603 | 5 | 0 | 8 |
| M2 | M1 | 0.7262 | 0.7257 | 0.0005 | -0.0094 | 0.0094 | 0.5977 | 5 | 3 | 5 |
| M4 | M1 | 0.7282 | 0.7257 | 0.0025 | -0.0084 | 0.0146 | 0.3628 | 7 | 1 | 5 |
[saved] aq-3/results/test_context_vs_rule.csv  (8 rows x 11 columns)

