# Log: 07_aq3_evaluate

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:33:43Z |
| Finished (UTC) | 2026-11-13T10:34:06Z |
| Duration | 23.4 s |
| Command | `../../venv/bin/python code/07_aq3_evaluate.py` |
| Exit status | 0 |

## Console output

```text
wrote results/aq3_test_by_run.csv (91 rows)
wrote results/aq3_test_pooled.csv (28 rows)
wrote results/aq3_s1.csv (5 rows)
S1: {'a': 'M1', 'b': 'RULE', 'per20': 5, 'runs': 13, 'norm_recall_a': np.float64(0.7252), 'norm_recall_b': np.float64(0.7044), 'difference': np.float64(0.0207), 'low': np.float64(0.0063), 'high': np.float64(0.0361), 'extra_listed_noncompleters': 82, 'list_places': 3955, 'mean_run_difference': np.float64(0.0197), 'signflip_p': 0.0035, 'wins': 11, 'ties': 0, 'losses': 2, 'met': True}
wrote results/aq3_sensitivity.csv (9 rows)
wrote results/aq3_discrimination_calibration.csv (12 rows)
wrote results/aq3_calibration_bins.csv (10 rows)
wrote results/aq3_capacity_curve.csv (40 rows)
wrote results/aq3_model_vs_rule.csv (4 rows)
wrote results/aq3_errors_by_slice.csv (13 rows)
wrote results/aq3_lead_time.csv (5 rows)
                                         band  listed_non_completers    share
withdrew days 28–34 (before the list can act)                    111 0.038703
                          withdrew days 35–90                    462 0.161088
                        withdrew after day 90                    571 0.199093
                       withdrawn, day unknown                     78 0.027197
                            failed at the end                   1646 0.573919
```
