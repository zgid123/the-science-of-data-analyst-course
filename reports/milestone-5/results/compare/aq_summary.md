# Comparisons between 2013 and 2014

Written by `src/analysis/aq_year_compare.py` (and, for the three cross-check files, by the 2013 scope of `src/analysis/aq_analysis.py` and by `src/analysis/aq1_year_shared_modules.py`). Rates carry 95% Wilson intervals and differences of two rates 95% Newcombe intervals unless a line says otherwise. Methods: `results/README.md`.

**`aq1_year_comparison_computed.csv`.** AQ1. Non-completion by year under both denominators, computed from the prepared views of each year, with the 2014 − 2013 difference (points, 95% Newcombe interval); module CCC ran only in 2014.

| level | unit | denominator | nc_2013 | n_2013 | rate_2013 | ci_low_2013 | ci_high_2013 | nc_2014 | n_2014 | rate_2014 | ci_low_2014 | ci_high_2014 | diff_pp_2014_minus_2013 | ci_low_pp | ci_high_pp |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| overall | all runs | day14_registered | 5515 | 12076 | 0.4567 | 0.4478 | 0.4656 | 7185 | 15985 | 0.4495 | 0.4418 | 0.4572 | -0.72 | -1.9 | 0.46 |
| shared_modules | the 6 modules run in both years | day14_registered | 5515 | 12076 | 0.4567 | 0.4478 | 0.4656 | 5191 | 12315 | 0.4215 | 0.4128 | 0.4303 | -3.52 | -4.76 | -2.27 |
| start_month | B | day14_registered | 2231 | 4323 | 0.5161 | 0.5012 | 0.531 | 3300 | 6654 | 0.4959 | 0.4839 | 0.508 | -2.01 | -3.93 | -0.1 |
| start_month | J | day14_registered | 3284 | 7753 | 0.4236 | 0.4126 | 0.4346 | 3885 | 9331 | 0.4164 | 0.4064 | 0.4264 | -0.72 | -2.21 | 0.76 |
| module | AAA | day14_registered | 92 | 370 | 0.2486 | 0.2073 | 0.2951 | 97 | 350 | 0.2771 | 0.2329 | 0.3263 | 2.85 | -3.57 | 9.27 |
| module | BBB | day14_registered | 1585 | 3457 | 0.4585 | 0.4419 | 0.4751 | 1212 | 3080 | 0.3935 | 0.3764 | 0.4109 | -6.5 | -8.89 | -4.1 |
| module | DDD | day14_registered | 1537 | 2872 | 0.5352 | 0.5169 | 0.5533 | 1259 | 2529 | 0.4978 | 0.4784 | 0.5173 | -3.73 | -6.4 | -1.06 |
| module | EEE | day14_registered | 325 | 933 | 0.3483 | 0.3184 | 0.3795 | 599 | 1640 | 0.3652 | 0.3423 | 0.3888 | 1.69 | -2.18 | 5.5 |
| module | FFF | day14_registered | 1642 | 3518 | 0.4667 | 0.4503 | 0.4833 | 1425 | 3195 | 0.446 | 0.4288 | 0.4633 | -2.07 | -4.45 | 0.31 |
| module | GGG | day14_registered | 334 | 926 | 0.3607 | 0.3304 | 0.3921 | 599 | 1521 | 0.3938 | 0.3696 | 0.4186 | 3.31 | -0.66 | 7.23 |
| module_start_month | AAA J | day14_registered | 92 | 370 | 0.2486 | 0.2073 | 0.2951 | 97 | 350 | 0.2771 | 0.2329 | 0.3263 | 2.85 | -3.57 | 9.27 |
| module_start_month | BBB B | day14_registered | 804 | 1606 | 0.5006 | 0.4762 | 0.525 | 564 | 1289 | 0.4375 | 0.4107 | 0.4648 | -6.31 | -9.94 | -2.65 |
| module_start_month | BBB J | day14_registered | 781 | 1851 | 0.4219 | 0.3996 | 0.4446 | 648 | 1791 | 0.3618 | 0.3399 | 0.3843 | -6.01 | -9.16 | -2.84 |
| module_start_month | DDD B | day14_registered | 688 | 1197 | 0.5748 | 0.5466 | 0.6025 | 572 | 1050 | 0.5448 | 0.5145 | 0.5747 | -3.0 | -7.1 | 1.11 |
| module_start_month | DDD J | day14_registered | 849 | 1675 | 0.5069 | 0.4829 | 0.5308 | 687 | 1479 | 0.4645 | 0.4392 | 0.49 | -4.24 | -7.72 | -0.74 |
| module_start_month | EEE J | day14_registered | 325 | 933 | 0.3483 | 0.3184 | 0.3795 | 343 | 1027 | 0.334 | 0.3058 | 0.3634 | -1.44 | -5.64 | 2.76 |
| module_start_month | FFF B | day14_registered | 739 | 1520 | 0.4862 | 0.4611 | 0.5113 | 656 | 1309 | 0.5011 | 0.4741 | 0.5282 | 1.5 | -2.2 | 5.18 |
| module_start_month | FFF J | day14_registered | 903 | 1998 | 0.452 | 0.4302 | 0.4738 | 769 | 1886 | 0.4077 | 0.3858 | 0.4301 | -4.42 | -7.52 | -1.31 |
| module_start_month | GGG J | day14_registered | 334 | 926 | 0.3607 | 0.3304 | 0.3921 | 275 | 719 | 0.3825 | 0.3477 | 0.4185 | 2.18 | -2.51 | 6.89 |
| module | CCC (2014 only) | day14_registered |  | 0 |  |  |  | 1994 | 3670 | 0.5433 | 0.5272 | 0.5594 |  |  |  |
| overall | all runs | all_enrolments | 6959 | 13529 | 0.5144 | 0.506 | 0.5228 | 10249 | 19064 | 0.5376 | 0.5305 | 0.5447 | 2.32 | 1.22 | 3.42 |
| shared_modules | the 6 modules run in both years | all_enrolments | 6959 | 13529 | 0.5144 | 0.506 | 0.5228 | 7493 | 14630 | 0.5122 | 0.5041 | 0.5203 | -0.22 | -1.39 | 0.95 |
| start_month | B | all_enrolments | 2589 | 4684 | 0.5527 | 0.5385 | 0.5669 | 4446 | 7804 | 0.5697 | 0.5587 | 0.5807 | 1.7 | -0.1 | 3.5 |
| start_month | J | all_enrolments | 4370 | 8845 | 0.4941 | 0.4836 | 0.5045 | 5803 | 11260 | 0.5154 | 0.5061 | 0.5246 | 2.13 | 0.74 | 3.52 |
| module | AAA | all_enrolments | 105 | 383 | 0.2742 | 0.2319 | 0.3209 | 112 | 365 | 0.3068 | 0.2618 | 0.356 | 3.27 | -3.23 | 9.75 |
| module | BBB | all_enrolments | 2129 | 4004 | 0.5317 | 0.5162 | 0.5471 | 2026 | 3905 | 0.5188 | 0.5031 | 0.5345 | -1.29 | -3.49 | 0.91 |
| module | DDD | all_enrolments | 1902 | 3241 | 0.5869 | 0.5698 | 0.6037 | 1760 | 3031 | 0.5807 | 0.563 | 0.5981 | -0.62 | -3.06 | 1.82 |
| module | EEE | all_enrolments | 443 | 1052 | 0.4211 | 0.3916 | 0.4512 | 841 | 1882 | 0.4469 | 0.4245 | 0.4694 | 2.58 | -1.17 | 6.29 |
| module | FFF | all_enrolments | 2020 | 3897 | 0.5183 | 0.5026 | 0.534 | 2094 | 3865 | 0.5418 | 0.526 | 0.5574 | 2.34 | 0.12 | 4.56 |
| module | GGG | all_enrolments | 360 | 952 | 0.3782 | 0.3479 | 0.4094 | 660 | 1582 | 0.4172 | 0.3931 | 0.4417 | 3.9 | -0.04 | 7.8 |
| module_start_month | AAA J | all_enrolments | 105 | 383 | 0.2742 | 0.2319 | 0.3209 | 112 | 365 | 0.3068 | 0.2618 | 0.356 | 3.27 | -3.23 | 9.75 |
| module_start_month | BBB B | all_enrolments | 964 | 1767 | 0.5456 | 0.5223 | 0.5686 | 886 | 1613 | 0.5493 | 0.5249 | 0.5734 | 0.37 | -2.98 | 3.73 |
| module_start_month | BBB J | all_enrolments | 1165 | 2237 | 0.5208 | 0.5001 | 0.5414 | 1140 | 2292 | 0.4974 | 0.4769 | 0.5178 | -2.34 | -5.25 | 0.57 |
| module_start_month | DDD B | all_enrolments | 793 | 1303 | 0.6086 | 0.5818 | 0.6347 | 749 | 1228 | 0.6099 | 0.5824 | 0.6368 | 0.13 | -3.67 | 3.93 |
| module_start_month | DDD J | all_enrolments | 1109 | 1938 | 0.5722 | 0.5501 | 0.5941 | 1011 | 1803 | 0.5607 | 0.5377 | 0.5835 | -1.15 | -4.33 | 2.02 |
| module_start_month | EEE J | all_enrolments | 443 | 1052 | 0.4211 | 0.3916 | 0.4512 | 504 | 1188 | 0.4242 | 0.3964 | 0.4525 | 0.31 | -3.78 | 4.4 |
| module_start_month | FFF B | all_enrolments | 832 | 1614 | 0.5155 | 0.4911 | 0.5398 | 846 | 1500 | 0.564 | 0.5388 | 0.5889 | 4.85 | 1.35 | 8.34 |
| module_start_month | FFF J | all_enrolments | 1188 | 2283 | 0.5204 | 0.4999 | 0.5408 | 1248 | 2365 | 0.5277 | 0.5075 | 0.5478 | 0.73 | -2.14 | 3.6 |
| module_start_month | GGG J | all_enrolments | 360 | 952 | 0.3782 | 0.3479 | 0.4094 | 305 | 749 | 0.4072 | 0.3726 | 0.4428 | 2.91 | -1.76 | 7.58 |
| module | CCC (2014 only) | all_enrolments |  | 0 |  |  |  | 2756 | 4434 | 0.6216 | 0.6072 | 0.6357 |  |  |  |

