# Log: aq-3 / 08_sensitivity

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:59:21Z |
| Finished (UTC) | 2026-11-12T15:59:46Z |
| Duration | 25.6 s |
| Command | `python aq-3/code/08_sensitivity.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output

[saved] aq-3/results/sensitivity_per_run_labels_available.csv  (6 rows x 12 columns)

### Sensitivity of the comparison model (M1) − rule

| variant | runs | enrolments | model_nr | rule_nr | difference | boot_ci_low | boot_ci_high | signflip_p | wins | ties | losses | extra_non_completers_listed | would_pass_s1_conditions |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MAIN: all 13 runs, day 27, 5 per 20 (the S1 gate) | 13 | 15,724 | 0.7257 | 0.7044 | 0.0212 | 0.0065 | 0.0364 | 0.0032 | 11 | 0 | 2 | 84 | yes |
| Paired runs (9): module and start month also ran in 2013 | 9 | 10,801 | 0.7076 | 0.6829 | 0.0247 | 0.0082 | 0.0417 | 0.0059 | 8 | 0 | 1 | 67 | yes |
| Unpaired runs (4): CCC-B, CCC-J, EEE-B, GGG-B | 4 | 4,923 | 0.7653 | 0.7516 | 0.0137 | -0.0133 | 0.0359 | 0.1875 | 3 | 0 | 1 | 17 | no |
| Module CCC only (2 runs; module absent from training) | 2 | 3,521 | 0.8023 | 0.7831 | 0.0192 | -0.0059 | 0.0463 | 0.2500 | 2 | 0 | 0 | 17 | no |
| Without module CCC (11 runs) | 11 | 12,203 | 0.7036 | 0.6818 | 0.0218 | 0.0055 | 0.0387 | 0.0088 | 9 | 0 | 2 | 67 | yes |
| Without test enrolments of students seen in 2013 | 13 | 14,138 | 0.7015 | 0.6805 | 0.0210 | 0.0065 | 0.0369 | 0.0020 | 11 | 0 | 2 | 75 | yes |
| Without Withdrawn enrolments that lack a withdrawal day | 13 | 15,634 | 0.7176 | 0.6967 | 0.0209 | 0.0067 | 0.0354 | 0.0022 | 11 | 1 | 1 | 82 | yes |
| Rule variant that also counts late CMAs | 13 | 15,724 | 0.7257 | 0.6999 | 0.0258 | 0.0099 | 0.0427 | 0.0023 | 11 | 0 | 2 | 102 | yes |
| Labels-available: 2014 February runs, model trained on 2013 February runs only | 6 | 6,510 | 0.7823 | 0.7621 | 0.0202 | 0.0017 | 0.0348 | 0.0312 | 5 | 1 | 0 | 33 | yes |
| Same February runs, model trained on all 2013 runs (for comparison) | 6 | 6,510 | 0.7780 | 0.7621 | 0.0159 | -0.0044 | 0.0339 | 0.0625 | 5 | 0 | 1 | 26 | no |
| Day 27, 3 per 20 | 13 | 15,724 | 0.8099 | 0.7779 | 0.0320 | 0.0061 | 0.0550 | 0.0104 | 11 | 0 | 2 | 76 | yes |
| Day 13, 5 per 20 | 13 | 15,989 | 0.6876 | 0.6670 | 0.0206 | 0.0020 | 0.0358 | 0.0271 | 9 | 0 | 4 | 83 | yes |
| Day 13, 3 per 20 | 13 | 15,989 | 0.7423 | 0.7072 | 0.0352 | 0.0083 | 0.0589 | 0.0059 | 9 | 1 | 3 | 85 | yes |

With fewer than 6 runs the sign-flip test cannot reach p < 0.05 (2 runs: smallest p = 0.25; 4 runs: 0.0625), so 'would_pass_s1_conditions' is not informative for the small subsets; read their difference and interval.
[saved] aq-3/results/sensitivity.csv  (13 rows x 14 columns)

