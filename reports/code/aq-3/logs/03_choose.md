# Log: aq-3 / 03_choose

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:50:56Z |
| Finished (UTC) | 2026-11-12T15:50:57Z |
| Duration | 1.4 s |
| Command | `python aq-3/code/03_choose.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ3 model choice (development folds, day 27, 5 per 20)

**Normalised recall per validation run**

| run | B2_rule | B3 | M1 | M2 | M3 | M4 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 0.385 | 0.308 | 0.462 | 0.462 | 0.495 | 0.462 |
| BBB-2013B | 0.795 | 0.571 | 0.829 | 0.829 | 0.826 | 0.821 |
| BBB-2013J | 0.680 | 0.543 | 0.713 | 0.713 | 0.704 | 0.709 |
| DDD-2013B | 0.890 | 0.724 | 0.883 | 0.886 | 0.886 | 0.897 |
| DDD-2013J | 0.817 | 0.629 | 0.824 | 0.829 | 0.829 | 0.834 |
| EEE-2013J | 0.685 | 0.417 | 0.660 | 0.668 | 0.630 | 0.634 |
| FFF-2013B | 0.723 | 0.573 | 0.767 | 0.759 | 0.770 | 0.764 |
| FFF-2013J | 0.740 | 0.610 | 0.772 | 0.772 | 0.780 | 0.778 |
| GGG-2013J | 0.502 | 0.468 | 0.532 | 0.511 | 0.515 | 0.506 |

**Choice table**

| config | pooled_normalised_recall | gain_vs_M1 | extra_non_completers_listed_vs_M1 | folds_with_gain_vs_M1 | meets_margin_0.03 | meets_7_of_9_folds | chosen |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| B3 | 0.5682 | -0.1821 | -542 | 0 | no | no | no |
| M1 | 0.7503 | 0.0000 | 0 | 0 | no | no | yes |
| M2 | 0.7493 | -0.0010 | -3 | 3 | no | no | no |
| M3 | 0.7487 | -0.0017 | -5 | 5 | no | no | no |
| M4 | 0.7480 | -0.0024 | -7 | 3 | no | no | no |

**Chosen configuration: M1** – Penalised logistic regression, primary set (primary approach). Reason: no challenger gains 0.03 pooled normalised recall and 7 of 9 folds, so the primary approach of Level 1 stays.
[saved] aq-3/results/model_choice.csv  (5 rows x 10 columns)

**Development only: M1 against the rule and the background-only model, per fold**

| run | B2_rule | M1 | B3 | M1_minus_rule |
| :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 0.385 | 0.462 | 0.308 | 0.077 |
| BBB-2013B | 0.795 | 0.829 | 0.571 | 0.034 |
| BBB-2013J | 0.680 | 0.713 | 0.543 | 0.033 |
| DDD-2013B | 0.890 | 0.883 | 0.724 | -0.007 |
| DDD-2013J | 0.817 | 0.824 | 0.629 | 0.007 |
| EEE-2013J | 0.685 | 0.660 | 0.417 | -0.026 |
| FFF-2013B | 0.723 | 0.767 | 0.573 | 0.044 |
| FFF-2013J | 0.740 | 0.772 | 0.610 | 0.032 |
| GGG-2013J | 0.502 | 0.532 | 0.468 | 0.030 |

pooled: rule 0.7272, background-only 0.5682, M1 0.7503; M1 above the rule in 7 of 9 folds. These fold values serve the choice only.
[saved] aq-3/results/dev_m1_vs_rule_by_fold.csv  (9 rows x 5 columns)

