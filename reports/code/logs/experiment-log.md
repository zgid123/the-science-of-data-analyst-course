# Experiment log

One row per executed step, appended by `common/run_step.py` in run order. Each row links to the step's full console log.

| Started (UTC) | Folder | Step | Command | Exit | Seconds | Log |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-11T22:58:39Z | aq-1 | 01_extract_2013 | `python aq-1/code/01_extract.py --scope 2013` | 0 | 1.0 | [01_extract_2013.md](../aq-1/logs/01_extract_2013.md) |
| 2026-11-11T22:58:40Z | aq-1 | 02_analyse_2013 | `python aq-1/code/02_analyse.py --scope 2013` | 0 | 0.7 | [02_analyse_2013.md](../aq-1/logs/02_analyse_2013.md) |
| 2026-11-11T22:58:41Z | aq-1 | 03_checks_2013 | `python aq-1/code/03_checks.py --scope 2013` | 1 | 0.7 | [03_checks_2013.md](../aq-1/logs/03_checks_2013.md) |
| 2026-11-11T22:58:51Z | aq-1 | 03_checks_2013 | `python aq-1/code/03_checks.py --scope 2013` | 0 | 1.0 | [03_checks_2013.md](../aq-1/logs/03_checks_2013.md) |
| 2026-11-11T23:00:23Z | aq-2 | 01_extract_2013 | `python aq-2/code/01_extract.py --scope 2013` | 0 | 3.7 | [01_extract_2013.md](../aq-2/logs/01_extract_2013.md) |
| 2026-11-11T23:00:27Z | aq-2 | 02_associations_2013 | `python aq-2/code/02_associations.py --scope 2013` | 0 | 2.4 | [02_associations_2013.md](../aq-2/logs/02_associations_2013.md) |
| 2026-11-11T23:01:56Z | aq-3 | 01_extract | `python aq-3/code/01_extract.py` | 0 | 3.4 | [01_extract.md](../aq-3/logs/01_extract.md) |
| 2026-11-11T23:02:27Z | aq-3 | 02_dev_folds | `python aq-3/code/02_dev_folds.py` | 0 | 186.8 | [02_dev_folds.md](../aq-3/logs/02_dev_folds.md) |
| 2026-11-11T23:06:10Z | aq-3 | 03_choose | `python aq-3/code/03_choose.py` | 0 | 4.4 | [03_choose.md](../aq-3/logs/03_choose.md) |
| 2026-11-11T23:06:14Z | aq-3 | 04_freeze | `python aq-3/code/04_freeze.py` | 0 | 722.9 | [04_freeze.md](../aq-3/logs/04_freeze.md) |
| 2026-11-11T23:18:44Z | logs | tests_lib | `python common/tests/test_lib.py` | 0 | 5.4 | [tests_lib.md](tests_lib.md) |
| 2026-11-11T23:18:58Z | aq-3 | 05_test | `python aq-3/code/05_test.py` | 0 | 35.5 | [05_test.md](../aq-3/logs/05_test.md) |
| 2026-11-11T23:19:41Z | aq-3 | 06_secondary | `python aq-3/code/06_secondary.py` | 0 | 4.2 | [06_secondary.md](../aq-3/logs/06_secondary.md) |
| 2026-11-11T23:19:46Z | aq-3 | 07_error_analysis | `python aq-3/code/07_error_analysis.py` | 0 | 6.2 | [07_error_analysis.md](../aq-3/logs/07_error_analysis.md) |
| 2026-11-11T23:19:53Z | aq-3 | 08_sensitivity | `python aq-3/code/08_sensitivity.py` | 0 | 40.7 | [08_sensitivity.md](../aq-3/logs/08_sensitivity.md) |
| 2026-11-11T23:21:48Z | aq-3 | 07_error_analysis | `python aq-3/code/07_error_analysis.py` | 0 | 2.9 | [07_error_analysis.md](../aq-3/logs/07_error_analysis.md) |
| 2026-11-11T23:21:51Z | aq-4 | 01_lists | `python aq-4/code/01_lists.py` | 0 | 3.8 | [01_lists.md](../aq-4/logs/01_lists.md) |
| 2026-11-11T23:21:55Z | aq-4 | 02_evaluate | `python aq-4/code/02_evaluate.py` | 0 | 1.2 | [02_evaluate.md](../aq-4/logs/02_evaluate.md) |
| 2026-11-11T23:22:46Z | aq-4 | 03_fairness | `python aq-4/code/03_fairness.py` | 0 | 50.9 | [03_fairness.md](../aq-4/logs/03_fairness.md) |
| 2026-11-11T23:23:49Z | aq-2 | 01_extract_2014 | `python aq-2/code/01_extract.py --scope 2014` | 0 | 3.1 | [01_extract_2014.md](../aq-2/logs/01_extract_2014.md) |
| 2026-11-11T23:23:53Z | aq-2 | 02_associations_2014 | `python aq-2/code/02_associations.py --scope 2014` | 0 | 3.3 | [02_associations_2014.md](../aq-2/logs/02_associations_2014.md) |
| 2026-11-11T23:23:56Z | aq-1 | 01_extract_all | `python aq-1/code/01_extract.py --scope all` | 0 | 0.8 | [01_extract_all.md](../aq-1/logs/01_extract_all.md) |
| 2026-11-11T23:23:57Z | aq-1 | 02_analyse_all | `python aq-1/code/02_analyse.py --scope all` | 0 | 0.6 | [02_analyse_all.md](../aq-1/logs/02_analyse_all.md) |
| 2026-11-11T23:23:57Z | aq-1 | 03_checks_all | `python aq-1/code/03_checks.py --scope all` | 0 | 0.7 | [03_checks_all.md](../aq-1/logs/03_checks_all.md) |
| 2026-11-11T23:24:39Z | aq-2 | 03_replication | `python aq-2/code/03_replication.py` | 0 | 2.6 | [03_replication.md](../aq-2/logs/03_replication.md) |
| 2026-11-11T23:24:42Z | aq-3 | 09_verify | `python aq-3/code/09_verify.py` | 1 | 2.0 | [09_verify.md](../aq-3/logs/09_verify.md) |
| 2026-11-11T23:25:14Z | aq-3 | 09_verify | `python aq-3/code/09_verify.py` | 0 | 2.4 | [09_verify.md](../aq-3/logs/09_verify.md) |
| 2026-11-11T23:25:44Z | aq-3 | 10_crosscheck_earlier_run | `python aq-3/code/10_crosscheck_earlier_run.py` | 0 | 2.6 | [10_crosscheck_earlier_run.md](../aq-3/logs/10_crosscheck_earlier_run.md) |
| 2026-11-11T23:26:59Z | aq-1 | 04_figures | `python aq-1/code/04_figures.py` | 1 | 0.4 | [04_figures.md](../aq-1/logs/04_figures.md) |
| 2026-11-11T23:26:59Z | aq-2 | 04_figures | `python aq-2/code/04_figures.py` | 1 | 1.0 | [04_figures.md](../aq-2/logs/04_figures.md) |
| 2026-11-11T23:27:00Z | aq-3 | 11_figures | `python aq-3/code/11_figures.py` | 1 | 0.2 | [11_figures.md](../aq-3/logs/11_figures.md) |
| 2026-11-11T23:27:00Z | aq-4 | 04_figures | `python aq-4/code/04_figures.py` | 1 | 0.1 | [04_figures.md](../aq-4/logs/04_figures.md) |
| 2026-11-11T23:27:09Z | aq-1 | 04_figures | `python aq-1/code/04_figures.py` | 0 | 1.8 | [04_figures.md](../aq-1/logs/04_figures.md) |
| 2026-11-11T23:27:11Z | aq-2 | 04_figures | `python aq-2/code/04_figures.py` | 0 | 2.7 | [04_figures.md](../aq-2/logs/04_figures.md) |
| 2026-11-11T23:27:13Z | aq-3 | 11_figures | `python aq-3/code/11_figures.py` | 0 | 2.9 | [11_figures.md](../aq-3/logs/11_figures.md) |
| 2026-11-11T23:27:16Z | aq-4 | 04_figures | `python aq-4/code/04_figures.py` | 0 | 1.0 | [04_figures.md](../aq-4/logs/04_figures.md) |
| 2026-11-11T23:27:38Z | aq-4 | 04_figures | `python aq-4/code/04_figures.py` | 0 | 1.9 | [04_figures.md](../aq-4/logs/04_figures.md) |
| 2026-11-11T23:28:00Z | aq-1 | 04_figures | `python aq-1/code/04_figures.py` | 0 | 3.7 | [04_figures.md](../aq-1/logs/04_figures.md) |
| 2026-11-11T23:28:04Z | aq-3 | 02_dev_folds_rerun | `python aq-3/code/02_dev_folds.py` | 0 | 231.0 | [02_dev_folds_rerun.md](../aq-3/logs/02_dev_folds_rerun.md) |
| 2026-11-11T23:33:50Z | aq-1 | 02_analyse_all | `python aq-1/code/02_analyse.py --scope all` | 0 | 0.9 | [02_analyse_all.md](../aq-1/logs/02_analyse_all.md) |
| 2026-11-11T23:33:51Z | aq-1 | 03_checks_all | `python aq-1/code/03_checks.py --scope all` | 0 | 0.6 | [03_checks_all.md](../aq-1/logs/03_checks_all.md) |
| 2026-11-11T23:39:03Z | logs | check_reports | `python common/check_reports.py` | 0 | 0.4 | [check_reports.md](check_reports.md) |
| 2026-11-11T23:39:22Z | logs | check_reports | `python common/check_reports.py` | 0 | 0.4 | [check_reports.md](check_reports.md) |
| 2026-11-11T23:39:44Z | logs | check_reports | `python common/check_reports.py` | 0 | 0.4 | [check_reports.md](check_reports.md) |
