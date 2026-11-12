# Experiment log

One row per executed step, appended by `common/run_step.py` in run order. Each row links to the step's full console log.

| Started (UTC) | Folder | Step | Command | Exit | Seconds | Log |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-12T15:33:58Z | logs | tests_lib | `python common/tests/test_lib.py` | 0 | 1.5 | [tests_lib.md](tests_lib.md) |
| 2026-11-12T15:34:00Z | logs | tests_aq2_model | `python common/tests/test_aq2_model.py` | 0 | 1.8 | [tests_aq2_model.md](tests_aq2_model.md) |
| 2026-11-12T15:34:02Z | aq-1 | 01_extract_2013 | `python aq-1/code/01_extract.py --scope 2013` | 0 | 0.5 | [01_extract_2013.md](../aq-1/logs/01_extract_2013.md) |
| 2026-11-12T15:34:02Z | aq-1 | 02_analyse_2013 | `python aq-1/code/02_analyse.py --scope 2013` | 0 | 0.5 | [02_analyse_2013.md](../aq-1/logs/02_analyse_2013.md) |
| 2026-11-12T15:34:03Z | aq-1 | 03_checks_2013 | `python aq-1/code/03_checks.py --scope 2013` | 0 | 0.6 | [03_checks_2013.md](../aq-1/logs/03_checks_2013.md) |
| 2026-11-12T15:34:03Z | aq-2 | 01_extract_2013 | `python aq-2/code/01_extract.py --scope 2013` | 0 | 1.5 | [01_extract_2013.md](../aq-2/logs/01_extract_2013.md) |
| 2026-11-12T15:34:05Z | aq-2 | 02_associations_2013 | `python aq-2/code/02_associations.py --scope 2013` | 0 | 2.8 | [02_associations_2013.md](../aq-2/logs/02_associations_2013.md) |
| 2026-11-12T15:34:08Z | aq-3 | 01_extract | `python aq-3/code/01_extract.py` | 0 | 2.4 | [01_extract.md](../aq-3/logs/01_extract.md) |
| 2026-11-12T15:34:10Z | aq-3 | 02_dev_folds | `python aq-3/code/02_dev_folds.py` | 0 | 142.3 | [02_dev_folds.md](../aq-3/logs/02_dev_folds.md) |
| 2026-11-12T15:36:32Z | aq-3 | 03_choose | `python aq-3/code/03_choose.py` | 0 | 1.5 | [03_choose.md](../aq-3/logs/03_choose.md) |
| 2026-11-12T15:36:34Z | aq-3 | 04_freeze | `python aq-3/code/04_freeze.py` | 0 | 482.7 | [04_freeze.md](../aq-3/logs/04_freeze.md) |
| 2026-11-12T15:44:37Z | aq-3 | 05_test | `python aq-3/code/05_test.py` | 0 | 24.5 | [05_test.md](../aq-3/logs/05_test.md) |
| 2026-11-12T15:45:01Z | aq-3 | 06_secondary | `python aq-3/code/06_secondary.py` | 0 | 2.4 | [06_secondary.md](../aq-3/logs/06_secondary.md) |
| 2026-11-12T15:45:04Z | aq-3 | 07_error_analysis | `python aq-3/code/07_error_analysis.py` | 0 | 1.6 | [07_error_analysis.md](../aq-3/logs/07_error_analysis.md) |
| 2026-11-12T15:45:06Z | aq-3 | 08_sensitivity | `python aq-3/code/08_sensitivity.py` | 0 | 25.7 | [08_sensitivity.md](../aq-3/logs/08_sensitivity.md) |
| 2026-11-12T15:45:31Z | aq-4 | 01_lists | `python aq-4/code/01_lists.py` | 0 | 1.7 | [01_lists.md](../aq-4/logs/01_lists.md) |
| 2026-11-12T15:45:33Z | aq-4 | 02_evaluate | `python aq-4/code/02_evaluate.py` | 0 | 0.3 | [02_evaluate.md](../aq-4/logs/02_evaluate.md) |
| 2026-11-12T15:45:33Z | aq-4 | 03_fairness | `python aq-4/code/03_fairness.py` | 0 | 35.0 | [03_fairness.md](../aq-4/logs/03_fairness.md) |
| 2026-11-12T15:46:08Z | aq-2 | 01_extract_2014 | `python aq-2/code/01_extract.py --scope 2014` | 0 | 1.5 | [01_extract_2014.md](../aq-2/logs/01_extract_2014.md) |
| 2026-11-12T15:46:10Z | aq-2 | 02_associations_2014 | `python aq-2/code/02_associations.py --scope 2014` | 0 | 3.5 | [02_associations_2014.md](../aq-2/logs/02_associations_2014.md) |
| 2026-11-12T15:46:13Z | aq-2 | 03_replication | `python aq-2/code/03_replication.py` | 0 | 1.4 | [03_replication.md](../aq-2/logs/03_replication.md) |
| 2026-11-12T15:46:15Z | aq-1 | 01_extract_all | `python aq-1/code/01_extract.py --scope all` | 0 | 0.5 | [01_extract_all.md](../aq-1/logs/01_extract_all.md) |
| 2026-11-12T15:46:15Z | aq-1 | 02_analyse_all | `python aq-1/code/02_analyse.py --scope all` | 0 | 0.5 | [02_analyse_all.md](../aq-1/logs/02_analyse_all.md) |
| 2026-11-12T15:46:16Z | aq-1 | 03_checks_all | `python aq-1/code/03_checks.py --scope all` | 0 | 1.2 | [03_checks_all.md](../aq-1/logs/03_checks_all.md) |
| 2026-11-12T15:46:17Z | aq-3 | 09_verify | `python aq-3/code/09_verify.py` | 0 | 1.8 | [09_verify.md](../aq-3/logs/09_verify.md) |
| 2026-11-12T15:46:19Z | aq-3 | 10_crosscheck_earlier_run | `python aq-3/code/10_crosscheck_earlier_run.py` | 0 | 1.4 | [10_crosscheck_earlier_run.md](../aq-3/logs/10_crosscheck_earlier_run.md) |
| 2026-11-12T15:46:21Z | logs | compare_first_run | `python common/compare_first_run.py` | 1 | 1.8 | [compare_first_run.md](compare_first_run.md) |
