# Log: aq-3 / 06_secondary

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:19:41Z |
| Finished (UTC) | 2026-11-11T23:19:46Z |
| Duration | 4.2 s |
| Command | `python aq-3/code/06_secondary.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Secondary metrics on the 13 test runs

| cutoff | per20 | ranking | precision | base_rate | max_attainable_precision | share_of_way_from_base_to_max | lift | recall | normalised_recall | roc_auc_within_run | pr_auc_within_run | pr_auc_chance_level |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 27 | 5 | B2_rule | 0.704 | 0.440 | 1.000 | 0.473 | 1.603 | 0.403 | 0.704 | 0.711 | 0.660 | 0.425 |
| 27 | 5 | B3 | 0.567 | 0.440 | 1.000 | 0.228 | 1.291 | 0.325 | 0.567 | 0.603 | 0.520 | 0.425 |
| 27 | 5 | M1 | 0.726 | 0.440 | 1.000 | 0.511 | 1.651 | 0.415 | 0.726 | 0.730 | 0.686 | 0.425 |
| 27 | 5 | M2 | 0.726 | 0.440 | 1.000 | 0.511 | 1.652 | 0.416 | 0.726 | 0.734 | 0.688 | 0.425 |
| 27 | 5 | M3 | 0.723 | 0.440 | 1.000 | 0.506 | 1.645 | 0.414 | 0.723 | 0.730 | 0.687 | 0.425 |
| 27 | 5 | M4 | 0.728 | 0.440 | 1.000 | 0.515 | 1.657 | 0.417 | 0.728 | 0.732 | 0.688 | 0.425 |
| 13 | 5 | B2_rule | 0.667 | 0.450 | 1.000 | 0.395 | 1.483 | 0.374 | 0.667 | 0.679 | 0.606 | 0.433 |
| 13 | 5 | B3 | 0.578 | 0.450 | 1.000 | 0.233 | 1.285 | 0.324 | 0.578 | 0.603 | 0.529 | 0.433 |
| 13 | 5 | M1 | 0.688 | 0.450 | 1.000 | 0.432 | 1.529 | 0.385 | 0.688 | 0.701 | 0.638 | 0.433 |
| 13 | 5 | M2 | 0.688 | 0.450 | 1.000 | 0.432 | 1.529 | 0.385 | 0.688 | 0.702 | 0.639 | 0.433 |
| 13 | 5 | M3 | 0.687 | 0.450 | 1.000 | 0.431 | 1.528 | 0.385 | 0.687 | 0.706 | 0.641 | 0.433 |
| 13 | 5 | M4 | 0.690 | 0.450 | 1.000 | 0.436 | 1.534 | 0.387 | 0.690 | 0.705 | 0.640 | 0.433 |
[saved] aq-3/results/secondary.csv  (24 rows x 13 columns)

### S2 (reported, not a gate): precision at capacity, day 27, 5 per 20

| ranking | precision | base_rate | max_attainable_precision | share_of_way_from_base_to_max | lift |
| :---- | :---- | :---- | :---- | :---- | :---- |
| B2_rule | 0.704 | 0.440 | 1.000 | 0.473 | 1.603 |
| B3 | 0.567 | 0.440 | 1.000 | 0.228 | 1.291 |
| M1 | 0.726 | 0.440 | 1.000 | 0.511 | 1.651 |

### Calibration of the frozen models on the test runs (no recalibration)

| cutoff | model | citl | citl_se | slope | slope_se | brier | mean_predicted | observed_rate | s3_bounds_met |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 27 | B3 | 0.075 | 0.017 | 0.780 | 0.035 | 0.239 | 0.422 | 0.440 | no |
| 27 | M1 | 0.124 | 0.018 | 0.873 | 0.020 | 0.208 | 0.415 | 0.440 | yes |
| 27 | M2 | 0.072 | 0.018 | 0.925 | 0.020 | 0.202 | 0.425 | 0.440 | yes |
| 27 | M3 | 0.002 | 0.017 | 1.178 | 0.026 | 0.201 | 0.439 | 0.440 | yes |
| 27 | M4 | -0.006 | 0.018 | 1.141 | 0.024 | 0.200 | 0.441 | 0.440 | yes |
| 13 | B3 | 0.068 | 0.016 | 0.762 | 0.034 | 0.240 | 0.434 | 0.450 | no |
| 13 | M1 | 0.065 | 0.017 | 0.915 | 0.022 | 0.216 | 0.436 | 0.450 | yes |
| 13 | M2 | 0.035 | 0.017 | 0.927 | 0.022 | 0.214 | 0.442 | 0.450 | yes |
| 13 | M3 | -0.001 | 0.017 | 1.009 | 0.023 | 0.213 | 0.450 | 0.450 | yes |
| 13 | M4 | -0.033 | 0.017 | 1.024 | 0.023 | 0.212 | 0.457 | 0.450 | yes |
[saved] aq-3/results/calibration.csv  (10 rows x 10 columns)

**S3, chosen model M1, day 27:** calibration-in-the-large +0.124 (bounds −0.2 to 0.2), slope 0.873 (bounds 0.8 to 1.2); mean predicted risk 0.415 against observed 0.440. **Met: probabilities may be shown**.

**Observed against predicted risk, chosen model, day 27**

| predicted_from | predicted_to | enrolments | mean_predicted | observed_rate | gap_observed_minus_predicted |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 0.000 | 0.100 | 192 | 0.085 | 0.161 | 0.077 |
| 0.100 | 0.200 | 1,922 | 0.160 | 0.211 | 0.052 |
| 0.200 | 0.300 | 3,487 | 0.251 | 0.297 | 0.046 |
| 0.300 | 0.400 | 3,352 | 0.349 | 0.367 | 0.019 |
| 0.400 | 0.500 | 2,437 | 0.447 | 0.470 | 0.023 |
| 0.500 | 0.600 | 1,487 | 0.546 | 0.557 | 0.011 |
| 0.600 | 0.700 | 868 | 0.645 | 0.613 | -0.032 |
| 0.700 | 0.800 | 580 | 0.746 | 0.774 | 0.028 |
| 0.800 | 0.900 | 629 | 0.854 | 0.831 | -0.022 |
| 0.900 | 1.000 | 770 | 0.945 | 0.947 | 0.002 |
[saved] aq-3/results/calibration_bins.csv  (10 rows x 6 columns)

**Calibration per run, chosen model, day 27**

| run | enrolments | observed_rate | mean_predicted | citl | slope |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 348 | 0.273 | 0.274 | -0.004 | 0.713 |
| BBB-2014B | 1,280 | 0.432 | 0.477 | -0.229 | 0.906 |
| BBB-2014J | 1,786 | 0.356 | 0.384 | -0.145 | 0.942 |
| CCC-2014B | 1,500 | 0.558 | 0.341 | 1.142 | 1.014 |
| CCC-2014J | 2,021 | 0.498 | 0.349 | 0.743 | 0.923 |
| DDD-2014B | 1,029 | 0.535 | 0.549 | -0.068 | 0.929 |
| DDD-2014J | 1,463 | 0.459 | 0.474 | -0.075 | 1.166 |
| EEE-2014B | 605 | 0.410 | 0.401 | 0.042 | 1.508 |
| EEE-2014J | 1,020 | 0.329 | 0.350 | -0.104 | 1.504 |
| FFF-2014B | 1,299 | 0.497 | 0.516 | -0.100 | 0.997 |
| FFF-2014J | 1,859 | 0.399 | 0.445 | -0.237 | 1.078 |
| GGG-2014B | 797 | 0.400 | 0.402 | -0.007 | 1.033 |
| GGG-2014J | 717 | 0.381 | 0.332 | 0.242 | 0.819 |
[saved] aq-3/results/calibration_by_run.csv  (13 rows x 6 columns)

### Net benefit (context: a threshold policy, not the fixed-capacity list)

| threshold_probability | model | share_contacted_model | contact_all | contact_none | rule_flags | share_contacted_rule |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 0.200 | 0.298 | 0.866 | 0.299 | 0.000 | 0.163 | 0.281 |
| 0.300 | 0.218 | 0.644 | 0.199 | 0.000 | 0.146 | 0.281 |
| 0.400 | 0.159 | 0.431 | 0.066 | 0.000 | 0.123 | 0.281 |
| 0.500 | 0.114 | 0.276 | -0.121 | 0.000 | 0.092 | 0.281 |
| 0.600 | 0.083 | 0.181 | -0.401 | 0.000 | 0.044 | 0.281 |
| 0.700 | 0.067 | 0.126 | -0.868 | 0.000 | -0.035 | 0.281 |
[saved] aq-3/results/net_benefit.csv  (6 rows x 7 columns)