**`aq1_left_before_day14.csv`.** AQ1. Share of all enrolments not registered at day 14, by year, with the 2014 − 2013 difference; it explains why the year difference changes sign between the two denominators.

| unit | year | n_all | not_registered_day14 | share | ci_low | ci_high | diff_pp_2014_minus_2013 | diff_ci_low | diff_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 2013 | 13529 | 1453 | 0.1074 | 0.1023 | 0.1127 |  |  |  |
| all runs | 2014 | 19064 | 3079 | 0.1615 | 0.1564 | 0.1668 | 5.41 | 4.67 | 6.15 |
| the 6 modules run in both years | 2013 | 13529 | 1453 | 0.1074 | 0.1023 | 0.1127 |  |  |  |
| the 6 modules run in both years | 2014 | 14630 | 2315 | 0.1582 | 0.1524 | 0.1642 | 5.08 | 4.29 | 5.87 |

**`aq1_first_missed_week_by_year.csv`.** AQ1. Share of the day-14 population with a missed assessed task and with one by week 4, and the median first missed week, by year and completion group.

| group | year | n | with_missed_task | share_any | ci_low_any | ci_high_any | missed_by_week4 | share_by_week4 | ci_low_week4 | ci_high_week4 | median_first_missed_week | diff_any_pp | diff_any_ci_low | diff_any_ci_high | diff_week4_pp | diff_week4_ci_low | diff_week4_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| all | 2013 | 12076 | 5746 | 0.4758 | 0.4669 | 0.4847 | 1110 | 0.0919 | 0.0869 | 0.0972 | 14.0 |  |  |  |  |  |  |
| all | 2014 | 15985 | 6936 | 0.4339 | 0.4262 | 0.4416 | 1107 | 0.0693 | 0.0654 | 0.0733 | 10.0 | -4.19 | -5.37 | -3.01 | -2.27 | -2.92 | -1.62 |
| Completed | 2013 | 6561 | 1439 | 0.2193 | 0.2095 | 0.2295 | 30 | 0.0046 | 0.0032 | 0.0065 | 24.0 |  |  |  |  |  |  |
| Completed | 2014 | 8800 | 1711 | 0.1944 | 0.1863 | 0.2028 | 54 | 0.0061 | 0.0047 | 0.008 | 22.0 | -2.49 | -3.79 | -1.2 | 0.16 | -0.09 | 0.39 |
| Not completed | 2013 | 5515 | 4307 | 0.781 | 0.7699 | 0.7917 | 1080 | 0.1958 | 0.1856 | 0.2065 | 9.0 |  |  |  |  |  |  |
| Not completed | 2014 | 7185 | 5225 | 0.7272 | 0.7168 | 0.7374 | 1053 | 0.1466 | 0.1386 | 0.1549 | 9.0 | -5.38 | -6.87 | -3.87 | -4.93 | -6.26 | -3.6 |

