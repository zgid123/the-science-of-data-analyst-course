# Experiment log

One row per executed step, appended by `common/run_step.py` in run order. Each row links to the step's full console log.

| Started (UTC) | Folder | Step | Command | Exit | Seconds | Log |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-12T15:48:06Z | logs | tests_lib | `python common/tests/test_lib.py` | 0 | 1.7 | [tests_lib.md](tests_lib.md) |
| 2026-11-12T15:48:08Z | logs | tests_aq2_model | `python common/tests/test_aq2_model.py` | 0 | 1.5 | [tests_aq2_model.md](tests_aq2_model.md) |
| 2026-11-12T15:48:10Z | aq-1 | 01_extract_2013 | `python aq-1/code/01_extract.py --scope 2013` | 0 | 0.5 | [01_extract_2013.md](../aq-1/logs/01_extract_2013.md) |
| 2026-11-12T15:48:10Z | aq-1 | 02_analyse_2013 | `python aq-1/code/02_analyse.py --scope 2013` | 0 | 0.5 | [02_analyse_2013.md](../aq-1/logs/02_analyse_2013.md) |
| 2026-11-12T15:48:11Z | aq-1 | 03_checks_2013 | `python aq-1/code/03_checks.py --scope 2013` | 0 | 0.5 | [03_checks_2013.md](../aq-1/logs/03_checks_2013.md) |
| 2026-11-12T15:48:11Z | aq-2 | 01_extract_2013 | `python aq-2/code/01_extract.py --scope 2013` | 0 | 1.6 | [01_extract_2013.md](../aq-2/logs/01_extract_2013.md) |
| 2026-11-12T15:48:13Z | aq-2 | 02_associations_2013 | `python aq-2/code/02_associations.py --scope 2013` | 0 | 2.8 | [02_associations_2013.md](../aq-2/logs/02_associations_2013.md) |
| 2026-11-12T15:48:16Z | aq-3 | 01_extract | `python aq-3/code/01_extract.py` | 0 | 1.5 | [01_extract.md](../aq-3/logs/01_extract.md) |
| 2026-11-12T15:48:18Z | aq-3 | 02_dev_folds | `python aq-3/code/02_dev_folds.py` | 0 | 158.1 | [02_dev_folds.md](../aq-3/logs/02_dev_folds.md) |
| 2026-11-12T15:50:56Z | aq-3 | 03_choose | `python aq-3/code/03_choose.py` | 0 | 1.4 | [03_choose.md](../aq-3/logs/03_choose.md) |
| 2026-11-12T15:50:57Z | aq-3 | 04_freeze | `python aq-3/code/04_freeze.py` | 0 | 473.7 | [04_freeze.md](../aq-3/logs/04_freeze.md) |
| 2026-11-12T15:58:51Z | aq-3 | 05_test | `python aq-3/code/05_test.py` | 0 | 25.1 | [05_test.md](../aq-3/logs/05_test.md) |
| 2026-11-12T15:59:16Z | aq-3 | 06_secondary | `python aq-3/code/06_secondary.py` | 0 | 2.6 | [06_secondary.md](../aq-3/logs/06_secondary.md) |
| 2026-11-12T15:59:19Z | aq-3 | 07_error_analysis | `python aq-3/code/07_error_analysis.py` | 0 | 1.7 | [07_error_analysis.md](../aq-3/logs/07_error_analysis.md) |
| 2026-11-12T15:59:21Z | aq-3 | 08_sensitivity | `python aq-3/code/08_sensitivity.py` | 0 | 25.6 | [08_sensitivity.md](../aq-3/logs/08_sensitivity.md) |
| 2026-11-12T15:59:46Z | aq-4 | 01_lists | `python aq-4/code/01_lists.py` | 0 | 1.7 | [01_lists.md](../aq-4/logs/01_lists.md) |
| 2026-11-12T15:59:48Z | aq-4 | 02_evaluate | `python aq-4/code/02_evaluate.py` | 0 | 0.2 | [02_evaluate.md](../aq-4/logs/02_evaluate.md) |
| 2026-11-12T15:59:48Z | aq-4 | 03_fairness | `python aq-4/code/03_fairness.py` | 0 | 34.1 | [03_fairness.md](../aq-4/logs/03_fairness.md) |
| 2026-11-12T16:00:22Z | aq-2 | 01_extract_2014 | `python aq-2/code/01_extract.py --scope 2014` | 0 | 1.5 | [01_extract_2014.md](../aq-2/logs/01_extract_2014.md) |
| 2026-11-12T16:00:24Z | aq-2 | 02_associations_2014 | `python aq-2/code/02_associations.py --scope 2014` | 0 | 3.4 | [02_associations_2014.md](../aq-2/logs/02_associations_2014.md) |
| 2026-11-12T16:00:27Z | aq-2 | 03_replication | `python aq-2/code/03_replication.py` | 0 | 1.5 | [03_replication.md](../aq-2/logs/03_replication.md) |
| 2026-11-12T16:00:29Z | aq-1 | 01_extract_all | `python aq-1/code/01_extract.py --scope all` | 0 | 0.5 | [01_extract_all.md](../aq-1/logs/01_extract_all.md) |
| 2026-11-12T16:00:29Z | aq-1 | 02_analyse_all | `python aq-1/code/02_analyse.py --scope all` | 0 | 0.6 | [02_analyse_all.md](../aq-1/logs/02_analyse_all.md) |
| 2026-11-12T16:00:30Z | aq-1 | 03_checks_all | `python aq-1/code/03_checks.py --scope all` | 0 | 1.1 | [03_checks_all.md](../aq-1/logs/03_checks_all.md) |
| 2026-11-12T16:00:31Z | aq-3 | 09_verify | `python aq-3/code/09_verify.py` | 0 | 1.6 | [09_verify.md](../aq-3/logs/09_verify.md) |
| 2026-11-12T16:00:33Z | aq-3 | 10_crosscheck_earlier_run | `python aq-3/code/10_crosscheck_earlier_run.py` | 0 | 1.4 | [10_crosscheck_earlier_run.md](../aq-3/logs/10_crosscheck_earlier_run.md) |
| 2026-11-12T16:00:34Z | logs | compare_first_run | `python common/compare_first_run.py` | 0 | 1.6 | [compare_first_run.md](compare_first_run.md) |
| 2026-11-12T16:00:36Z | logs | determinism_before | `python common/hash_outputs.py before` | 0 | 0.2 | [determinism_before.md](determinism_before.md) |
| 2026-11-12T16:00:36Z | aq-3 | 02_dev_folds_rerun | `python aq-3/code/02_dev_folds.py` | 0 | 469.2 | [02_dev_folds_rerun.md](../aq-3/logs/02_dev_folds_rerun.md) |
| 2026-11-12T16:08:26Z | logs | determinism_after | `python common/hash_outputs.py after` | 0 | 7.3 | [determinism_after.md](determinism_after.md) |
| 2026-11-12T16:08:33Z | aq-1 | 04_figures | `python aq-1/code/04_figures.py` | 0 | 6.2 | [04_figures.md](../aq-1/logs/04_figures.md) |
| 2026-11-12T16:08:40Z | aq-2 | 04_figures | `python aq-2/code/04_figures.py` | 0 | 9.1 | [04_figures.md](../aq-2/logs/04_figures.md) |
| 2026-11-12T16:08:49Z | aq-3 | 11_figures | `python aq-3/code/11_figures.py` | 0 | 8.0 | [11_figures.md](../aq-3/logs/11_figures.md) |
| 2026-11-12T16:08:57Z | aq-4 | 04_figures | `python aq-4/code/04_figures.py` | 0 | 3.7 | [04_figures.md](../aq-4/logs/04_figures.md) |
| 2026-11-12T16:13:46Z | logs | report_tables | `python common/report_tables.py` | 0 | 1.5 | [report_tables.md](report_tables.md) |
| 2026-11-12T16:13:47Z | logs | fill_report_tables | `python common/fill_report_tables.py` | 0 | 1.2 | [fill_report_tables.md](fill_report_tables.md) |
| 2026-11-12T16:13:49Z | logs | check_reports | `python common/check_reports.py` | 0 | 2.6 | [check_reports.md](check_reports.md) |
| 2026-11-12T16:14:14Z | logs | check_reports | `python common/check_reports.py` | 0 | 1.9 | [check_reports.md](check_reports.md) |
| 2026-11-12T16:14:36Z | logs | check_reports | `python common/check_reports.py` | 0 | 2.3 | [check_reports.md](check_reports.md) |
