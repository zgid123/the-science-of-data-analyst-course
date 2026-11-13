# Experiment log

One row per executed step, appended by `run_step.py` in run order. A **new run** row marks the start of each full run; the rows after the last one are the run that produced the delivered results.

| Started (UTC) | Step | Command | Exit | Seconds | Log |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-13T09:12:03Z | **new run** | – | – | – | – |
| 2026-11-13T09:12:03Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 3.9 | [01_profile.md](01_profile.md) |
| 2026-11-13T09:12:12Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T09:12:12Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.1 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T09:12:13Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.2 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T09:12:25Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 175.3 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T09:15:37Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.1 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T09:15:37Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 3.0 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T09:15:40Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 22.4 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:16:22Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 559.6 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T09:25:41Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.5 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T09:25:46Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T09:25:46Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 300.9 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:32:17Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.7 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T09:33:19Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 1 | 0.9 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:33:28Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:33:35Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:34:23Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.3 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:35:19Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.0 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:35:32Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.0 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:36:37Z | 14_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.6 | [14_headlines.md](14_headlines.md) |
| 2026-11-13T09:38:46Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 22.9 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:39:09Z | 14_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.5 | [14_headlines.md](14_headlines.md) |
| 2026-11-13T09:45:07Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.5 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:45:32Z | **new run** | – | – | – | – |
| 2026-11-13T09:45:32Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T09:45:32Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.4 | [01_profile.md](01_profile.md) |
| 2026-11-13T09:45:34Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.1 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T09:45:36Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.4 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T09:45:40Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 5.3 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T09:45:45Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.0 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T09:45:46Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.3 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T09:45:47Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.5 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:46:11Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 18.4 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T09:46:29Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.5 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T09:46:34Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T09:46:34Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.1 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:46:35Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.4 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T09:46:36Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.4 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:46:36Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T09:46:36Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 1.8 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:46:38Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.0 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T09:46:38Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 1 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T09:46:49Z | **new run** | – | – | – | – |
| 2026-11-13T09:46:49Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T09:46:49Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.3 | [01_profile.md](01_profile.md) |
| 2026-11-13T09:46:51Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.0 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T09:46:52Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 3.9 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T09:46:56Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 3.8 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T09:47:00Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.0 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T09:47:00Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.4 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T09:47:02Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 22.3 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:47:24Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 17.6 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T09:47:42Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.5 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T09:47:46Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T09:47:47Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.1 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:47:48Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.4 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T09:47:48Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.4 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:47:49Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T09:47:49Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 1.7 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:47:51Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.0 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T09:47:51Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T09:49:28Z | **new run** | – | – | – | – |
| 2026-11-13T09:49:28Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T09:49:29Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.2 | [01_profile.md](01_profile.md) |
| 2026-11-13T09:49:31Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.0 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T09:49:32Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.1 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T09:49:36Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 4.6 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T09:49:41Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.0 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T09:49:41Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.4 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T09:49:42Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.4 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:50:06Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 18.3 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T09:50:24Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.8 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T09:50:29Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.5 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T09:50:30Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.3 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:50:31Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.5 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T09:50:31Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.4 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:50:32Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T09:50:32Z | 14b_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.4 | [14b_headlines.md](14b_headlines.md) |
| 2026-11-13T09:50:32Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.0 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:50:34Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.0 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T09:50:35Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T09:56:20Z | **new run** | – | – | – | – |
| 2026-11-13T09:56:20Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T09:56:20Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.7 | [01_profile.md](01_profile.md) |
| 2026-11-13T09:56:23Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.1 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T09:56:24Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.5 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T09:56:29Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 5.7 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T09:56:35Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.0 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T09:56:35Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.5 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T09:56:36Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.8 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T09:57:00Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 18.9 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T09:57:19Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 5.0 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T09:57:24Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T09:57:25Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.5 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T09:57:26Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.5 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T09:57:27Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T09:57:27Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T09:57:27Z | 14b_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.4 | [14b_headlines.md](14b_headlines.md) |
| 2026-11-13T09:57:28Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.1 | [15_figures.md](15_figures.md) |
| 2026-11-13T09:57:30Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.1 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T09:57:30Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T10:03:29Z | 16_compare_m4 | `../../venv/bin/python code/16_compare_m4.py` | 0 | 0.8 | [16_compare_m4.md](16_compare_m4.md) |
| 2026-11-13T10:05:20Z | **new run** | – | – | – | – |
| 2026-11-13T10:05:20Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T10:05:20Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.5 | [01_profile.md](01_profile.md) |
| 2026-11-13T10:05:22Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.3 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T10:05:24Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.6 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T10:05:28Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 4.6 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T10:05:33Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.1 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T10:05:33Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.4 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T10:05:35Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.5 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T10:05:58Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 19.2 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T10:06:17Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.7 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T10:06:22Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T10:06:23Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.2 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T10:06:24Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.5 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T10:06:24Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T10:06:25Z | 13b_compare_m4 | `../../venv/bin/python code/16_compare_m4.py` | 0 | 0.5 | [13b_compare_m4.md](13b_compare_m4.md) |
| 2026-11-13T10:06:26Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.1 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T10:06:26Z | 14b_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.5 | [14b_headlines.md](14b_headlines.md) |
| 2026-11-13T10:06:26Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 1.9 | [15_figures.md](15_figures.md) |
| 2026-11-13T10:06:28Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.1 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T10:06:28Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T10:06:28Z | 99b_check_comparison | `../../venv/bin/python tools/report_tables.py fill comparison.md` | 0 | 0.0 | [99b_check_comparison.md](99b_check_comparison.md) |
| 2026-11-13T10:06:28Z | 99c_check_comparison | `../../venv/bin/python tools/check_report.py comparison.md --claims comparison-claims.json` | 0 | 0.1 | [99c_check_comparison.md](99c_check_comparison.md) |
| 2026-11-13T10:06:34Z | **new run** | – | – | – | – |
| 2026-11-13T10:06:34Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T10:06:34Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.3 | [01_profile.md](01_profile.md) |
| 2026-11-13T10:06:36Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.0 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T10:06:37Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.3 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T10:06:42Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 4.2 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T10:06:46Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.1 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T10:06:46Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.4 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T10:06:47Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.4 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T10:07:11Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 19.8 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T10:07:31Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 5.5 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T10:07:36Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.4 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T10:07:37Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.2 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T10:07:38Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.5 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T10:07:38Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T10:07:39Z | 13b_compare_m4 | `../../venv/bin/python code/16_compare_m4.py` | 0 | 0.5 | [13b_compare_m4.md](13b_compare_m4.md) |
| 2026-11-13T10:07:40Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T10:07:40Z | 14b_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.4 | [14b_headlines.md](14b_headlines.md) |
| 2026-11-13T10:07:40Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 1.9 | [15_figures.md](15_figures.md) |
| 2026-11-13T10:07:42Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.1 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T10:07:42Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T10:07:42Z | 99b_fill_comparison | `../../venv/bin/python tools/report_tables.py fill comparison.md` | 0 | 0.1 | [99b_fill_comparison.md](99b_fill_comparison.md) |
| 2026-11-13T10:07:42Z | 99c_check_comparison | `../../venv/bin/python tools/check_report.py comparison.md --claims comparison-claims.json` | 0 | 0.1 | [99c_check_comparison.md](99c_check_comparison.md) |
| 2026-11-13T10:33:28Z | **new run** | – | – | – | – |
| 2026-11-13T10:33:28Z | 00_verify_inputs | `../../venv/bin/python tools/data_manifest.py verify data-manifest.json` | 0 | 0.1 | [00_verify_inputs.md](00_verify_inputs.md) |
| 2026-11-13T10:33:28Z | 01_profile | `../../venv/bin/python tools/profile_data.py ../milestone-3/package/data/processed/enrolment.parquet ../milestone-3/package/data/processed/features_d13.parquet ../milestone-3/package/data/processed/features_d27.parquet ../milestone-3/package/data/processed/assessment_due.parquet -o results/profile.md` | 0 | 2.8 | [01_profile.md](01_profile.md) |
| 2026-11-13T10:33:31Z | 02_prepare | `../../venv/bin/python code/02_prepare.py` | 0 | 1.2 | [02_prepare.md](02_prepare.md) |
| 2026-11-13T10:33:32Z | 03_aq2_2013 | `../../venv/bin/python code/03_aq2.py 2013` | 0 | 4.6 | [03_aq2_2013.md](03_aq2_2013.md) |
| 2026-11-13T10:33:37Z | 04_aq3_dev | `../../venv/bin/python code/04_aq3_dev.py` | 0 | 4.1 | [04_aq3_dev.md](04_aq3_dev.md) |
| 2026-11-13T10:33:41Z | 05_freeze | `../../venv/bin/python tools/holdout_guard.py freeze --record results/freeze.json --choices results/aq3_choices.json code/models.py models/B3_d13.pkl models/B3_d27.pkl models/M1_d13.pkl models/M1_d27.pkl models/M2_d13.pkl models/M2_d27.pkl models/M3_d13.pkl models/M3_d27.pkl models/M4_d13.pkl models/M4_d27.pkl` | 0 | 0.0 | [05_freeze.md](05_freeze.md) |
| 2026-11-13T10:33:41Z | 06_aq3_score | `../../venv/bin/python code/06_aq3_score.py` | 0 | 1.3 | [06_aq3_score.md](06_aq3_score.md) |
| 2026-11-13T10:33:43Z | 07_aq3_evaluate | `../../venv/bin/python code/07_aq3_evaluate.py` | 0 | 23.4 | [07_aq3_evaluate.md](07_aq3_evaluate.md) |
| 2026-11-13T10:34:06Z | 08_aq4_lists | `../../venv/bin/python code/08_aq4_lists.py` | 0 | 18.7 | [08_aq4_lists.md](08_aq4_lists.md) |
| 2026-11-13T10:34:25Z | 09_aq2_2014 | `../../venv/bin/python code/03_aq2.py 2014` | 0 | 4.8 | [09_aq2_2014.md](09_aq2_2014.md) |
| 2026-11-13T10:34:30Z | 10_aq2_compare | `../../venv/bin/python code/10_aq2_compare.py` | 0 | 0.5 | [10_aq2_compare.md](10_aq2_compare.md) |
| 2026-11-13T10:34:30Z | 11_aq1 | `../../venv/bin/python code/11_aq1.py` | 0 | 1.4 | [11_aq1.md](11_aq1.md) |
| 2026-11-13T10:34:32Z | 12_recompute | `../../venv/bin/python code/12_recompute.py` | 0 | 0.5 | [12_recompute.md](12_recompute.md) |
| 2026-11-13T10:34:32Z | 13_compare_prior | `../../venv/bin/python code/13_compare_prior.py` | 0 | 0.5 | [13_compare_prior.md](13_compare_prior.md) |
| 2026-11-13T10:34:33Z | 13b_compare_m4 | `../../venv/bin/python code/16_compare_m4.py` | 0 | 0.5 | [13b_compare_m4.md](13b_compare_m4.md) |
| 2026-11-13T10:34:33Z | 14_holdout_order | `../../venv/bin/python tools/holdout_guard.py status --record results/freeze.json --access logs/holdout-access.md` | 0 | 0.0 | [14_holdout_order.md](14_holdout_order.md) |
| 2026-11-13T10:34:33Z | 14b_headlines | `../../venv/bin/python code/14_headlines.py` | 0 | 0.5 | [14b_headlines.md](14b_headlines.md) |
| 2026-11-13T10:34:34Z | 15_figures | `../../venv/bin/python code/15_figures.py` | 0 | 2.0 | [15_figures.md](15_figures.md) |
| 2026-11-13T10:34:36Z | 98_fill_tables | `../../venv/bin/python tools/report_tables.py fill report.md` | 0 | 0.1 | [98_fill_tables.md](98_fill_tables.md) |
| 2026-11-13T10:34:36Z | 99_check_report | `../../venv/bin/python tools/check_report.py report.md --claims claims.json` | 0 | 0.1 | [99_check_report.md](99_check_report.md) |
| 2026-11-13T10:34:36Z | 99b_fill_comparison | `../../venv/bin/python tools/report_tables.py fill comparison.md` | 0 | 0.0 | [99b_fill_comparison.md](99b_fill_comparison.md) |
| 2026-11-13T10:34:36Z | 99c_check_comparison | `../../venv/bin/python tools/check_report.py comparison.md --claims comparison-claims.json` | 0 | 0.1 | [99c_check_comparison.md](99c_check_comparison.md) |