**`aq2_year_comparison.csv`.** AQ2. Mutually adjusted average risk difference of each early sign in 2013 and 2014 (points, four decimals), the 2014 − 2013 difference with its 95% interval, module direction and verdict.

| sign | n_2013 | rd_2013_pp | ci_low_2013 | ci_high_2013 | modules_2013 | verdict_2013 | n_2014 | rd_2014_pp | ci_low_2014 | ci_high_2014 | modules_2014 | verdict_2014 | diff_pp_2014_minus_2013 | diff_ci_low | diff_ci_high | rd_unadj_2013_pp | rd_unadj_2014_pp |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| missed_task | 9960 | 40.8308 | 37.7305 | 43.9311 | 4/4 | consistent association | 12585 | 39.2638 | 36.4493 | 42.0783 | 5/5 | consistent association | -1.567 | -5.7542 | 2.6202 | 50.32 | 48.77 |
| late_tma | 9960 | 20.1978 | 15.8725 | 24.5231 | 4/4 | consistent association | 12585 | 20.2543 | 15.6397 | 24.8689 | 3/4 | consistent association | 0.0566 | -6.2682 | 6.3813 | 18.54 | 14.36 |
| inactive_last7 | 11811 | 14.4602 | 11.3025 | 17.6178 | 6/6 | consistent association | 15724 | 15.8245 | 13.2999 | 18.3491 | 7/7 | consistent association | 1.3643 | -2.6785 | 5.4071 | 25.26 | 26.53 |
| low_relative_activity | 11811 | 13.3567 | 11.4819 | 15.2316 | 6/6 | consistent association | 15724 | 14.5996 | 12.9798 | 16.2194 | 7/7 | consistent association | 1.2429 | -1.2348 | 3.7205 | 27.29 | 26.97 |
| no_pre_start_activity | 11811 | 10.5623 | 7.8395 | 13.2852 | 6/6 | consistent association | 15724 | 8.6542 | 6.4378 | 10.8706 | 7/7 | consistent association | -1.9081 | -5.419 | 1.6028 | 21.24 | 17.92 |

