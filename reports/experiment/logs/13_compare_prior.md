# Log: 13_compare_prior

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:34:32Z |
| Finished (UTC) | 2026-11-13T10:34:33Z |
| Duration | 0.5 s |
| Command | `../../venv/bin/python code/13_compare_prior.py` |
| Exit status | 0 |

## Console output

```text
wrote results/compare_prior.csv (5 rows)
     comparison  rows_compared  differences
aq1_rate_by_run             22            0
aq2_adjusted_rd              5            0
aq3_test_listed             24            7
 aq3_dev_choice              6            0
   aq4_fairness              3            5
aq3_test_listed -> B3|13|5 non_completers_on_list: mine 2327.0, earlier 2328; M1|13|5 non_completers_on_list: mine 2772.0, earlier 2771; M1|27|3 non_completers_on_list: mine 1920.0, earlier 1922; M1|27|5 non_completers_on_list: mine 2868.0, earlier 2870; M2|13|5 non_completers_on_list: mine 2773.0, earlier 2771; M2|27|3 non_completers_on_list: mine 1926.0, earlier 1925; M2|27|5 non_completers_on_list: mine 2869.0, earlier 2872
aq4_fairness -> model|Deprivation band 0–10% recall_group: mine 0.4269377382465057, earlier 0.425667; model|Deprivation band missing recall_group: mine 0.3425414364640884, earlier 0.348066; rule|Declared disability : mine absent, earlier present; rule|Deprivation band 0–10% : mine absent, earlier present; rule|Deprivation band missing : mine absent, earlier present
```
