# Log: aq-2 / 03_replication

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:27Z |
| Finished (UTC) | 2026-11-12T16:00:29Z |
| Duration | 1.5 s |
| Command | `python aq-2/code/03_replication.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 replication: adjusted risk difference per sign, 2013 runs (estimation) and 2014 runs (replication)

| label | n_2013 | adjusted_rd | adj_ci_low | adj_ci_high | n_2014 | adjusted_rd_2014 | adj_ci_low_2014 | adj_ci_high_2014 | change_2014_minus_2013 | change_ci_low | change_ci_high | change_interval_includes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task due by day 27 not submitted | 9,960 | 0.407 | 0.375 | 0.438 | 12,585 | 0.396 | 0.368 | 0.425 | -0.010 | -0.052 | 0.032 | yes |
| TMA submitted late | 9,960 | 0.217 | 0.174 | 0.259 | 9,064 | 0.225 | 0.179 | 0.272 | 0.009 | -0.054 | 0.072 | yes |
| No platform activity in the last 7 days | 11,811 | 0.135 | 0.101 | 0.168 | 15,724 | 0.154 | 0.128 | 0.181 | 0.019 | -0.023 | 0.062 | yes |
| Clicks below half the run median | 11,811 | 0.147 | 0.123 | 0.170 | 15,724 | 0.148 | 0.127 | 0.168 | 0.001 | -0.030 | 0.032 | yes |
| No activity before the start | 11,811 | 0.113 | 0.085 | 0.140 | 15,724 | 0.092 | 0.069 | 0.114 | -0.021 | -0.057 | 0.015 | yes |

**Verdicts**

| label | modules_defined | modules_same_direction | modules_same_direction_interval_excludes_0 | modules_interval_includes_0 | verdict | verdict_strict | modules_defined_2014 | modules_same_direction_2014 | modules_same_direction_interval_excludes_0_2014 | modules_interval_includes_0_2014 | verdict_2014 | verdict_strict_2014 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task due by day 27 not submitted | 4 | 4 | 4 | none | consistent association | consistent association | 5 | 5 | 5 | none | consistent association | consistent association |
| TMA submitted late | 4 | 4 | 4 | none | consistent association | consistent association | 4 | 4 | 3 | AAA | consistent association | consistent association |
| No platform activity in the last 7 days | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association | 7 | 7 | 7 | none | consistent association | consistent association |
| Clicks below half the run median | 6 | 6 | 6 | none | consistent association | consistent association | 7 | 7 | 6 | AAA | consistent association | consistent association |
| No activity before the start | 6 | 6 | 4 | AAA, GGG | consistent association | consistent association | 7 | 7 | 4 | AAA, BBB, DDD | consistent association | weak or inconsistent |
[saved] aq-2/results/replication.csv  (5 rows x 39 columns)

**By module (CCC has no 2013 run; the late-TMA sign is not defined in CCC)**

| sign | code_module | enrolments | adjusted_rd | adj_ci_low | adj_ci_high | enrolments_2014 | adjusted_rd_2014 | adj_ci_low_2014 | adj_ci_high_2014 | interval_excludes_0 | interval_excludes_0_2014 | same_direction_point_estimates | both_intervals_exclude_0_same_side |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_inactive_last7 | AAA | 369 | 0.049 | -0.082 | 0.179 | 348 | 0.165 | 0.032 | 0.298 | no | yes | yes | no |
| sign_inactive_last7 | BBB | 3,364 | 0.088 | 0.044 | 0.132 | 3,066 | 0.122 | 0.079 | 0.166 | yes | yes | yes | yes |
| sign_inactive_last7 | CCC |  |  |  |  | 3,521 | 0.189 | 0.147 | 0.231 |  | yes |  |  |
| sign_inactive_last7 | DDD | 2,790 | 0.193 | 0.092 | 0.294 | 2,492 | 0.142 | 0.068 | 0.216 | yes | yes | yes | yes |
| sign_inactive_last7 | EEE | 927 | 0.193 | 0.096 | 0.291 | 1,625 | 0.136 | 0.064 | 0.208 | yes | yes | yes | yes |
| sign_inactive_last7 | FFF | 3,437 | 0.153 | 0.093 | 0.212 | 3,158 | 0.168 | 0.081 | 0.255 | yes | yes | yes | yes |
| sign_inactive_last7 | GGG | 924 | 0.039 | -0.033 | 0.111 | 1,514 | 0.146 | 0.091 | 0.202 | no | yes | yes | no |
| sign_low_activity | AAA | 369 | 0.141 | 0.010 | 0.272 | 348 | 0.008 | -0.098 | 0.113 | yes | no | yes | no |
| sign_low_activity | BBB | 3,364 | 0.108 | 0.065 | 0.151 | 3,066 | 0.074 | 0.031 | 0.117 | yes | yes | yes | yes |
| sign_low_activity | CCC |  |  |  |  | 3,521 | 0.086 | 0.040 | 0.132 |  | yes |  |  |
| sign_low_activity | DDD | 2,790 | 0.161 | 0.115 | 0.208 | 2,492 | 0.176 | 0.125 | 0.227 | yes | yes | yes | yes |
| sign_low_activity | EEE | 927 | 0.346 | 0.249 | 0.444 | 1,625 | 0.290 | 0.220 | 0.360 | yes | yes | yes | yes |
| sign_low_activity | FFF | 3,437 | 0.124 | 0.077 | 0.170 | 3,158 | 0.205 | 0.160 | 0.251 | yes | yes | yes | yes |
| sign_low_activity | GGG | 924 | 0.129 | 0.050 | 0.207 | 1,514 | 0.153 | 0.093 | 0.213 | yes | yes | yes | yes |
| sign_no_pre_activity | AAA | 369 | 0.093 | -0.088 | 0.274 | 348 | 0.097 | -0.091 | 0.286 | no | no | yes | no |
| sign_no_pre_activity | BBB | 3,364 | 0.082 | 0.045 | 0.119 | 3,066 | 0.013 | -0.024 | 0.050 | yes | no | yes | no |
| sign_no_pre_activity | CCC |  |  |  |  | 3,521 | 0.130 | 0.080 | 0.179 |  | yes |  |  |
| sign_no_pre_activity | DDD | 2,790 | 0.136 | 0.071 | 0.200 | 2,492 | 0.060 | -0.013 | 0.132 | yes | no | yes | no |
| sign_no_pre_activity | EEE | 927 | 0.162 | 0.084 | 0.240 | 1,625 | 0.225 | 0.163 | 0.287 | yes | yes | yes | yes |
| sign_no_pre_activity | FFF | 3,437 | 0.131 | 0.069 | 0.193 | 3,158 | 0.089 | 0.035 | 0.144 | yes | yes | yes | yes |
| sign_no_pre_activity | GGG | 924 | 0.047 | -0.020 | 0.114 | 1,514 | 0.074 | 0.024 | 0.123 | no | yes | yes | no |
| sign_task_missed | AAA | 369 | 0.436 | 0.219 | 0.653 | 348 | 0.415 | 0.235 | 0.594 | yes | yes | yes | yes |
| sign_task_missed | BBB | 3,364 | 0.448 | 0.398 | 0.497 | 3,066 | 0.534 | 0.480 | 0.588 | yes | yes | yes | yes |
| sign_task_missed | CCC |  |  |  |  | 3,521 | 0.353 | 0.302 | 0.404 |  | yes |  |  |
| sign_task_missed | DDD | 2,790 | 0.352 | 0.304 | 0.401 | 2,492 | 0.367 | 0.305 | 0.428 | yes | yes | yes | yes |
| sign_task_missed | FFF | 3,437 | 0.408 | 0.347 | 0.469 | 3,158 | 0.332 | 0.269 | 0.395 | yes | yes | yes | yes |
| sign_tma_late | AAA | 369 | 0.198 | 0.063 | 0.333 | 348 | 0.002 | -0.132 | 0.135 | yes | no | yes | no |
| sign_tma_late | BBB | 3,364 | 0.224 | 0.167 | 0.281 | 3,066 | 0.257 | 0.189 | 0.326 | yes | yes | yes | yes |
| sign_tma_late | DDD | 2,790 | 0.171 | 0.063 | 0.280 | 2,492 | 0.208 | 0.122 | 0.293 | yes | yes | yes | yes |
| sign_tma_late | FFF | 3,437 | 0.248 | 0.186 | 0.310 | 3,158 | 0.233 | 0.139 | 0.327 | yes | yes | yes | yes |
[saved] aq-2/results/replication_by_module.csv  (30 rows x 16 columns)

sign x module cells estimated in both years: 26; same direction of the point estimates: 26; interval excludes 0 on the same side in both years: 18; 2014 interval includes 0: 5; 2013 interval includes 0: 4
cells estimated in 2014 only (module CCC): 4; their interval excludes 0: 4
all 2014 module estimates: 30; interval excludes 0: 25; includes 0: 5

**Every sign under every variant, both years (n = rows of the support)**

| variant | label | n | adjusted_rd | adj_ci_low | adj_ci_high | modules_same_direction | modules_defined | verdict | n_2014 | adjusted_rd_2014 | adj_ci_low_2014 | adj_ci_high_2014 | modules_same_direction_2014 | modules_defined_2014 | verdict_2014 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main | Task due by day 27 not submitted | 9,960 | 0.407 | 0.375 | 0.438 | 4 | 4 | consistent association | 12,585 | 0.396 | 0.368 | 0.425 | 5 | 5 | consistent association |
| main | TMA submitted late | 9,960 | 0.217 | 0.174 | 0.259 | 4 | 4 | consistent association | 9,064 | 0.225 | 0.179 | 0.272 | 4 | 4 | consistent association |
| main | No platform activity in the last 7 days | 11,811 | 0.135 | 0.101 | 0.168 | 6 | 6 | consistent association | 15,724 | 0.154 | 0.128 | 0.181 | 7 | 7 | consistent association |
| main | Clicks below half the run median | 11,811 | 0.147 | 0.123 | 0.170 | 6 | 6 | consistent association | 15,724 | 0.148 | 0.127 | 0.168 | 7 | 7 | consistent association |
| main | No activity before the start | 11,811 | 0.113 | 0.085 | 0.140 | 6 | 6 | consistent association | 15,724 | 0.092 | 0.069 | 0.114 | 7 | 7 | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | Task due by day 27 not submitted | 9,960 | 0.406 | 0.375 | 0.437 | 4 | 4 | consistent association | 12,585 | 0.398 | 0.369 | 0.426 | 5 | 5 | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | TMA submitted late | 9,960 | 0.216 | 0.174 | 0.258 | 4 | 4 | consistent association | 9,064 | 0.226 | 0.179 | 0.273 | 4 | 4 | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | No platform activity in the last 7 days | 11,811 | 0.135 | 0.101 | 0.169 | 6 | 6 | consistent association | 15,724 | 0.155 | 0.128 | 0.181 | 7 | 7 | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | De-duplicated clicks below half the run median | 11,811 | 0.148 | 0.124 | 0.172 | 6 | 6 | consistent association | 15,724 | 0.146 | 0.125 | 0.166 | 6 | 7 | consistent association |
| clicks de-duplicated (low-activity sign from de-duplicated clicks) | No activity before the start | 11,811 | 0.112 | 0.084 | 0.140 | 6 | 6 | consistent association | 15,724 | 0.091 | 0.069 | 0.114 | 7 | 7 | consistent association |
| late CMAs also count as late | Task due by day 27 not submitted | 9,960 | 0.406 | 0.374 | 0.437 | 4 | 4 | consistent association | 12,585 | 0.409 | 0.372 | 0.445 | 5 | 5 | consistent association |
| late CMAs also count as late | TMA or CMA submitted late | 9,960 | 0.167 | 0.128 | 0.206 | 3 | 4 | consistent association | 12,585 | 0.183 | 0.128 | 0.238 | 5 | 5 | consistent association |
| late CMAs also count as late | No platform activity in the last 7 days | 11,811 | 0.134 | 0.100 | 0.168 | 6 | 6 | consistent association | 15,724 | 0.154 | 0.128 | 0.181 | 7 | 7 | consistent association |
| late CMAs also count as late | Clicks below half the run median | 11,811 | 0.147 | 0.123 | 0.171 | 6 | 6 | consistent association | 15,724 | 0.148 | 0.128 | 0.169 | 7 | 7 | consistent association |
| late CMAs also count as late | No activity before the start | 11,811 | 0.113 | 0.085 | 0.141 | 6 | 6 | consistent association | 15,724 | 0.092 | 0.069 | 0.114 | 7 | 7 | consistent association |
| without flagged enrolments | Task due by day 27 not submitted | 9,954 | 0.407 | 0.375 | 0.438 | 4 | 4 | consistent association | 12,499 | 0.393 | 0.364 | 0.422 | 5 | 5 | consistent association |
| without flagged enrolments | TMA submitted late | 9,954 | 0.217 | 0.175 | 0.259 | 4 | 4 | consistent association | 9,007 | 0.226 | 0.179 | 0.274 | 4 | 4 | consistent association |
| without flagged enrolments | No platform activity in the last 7 days | 11,803 | 0.135 | 0.101 | 0.168 | 6 | 6 | consistent association | 15,632 | 0.151 | 0.124 | 0.178 | 7 | 7 | consistent association |
| without flagged enrolments | Clicks below half the run median | 11,803 | 0.146 | 0.123 | 0.170 | 6 | 6 | consistent association | 15,632 | 0.148 | 0.128 | 0.169 | 7 | 7 | consistent association |
| without flagged enrolments | No activity before the start | 11,803 | 0.113 | 0.085 | 0.140 | 6 | 6 | consistent association | 15,632 | 0.092 | 0.070 | 0.115 | 7 | 7 | consistent association |
| only runs with a task due by day 27 | Task due by day 27 not submitted | 9,960 | 0.406 | 0.375 | 0.438 | 4 | 4 | consistent association | 12,585 | 0.397 | 0.368 | 0.425 | 5 | 5 | consistent association |
| only runs with a task due by day 27 | TMA submitted late | 9,960 | 0.216 | 0.174 | 0.259 | 4 | 4 | consistent association | 9,064 | 0.225 | 0.179 | 0.272 | 4 | 4 | consistent association |
| only runs with a task due by day 27 | No platform activity in the last 7 days | 9,960 | 0.138 | 0.100 | 0.177 | 4 | 4 | consistent association | 12,585 | 0.157 | 0.126 | 0.188 | 5 | 5 | consistent association |
| only runs with a task due by day 27 | Clicks below half the run median | 9,960 | 0.129 | 0.104 | 0.155 | 4 | 4 | consistent association | 12,585 | 0.127 | 0.104 | 0.150 | 5 | 5 | consistent association |
| only runs with a task due by day 27 | No activity before the start | 9,960 | 0.114 | 0.083 | 0.145 | 4 | 4 | consistent association | 12,585 | 0.076 | 0.050 | 0.102 | 5 | 5 | consistent association |
| low activity = below a quarter of the run median | Task due by day 27 not submitted | 9,960 | 0.414 | 0.382 | 0.445 | 4 | 4 | consistent association | 12,585 | 0.404 | 0.375 | 0.432 | 5 | 5 | consistent association |
| low activity = below a quarter of the run median | TMA submitted late | 9,960 | 0.224 | 0.183 | 0.266 | 4 | 4 | consistent association | 9,064 | 0.238 | 0.192 | 0.284 | 4 | 4 | consistent association |
| low activity = below a quarter of the run median | No platform activity in the last 7 days | 11,811 | 0.154 | 0.121 | 0.188 | 6 | 6 | consistent association | 15,724 | 0.170 | 0.144 | 0.196 | 7 | 7 | consistent association |
| low activity = below a quarter of the run median | Clicks below a quarter of the run median | 11,811 | 0.144 | 0.110 | 0.178 | 6 | 6 | consistent association | 15,724 | 0.152 | 0.120 | 0.184 | 7 | 7 | consistent association |
| low activity = below a quarter of the run median | No activity before the start | 11,811 | 0.120 | 0.093 | 0.148 | 6 | 6 | consistent association | 15,724 | 0.099 | 0.076 | 0.121 | 7 | 7 | consistent association |
| low activity = below the run median | Task due by day 27 not submitted | 9,960 | 0.409 | 0.378 | 0.440 | 4 | 4 | consistent association | 12,585 | 0.393 | 0.365 | 0.421 | 5 | 5 | consistent association |
| low activity = below the run median | TMA submitted late | 9,960 | 0.203 | 0.160 | 0.246 | 4 | 4 | consistent association | 9,064 | 0.218 | 0.171 | 0.266 | 3 | 4 | consistent association |
| low activity = below the run median | No platform activity in the last 7 days | 11,811 | 0.143 | 0.112 | 0.175 | 6 | 6 | consistent association | 15,724 | 0.157 | 0.132 | 0.183 | 7 | 7 | consistent association |
| low activity = below the run median | Clicks below the run median | 11,811 | 0.134 | 0.115 | 0.152 | 6 | 6 | consistent association | 15,724 | 0.146 | 0.130 | 0.162 | 7 | 7 | consistent association |
| low activity = below the run median | No activity before the start | 11,811 | 0.106 | 0.078 | 0.133 | 6 | 6 | consistent association | 15,724 | 0.086 | 0.064 | 0.108 | 7 | 7 | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | Task due by day 27 not submitted | 9,960 | 0.373 | 0.338 | 0.408 | 4 | 4 | consistent association | 12,585 | 0.358 | 0.327 | 0.390 | 5 | 5 | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | TMA submitted late | 9,960 | 0.204 | 0.161 | 0.246 | 4 | 4 | consistent association | 9,064 | 0.212 | 0.165 | 0.260 | 3 | 4 | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | No platform activity in the last 7 days | 11,811 | 0.087 | 0.051 | 0.122 | 5 | 6 | consistent association | 15,724 | 0.102 | 0.075 | 0.130 | 7 | 7 | consistent association |
| post hoc: + log(1 + clicks on days 0-27) | Clicks below half the run median | 11,811 | 0.029 | -0.002 | 0.060 | 4 | 6 | weak or inconsistent | 15,724 | 0.008 | -0.019 | 0.034 | 3 | 7 | weak or inconsistent |
| post hoc: + log(1 + clicks on days 0-27) | No activity before the start | 11,811 | 0.091 | 0.063 | 0.119 | 6 | 6 | consistent association | 15,724 | 0.065 | 0.043 | 0.088 | 6 | 7 | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | Task due by day 27 not submitted | 9,960 | 0.374 | 0.339 | 0.409 | 4 | 4 | consistent association | 12,585 | 0.357 | 0.325 | 0.389 | 5 | 5 | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | TMA submitted late | 9,960 | 0.196 | 0.153 | 0.239 | 4 | 4 | consistent association | 9,064 | 0.210 | 0.162 | 0.258 | 3 | 4 | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | No platform activity in the last 7 days | 11,811 | 0.092 | 0.058 | 0.127 | 6 | 6 | consistent association | 15,724 | 0.107 | 0.080 | 0.133 | 7 | 7 | consistent association |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | Clicks below the run median | 11,811 | 0.059 | 0.034 | 0.083 | 5 | 6 | consistent association | 15,724 | 0.059 | 0.038 | 0.081 | 4 | 7 | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | No activity before the start | 11,811 | 0.089 | 0.061 | 0.116 | 6 | 6 | consistent association | 15,724 | 0.065 | 0.042 | 0.087 | 6 | 7 | consistent association |
[saved] aq-2/results/replication_sensitivity.csv  (45 rows x 22 columns)

sign x variant rows where the Level 1 criterion is not met in at least one year: 2 of 45

| variant | status | label | adjusted_rd | adj_ci_low | verdict | adjusted_rd_2014 | adj_ci_low_2014 | modules_same_direction_2014 | modules_defined_2014 | verdict_2014 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| post hoc: + log(1 + clicks on days 0-27) | post hoc | Clicks below half the run median | 0.029 | -0.002 | weak or inconsistent | 0.008 | -0.019 | 3 | 7 | weak or inconsistent |
| post hoc: low activity = below the run median, + log(1 + clicks on days 0-27) | post hoc | Clicks below the run median | 0.059 | 0.034 | consistent association | 0.059 | 0.038 | 4 | 7 | weak or inconsistent |

**Late TMA in 2014: the average over the support against an average that counts rows without a slope as 0**

| sign | year | n_support | adjusted_rd_over_support | rows_of_runs_with_any_task_due | rows_without_a_slope | average_if_those_rows_counted_as_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_tma_late | 2,014 | 9,064 | 0.2254 | 12,585 | 3,521 | 0.1623 |
[saved] aq-2/results/late_tma_average_check.csv  (1 rows x 7 columns)