**`aq2_concurrent_2014.csv`.** AQ2. The sign 'tasks missed in several modules at once', described on the 2014 runs only (Change Log C12), unadjusted; with the count of concurrent enrolments in each year.

| year | population | group | n | non_completers | rate | ci_low | ci_high | rd_pp | rd_ci_low | rd_ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2013 | registered at day 27 | concurrent enrolment (another enrolment in the same presentation, registered at day 27) | 12 | 7 |  |  |  |  |  |  |
| 2014 | registered at day 27 | concurrent enrolment (another enrolment in the same presentation, registered at day 27) | 1288 | 694 |  |  |  |  |  |  |
| 2014 | all 2014 enrolments registered at day 27 | missed tasks in several modules at once | 28 | 27 | 0.9643 | 0.8229 | 0.9937 | 52.57 | 38.41 | 55.61 |
| 2014 | all 2014 enrolments registered at day 27 | all others | 15696 | 6884 | 0.4386 | 0.4308 | 0.4464 |  |  |  |
| 2014 | 2014 concurrent enrolments registered at day 27 | missed tasks in several modules at once | 28 | 27 | 0.9643 | 0.8229 | 0.9937 | 43.49 | 29.09 | 47.52 |
| 2014 | 2014 concurrent enrolments registered at day 27 | all others | 1260 | 667 | 0.5294 | 0.5018 | 0.5568 |  |  |  |

**`aq1_year_comparison_published.csv`.** Cross-check. Outcome shares by year over all enrolments, 2013 computed and 2014 as the per-run counts Milestone 3 published (written by the 2013 scope of aq_analysis.py); the computed 2014 counts equal these cell by cell.

