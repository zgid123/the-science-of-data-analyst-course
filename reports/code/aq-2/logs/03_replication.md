# Log: aq-2 / 03_replication

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:24:39Z |
| Finished (UTC) | 2026-11-11T23:24:42Z |
| Duration | 2.6 s |
| Command | `python aq-2/code/03_replication.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 replication: adjusted risk difference per sign, 2013 runs (estimation) and 2014 runs (replication)

| label | adjusted_rd | adj_ci_low | adj_ci_high | adjusted_rd_2014 | adj_ci_low_2014 | adj_ci_high_2014 | change_2014_minus_2013 | intervals_overlap | verdict | verdict_2014 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task due by day 27 not submitted | 0.407 | 0.375 | 0.438 | 0.396 | 0.368 | 0.425 | -0.010 | yes | consistent association | consistent association |
| TMA submitted late | 0.217 | 0.174 | 0.259 | 0.162 | 0.129 | 0.196 | -0.054 | yes | consistent association | consistent association |
| No platform activity in the last 7 days | 0.135 | 0.101 | 0.168 | 0.154 | 0.128 | 0.181 | 0.019 | yes | consistent association | consistent association |
| Clicks below half the run median | 0.147 | 0.123 | 0.170 | 0.148 | 0.127 | 0.168 | 0.001 | yes | consistent association | consistent association |
| No activity before the start | 0.113 | 0.085 | 0.140 | 0.092 | 0.069 | 0.114 | -0.021 | yes | consistent association | consistent association |
[saved] aq-2/results/replication.csv  (5 rows x 23 columns)

**By module (CCC has no 2013 run)**

| sign | code_module | adjusted_rd | adj_ci_low | adj_ci_high | adjusted_rd_2014 | adj_ci_low_2014 | adj_ci_high_2014 | same_direction | interval_2014_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| sign_inactive_last7 | AAA | 0.049 | -0.082 | 0.179 | 0.165 | 0.032 | 0.298 | yes | yes |
| sign_inactive_last7 | BBB | 0.088 | 0.044 | 0.132 | 0.122 | 0.079 | 0.166 | yes | yes |
| sign_inactive_last7 | CCC |  |  |  | 0.189 | 0.147 | 0.231 |  | yes |
| sign_inactive_last7 | DDD | 0.193 | 0.092 | 0.294 | 0.142 | 0.068 | 0.216 | yes | yes |
| sign_inactive_last7 | EEE | 0.193 | 0.096 | 0.291 | 0.136 | 0.064 | 0.208 | yes | yes |
| sign_inactive_last7 | FFF | 0.153 | 0.093 | 0.212 | 0.168 | 0.081 | 0.255 | yes | yes |
| sign_inactive_last7 | GGG | 0.039 | -0.033 | 0.111 | 0.146 | 0.091 | 0.202 | yes | yes |
| sign_low_activity | AAA | 0.141 | 0.010 | 0.272 | 0.008 | -0.098 | 0.113 | yes | no |
| sign_low_activity | BBB | 0.108 | 0.065 | 0.151 | 0.074 | 0.031 | 0.117 | yes | yes |
| sign_low_activity | CCC |  |  |  | 0.086 | 0.040 | 0.132 |  | yes |
| sign_low_activity | DDD | 0.161 | 0.115 | 0.208 | 0.176 | 0.125 | 0.227 | yes | yes |
| sign_low_activity | EEE | 0.346 | 0.249 | 0.444 | 0.290 | 0.220 | 0.360 | yes | yes |
| sign_low_activity | FFF | 0.124 | 0.077 | 0.170 | 0.205 | 0.160 | 0.251 | yes | yes |
| sign_low_activity | GGG | 0.129 | 0.050 | 0.207 | 0.153 | 0.093 | 0.213 | yes | yes |
| sign_no_pre_activity | AAA | 0.093 | -0.088 | 0.274 | 0.097 | -0.091 | 0.286 | yes | no |
| sign_no_pre_activity | BBB | 0.082 | 0.045 | 0.119 | 0.013 | -0.024 | 0.050 | yes | no |
| sign_no_pre_activity | CCC |  |  |  | 0.130 | 0.080 | 0.179 |  | yes |
| sign_no_pre_activity | DDD | 0.136 | 0.071 | 0.200 | 0.060 | -0.013 | 0.132 | yes | no |
| sign_no_pre_activity | EEE | 0.162 | 0.084 | 0.240 | 0.225 | 0.163 | 0.287 | yes | yes |
| sign_no_pre_activity | FFF | 0.131 | 0.069 | 0.193 | 0.089 | 0.035 | 0.144 | yes | yes |
| sign_no_pre_activity | GGG | 0.047 | -0.020 | 0.114 | 0.074 | 0.024 | 0.123 | yes | yes |
| sign_task_missed | AAA | 0.436 | 0.219 | 0.653 | 0.415 | 0.235 | 0.594 | yes | yes |
| sign_task_missed | BBB | 0.448 | 0.398 | 0.497 | 0.534 | 0.480 | 0.588 | yes | yes |
| sign_task_missed | CCC |  |  |  | 0.353 | 0.302 | 0.404 |  | yes |
| sign_task_missed | DDD | 0.352 | 0.304 | 0.401 | 0.367 | 0.305 | 0.428 | yes | yes |
| sign_task_missed | FFF | 0.408 | 0.347 | 0.469 | 0.332 | 0.269 | 0.395 | yes | yes |
| sign_tma_late | AAA | 0.198 | 0.063 | 0.333 | 0.002 | -0.132 | 0.135 | yes | no |
| sign_tma_late | BBB | 0.224 | 0.167 | 0.281 | 0.257 | 0.189 | 0.326 | yes | yes |
| sign_tma_late | DDD | 0.171 | 0.063 | 0.280 | 0.208 | 0.122 | 0.293 | yes | yes |
| sign_tma_late | FFF | 0.248 | 0.186 | 0.310 | 0.233 | 0.139 | 0.327 | yes | yes |
[saved] aq-2/results/replication_by_module.csv  (30 rows x 14 columns)

sign x module cells estimated in both years: 26; same direction: 26; 2014 interval excludes 0: 21

