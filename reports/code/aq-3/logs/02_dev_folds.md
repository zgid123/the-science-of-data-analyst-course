# Log: aq-3 / 02_dev_folds

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:02:27Z |
| Finished (UTC) | 2026-11-11T23:05:34Z |
| Duration | 186.8 s |
| Command | `python aq-3/code/02_dev_folds.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ3 development folds (2013 runs only)

90 fits = 5 configurations x 2 cut-offs x 9 validation runs, each with an inner 8-run tuning loop
finished in 183 s
[saved] aq-3/extracted-datasets/aq3_dev_oof_scores_d27.csv  (11,811 rows x 13 columns)  – out-of-fold scores, 2013 runs
[saved] aq-3/extracted-datasets/aq3_dev_oof_scores_d13.csv  (12,080 rows x 13 columns)  – out-of-fold scores, 2013 runs
[saved] aq-3/results/dev_folds.csv  (216 rows x 17 columns)
[saved] aq-3/results/dev_tuning.csv  (1,080 rows x 6 columns)
[saved] aq-3/results/dev_fold_design.csv  (90 rows x 7 columns)
[saved] aq-3/results/dev_pooled.csv  (24 rows x 17 columns)

**Fold design at day 27 (the same for every configuration)**

| validation_run | train_rows | students_removed | rows_removed |
| :---- | :---- | :---- | :---- |
| AAA-2013J | 11,442 | 0 | 0 |
| BBB-2013B | 10,248 | 33 | 33 |
| BBB-2013J | 9,948 | 29 | 29 |
| DDD-2013B | 10,613 | 55 | 55 |
| DDD-2013J | 10,111 | 53 | 53 |
| EEE-2013J | 10,879 | 5 | 5 |
| FFF-2013B | 10,326 | 31 | 31 |
| FFF-2013J | 9,793 | 35 | 35 |
| GGG-2013J | 10,886 | 1 | 1 |

**Hyperparameters chosen by the inner loops (number of outer folds)**

| cutoff | config | grid_point | folds |
| :---- | :---- | :---- | :---- |
| 27 | B3 | {"C": 0.01} | 3 |
| 27 | B3 | {"C": 0.1} | 2 |
| 27 | B3 | {"C": 0.003} | 2 |
| 27 | B3 | {"C": 0.03} | 1 |
| 27 | B3 | {"C": 10.0} | 1 |
| 27 | M1 | {"C": 0.003} | 3 |
| 27 | M1 | {"C": 0.1} | 2 |
| 27 | M1 | {"C": 0.3} | 2 |
| 27 | M1 | {"C": 0.01} | 1 |
| 27 | M1 | {"C": 10.0} | 1 |
| 27 | M2 | {"C": 0.3} | 4 |
| 27 | M2 | {"C": 0.003} | 2 |
| 27 | M2 | {"C": 0.01} | 1 |
| 27 | M2 | {"C": 1.0} | 1 |
| 27 | M2 | {"C": 0.1} | 1 |
| 27 | M3 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 4 |
| 27 | M3 | {"max_depth": 2, "learning_rate": 0.1, "trees": 100} | 2 |
| 27 | M3 | {"max_depth": 2, "learning_rate": 0.05, "trees": 100} | 1 |
| 27 | M3 | {"max_depth": 3, "learning_rate": 0.05, "trees": 100} | 1 |
| 27 | M3 | {"max_depth": 3, "learning_rate": 0.1, "trees": 100} | 1 |
| 27 | M4 | {"max_depth": 2, "learning_rate": 0.05, "trees": 100} | 3 |
| 27 | M4 | {"max_depth": 2, "learning_rate": 0.05, "trees": 400} | 2 |
| 27 | M4 | {"max_depth": 4, "learning_rate": 0.05, "trees": 100} | 1 |
| 27 | M4 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 1 |
| 27 | M4 | {"max_depth": 3, "learning_rate": 0.05, "trees": 100} | 1 |
| 27 | M4 | {"max_depth": 2, "learning_rate": 0.1, "trees": 200} | 1 |
| 13 | B3 | {"C": 0.01} | 2 |
| 13 | B3 | {"C": 0.003} | 2 |
| 13 | B3 | {"C": 0.03} | 2 |
| 13 | B3 | {"C": 0.3} | 1 |
| 13 | B3 | {"C": 10.0} | 1 |
| 13 | B3 | {"C": 0.1} | 1 |
| 13 | M1 | {"C": 0.03} | 3 |
| 13 | M1 | {"C": 0.003} | 3 |
| 13 | M1 | {"C": 0.01} | 3 |
| 13 | M2 | {"C": 0.1} | 3 |
| 13 | M2 | {"C": 0.003} | 3 |
| 13 | M2 | {"C": 0.01} | 2 |
| 13 | M2 | {"C": 0.03} | 1 |
| 13 | M3 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 4 |
| 13 | M3 | {"max_depth": 2, "learning_rate": 0.1, "trees": 100} | 4 |
| 13 | M3 | {"max_depth": 2, "learning_rate": 0.05, "trees": 400} | 1 |
| 13 | M4 | {"max_depth": 2, "learning_rate": 0.1, "trees": 100} | 3 |
| 13 | M4 | {"max_depth": 2, "learning_rate": 0.1, "trees": 200} | 3 |
| 13 | M4 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 2 |
| 13 | M4 | {"max_depth": 2, "learning_rate": 0.05, "trees": 400} | 1 |

**Pooled over the 9 development folds (for the model choice only)**

| cutoff | per20 | ranking | non_completers_on_list | max_attainable | pooled_normalised_recall | random_list_normalised_recall | pooled_recall | pooled_precision | base_rate | pooled_lift |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 13 | 3 | B2_rule | 1,334 | 1,821 | 0.733 | 0.457 | 0.242 | 0.733 | 0.457 | 1.603 |
| 13 | 3 | B3 | 1,123 | 1,821 | 0.617 | 0.457 | 0.203 | 0.617 | 0.457 | 1.350 |
| 13 | 3 | M1 | 1,415 | 1,821 | 0.777 | 0.457 | 0.256 | 0.777 | 0.457 | 1.701 |
| 13 | 3 | M2 | 1,404 | 1,821 | 0.771 | 0.457 | 0.254 | 0.771 | 0.457 | 1.688 |
| 13 | 3 | M3 | 1,405 | 1,821 | 0.772 | 0.457 | 0.255 | 0.772 | 0.457 | 1.689 |
| 13 | 3 | M4 | 1,396 | 1,821 | 0.767 | 0.457 | 0.253 | 0.767 | 0.457 | 1.678 |
| 13 | 5 | B2_rule | 2,065 | 3,032 | 0.681 | 0.457 | 0.374 | 0.680 | 0.457 | 1.489 |
| 13 | 5 | B3 | 1,767 | 3,032 | 0.583 | 0.457 | 0.320 | 0.582 | 0.457 | 1.274 |
| 13 | 5 | M1 | 2,162 | 3,032 | 0.713 | 0.457 | 0.392 | 0.712 | 0.457 | 1.559 |
| 13 | 5 | M2 | 2,180 | 3,032 | 0.719 | 0.457 | 0.395 | 0.718 | 0.457 | 1.572 |
| 13 | 5 | M3 | 2,183 | 3,032 | 0.720 | 0.457 | 0.396 | 0.719 | 0.457 | 1.574 |
| 13 | 5 | M4 | 2,191 | 3,032 | 0.723 | 0.457 | 0.397 | 0.722 | 0.457 | 1.580 |
| 27 | 3 | B2_rule | 1,425 | 1,788 | 0.797 | 0.444 | 0.272 | 0.797 | 0.444 | 1.795 |
| 27 | 3 | B3 | 1,073 | 1,788 | 0.600 | 0.444 | 0.205 | 0.600 | 0.444 | 1.351 |
| 27 | 3 | M1 | 1,475 | 1,788 | 0.825 | 0.444 | 0.281 | 0.825 | 0.444 | 1.858 |
| 27 | 3 | M2 | 1,472 | 1,788 | 0.823 | 0.444 | 0.281 | 0.823 | 0.444 | 1.854 |
| 27 | 3 | M3 | 1,468 | 1,788 | 0.821 | 0.444 | 0.280 | 0.821 | 0.444 | 1.849 |
| 27 | 3 | M4 | 1,469 | 1,788 | 0.822 | 0.444 | 0.280 | 0.822 | 0.444 | 1.850 |
| 27 | 5 | B2_rule | 2,164 | 2,976 | 0.727 | 0.445 | 0.413 | 0.726 | 0.444 | 1.635 |
| 27 | 5 | B3 | 1,691 | 2,976 | 0.568 | 0.445 | 0.322 | 0.567 | 0.444 | 1.278 |
| 27 | 5 | M1 | 2,233 | 2,976 | 0.750 | 0.445 | 0.426 | 0.749 | 0.444 | 1.687 |
| 27 | 5 | M2 | 2,230 | 2,976 | 0.749 | 0.445 | 0.425 | 0.748 | 0.444 | 1.685 |
| 27 | 5 | M3 | 2,228 | 2,976 | 0.749 | 0.445 | 0.425 | 0.748 | 0.444 | 1.684 |
| 27 | 5 | M4 | 2,226 | 2,976 | 0.748 | 0.445 | 0.424 | 0.747 | 0.444 | 1.682 |

