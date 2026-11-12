# Log: aq-3 / 04_freeze

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:50:57Z |
| Finished (UTC) | 2026-11-12T15:58:51Z |
| Duration | 473.7 s |
| Command | `python aq-3/code/04_freeze.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ3 second freeze – chosen configuration M1

| name | cutoff | hyperparameters | train_runs | train_rows | columns | mean_fitted_risk_train | train_rate | sha256 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| B3 | 27 | {"C": 0.01} | 9 | 11,811 | 10 | 0.4441 | 0.4441 | 3ac62f049fd5994221ff52f9fe3fe0fe41d5befdc438a96ff6638a8e661cb212 |
| M1 | 27 | {"C": 10.0} | 9 | 11,811 | 23 | 0.4441 | 0.4441 | 35b26eaa26a496077fbd1bb8aba1b381ce87a4370aa6eefbe691733955268c58 |
| M2 | 27 | {"C": 10.0} | 9 | 11,811 | 37 | 0.4441 | 0.4441 | 49a0409064bf256606c7fc8544a513c3ce21b9e12d1e0491fa24eafc3cde9407 |
| M3 | 27 | {"max_depth": 3, "learning_rate": 0.05, "trees": 100} | 9 | 11,811 | 19 | 0.4441 | 0.4441 | 2db97136b33b749330e05e0be1124b35da2b38fe1d67701014164fe4ea89e9e1 |
| M4 | 27 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 9 | 11,811 | 33 | 0.4441 | 0.4441 | 4f1c63190c5ea7a6e963438cc48202fbaa6535ebd451c833269675b0e1a47c2e |
| M1_labels_available | 27 | {"C": 0.003} | 3 | 4,127 | 19 | 0.4929 | 0.4929 | 738958e7bfcd13cc76bccc4695d4e7b085702e57e902e02a565d7e3209959bcf |
| B3 | 13 | {"C": 0.01} | 9 | 12,080 | 10 | 0.4569 | 0.4569 | 7fc0796d88307ec5d378708ce96aef46c54ef69f389cb46d788c0fbd466f4416 |
| M1 | 13 | {"C": 0.01} | 9 | 12,080 | 23 | 0.4569 | 0.4569 | a6b5dd95920e174daf9c0183c06aa931a7102318068570063472046100d54692 |
| M2 | 13 | {"C": 0.01} | 9 | 12,080 | 35 | 0.4569 | 0.4569 | 4f7632161ff93a55cff52b5a71d4e1453303853748bf0d20c4876fe083723db8 |
| M3 | 13 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 9 | 12,080 | 19 | 0.4569 | 0.4569 | 3eaef2be18c67dd2c2e2403d6a416747d2742b58797bbd8eeb82af54cc6d469d |
| M4 | 13 | {"max_depth": 2, "learning_rate": 0.05, "trees": 200} | 9 | 12,080 | 31 | 0.4569 | 0.4569 | 73b5140fa80a7c66b68aab805db3625f8c91015b3909ae75ee13abdb994502ad |
| M1_labels_available | 13 | {"C": 0.003} | 3 | 4,324 | 19 | 0.5162 | 0.5162 | 493578946fffcbd9f9acfb40c6b484fbcc7125f3fbff66f39277e72e366dd6de |
[saved] aq-3/results/frozen_models.csv  (12 rows x 11 columns)
[saved] aq-3/results/freeze_tuning.csv  (136 rows x 4 columns)

**Frozen M1 at day 27: 23 parameters besides the intercept (Level 1 expected 23); coefficients per training standard deviation, log-odds scale**

| column | coefficient_per_sd |
| :---- | :---- |
| tasks_missed_c | 0.568 |
| active_days_0c | -0.489 |
| highest_education | -0.326 |
| tma_late_c | 0.289 |
| code_module[DDD] | 0.251 |
| code_module[FFF] | 0.247 |
| code_module[BBB] | -0.222 |
| clicks_pre | -0.192 |
| tasks_due_c | 0.160 |
| tasks_late_c | -0.158 |
| code_module[AAA] | -0.155 |
| code_module[EEE] | 0.153 |
| studied_credits | 0.142 |
| num_of_prev_attempts | 0.116 |
| start_month[B] | 0.111 |
| cma_marked_c | -0.094 |
| cma_late_c | 0.077 |
| sites_0c | -0.070 |
| inactive_last7 | 0.065 |
| registration_lead | -0.029 |
| clicks_0c | -0.019 |
| activity_ratio_run | 0.018 |
| banked_results | 0.005 |
[saved] aq-3/results/frozen_M1_d27_coefficients.csv  (23 rows x 2 columns)

**Frozen at 2026-11-12T15:58:51Z** – written to aq-3/results/freeze.json. No script of this rerun has read a 2014 outcome before this line. This freeze reproduces the first run's freeze of 2026-11-11T23:18:16Z, whose test results were known to the analyst when the rerun started; it is not a second blind test.

