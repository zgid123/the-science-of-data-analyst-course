# Test-access record (2014 outcomes), rerun

Every read of a 2014 outcome by a script of this rerun is appended here. The first row is the first test access of the rerun; the freeze it follows is `aq-3/results/freeze.json`. This record shows the order in which the scripts ran. It does not show a blind test: the first run of this folder (commit `11f4aca`) froze at 2026-11-11T23:18:16Z and first read the 2014 outcomes at 2026-11-11T23:19:02Z, and those results were known when the rerun started.

| UTC time | Script | Purpose | Freeze time (UTC) |
| :---- | :---- | :---- | :---- |
| 2026-11-12T15:58:53Z | `aq-3/code/05_test.py` | single test of the frozen models, day 27 | 2026-11-12T15:58:51Z |
| 2026-11-12T15:58:53Z | `aq-3/code/05_test.py` | withdrawal day for the reach analysis | 2026-11-12T15:58:51Z |
| 2026-11-12T15:58:53Z | `aq-3/code/05_test.py` | single test of the frozen models, day 13 | 2026-11-12T15:58:51Z |
| 2026-11-12T15:58:53Z | `aq-3/code/05_test.py` | withdrawal day for the reach analysis | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:17Z | `aq-3/code/06_secondary.py` | secondary metrics and calibration of the frozen models | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:20Z | `aq-3/code/07_error_analysis.py` | error analysis of the frozen model | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:22Z | `aq-3/code/08_sensitivity.py` | sensitivity analyses of the S1 comparison | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:46Z | `aq-4/code/01_lists.py` | AQ4 lists formed from the frozen scores (outcomes kept for evaluation columns) | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:48Z | `aq-4/code/02_evaluate.py` | AQ4 list quality on the test runs | 2026-11-12T15:58:51Z |
| 2026-11-12T15:59:49Z | `aq-4/code/03_fairness.py` | fairness audit of the frozen list | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:24Z | `aq-2/code/01_extract.py` | AQ2 replication on the 2014 runs (Appendix III step 8) | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:24Z | `aq-2/code/01_extract.py` | AQ2 task calendar of the 2014 runs (due days only) | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:25Z | `aq-2/code/02_associations.py` | AQ2 replication on the 2014 runs (Appendix III step 8) | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:29Z | `aq-2/code/03_replication.py` | AQ2 replication table | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:29Z | `aq-1/code/01_extract.py` | AQ1 descriptive rates for the 2014 runs | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:29Z | `aq-1/code/01_extract.py` | AQ1 first missed task for the 2014 runs | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:30Z | `aq-1/code/03_checks.py` | AQ1 second aggregation path from the raw tables (2014 runs included) | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:32Z | `aq-3/code/09_verify.py` | independent verification of the S1 numbers | 2026-11-12T15:58:51Z |
| 2026-11-12T16:00:34Z | `aq-3/code/10_crosscheck_earlier_run.py` | cross-check with the earlier prototype run | 2026-11-12T15:58:51Z |
| 2026-11-12T16:08:36Z | `aq-1/code/04_figures.py` | AQ1 figures for all 22 runs | 2026-11-12T15:58:51Z |
| 2026-11-12T16:08:45Z | `aq-2/code/04_figures.py` | AQ2 figures including the 2014 replication | 2026-11-12T15:58:51Z |
| 2026-11-12T16:08:52Z | `aq-3/code/11_figures.py` | AQ3 figures of the test results | 2026-11-12T15:58:51Z |
| 2026-11-12T16:08:59Z | `aq-4/code/04_figures.py` | AQ4 figures | 2026-11-12T15:58:51Z |
