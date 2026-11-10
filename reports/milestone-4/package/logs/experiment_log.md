# Experiment log – Milestone 4 Level 2 prototype (team N04)

One entry per run, newest last.

## Run 2026-11-09T17:33:13Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:33:13Z / 2026-11-09T17:34:48Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: first full run

## Run 2026-11-09T17:35:23Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:35:23Z / 2026-11-09T17:36:58Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: determinism check, run 1 of 2

## Run 2026-11-09T17:36:58Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:36:58Z / 2026-11-09T17:38:33Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: determinism check, run 2 of 2

## Run 2026-11-09T17:39:35Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:39:35Z / 2026-11-09T17:41:12Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: re-run after lead review: C grid extended to 1e-5..100 (development on 2013, before any 2014 access)

## Run 2026-11-09T17:41:12Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:41:12Z / 2026-11-09T17:42:50Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: determinism check, run 1 of 2

## Run 2026-11-09T17:42:50Z (phase 1: development on 2013 and freeze)

- UTC start / end: 2026-11-09T17:42:50Z / 2026-11-09T17:44:27Z
- Command: `bash src/run_dev.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 01_load_check=0, 02_baselines=0, 03_dev_folds=0, 04_choose=0, 05_freeze=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold and fit); no 2014 row read, no metric on 2014
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '' (empty: test not accessed)
- Test-access record: none (phase 1; the 2014 outcomes are not opened)
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
- Note: determinism check, run 2 of 2

## Test access 2026-11-09T17:55:05Z (phase 2, step 6: single test on the 13 runs of 2014)

- first_test_access_utc: 2026-11-09T17:55:05Z (written to results/freeze.csv before any 2014 row was read)
- Command: `src/06_test.py`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Python 3.12.7
- Frozen models re-verified against results/freeze.csv: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1 OK; models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96 OK
- B3 (fitted on all 2013 runs before access): models/fitted_B3_d13.joblib sha256 a871b9295b4c6a7e414458318cd803b4dab7e520b04efdd8316d265dedcdf8b6; models/fitted_B3_d27.joblib sha256 2268df1b239ef2439d0e6a5227d3649d93cf2a274e6929a3712651bbbb5afe31
- Seeds: SEED=20131; B1 draws default_rng([SEED, 2014, cutoff, run index]), 100 draws

## Run 2026-11-09T17:54:59Z (phase 2: single test on 2014, gates, fairness, sensitivity, AQ4 lists, AQ2 replication, report)

- UTC start / end: 2026-11-09T17:54:59Z / 2026-11-09T17:55:58Z
- Command: `bash src/run_test.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 06_test=0, 07_gates=0, 08_fairness=0, 09_sensitivity=0, 10_aq4_lists=0, 11_aq2_replication=0, 12_report=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: 2013 (fits) and 2014 (scoring only, after the recorded access at 2026-11-09T17:55:05Z); no refit or tuning on 2014; bootstrap B=2000, seed 20131
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Test-access record: first_test_access_utc 2026-11-09T17:55:05Z (results/freeze.csv); this run used 06_test.py --reproduce if the access was already recorded
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
  - Bootstrap: 2000 resamples, seeded default_rng([20131, purpose]); percentile intervals (Appendix III fixes neither the number nor the interval type). Sign-flip test: exact over all 2^m sign assignments, statistic = mean of per-run normalised-recall differences, one-sided, p counts ties.
  - B3 on the test runs: refitted on all 9 runs of 2013 with the M1 tuning procedure (leave-one-run-out, extended C grid) before the test access; saved as models/fitted_B3_d<cutoff>.joblib with its hash in results/b3_fit.csv.
  - Net benefit: thresholds 0.05-0.95 by 0.05, pooled over the test runs; the rule as a policy contacts every flagged student (early_sign_rule); B1 has no probability and is omitted.
  - Calibration: statsmodels GLM Binomial on the pooled test rows; CITL with logit(p) as offset, slope from logit(y) ~ 1 + logit(p); S3 is judged on M1 at day 27 only, other rows are descriptive.
  - Fairness: recall pooled within run as sum of listed non-completers over sum of non-completers per group; Holm applied to one-sided bootstrap p-values (share of resamples with difference >= 0), each group's upper bound taken at its Holm level; gender and age rows are descriptive.
  - Sensitivity 'module CCC apart' is run as two variants: CCC runs only and the runs without CCC.
  - Labels-available variant: M1 specification tuned (leave-one-run-out) and fitted on the 3 runs of 2013B only, scored on the 6 runs of 2014B, compared with the rule on the same runs.