| level | group | year | denominator | measure | events | n | rate | ci_low | ci_high | source |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| year | 2013 | 2013 | all_enrolments | completion | 6570 | 13529 | 0.4856 | 0.4772 | 0.494 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2013 | 2013 | all_enrolments | non_completion | 6959 | 13529 | 0.5144 | 0.506 | 0.5228 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2013 | 2013 | all_enrolments | Pass | 5494 | 13529 | 0.4061 | 0.3978 | 0.4144 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2013 | 2013 | all_enrolments | Distinction | 1076 | 13529 | 0.0795 | 0.0751 | 0.0842 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2013 | 2013 | all_enrolments | Fail | 3242 | 13529 | 0.2396 | 0.2325 | 0.2469 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2013 | 2013 | all_enrolments | Withdrawn | 3717 | 13529 | 0.2747 | 0.2673 | 0.2823 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| year | 2014 | 2014 | all_enrolments | completion | 8815 | 19064 | 0.4624 | 0.4553 | 0.4695 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| year | 2014 | 2014 | all_enrolments | non_completion | 10249 | 19064 | 0.5376 | 0.5305 | 0.5447 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| year | 2014 | 2014 | all_enrolments | Pass | 6867 | 19064 | 0.3602 | 0.3534 | 0.367 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| year | 2014 | 2014 | all_enrolments | Distinction | 1948 | 19064 | 0.1022 | 0.098 | 0.1066 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| year | 2014 | 2014 | all_enrolments | Fail | 3810 | 19064 | 0.1999 | 0.1942 | 0.2056 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| year | 2014 | 2014 | all_enrolments | Withdrawn | 6439 | 19064 | 0.3378 | 0.3311 | 0.3445 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2013 | 2013 | all_enrolments | completion | 278 | 383 | 0.7258 | 0.6791 | 0.7681 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2013 | 2013 | all_enrolments | non_completion | 105 | 383 | 0.2742 | 0.2319 | 0.3209 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2013 | 2013 | all_enrolments | Pass | 258 | 383 | 0.6736 | 0.6251 | 0.7187 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2013 | 2013 | all_enrolments | Distinction | 20 | 383 | 0.0522 | 0.0341 | 0.0793 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2013 | 2013 | all_enrolments | Fail | 45 | 383 | 0.1175 | 0.089 | 0.1536 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2013 | 2013 | all_enrolments | Withdrawn | 60 | 383 | 0.1567 | 0.1237 | 0.1964 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | AAA 2014 | 2014 | all_enrolments | completion | 253 | 365 | 0.6932 | 0.644 | 0.7382 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2014 | 2014 | all_enrolments | non_completion | 112 | 365 | 0.3068 | 0.2618 | 0.356 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2014 | 2014 | all_enrolments | Pass | 229 | 365 | 0.6274 | 0.5767 | 0.6754 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2014 | 2014 | all_enrolments | Distinction | 24 | 365 | 0.0658 | 0.0446 | 0.096 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2014 | 2014 | all_enrolments | Fail | 46 | 365 | 0.126 | 0.0958 | 0.164 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | AAA 2014 | 2014 | all_enrolments | Withdrawn | 66 | 365 | 0.1808 | 0.1447 | 0.2236 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2013 | 2013 | all_enrolments | completion | 1875 | 4004 | 0.4683 | 0.4529 | 0.4838 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2013 | 2013 | all_enrolments | non_completion | 2129 | 4004 | 0.5317 | 0.5162 | 0.5471 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2013 | 2013 | all_enrolments | Pass | 1544 | 4004 | 0.3856 | 0.3707 | 0.4008 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2013 | 2013 | all_enrolments | Distinction | 331 | 4004 | 0.0827 | 0.0745 | 0.0916 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2013 | 2013 | all_enrolments | Fail | 980 | 4004 | 0.2448 | 0.2317 | 0.2583 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2013 | 2013 | all_enrolments | Withdrawn | 1149 | 4004 | 0.287 | 0.2732 | 0.3012 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | BBB 2014 | 2014 | all_enrolments | completion | 1879 | 3905 | 0.4812 | 0.4655 | 0.4969 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2014 | 2014 | all_enrolments | non_completion | 2026 | 3905 | 0.5188 | 0.5031 | 0.5345 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2014 | 2014 | all_enrolments | Pass | 1533 | 3905 | 0.3926 | 0.3774 | 0.408 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2014 | 2014 | all_enrolments | Distinction | 346 | 3905 | 0.0886 | 0.0801 | 0.0979 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2014 | 2014 | all_enrolments | Fail | 787 | 3905 | 0.2015 | 0.1893 | 0.2144 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | BBB 2014 | 2014 | all_enrolments | Withdrawn | 1239 | 3905 | 0.3173 | 0.3029 | 0.3321 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | completion | 1678 | 4434 | 0.3784 | 0.3643 | 0.3928 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | non_completion | 2756 | 4434 | 0.6216 | 0.6072 | 0.6357 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | Pass | 1180 | 4434 | 0.2661 | 0.2533 | 0.2793 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | Distinction | 498 | 4434 | 0.1123 | 0.1034 | 0.1219 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | Fail | 781 | 4434 | 0.1761 | 0.1652 | 0.1876 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | CCC 2014 | 2014 | all_enrolments | Withdrawn | 1975 | 4434 | 0.4454 | 0.4308 | 0.4601 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2013 | 2013 | all_enrolments | completion | 1339 | 3241 | 0.4131 | 0.3963 | 0.4302 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2013 | 2013 | all_enrolments | non_completion | 1902 | 3241 | 0.5869 | 0.5698 | 0.6037 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2013 | 2013 | all_enrolments | Pass | 1187 | 3241 | 0.3662 | 0.3498 | 0.383 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2013 | 2013 | all_enrolments | Distinction | 152 | 3241 | 0.0469 | 0.0401 | 0.0547 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2013 | 2013 | all_enrolments | Fail | 789 | 3241 | 0.2434 | 0.229 | 0.2585 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2013 | 2013 | all_enrolments | Withdrawn | 1113 | 3241 | 0.3434 | 0.3273 | 0.3599 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | DDD 2014 | 2014 | all_enrolments | completion | 1271 | 3031 | 0.4193 | 0.4019 | 0.437 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2014 | 2014 | all_enrolments | non_completion | 1760 | 3031 | 0.5807 | 0.563 | 0.5981 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2014 | 2014 | all_enrolments | Pass | 1040 | 3031 | 0.3431 | 0.3264 | 0.3602 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2014 | 2014 | all_enrolments | Distinction | 231 | 3031 | 0.0762 | 0.0673 | 0.0862 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2014 | 2014 | all_enrolments | Fail | 623 | 3031 | 0.2055 | 0.1915 | 0.2203 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | DDD 2014 | 2014 | all_enrolments | Withdrawn | 1137 | 3031 | 0.3751 | 0.3581 | 0.3925 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2013 | 2013 | all_enrolments | completion | 609 | 1052 | 0.5789 | 0.5488 | 0.6084 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2013 | 2013 | all_enrolments | non_completion | 443 | 1052 | 0.4211 | 0.3916 | 0.4512 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2013 | 2013 | all_enrolments | Pass | 482 | 1052 | 0.4582 | 0.4283 | 0.4884 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2013 | 2013 | all_enrolments | Distinction | 127 | 1052 | 0.1207 | 0.1024 | 0.1418 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2013 | 2013 | all_enrolments | Fail | 200 | 1052 | 0.1901 | 0.1675 | 0.2149 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2013 | 2013 | all_enrolments | Withdrawn | 243 | 1052 | 0.231 | 0.2065 | 0.2574 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | EEE 2014 | 2014 | all_enrolments | completion | 1041 | 1882 | 0.5531 | 0.5306 | 0.5755 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2014 | 2014 | all_enrolments | non_completion | 841 | 1882 | 0.4469 | 0.4245 | 0.4694 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2014 | 2014 | all_enrolments | Pass | 812 | 1882 | 0.4315 | 0.4092 | 0.4539 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2014 | 2014 | all_enrolments | Distinction | 229 | 1882 | 0.1217 | 0.1077 | 0.1372 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2014 | 2014 | all_enrolments | Fail | 362 | 1882 | 0.1923 | 0.1752 | 0.2108 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | EEE 2014 | 2014 | all_enrolments | Withdrawn | 479 | 1882 | 0.2545 | 0.2354 | 0.2747 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2013 | 2013 | all_enrolments | completion | 1877 | 3897 | 0.4817 | 0.466 | 0.4974 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2013 | 2013 | all_enrolments | non_completion | 2020 | 3897 | 0.5183 | 0.5026 | 0.534 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2013 | 2013 | all_enrolments | Pass | 1572 | 3897 | 0.4034 | 0.3881 | 0.4189 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2013 | 2013 | all_enrolments | Distinction | 305 | 3897 | 0.0783 | 0.0702 | 0.0871 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2013 | 2013 | all_enrolments | Fail | 934 | 3897 | 0.2397 | 0.2265 | 0.2533 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2013 | 2013 | all_enrolments | Withdrawn | 1086 | 3897 | 0.2787 | 0.2648 | 0.293 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | FFF 2014 | 2014 | all_enrolments | completion | 1771 | 3865 | 0.4582 | 0.4426 | 0.474 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2014 | 2014 | all_enrolments | non_completion | 2094 | 3865 | 0.5418 | 0.526 | 0.5574 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2014 | 2014 | all_enrolments | Pass | 1406 | 3865 | 0.3638 | 0.3488 | 0.3791 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2014 | 2014 | all_enrolments | Distinction | 365 | 3865 | 0.0944 | 0.0856 | 0.1041 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2014 | 2014 | all_enrolments | Fail | 777 | 3865 | 0.201 | 0.1887 | 0.214 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | FFF 2014 | 2014 | all_enrolments | Withdrawn | 1317 | 3865 | 0.3408 | 0.326 | 0.3558 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2013 | 2013 | all_enrolments | completion | 592 | 952 | 0.6218 | 0.5906 | 0.6521 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2013 | 2013 | all_enrolments | non_completion | 360 | 952 | 0.3782 | 0.3479 | 0.4094 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2013 | 2013 | all_enrolments | Pass | 451 | 952 | 0.4737 | 0.4422 | 0.5055 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2013 | 2013 | all_enrolments | Distinction | 141 | 952 | 0.1481 | 0.127 | 0.1721 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2013 | 2013 | all_enrolments | Fail | 294 | 952 | 0.3088 | 0.2803 | 0.3389 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2013 | 2013 | all_enrolments | Withdrawn | 66 | 952 | 0.0693 | 0.0549 | 0.0873 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| module_year | GGG 2014 | 2014 | all_enrolments | completion | 922 | 1582 | 0.5828 | 0.5583 | 0.6069 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2014 | 2014 | all_enrolments | non_completion | 660 | 1582 | 0.4172 | 0.3931 | 0.4417 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2014 | 2014 | all_enrolments | Pass | 667 | 1582 | 0.4216 | 0.3975 | 0.4461 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2014 | 2014 | all_enrolments | Distinction | 255 | 1582 | 0.1612 | 0.1439 | 0.1801 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2014 | 2014 | all_enrolments | Fail | 434 | 1582 | 0.2743 | 0.2529 | 0.2968 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| module_year | GGG 2014 | 2014 | all_enrolments | Withdrawn | 226 | 1582 | 0.1429 | 0.1265 | 0.161 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2013 | 2013 | all_enrolments | completion | 2095 | 4684 | 0.4473 | 0.4331 | 0.4615 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2013 | 2013 | all_enrolments | non_completion | 2589 | 4684 | 0.5527 | 0.5385 | 0.5669 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2013 | 2013 | all_enrolments | Pass | 1768 | 4684 | 0.3775 | 0.3637 | 0.3914 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2013 | 2013 | all_enrolments | Distinction | 327 | 4684 | 0.0698 | 0.0629 | 0.0775 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2013 | 2013 | all_enrolments | Fail | 1241 | 4684 | 0.2649 | 0.2525 | 0.2778 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2013 | 2013 | all_enrolments | Withdrawn | 1348 | 4684 | 0.2878 | 0.275 | 0.3009 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | B 2014 | 2014 | all_enrolments | completion | 3358 | 7804 | 0.4303 | 0.4193 | 0.4413 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2014 | 2014 | all_enrolments | non_completion | 4446 | 7804 | 0.5697 | 0.5587 | 0.5807 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2014 | 2014 | all_enrolments | Pass | 2574 | 7804 | 0.3298 | 0.3195 | 0.3403 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2014 | 2014 | all_enrolments | Distinction | 784 | 7804 | 0.1005 | 0.094 | 0.1073 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2014 | 2014 | all_enrolments | Fail | 1833 | 7804 | 0.2349 | 0.2256 | 0.2444 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | B 2014 | 2014 | all_enrolments | Withdrawn | 2613 | 7804 | 0.3348 | 0.3244 | 0.3454 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2013 | 2013 | all_enrolments | completion | 4475 | 8845 | 0.5059 | 0.4955 | 0.5164 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2013 | 2013 | all_enrolments | non_completion | 4370 | 8845 | 0.4941 | 0.4836 | 0.5045 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2013 | 2013 | all_enrolments | Pass | 3726 | 8845 | 0.4213 | 0.411 | 0.4316 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2013 | 2013 | all_enrolments | Distinction | 749 | 8845 | 0.0847 | 0.0791 | 0.0907 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2013 | 2013 | all_enrolments | Fail | 2001 | 8845 | 0.2262 | 0.2176 | 0.2351 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2013 | 2013 | all_enrolments | Withdrawn | 2369 | 8845 | 0.2678 | 0.2587 | 0.2772 | computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log) |
| start_month_year | J 2014 | 2014 | all_enrolments | completion | 5457 | 11260 | 0.4846 | 0.4754 | 0.4939 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2014 | 2014 | all_enrolments | non_completion | 5803 | 11260 | 0.5154 | 0.5061 | 0.5246 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2014 | 2014 | all_enrolments | Pass | 4293 | 11260 | 0.3813 | 0.3723 | 0.3903 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2014 | 2014 | all_enrolments | Distinction | 1164 | 11260 | 0.1034 | 0.0979 | 0.1091 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2014 | 2014 | all_enrolments | Fail | 1977 | 11260 | 0.1756 | 0.1687 | 0.1827 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |
| start_month_year | J 2014 | 2014 | all_enrolments | Withdrawn | 3826 | 11260 | 0.3398 | 0.3311 | 0.3486 | published in Milestone 3 (fig_outcome_by_run.csv); not recomputed |

