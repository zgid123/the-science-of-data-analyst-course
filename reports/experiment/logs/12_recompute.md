# Log: 12_recompute

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:34:32Z |
| Finished (UTC) | 2026-11-13T10:34:32Z |
| Duration | 0.5 s |
| Command | `../../venv/bin/python code/12_recompute.py` |
| Exit status | 0 |

## Console output

```text
wrote results/check_recompute.csv (8 rows)
                                                     check  recomputed  reported status
                                            raw enrolments       32593   32593.0   PASS
                     KPI population (registered at day 14)       28061   28061.0   PASS
                                        KPI non-completers       12700   12700.0   PASS
runs whose KPI counts differ between the two paths (of 22)           0       0.0   PASS
                                    withdrew before day 14        4457    4457.0   PASS
                                         failed at the end        7052    7052.0   PASS
               listed non-completers, M1, day 27, 5 per 20        2868    2868.0   PASS
             listed non-completers, RULE, day 27, 5 per 20        2786    2786.0   PASS
```
