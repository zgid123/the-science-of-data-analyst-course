# Log: 10_aq2_compare

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:34:30Z |
| Finished (UTC) | 2026-11-13T10:34:30Z |
| Duration | 0.5 s |
| Command | `../../venv/bin/python code/10_aq2_compare.py` |
| Exit status | 0 |

## Console output

```text
wrote results/aq2_replication.csv (5 rows)
        sign  rd_2013  rd_2014  change  change_low  change_high  criterion_2013  criterion_2014
 missed_task    0.407    0.396  -0.010      -0.052        0.032            True            True
    late_tma    0.217    0.225   0.009      -0.054        0.072            True            True
 inactive_7d    0.135    0.154   0.019      -0.023        0.062            True            True
low_activity    0.147    0.148   0.001      -0.030        0.032            True            True
 no_prestart    0.113    0.092  -0.021      -0.057        0.015            True            True
```