**`aq1_year_difference_published.csv`.** Cross-check. The 2014 − 2013 difference over all enrolments from the published 2014 counts; equal to the all-enrolment rows of aq1_year_comparison_computed.csv.

| level | unit | measure | rate_2013 | n_2013 | rate_2014_published | n_2014 | diff_pp_2014_minus_2013 | ci_low_pp | ci_high_pp |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| year | all runs | non_completion | 0.5144 | 13529 | 0.5376 | 19064 | 2.32 | 1.22 | 3.42 |
| module_year | AAA | non_completion | 0.2742 | 383 | 0.3068 | 365 | 3.27 | -3.23 | 9.75 |
| module_year | BBB | non_completion | 0.5317 | 4004 | 0.5188 | 3905 | -1.29 | -3.49 | 0.91 |
| module_year | DDD | non_completion | 0.5869 | 3241 | 0.5807 | 3031 | -0.62 | -3.06 | 1.82 |
| module_year | EEE | non_completion | 0.4211 | 1052 | 0.4469 | 1882 | 2.58 | -1.17 | 6.29 |
| module_year | FFF | non_completion | 0.5183 | 3897 | 0.5418 | 3865 | 2.34 | 0.12 | 4.56 |
| module_year | GGG | non_completion | 0.3782 | 952 | 0.4172 | 1582 | 3.9 | -0.04 | 7.8 |
| start_month_year | B | non_completion | 0.5527 | 4684 | 0.5697 | 7804 | 1.7 | -0.1 | 3.5 |
| start_month_year | J | non_completion | 0.4941 | 8845 | 0.5154 | 11260 | 2.13 | 0.74 | 3.52 |

**`aq1_year_shared_modules_published.csv`.** Cross-check. The same difference restricted to the six modules that ran in both years, from the published counts (Wald interval).

| unit | rate_2013 | n_2013 | rate_2014_published | n_2014 | diff_pp_2014_minus_2013 | ci_low_pp | ci_high_pp |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| shared modules (6) | 0.5144 | 13529 | 0.5122 | 14630 | -0.22 | -1.39 | 0.95 |
| CCC (2014 only) |  | 0 | 0.6216 | 4434 |  |  |  |