- Note: phase 2, first and only test access

## Run 2026-11-09T17:57:45Z (phase 2: single test on 2014, gates, fairness, sensitivity, AQ4 lists, AQ2 replication, report)

- UTC start / end: 2026-11-09T17:57:45Z / 2026-11-09T17:58:42Z
- Command: `bash src/run_test.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 06_test_reproduce=0, 07_gates=0, 08_fairness=0, 09_sensitivity=0, 10_aq4_lists=0, 11_aq2_replication=0, 12_report=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: 2013 (fits) and 2014 (scoring only, after the recorded access at 2026-11-09T17:55:05Z); no refit or tuning on 2014; bootstrap B=2000, seed 20131
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Test-access record: first_test_access_utc 2026-11-09T17:55:05Z (results/freeze.csv); this run used 06_test.py --reproduce if the access was already recorded
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
  - Bootstrap: 2000 resamples, seeded default_rng([20131, purpose]); percentile intervals (Appendix III fixes neither the number nor the interval type). Sign-flip test: exact over all 2^m sign assignments, statistic = mean of per-run normalised-recall differences, one-sided, p counts ties.
  - B3 on the test runs: refitted on all 9 runs of 2013 with the M1 tuning procedure (leave-one-run-out, extended C grid) before the test access; saved as models/fitted_B3_d<cutoff>.joblib with its hash in results/b3_fit.csv.
  - Net benefit: thresholds 0.05-0.95 by 0.05, pooled over the test runs; the rule as a policy contacts every flagged student (early_sign_rule); B1 has no probability and is omitted.
  - Calibration: statsmodels GLM Binomial on the pooled test rows; CITL with logit(p) as offset, slope from logit(y) ~ 1 + logit(p); S3 is judged on M1 at day 27 only, other rows are descriptive.
  - Fairness: recall pooled within run as sum of listed non-completers over sum of non-completers per group; Holm applied to one-sided bootstrap p-values (share of resamples with difference >= 0), each group's upper bound taken at its Holm level; gender and age rows are descriptive.
  - Sensitivity 'module CCC apart' is run as two variants: CCC runs only and the runs without CCC.
  - AQ2 replication: the copied Milestone 5 model gives a sign x module term only to modules where the sign occurs (no 2014 CCC enrolment has a late TMA, which made the copied model singular); a module without the sign gets the average-module effect. The 2013 estimates still equal the Milestone 5 results exactly (31 of 31).
  - Labels-available variant: M1 specification tuned (leave-one-run-out) and fitted on the 3 runs of 2013B only, scored on the 6 runs of 2014B, compared with the rule on the same runs.
- Note: phase-2 determinism check, run 1 of 2

## Run 2026-11-09T17:58:42Z (phase 2: single test on 2014, gates, fairness, sensitivity, AQ4 lists, AQ2 replication, report)

- UTC start / end: 2026-11-09T17:58:42Z / 2026-11-09T17:59:39Z
- Command: `bash src/run_test.sh`
- Git commit: 71d764c921e04193666a43b7a6083cf53acda89f+uncommitted-package-changes
- Exit status: 0 (tests=0, 06_test_reproduce=0, 07_gates=0, 08_fairness=0, 09_sensitivity=0, 10_aq4_lists=0, 11_aq2_replication=0, 12_report=0)
- Python 3.12.7; numpy 2.5.4, pandas 3.1.1, polars 2.1.0, scipy 1.18.1, scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, statsmodels 0.15.0
- Prepared data: OULAD-N04-prepared-1.0 (hash check in logs/01_load_check.log, results/input_hashes.csv); files read: features_d13.parquet c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6; features_d27.parquet 4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347; capacity_by_run.parquet 38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08
- Metadata read (no manifest hash; recorded): data/metadata/version_manifest.json 3a2be1989591cf5ab45fd80d4fccda7f06f9b6fc0767a31e8df408df239f7ce0; data/metadata/predictor_sets.json 0ad6ee292b134a7faa2bbc21ea4383352f42963b6e36765fad9f7cc89f7c1df3; data/metadata/data_dictionary.md 2743cdaebe23fe94d836041bf8efdffa93988738e3e2e5f278d7b38d25b1f688
- Seeds: SEED=20131 (B1 draws: numpy default_rng([SEED, cutoff, fold index]), 100 draws; HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)
- Rows read: 2013 (fits) and 2014 (scoring only, after the recorded access at 2026-11-09T17:55:05Z); no refit or tuning on 2014; bootstrap B=2000, seed 20131
- Folds, day 13: leave-one-run-out over 9 runs: AAA_2013J (valid 370, train 11710, removed 0), BBB_2013B (valid 1607, train 10438, removed 35), BBB_2013J (valid 1852, train 10197, removed 31), DDD_2013B (valid 1197, train 10824, removed 59), DDD_2013J (valid 1675, train 10349, removed 56), EEE_2013J (valid 934, train 11141, removed 5), FFF_2013B (valid 1520, train 10527, removed 33), FFF_2013J (valid 1998, train 10044, removed 38), GGG_2013J (valid 927, train 11152, removed 1)
- Folds, day 27: leave-one-run-out over 9 runs: AAA_2013J (valid 369, train 11442, removed 0), BBB_2013B (valid 1530, train 10248, removed 33), BBB_2013J (valid 1834, train 9948, removed 29), DDD_2013B (valid 1143, train 10613, removed 55), DDD_2013J (valid 1647, train 10111, removed 53), EEE_2013J (valid 927, train 10879, removed 5), FFF_2013B (valid 1454, train 10326, removed 31), FFF_2013J (valid 1983, train 9793, removed 35), GGG_2013J (valid 924, train 10886, removed 1)
- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)
- Freeze: models/frozen_M1_d13.joblib sha256 5eeb1b3234bee08c6173eb55499c846235092c1cc25e44dac8a2f1b2a82c0fd1; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Freeze: models/frozen_M1_d27.joblib sha256 49f462fbeb6d1631ecf233cc46a370da0947365f4be48a18c125aa10a86b9a96; first_test_access_utc '2026-11-09T17:55:05Z' (empty: test not accessed)
- Test-access record: first_test_access_utc 2026-11-09T17:55:05Z (results/freeze.csv); this run used 06_test.py --reproduce if the access was already recorded
- Deviations from the contract (implementation details it leaves open):
  - Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).
  - Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).
  - Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.
  - B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.
  - Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending id_student (randomised by the provider); not specified in the contract.
  - B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list and roc_auc_within_run are those means.
  - Trees: module and start month enter as native categories of HistGradientBoostingClassifier (levels learnt in the training fold, unseen level -> missing); education as its ordinal code; early stopping off so the number of trees is the tuned value.
  - List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use capacity_by_run itself (equal by construction, asserted).
  - freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the contract is kept and the cut-off is written in the spec column.
  - Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, ties to the simpler (order M1 < M2 < M3 < M4).
  - C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary (C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).
  - version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 values are recorded in the experiment log instead.
  - Bootstrap: 2000 resamples, seeded default_rng([20131, purpose]); percentile intervals (Appendix III fixes neither the number nor the interval type). Sign-flip test: exact over all 2^m sign assignments, statistic = mean of per-run normalised-recall differences, one-sided, p counts ties.
  - B3 on the test runs: refitted on all 9 runs of 2013 with the M1 tuning procedure (leave-one-run-out, extended C grid) before the test access; saved as models/fitted_B3_d<cutoff>.joblib with its hash in results/b3_fit.csv.
  - Net benefit: thresholds 0.05-0.95 by 0.05, pooled over the test runs; the rule as a policy contacts every flagged student (early_sign_rule); B1 has no probability and is omitted.
  - Calibration: statsmodels GLM Binomial on the pooled test rows; CITL with logit(p) as offset, slope from logit(y) ~ 1 + logit(p); S3 is judged on M1 at day 27 only, other rows are descriptive.
  - Fairness: recall pooled within run as sum of listed non-completers over sum of non-completers per group; Holm applied to one-sided bootstrap p-values (share of resamples with difference >= 0), each group's upper bound taken at its Holm level; gender and age rows are descriptive.
  - Sensitivity 'module CCC apart' is run as two variants: CCC runs only and the runs without CCC.
  - AQ2 replication: the copied Milestone 5 model gives a sign x module term only to modules where the sign occurs (no 2014 CCC enrolment has a late TMA, which made the copied model singular); a module without the sign gets the average-module effect. The 2013 estimates still equal the Milestone 5 results exactly (31 of 31).
  - Labels-available variant: M1 specification tuned (leave-one-run-out) and fitted on the 3 runs of 2013B only, scored on the 6 runs of 2014B, compared with the rule on the same runs.
- Note: phase-2 determinism check, run 2 of 2

