# Log: logs / report_tables

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:13:46Z |
| Finished (UTC) | 2026-11-12T16:13:47Z |
| Duration | 1.5 s |
| Command | `python common/report_tables.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


## aq-1

**AQ1 Table 1. Non-completion rate (Fail or Withdrawn) of enrolments registered at day 14, with Wilson 95% intervals**

| Level | Group | Enrolments | Non-completers | Rate | 95% interval |
| :---- | :---- | :---- | :---- | :---- | :---- |
| All runs | 22 runs | 28,061 | 12,700 | 45.3% | 44.7 to 45.8 |
| Year | 2013 | 12,076 | 5,515 | 45.7% | 44.8 to 46.6 |
| Year | 2014 | 15,985 | 7,185 | 44.9% | 44.2 to 45.7 |
| Start month | February (B) | 10,977 | 5,531 | 50.4% | 49.5 to 51.3 |
| Start month | October (J) | 17,084 | 7,169 | 42.0% | 41.2 to 42.7 |
| Module | AAA | 720 | 189 | 26.3% | 23.2 to 29.6 |
| Module | BBB | 6,537 | 2,797 | 42.8% | 41.6 to 44.0 |
| Module | CCC | 3,670 | 1,994 | 54.3% | 52.7 to 55.9 |
| Module | DDD | 5,401 | 2,796 | 51.8% | 50.4 to 53.1 |
| Module | EEE | 2,573 | 924 | 35.9% | 34.1 to 37.8 |
| Module | FFF | 6,713 | 3,067 | 45.7% | 44.5 to 46.9 |
| Module | GGG | 2,447 | 933 | 38.1% | 36.2 to 40.1 |

**AQ1 Table 2. Non-completion in 2014 minus 2013, percentage points with 95% interval, under two denominators**

| Denominator | Runs compared | Method | 2013 enrolments | 2013 rate | 2014 enrolments | 2014 rate | 2014 − 2013 (95% interval) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Registered at day 14 | all runs (9 of 2013, 13 of 2014) | pooled | 12,076 | 45.7% | 15,985 | 44.9% | −0.7 (−1.9 to +0.5) |
| Registered at day 14 | 6 modules run in both years | pooled | 12,076 | 45.7% | 12,315 | 42.2% | −3.5 (−4.8 to −2.3) |
| Registered at day 14 | 9 module × start-month pairs run in both years | pooled | 12,076 | 45.7% | 10,900 | 42.3% | −3.4 (−4.6 to −2.1) |
| Registered at day 14 | 9 module × start-month pairs run in both years | weighted over the pairs | 12,076 | 45.7% | 10,900 | 42.3% | −3.1 (−4.3 to −1.8) |
| All enrolments | all runs (9 of 2013, 13 of 2014) | pooled | 13,529 | 51.4% | 19,064 | 53.8% | +2.3 (+1.2 to +3.4) |
| All enrolments | 6 modules run in both years | pooled | 13,529 | 51.4% | 14,630 | 51.2% | −0.2 (−1.4 to +0.9) |
| All enrolments | 9 module × start-month pairs run in both years | pooled | 13,529 | 51.4% | 13,103 | 51.9% | +0.5 (−0.7 to +1.7) |
| All enrolments | 9 module × start-month pairs run in both years | weighted over the pairs | 13,529 | 51.4% | 13,103 | 51.9% | +0.5 (−0.7 to +1.7) |

**AQ1 Table 3. The year difference by module and by start month (2013 / 2014)**

| Group | Registered at day 14: enrolments | Rate | 2014 − 2013 (95% interval) | All enrolments: enrolments | Rate | 2014 − 2013 (95% interval) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 370 / 350 | 24.9% / 27.7% | +2.8 (−3.6 to +9.3) | 383 / 365 | 27.4% / 30.7% | +3.3 (−3.2 to +9.8) |
| BBB | 3,457 / 3,080 | 45.8% / 39.4% | −6.5 (−8.9 to −4.1) | 4,004 / 3,905 | 53.2% / 51.9% | −1.3 (−3.5 to +0.9) |
| DDD | 2,872 / 2,529 | 53.5% / 49.8% | −3.7 (−6.4 to −1.1) | 3,241 / 3,031 | 58.7% / 58.1% | −0.6 (−3.1 to +1.8) |
| EEE | 933 / 1,640 | 34.8% / 36.5% | +1.7 (−2.2 to +5.5) | 1,052 / 1,882 | 42.1% / 44.7% | +2.6 (−1.2 to +6.3) |
| FFF | 3,518 / 3,195 | 46.7% / 44.6% | −2.1 (−4.5 to +0.3) | 3,897 / 3,865 | 51.8% / 54.2% | +2.3 (+0.1 to +4.6) |
| GGG | 926 / 1,521 | 36.1% / 39.4% | +3.3 (−0.7 to +7.2) | 952 / 1,582 | 37.8% / 41.7% | +3.9 (+0.0 to +7.8) |
| February runs, modules run in both years | 4,323 / 5,063 | 51.6% / 46.8% | −4.8 (−6.8 to −2.7) | 4,684 / 5,868 | 55.3% / 54.1% | −1.2 (−3.1 to +0.7) |
| October runs, modules run in both years | 7,753 / 7,252 | 42.4% / 38.9% | −3.5 (−5.1 to −1.9) | 8,845 / 8,762 | 49.4% / 49.3% | −0.1 (−1.6 to +1.4) |
| February runs, all modules | 4,323 / 6,654 | 51.6% / 49.6% | −2.0 (−3.9 to −0.1) | 4,684 / 7,804 | 55.3% / 57.0% | +1.7 (−0.1 to +3.5) |
| October runs, all modules | 7,753 / 9,331 | 42.4% / 41.6% | −0.7 (−2.2 to +0.8) | 8,845 / 11,260 | 49.4% / 51.5% | +2.1 (+0.7 to +3.5) |

**AQ1 Table 4. Enrolments not registered at day 14, by year**

| Runs compared | 2013 | 2014 | 2014 − 2013 (95% interval) | Of these, Fail or Withdrawn (2013 / 2014) |
| :---- | :---- | :---- | :---- | :---- |
| all runs | 1,453 of 13,529 (10.7%) | 3,079 of 19,064 (16.2%) | +5.4 (+4.7 to +6.1) | 99.4% / 99.5% |
| 6 modules run in both years | 1,453 of 13,529 (10.7%) | 2,315 of 14,630 (15.8%) | +5.1 (+4.3 to +5.9) | 99.4% / 99.4% |
| 9 module × start-month pairs run in both years | 1,453 of 13,529 (10.7%) | 2,203 of 13,103 (16.8%) | +6.1 (+5.2 to +6.9) | 99.4% / 99.4% |

**AQ1 Table 5. Outcome shares by module, KPI population**

| Module | Enrolments | Distinction | Pass | Fail | Withdrawn |
| :---- | :---- | :---- | :---- | :---- | :---- |
| All runs | 28,061 | 10.8% | 44.0% | 25.0% | 20.2% |
| AAA | 720 | 6.1% | 67.6% | 12.4% | 13.9% |
| BBB | 6,537 | 10.3% | 46.9% | 26.9% | 15.9% |
| CCC | 3,670 | 13.6% | 32.1% | 21.3% | 33.1% |
| DDD | 5,401 | 7.1% | 41.1% | 26.1% | 25.7% |
| EEE | 2,573 | 13.8% | 50.3% | 21.8% | 14.1% |
| FFF | 6,713 | 10.0% | 44.3% | 25.4% | 20.3% |
| GGG | 2,447 | 16.2% | 45.7% | 29.7% | 8.4% |

**AQ1 Table 6. The same rate under three denominators**

| Denominator | Enrolments | Non-completers | Rate |
| :---- | :---- | :---- | :---- |
| KPI (registered at day 14) | 28,061 | 12,700 | 45.3% |
| all enrolments | 32,593 | 17,208 | 52.8% |
| KPI without flagged | 27,962 | 12,602 | 45.1% |

**AQ1 Table 7. First assessed task (TMA or CMA) due while enrolled and not submitted, KPI population**

| Final result | Enrolments | Ever missed a task | Median week of the first miss | Missed by week 4 | By week 8 | By week 12 | By week 20 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Non-completers (Fail or Withdrawn) | 12,700 | 75.1% | 9 | 16.8% | 35.1% | 43.0% | 61.9% |
| – Fail | 7,027 | 82.8% | 12 | 15.0% | 33.5% | 42.4% | 63.6% |
| – Withdrawn | 5,673 | 65.5% | 8 | 19.0% | 37.1% | 43.6% | 59.8% |
| Completers (Pass or Distinction) | 15,361 | 20.5% | 24 | 0.5% | 3.8% | 4.7% | 8.1% |

**AQ1 Table 8. Non-completers with a missed task by the end of week 4**

| Runs | Year | Number of runs | Non-completers | Missed a task by week 4 | Share | 95% interval |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| All runs | Both years | 22 | 12,700 | 2,133 | 16.8% | 16.2 to 17.5 |
| All runs | 2013 | 9 | 5,515 | 1,080 | 19.6% | 18.6 to 20.7 |
| All runs | 2014 | 13 | 7,185 | 1,053 | 14.7% | 13.9 to 15.5 |
| Runs with a task due by day 27 | Both years | 16 | 10,843 | 2,133 | 19.7% | 18.9 to 20.4 |
| Runs with a task due by day 27 | 2013 | 7 | 4,856 | 1,080 | 22.2% | 21.1 to 23.4 |
| Runs with a task due by day 27 | 2014 | 9 | 5,987 | 1,053 | 17.6% | 16.6 to 18.6 |

**AQ1 Table 9. Non-completers by module: when the first missed task appears**

| Module | Runs with a task due by day 27 | Non-completers | Ever missed a task | Median week of the first miss | Missed by week 4 | Missed by week 8 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 2 of 2 | 189 | 60.3% | 12.5 | 12.2% | 30.2% |
| BBB | 4 of 4 | 2,797 | 79.5% | 8 | 21.2% | 42.3% |
| CCC | 2 of 2 | 1,994 | 72.5% | 5 | 20.4% | 44.7% |
| DDD | 4 of 4 | 2,796 | 71.2% | 8 | 21.2% | 36.6% |
| EEE | 0 of 3 | 924 | 75.3% | 10 | no task due by day 27 | 28.1% |
| FFF | 4 of 4 | 3,067 | 75.3% | 13 | 16.9% | 34.0% |
| GGG | 0 of 3 | 933 | 80.7% | 17 | no task due by day 27 | 0.0% |

**AQ1 Table 10. Non-completion by audit attribute, KPI population**

| Attribute | Group | Enrolments | Rate | 95% interval |
| :---- | :---- | :---- | :---- | :---- |
| Gender | Female | 12,573 | 43.4% | 42.6 to 44.3 |
| Gender | Male | 15,488 | 46.7% | 45.9 to 47.5 |
| Disability | Not declared | 25,385 | 44.2% | 43.6 to 44.9 |
| Disability | Declared | 2,676 | 54.9% | 53.0 to 56.8 |
| Deprivation band | 0–10% (most deprived) | 2,708 | 57.1% | 55.2 to 58.9 |
| Deprivation band | 40–50% | 2,773 | 45.3% | 43.5 to 47.2 |
| Deprivation band | 90–100% (least deprived) | 2,268 | 35.7% | 33.7 to 37.7 |
| Deprivation band | Missing | 1,037 | 29.9% | 27.2 to 32.8 |
| Age band | 0–35 | 19,580 | 47.3% | 46.6 to 48.0 |
| Age band | 35–55 | 8,283 | 40.7% | 39.7 to 41.8 |
| Age band | 55 or over | 198 | 32.8% | 26.7 to 39.6 |


## aq-2

**AQ2 Table 1. Risk difference in non-completion per sign, 9 runs of 2013, enrolments registered at day 27**

| Sign at day 27 | n (rows averaged over) | Students with the sign | Non-completion with / without | Unadjusted difference (95% interval) | Adjusted difference (95% interval) | Odds ratio (95% interval) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task due and not submitted | 9,960 | 1,285 (12.9%) | 90.0% / 39.6% | +50.3 (48.3 to 52.2) | **+40.7** (37.5 to 43.8) | 7.5 (6.1 to 9.1) |
| TMA submitted late | 9,960 | 577 (5.8%) | 63.6% / 45.1% | +18.5 (14.4 to 22.5) | **+21.7** (17.4 to 25.9) | 2.9 (2.4 to 3.5) |
| Clicks below half the run median | 11,811 | 3,175 (26.9%) | 67.8% / 35.8% | +32.1 (30.1 to 33.9) | **+14.7** (12.3 to 17.0) | 1.9 (1.8 to 2.2) |
| No platform activity in the last 7 days | 11,811 | 2,444 (20.7%) | 64.4% / 39.2% | +25.3 (23.1 to 27.4) | **+13.5** (10.1 to 16.8) | 1.7 (1.5 to 1.9) |
| No activity before the start | 11,811 | 2,297 (19.4%) | 61.5% / 40.3% | +21.2 (19.0 to 23.4) | **+11.3** (8.5 to 14.0) | 1.6 (1.4 to 1.8) |

**AQ2 Table 2. Adjusted risk difference by module, 2013 runs (percentage points, 95% interval, n)**

| Sign | AAA | BBB | DDD | EEE | FFF | GGG | Same direction (point estimate) | Same direction, interval excludes 0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task missed | +44 (22 to 65; n = 369) | +45 (40 to 50; n = 3,364) | +35 (30 to 40; n = 2,790) | not defined | +41 (35 to 47; n = 3,437) | not defined | 4 of 4 | 4 of 4 |
| TMA late | +20 (6 to 33; n = 369) | +22 (17 to 28; n = 3,364) | +17 (6 to 28; n = 2,790) | not defined | +25 (19 to 31; n = 3,437) | not defined | 4 of 4 | 4 of 4 |
| Low activity | +14 (1 to 27; n = 369) | +11 (7 to 15; n = 3,364) | +16 (11 to 21; n = 2,790) | +35 (25 to 44; n = 927) | +12 (8 to 17; n = 3,437) | +13 (5 to 21; n = 924) | 6 of 6 | 6 of 6 |
| Inactive last 7 days | *+5 (−8 to 18; n = 369)* | +9 (4 to 13; n = 3,364) | +19 (9 to 29; n = 2,790) | +19 (10 to 29; n = 927) | +15 (9 to 21; n = 3,437) | *+4 (−3 to 11; n = 924)* | 6 of 6 | 4 of 6 |
| No pre-start activity | *+9 (−9 to 27; n = 369)* | +8 (4 to 12; n = 3,364) | +14 (7 to 20; n = 2,790) | +16 (8 to 24; n = 927) | +13 (7 to 19; n = 3,437) | *+5 (−2 to 11; n = 924)* | 6 of 6 | 4 of 6 |

**AQ2 Table 1b. Risk difference in non-completion per sign, 13 runs of 2014, enrolments registered at day 27**

| Sign at day 27 | n (rows averaged over) | Students with the sign | Non-completion with / without | Unadjusted difference (95% interval) | Adjusted difference (95% interval) | Odds ratio (95% interval) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task due and not submitted | 12,585 | 1,368 (10.9%) | 89.0% / 40.3% | +48.8 (46.8 to 50.6) | **+39.6** (36.8 to 42.5) | 6.6 (5.5 to 7.9) |
| TMA submitted late | 9,064 | 429 (4.7%) | 59.4% / 42.1% | +17.3 (12.5 to 22.0) | **+22.5** (17.9 to 27.2) | 2.7 (2.2 to 3.3) |
| Clicks below half the run median | 15,724 | 4,099 (26.1%) | 66.3% / 36.1% | +30.2 (28.5 to 31.9) | **+14.8** (12.7 to 16.8) | 1.9 (1.8 to 2.1) |
| No platform activity in the last 7 days | 15,724 | 3,440 (21.9%) | 64.7% / 38.1% | +26.5 (24.7 to 28.3) | **+15.4** (12.8 to 18.1) | 2.0 (1.8 to 2.2) |
| No activity before the start | 15,724 | 3,161 (20.1%) | 58.3% / 40.3% | +17.9 (16.0 to 19.8) | **+9.2** (6.9 to 11.4) | 1.5 (1.4 to 1.7) |

**AQ2 Table 2b. Adjusted risk difference by module, 2014 runs (percentage points, 95% interval, n)**

| Sign | AAA | BBB | CCC | DDD | EEE | FFF | GGG | Same direction (point estimate) | Same direction, interval excludes 0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Task missed | +41 (24 to 59; n = 348) | +53 (48 to 59; n = 3,066) | +35 (30 to 40; n = 3,521) | +37 (30 to 43; n = 2,492) | not defined | +33 (27 to 40; n = 3,158) | not defined | 5 of 5 | 5 of 5 |
| TMA late | *+0 (−13 to 13; n = 348)* | +26 (19 to 33; n = 3,066) | not defined | +21 (12 to 29; n = 2,492) | not defined | +23 (14 to 33; n = 3,158) | not defined | 4 of 4 | 3 of 4 |
| Low activity | *+1 (−10 to 11; n = 348)* | +7 (3 to 12; n = 3,066) | +9 (4 to 13; n = 3,521) | +18 (12 to 23; n = 2,492) | +29 (22 to 36; n = 1,625) | +21 (16 to 25; n = 3,158) | +15 (9 to 21; n = 1,514) | 7 of 7 | 6 of 7 |
| Inactive last 7 days | +16 (3 to 30; n = 348) | +12 (8 to 17; n = 3,066) | +19 (15 to 23; n = 3,521) | +14 (7 to 22; n = 2,492) | +14 (6 to 21; n = 1,625) | +17 (8 to 25; n = 3,158) | +15 (9 to 20; n = 1,514) | 7 of 7 | 7 of 7 |
| No pre-start activity | *+10 (−9 to 29; n = 348)* | *+1 (−2 to 5; n = 3,066)* | +13 (8 to 18; n = 3,521) | *+6 (−1 to 13; n = 2,492)* | +22 (16 to 29; n = 1,625) | +9 (4 to 14; n = 3,158) | +7 (2 to 12; n = 1,514) | 7 of 7 | 4 of 7 |

**AQ2 Table 3. Adjusted risk difference per sign, estimation and replication**

| Sign | 2013 runs | 2014 runs | Change 2014 − 2013 (95% interval) | Level 1 criterion (2013 / 2014) | Counting only modules whose interval excludes 0 (2013 / 2014) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Task missed | +40.7 (37.5 to 43.8), n = 9,960 | +39.6 (36.8 to 42.5), n = 12,585 | −1.0 (−5.2 to +3.2) | Consistent / Consistent | Consistent / Consistent |
| TMA late | +21.7 (17.4 to 25.9), n = 9,960 | +22.5 (17.9 to 27.2), n = 9,064 | +0.9 (−5.4 to +7.2) | Consistent / Consistent | Consistent / Consistent |
| Low activity | +14.7 (12.3 to 17.0), n = 11,811 | +14.8 (12.7 to 16.8), n = 15,724 | +0.1 (−3.0 to +3.2) | Consistent / Consistent | Consistent / Consistent |
| Inactive last 7 days | +13.5 (10.1 to 16.8), n = 11,811 | +15.4 (12.8 to 18.1), n = 15,724 | +1.9 (−2.3 to +6.2) | Consistent / Consistent | Consistent / Consistent |
| No pre-start activity | +11.3 (8.5 to 14.0), n = 11,811 | +9.2 (6.9 to 11.4), n = 15,724 | −2.1 (−5.7 to +1.5) | Consistent / Consistent | Consistent / Weak or inconsistent |

**AQ2 Table 4. Sensitivity of the adjusted risk differences, 2013 runs (percentage points; n = rows averaged over)**

| Variant | Task missed | TMA late | Low activity | Inactive last 7 days | No pre-start activity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Main model | 40.7 (n = 9,960) | 21.7 (n = 9,960) | 14.7 (n = 11,811) | 13.5 (n = 11,811) | 11.3 (n = 11,811) |
| Low activity from de-duplicated clicks | 40.6 (n = 9,960) | 21.6 (n = 9,960) | 14.8 (n = 11,811) | 13.5 (n = 11,811) | 11.2 (n = 11,811) |
| Late CMAs also count as late | 40.6 (n = 9,960) | 16.7 (n = 9,960) | 14.7 (n = 11,811) | 13.4 (n = 11,811) | 11.3 (n = 11,811) |
| Without flagged enrolments | 40.7 (n = 9,954) | 21.7 (n = 9,954) | 14.6 (n = 11,803) | 13.5 (n = 11,803) | 11.3 (n = 11,803) |
| Only the runs with a task due by day 27 | 40.6 (n = 9,960) | 21.6 (n = 9,960) | 12.9 (n = 9,960) | 13.8 (n = 9,960) | 11.4 (n = 9,960) |
| Low activity = below a quarter of the run median | 41.4 (n = 9,960) | 22.4 (n = 9,960) | 14.4 (n = 11,811) | 15.4 (n = 11,811) | 12.0 (n = 11,811) |
| Low activity = below the run median (the Milestone 5 cut) | 40.9 (n = 9,960) | 20.3 (n = 9,960) | 13.4 (n = 11,811) | 14.3 (n = 11,811) | 10.6 (n = 11,811) |
| Post hoc: plus log(1 + clicks on days 0–27) | 37.3 (n = 9,960) | 20.4 (n = 9,960) | **2.9 (n = 11,811): criterion not met** | 8.7 (n = 11,811) | 9.1 (n = 11,811) |
| Post hoc: low activity = below the run median, plus log(1 + clicks) | 37.4 (n = 9,960) | 19.6 (n = 9,960) | 5.9 (n = 11,811) | 9.2 (n = 11,811) | 8.9 (n = 11,811) |

**AQ2 Table 4b. Sensitivity of the adjusted risk differences, 2014 runs (percentage points; n = rows averaged over)**

| Variant | Task missed | TMA late | Low activity | Inactive last 7 days | No pre-start activity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Main model | 39.6 (n = 12,585) | 22.5 (n = 9,064) | 14.8 (n = 15,724) | 15.4 (n = 15,724) | 9.2 (n = 15,724) |
| Low activity from de-duplicated clicks | 39.8 (n = 12,585) | 22.6 (n = 9,064) | 14.6 (n = 15,724) | 15.5 (n = 15,724) | 9.1 (n = 15,724) |
| Late CMAs also count as late | 40.9 (n = 12,585) | 18.3 (n = 12,585) | 14.8 (n = 15,724) | 15.4 (n = 15,724) | 9.2 (n = 15,724) |
| Without flagged enrolments | 39.3 (n = 12,499) | 22.6 (n = 9,007) | 14.8 (n = 15,632) | 15.1 (n = 15,632) | 9.2 (n = 15,632) |
| Only the runs with a task due by day 27 | 39.7 (n = 12,585) | 22.5 (n = 9,064) | 12.7 (n = 12,585) | 15.7 (n = 12,585) | 7.6 (n = 12,585) |
| Low activity = below a quarter of the run median | 40.4 (n = 12,585) | 23.8 (n = 9,064) | 15.2 (n = 15,724) | 17.0 (n = 15,724) | 9.9 (n = 15,724) |
| Low activity = below the run median (the Milestone 5 cut) | 39.3 (n = 12,585) | 21.8 (n = 9,064) | 14.6 (n = 15,724) | 15.7 (n = 15,724) | 8.6 (n = 15,724) |
| Post hoc: plus log(1 + clicks on days 0–27) | 35.8 (n = 12,585) | 21.2 (n = 9,064) | **0.8 (n = 15,724): criterion not met** | 10.2 (n = 15,724) | 6.5 (n = 15,724) |
| Post hoc: low activity = below the run median, plus log(1 + clicks) | 35.7 (n = 12,585) | 21.0 (n = 9,064) | **5.9 (n = 15,724): criterion not met** | 10.7 (n = 15,724) | 6.5 (n = 15,724) |

**AQ2 Table 6. Each sign against the Level 1 criterion when clicks on days 0–27 enter as a continuous adjustment (post hoc)**

| Low-activity cut in the model | Sign | 2013: adjusted difference (95% interval) | 2013: modules, same direction | 2013: criterion | 2014: adjusted difference (95% interval) | 2014: modules, same direction | 2014: criterion |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Half the run median (primary) | Task missed | +37.3 (33.8 to 40.8) | 4 of 4 | Consistent | +35.8 (32.7 to 39.0) | 5 of 5 | Consistent |
| Half the run median (primary) | TMA late | +20.4 (16.1 to 24.6) | 4 of 4 | Consistent | +21.2 (16.5 to 26.0) | 3 of 4 | Consistent |
| Half the run median (primary) | Inactive last 7 days | +8.7 (5.1 to 12.2) | 5 of 6 | Consistent | +10.2 (7.5 to 13.0) | 7 of 7 | Consistent |
| Half the run median (primary) | Low activity (below half the run median) | +2.9 (−0.2 to 6.0) | 4 of 6 | Weak or inconsistent | +0.8 (−1.9 to 3.4) | 3 of 7 | Weak or inconsistent |
| Half the run median (primary) | No pre-start activity | +9.1 (6.3 to 11.9) | 6 of 6 | Consistent | +6.5 (4.3 to 8.8) | 6 of 7 | Consistent |
| Run median | Task missed | +37.4 (33.9 to 40.9) | 4 of 4 | Consistent | +35.7 (32.5 to 38.9) | 5 of 5 | Consistent |
| Run median | TMA late | +19.6 (15.3 to 23.9) | 4 of 4 | Consistent | +21.0 (16.2 to 25.8) | 3 of 4 | Consistent |
| Run median | Inactive last 7 days | +9.2 (5.8 to 12.7) | 6 of 6 | Consistent | +10.7 (8.0 to 13.3) | 7 of 7 | Consistent |
| Run median | Low activity (below the run median) | +5.9 (3.4 to 8.3) | 5 of 6 | Consistent | +5.9 (3.8 to 8.1) | 4 of 7 | Weak or inconsistent |
| Run median | No pre-start activity | +8.9 (6.1 to 11.6) | 6 of 6 | Consistent | +6.5 (4.2 to 8.7) | 6 of 7 | Consistent |

**AQ2 Table 5. Binned residuals by activity level on days 0–27: observed minus predicted non-completion (percentage points; band = ±2 standard errors; bold = outside the band)**

| Model | Activity level | 2013: enrolments | 2013: observed / predicted | 2013: residual (band) | 2014: enrolments | 2014: observed / predicted | 2014: residual (band) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Main model | No click | 607 | 81.1% / 77.5% | **+3.6 (±2.9)** | 624 | 82.2% / 79.3% | +2.9 (±2.9) |
| Main model | Below half the run median | 2,568 | 64.7% / 65.6% | −0.9 (±1.7) | 3,475 | 63.5% / 64.0% | −0.5 (±1.5) |
| Main model | Half the median to the median | 2,714 | 46.7% / 39.6% | **+7.0 (±1.8)** | 3,734 | 47.8% / 39.9% | **+7.9 (±1.5)** |
| Main model | Median to twice the median | 3,447 | 33.4% / 34.9% | −1.5 (±1.6) | 4,660 | 34.9% / 35.1% | −0.2 (±1.4) |
| Main model | Twice the median or more | 2,475 | 27.2% / 32.8% | **−5.7 (±1.8)** | 3,231 | 24.2% / 33.0% | **−8.8 (±1.6)** |
| Post hoc: plus log(1 + clicks) | No click | 607 | 81.1% / 82.8% | −1.8 (±2.7) | 624 | 82.2% / 86.8% | **−4.6 (±2.5)** |
| Post hoc: plus log(1 + clicks) | Below half the run median | 2,568 | 64.7% / 64.3% | +0.4 (±1.7) | 3,475 | 63.5% / 62.6% | +0.8 (±1.5) |
| Post hoc: plus log(1 + clicks) | Half the median to the median | 2,714 | 46.7% / 43.5% | **+3.2 (±1.8)** | 3,734 | 47.8% / 44.6% | **+3.2 (±1.6)** |
| Post hoc: plus log(1 + clicks) | Median to twice the median | 3,447 | 33.4% / 35.1% | **−1.6 (±1.6)** | 4,660 | 34.9% / 35.2% | −0.3 (±1.4) |
| Post hoc: plus log(1 + clicks) | Twice the median or more | 2,475 | 27.2% / 28.4% | −1.3 (±1.8) | 3,231 | 24.2% / 27.5% | **−3.3 (±1.5)** |

**AQ2 Table 7. Adjusted risk difference by student group, 2013 runs (percentage points; n = rows of the group averaged over)**

| Group | Task missed | TMA late | Low activity | Inactive last 7 days | No pre-start activity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Women | 42.3 (n = 4,852) | 21.6 (n = 4,852) | 12.8 (n = 5,697) | 11.1 (n = 5,697) | 9.5 (n = 5,697) |
| Men | 39.1 (n = 5,108) | 21.7 (n = 5,108) | 16.3 (n = 6,114) | 15.7 (n = 6,114) | 12.9 (n = 6,114) |
| No declared disability | 40.7 (n = 9,004) | 21.8 (n = 9,004) | 14.8 (n = 10,688) | 13.5 (n = 10,688) | 11.3 (n = 10,688) |
| Declared disability | 40.0 (n = 956) | 20.7 (n = 956) | 13.8 (n = 1,123) | 12.9 (n = 1,123) | 10.7 (n = 1,123) |
| Deprivation 0–30% (most deprived) | 40.2 (n = 3,132) | 21.2 (n = 3,132) | 13.8 (n = 3,690) | 12.7 (n = 3,690) | 10.7 (n = 3,690) |
| Deprivation 30–70% | 40.8 (n = 3,936) | 21.7 (n = 3,936) | 14.7 (n = 4,684) | 13.4 (n = 4,684) | 11.2 (n = 4,684) |
| Deprivation 70–100% (least deprived) | 41.1 (n = 2,527) | 22.1 (n = 2,527) | 15.4 (n = 3,019) | 14.1 (n = 3,019) | 11.8 (n = 3,019) |
| Deprivation band missing | 40.9 (n = 365) | 22.8 (n = 365) | 16.6 (n = 418) | 16.6 (n = 418) | 13.5 (n = 418) |


## aq-3

**AQ3 Table 2. All rankings on the test runs, day 27, 5 per 20**

| Ranking | Pooled normalised recall | Lift over the base rate | ROC-AUC within run | Difference to M1 (95% interval) |
| :---- | :---- | :---- | :---- | :---- |
| Random list (expected) | 0.439 | 1.00 | 0.500 | – |
| B3 background-only logistic model | 0.567 | 1.29 | 0.603 | −0.158 (−0.186 to −0.132) |
| B2 early-sign rule, ranked | 0.704 | 1.60 | 0.711 | −0.021 (−0.036 to −0.007) |
| **M1 penalised logistic regression, primary set (chosen)** | **0.726** | **1.65** | **0.730** | – |
| M2 penalised logistic regression, extended set | 0.726 | 1.65 | 0.734 | +0.001 (−0.009 to +0.009) |
| M3 gradient-boosted trees, primary set | 0.723 | 1.65 | 0.730 | −0.003 (−0.012 to +0.010) |
| M4 gradient-boosted trees, extended set | 0.728 | 1.66 | 0.732 | +0.003 (−0.008 to +0.015) |

**AQ3 Table 3. Recall by activity level and history, day 27, 5 per 20 (share of the group's non-completers who are listed)**

| Group at day 27 | Enrolments | Non-completers | Model recall | Rule recall |
| :---- | :---- | :---- | :---- | :---- |
| No clicks since the start | 624 | 513 | 98.4% | 100.0% |
| Low activity (below half the run median) | 3,475 | 2,205 | 70.9% | 73.3% |
| Normal activity | 11,625 | 4,193 | 19.1% | 15.6% |
| First attempt at the module | 13,865 | 5,801 | 37.0% | 37.9% |
| Repeat attempt | 1,859 | 1,110 | 65.3% | 53.0% |
| Registered after the start | 152 | 65 | 73.8% | 53.8% |
| Final result Fail | 3,805 | 3,805 | 43.2% | 41.9% |
| Final result Withdrawn | 3,106 | 3,106 | 39.5% | 38.3% |

**AQ3 Table 4. Calibration of the frozen M1 at day 27 (no recalibration on any 2014 row)**

| Scope | Calibration-in-the-large (target 0) | Slope (target 1) | Mean predicted | Observed |
| :---- | :---- | :---- | :---- | :---- |
| All 13 test runs (S3) | +0.124 | 0.873 | 41.5% | 44.0% |
| CCC-2014B (module absent from training) | +1.142 | 1.014 | 34.1% | 55.8% |
| CCC-2014J | +0.743 | 0.923 | 34.9% | 49.8% |
| Runs outside ±0.2 | 5 of 13 (BBB-2014B, CCC-2014B, CCC-2014J, FFF-2014J, GGG-2014J) |  |  |  |
| Declared disability | +0.386 | 0.881 | 46.2% | 54.0% |
| Deprivation band 0–10% | +0.363 | 0.840 | 45.7% | 53.0% |

**AQ3 Table 5. Sensitivity of the model-minus-rule difference (none of these can change the S1 verdict)**

| Variant | Runs | Model | Rule | Difference (95% interval) | Wins / ties / losses |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Main: all runs, day 27, 5 per 20 | 13 | 0.726 | 0.704 | +0.021 (+0.007 to +0.036) | 11 / 0 / 2 |
| Paired runs (module and start month also ran in 2013) | 9 | 0.708 | 0.683 | +0.025 (+0.008 to +0.042) | 8 / 0 / 1 |
| Unpaired runs (CCC-B, CCC-J, EEE-B, GGG-B) | 4 | 0.765 | 0.752 | +0.014 (−0.013 to +0.036) | 3 / 0 / 1 |
| Module CCC only | 2 | 0.802 | 0.783 | +0.019 (−0.006 to +0.046) | 2 / 0 / 0 |
| Without module CCC | 11 | 0.704 | 0.682 | +0.022 (+0.005 to +0.039) | 9 / 0 / 2 |
| Without test enrolments of students seen in 2013 | 13 | 0.702 | 0.681 | +0.021 (+0.006 to +0.037) | 11 / 0 / 2 |
| Without Withdrawn enrolments lacking a withdrawal day | 13 | 0.718 | 0.697 | +0.021 (+0.007 to +0.035) | 11 / 1 / 1 |
| Rule variant that also counts late CMAs | 13 | 0.726 | 0.700 | +0.026 (+0.010 to +0.043) | 11 / 0 / 2 |
| Labels-available: February runs, trained on 2013 February runs only | 6 | 0.782 | 0.762 | +0.020 (+0.002 to +0.035) | 5 / 1 / 0 |
| Same February runs, model trained on all 2013 runs | 6 | 0.778 | 0.762 | +0.016 (−0.004 to +0.034) | 5 / 0 / 1 |
| Day 27, 3 per 20 | 13 | 0.810 | 0.778 | +0.032 (+0.006 to +0.055) | 11 / 0 / 2 |
| Day 13, 5 per 20 | 13 | 0.688 | 0.667 | +0.021 (+0.002 to +0.036) | 9 / 0 / 4 |
| Day 13, 3 per 20 | 13 | 0.742 | 0.707 | +0.035 (+0.008 to +0.059) | 9 / 1 / 3 |

**AQ3 Table 6. Model choice on the 9 development folds of 2013 (day 27, 5 per 20)**

| Configuration | Pooled normalised recall | Gain over M1 | Folds with a gain over M1 | Choice |
| :---- | :---- | :---- | :---- | :---- |
| B3 | 0.568 | −0.182 | 0 of 9 |  |
| M1 | 0.750 | – | – | chosen |
| M2 | 0.749 | −0.001 | 3 of 9 |  |
| M3 | 0.749 | −0.002 | 5 of 9 |  |
| M4 | 0.748 | −0.002 | 3 of 9 |  |


## aq-4

**AQ4 Table 1. List quality on the 13 test runs of 2014**

| Cut-off and capacity | List places | Ranking | Non-completers listed | Recall | Ceiling of recall | Normalised recall | Precision | Lift |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Day 27, 5 per 20 (main) | 3,955 | Model | 2,870 | 41.5% | 57.2% | 0.726 | 72.6% | 1.65 |
|  |  | Rule | 2,786 | 40.3% | 57.2% | 0.704 | 70.4% | 1.60 |
|  |  | Random (expected) | 1,738 | 25.1% | 57.2% | 0.439 | 43.9% | 1.00 |
| Day 27, 3 per 20 | 2,373 | Model | 1,922 | 27.8% | 34.3% | 0.810 | 81.0% | 1.84 |
|  |  | Rule | 1,846 | 26.7% | 34.3% | 0.778 | 77.8% | 1.77 |
|  |  | Random (expected) | 1,043 | 15.1% | 34.3% | 0.439 | 43.9% | 1.00 |
| Day 13, 5 per 20 | 4,030 | Model | 2,771 | 38.5% | 56.1% | 0.688 | 68.8% | 1.53 |
|  |  | Rule | 2,688 | 37.4% | 56.1% | 0.667 | 66.7% | 1.48 |
| Day 13, 3 per 20 | 2,418 | Model | 1,795 | 25.0% | 33.6% | 0.742 | 74.2% | 1.65 |
|  |  | Rule | 1,710 | 23.8% | 33.6% | 0.707 | 70.7% | 1.57 |

**AQ4 Table 2. Non-completion by tier of the model list, day 27**

| Tier | Enrolments | Did not complete | Withdrawn | Failed |
| :---- | :---- | :---- | :---- | :---- |
| Tier 1 (top 3 per 20) | 2,373 | 81.0% (1,922) | 812 | 1,110 |
| Tier 2 (next 2 per 20) | 1,582 | 59.9% (948) | 414 | 534 |
| Not listed | 11,769 | 34.3% (4,041) | 1,880 | 2,161 |

**AQ4 Table 3. First reason of the listed students, day 27, 5 per 20**

| First reason | Listed students | Share of the list | Did not complete |
| :---- | :---- | :---- | :---- |
| Few active days since the start | 1,500 | 37.9% | 64.4% |
| Task due and not submitted | 1,362 | 34.4% | 89.0% |
| Lower prior education | 572 | 14.5% | 64.9% |
| TMA submitted late | 292 | 7.4% | 62.0% |
| Previous attempt at the module | 94 | 2.4% | 60.6% |
| Other reasons together | 135 | 3.4% | – |

**AQ4 Table 4. Confirmatory check FR1, model list, day 27, 5 per 20 (5,000 two-level bootstrap replicates)**

| Group | Test enrolments | Non-completers | Recall of the group | Recall of the others | Gap (95% interval) | Holm-adjusted p | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Declared disability | 1,488 | 803 | 46.3% | 40.9% | +5.4 points (+0.4 to +9.8) | 1.00 | Not flagged |
| Deprivation band 0–10% | 1,486 | 787 | 42.6% | 41.4% | +1.2 points (−5.0 to +6.3) | 1.00 | Not flagged |
| Deprivation band missing | 610 | 181 | 34.8% | 41.7% | −6.9 points (−16.8 to +2.4) | 0.20 | Not flagged |
| Age 55 or over (below 400 enrolments) | 118 | 42 | 26.2% | 41.6% | −15.4 points (−32.8 to +9.2) | – | Insufficient data, not cleared |

**AQ4 Table 5. Descriptive checks by group, model list, day 27, 5 per 20**

| Group | Non-completion rate | Share listed | Recall | Precision | Calibration-in-the-large |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Female | 41.3% | 23.9% | 38.7% | 66.8% | +0.03 |
| Male | 45.9% | 26.1% | 43.4% | 76.5% | +0.20 |
| No declared disability | 42.9% | 24.4% | 40.9% | 71.9% | – |
| Declared disability | 54.0% | 32.5% | 46.3% | 77.0% | +0.39 |
| Deprivation band 0–10% | 53.0% | 29.5% | 42.6% | 76.3% | +0.36 |
| Deprivation band 90–100% | 35.2% | 20.0% | 39.2% | 68.9% | – |
| Deprivation band missing | 29.7% | 15.7% | 34.8% | 65.6% | −0.27 |
| Age 0–35 | 45.9% | 27.5% | 43.6% | 72.8% | – |
| Age 35–55 | 39.7% | 20.1% | 36.3% | 71.7% | – |

30 report tables built from the result tables

