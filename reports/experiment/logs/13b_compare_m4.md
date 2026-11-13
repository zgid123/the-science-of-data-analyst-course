# Log: 13b_compare_m4

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:34:33Z |
| Finished (UTC) | 2026-11-13T10:34:33Z |
| Duration | 0.5 s |
| Command | `../../venv/bin/python code/16_compare_m4.py` |
| Exit status | 0 |

## Console output

```text
wrote results/compare_m4_runs.csv (13 rows)
wrote results/compare_m4.csv (42 rows)
             aq                                                 item milestone_4       new difference              unit                        same_conclusion
            AQ2                              Missed a task due, 2013       40.83     40.67      -0.16            points                                    yes
            AQ2                              Missed a task due, 2014       39.26     39.64       0.38            points                                    yes
            AQ2                           Submitted a TMA late, 2013        20.2     21.66       1.46            points                                    yes
            AQ2                           Submitted a TMA late, 2014       20.25     22.54       2.29            points                                    yes
            AQ2                 No activity in the last 7 days, 2013       14.46     13.48      -0.98            points                                    yes
            AQ2                 No activity in the last 7 days, 2014       15.82     15.41      -0.41            points                                    yes
            AQ2               Clicks below half the run median, 2013       13.36     14.66        1.3            points                                    yes
            AQ2               Clicks below half the run median, 2014        14.6     14.75       0.15            points                                    yes
            AQ2                   No activity before the start, 2013       10.56     11.26        0.7            points                                    yes
            AQ2                   No activity before the start, 2014        8.65      9.15        0.5            points                                    yes
AQ3 development                                      Development, M1    0.752688  0.750336  -0.002352 normalised recall                                    yes
AQ3 development                                    Development, rule    0.727487  0.727151  -0.000336 normalised recall                                    yes
AQ3 development                                      Development, B3    0.570901  0.567876  -0.003025 normalised recall                                    yes
AQ3 development                                      Development, M2    0.746976  0.748992   0.002016 normalised recall                                    yes
AQ3 development                                      Development, M3        0.75  0.748656  -0.001344 normalised recall                                    yes
AQ3 development                                      Development, M4    0.748992  0.747984  -0.001008 normalised recall                                    yes
      AQ3 setup                                 Chosen configuration          M1        M1                                                                 yes
      AQ3 setup                               M1 penalty C at day 27       0.001        10                                        no: tuning criterion differs
       AQ3 test                          S1 normalised recall, model    0.725917  0.725158  -0.000759 normalised recall                                    yes
       AQ3 test                           S1 normalised recall, rule    0.704425  0.704425       -0.0 normalised recall                                    yes
       AQ3 test                                        S1 difference    0.021492  0.020733  -0.000759 normalised recall                                    yes
       AQ3 test                                     S1 interval, low    0.009259  0.006336  -0.002923 normalised recall                                    yes
       AQ3 test                                    S1 interval, high    0.033739  0.036139     0.0024 normalised recall                                    yes
       AQ3 test                                       S1 sign-flip p    0.000244   0.00354   0.003296                 p                                    yes
       AQ3 test                                  S1 runs won (of 13)        12.0      11.0       -1.0              runs                                    yes
       AQ3 test Non-completers listed by the model, day 27, 5 per 20        2871      2868         -3          students                                    yes
       AQ3 test      Runs where the rule's list is identical (of 13)          13        13          0              runs                                    yes
       AQ3 test                          S3 calibration-in-the-large    0.057997  0.116783   0.058786                                                      yes
       AQ3 test                                 S3 calibration slope    1.310605   0.88569  -0.424915                   no: S3 fails in M4, passes pooled here
AQ3 sensitivity                                     Day 13, 5 per 20     0.02134  0.020844  -0.000496 normalised recall                                    yes
AQ3 sensitivity                                     Day 27, 3 per 20    0.027813  0.031184   0.003371 normalised recall                                    yes
AQ3 sensitivity                              9 runs also run in 2013    0.025414  0.024309  -0.001105 normalised recall                                    yes
AQ3 sensitivity                               4 runs not run in 2013    0.012903  0.012903        0.0 normalised recall                                    yes
AQ3 sensitivity                                   Without module CCC    0.022801  0.021498  -0.001303 normalised recall                                    yes
AQ3 sensitivity                                      Module CCC only    0.016949  0.018079    0.00113 normalised recall                                    yes
AQ3 sensitivity                        Without students seen in 2013    0.022721  0.020477  -0.002244 normalised recall                                    yes
AQ3 sensitivity           Without Withdrawn lacking a withdrawal day    0.022392  0.020102   -0.00229 normalised recall                                    yes
            AQ4                      Recall gap: Declared disability        5.41      5.46       0.05            points              yes (not flagged in both)
            AQ4               Recall gap: Most deprived band (0–10%)        1.73      1.35      -0.38            points              yes (not flagged in both)
            AQ4                 Recall gap: Deprivation band missing       -8.05     -7.44       0.61            points              yes (not flagged in both)
AQ4 descriptive                                        Recall, women       0.388  0.386909  -0.001091             share                                    yes
AQ4 descriptive                                          Recall, men     0.43355   0.43355       -0.0             share                                    yes
wrote results/compare_m4_summary.csv (8 rows)
                                               aq  max_abs_difference
                                              AQ2            2.290000
                                  AQ3 development            0.003025
                                  AQ3 sensitivity            0.003371
                                         AQ3 test            3.000000
                                              AQ4            0.610000
                                  AQ4 descriptive            0.001091
AQ3 test, S1 quantities other than p and runs won            0.002923
                Runs with the same winner (of 13)           12.000000
```
