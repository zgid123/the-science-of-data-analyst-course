# Log: aq-1 / 02_analyse_all

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:29Z |
| Finished (UTC) | 2026-11-12T16:00:30Z |
| Duration | 0.6 s |
| Command | `python aq-1/code/02_analyse.py --scope all` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Populations, scope = all

| population | enrolments |
| :---- | :---- |
| all enrolments | 32,593 |
| KPI: registered at day 14 | 28,061 |
| KPI without flagged enrolments | 27,962 |
| flagged (missing withdrawal or registration day), all | 138 |
| flagged, in the KPI population | 99 |
[saved] aq-1/results/populations_all.csv  (5 rows x 2 columns)

### Non-completion rate (Fail or Withdrawn) with Wilson 95% intervals, KPI population

**By pooled**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 28,061 | 12,700 | 0.453 | 0.447 | 0.458 |

**By year**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013 | 12,076 | 5,515 | 0.457 | 0.448 | 0.466 |
| 2014 | 15,985 | 7,185 | 0.449 | 0.442 | 0.457 |

**By start_month**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| B | 10,977 | 5,531 | 0.504 | 0.495 | 0.513 |
| J | 17,084 | 7,169 | 0.420 | 0.412 | 0.427 |

**By year_start**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2013-B | 4,323 | 2,231 | 0.516 | 0.501 | 0.531 |
| 2013-J | 7,753 | 3,284 | 0.424 | 0.413 | 0.435 |
| 2014-B | 6,654 | 3,300 | 0.496 | 0.484 | 0.508 |
| 2014-J | 9,331 | 3,885 | 0.416 | 0.406 | 0.426 |

**By module**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 720 | 189 | 0.263 | 0.232 | 0.296 |
| BBB | 6,537 | 2,797 | 0.428 | 0.416 | 0.440 |
| CCC | 3,670 | 1,994 | 0.543 | 0.527 | 0.559 |
| DDD | 5,401 | 2,796 | 0.518 | 0.504 | 0.531 |
| EEE | 2,573 | 924 | 0.359 | 0.341 | 0.378 |
| FFF | 6,713 | 3,067 | 0.457 | 0.445 | 0.469 |
| GGG | 2,447 | 933 | 0.381 | 0.362 | 0.401 |

**By run**

| group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 92 | 0.249 | 0.207 | 0.295 |
| AAA-2014J | 350 | 97 | 0.277 | 0.233 | 0.326 |
| BBB-2013B | 1,606 | 804 | 0.501 | 0.476 | 0.525 |
| BBB-2013J | 1,851 | 781 | 0.422 | 0.400 | 0.445 |
| BBB-2014B | 1,289 | 564 | 0.438 | 0.411 | 0.465 |
| BBB-2014J | 1,791 | 648 | 0.362 | 0.340 | 0.384 |
| CCC-2014B | 1,591 | 928 | 0.583 | 0.559 | 0.607 |
| CCC-2014J | 2,079 | 1,066 | 0.513 | 0.491 | 0.534 |
| DDD-2013B | 1,197 | 688 | 0.575 | 0.547 | 0.602 |
| DDD-2013J | 1,675 | 849 | 0.507 | 0.483 | 0.531 |
| DDD-2014B | 1,050 | 572 | 0.545 | 0.515 | 0.575 |
| DDD-2014J | 1,479 | 687 | 0.465 | 0.439 | 0.490 |
| EEE-2013J | 933 | 325 | 0.348 | 0.318 | 0.379 |
| EEE-2014B | 613 | 256 | 0.418 | 0.379 | 0.457 |
| EEE-2014J | 1,027 | 343 | 0.334 | 0.306 | 0.363 |
| FFF-2013B | 1,520 | 739 | 0.486 | 0.461 | 0.511 |
| FFF-2013J | 1,998 | 903 | 0.452 | 0.430 | 0.474 |
| FFF-2014B | 1,309 | 656 | 0.501 | 0.474 | 0.528 |
| FFF-2014J | 1,886 | 769 | 0.408 | 0.386 | 0.430 |
| GGG-2013J | 926 | 334 | 0.361 | 0.330 | 0.392 |
| GGG-2014B | 802 | 324 | 0.404 | 0.371 | 0.438 |
| GGG-2014J | 719 | 275 | 0.382 | 0.348 | 0.419 |

[saved] aq-1/results/rates_all.csv  (38 rows x 7 columns)  – non-completion rate by level, KPI population
**Module by start month (B = February, J = October)**

| code_module | enrolments_J | enrolments_B | rate_J | rate_B | february_minus_october |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 720 |  | 0.263 |  |  |
| BBB | 3,642 | 2,895 | 0.392 | 0.473 | 0.080 |
| CCC | 2,079 | 1,591 | 0.513 | 0.583 | 0.071 |
| DDD | 3,154 | 2,247 | 0.487 | 0.561 | 0.074 |
| EEE | 1,960 | 613 | 0.341 | 0.418 | 0.077 |
| FFF | 3,884 | 2,829 | 0.430 | 0.493 | 0.063 |
| GGG | 1,645 | 802 | 0.370 | 0.404 | 0.034 |

modules with both start months: 6; February rate higher in 6 of them (gap 0.034 to 0.080)

[saved] aq-1/results/rates_module_by_start_month_all.csv  (7 rows x 6 columns)

### Year comparison: 2014 minus 2013 non-completion, Newcombe 95% interval, two denominators

**Overall scopes**

| denominator | level | scope | method | n_2013 | rate_2013 | n_2014 | rate_2014 | difference_2014_minus_2013 | ci_low | ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| registered at day 14 (KPI population) | overall | all runs (9 of 2013, 13 of 2014) | pooled counts, Newcombe interval | 12,076 | 0.4567 | 15,985 | 0.4495 | -0.0072 | -0.0190 | 0.0046 | no |
| registered at day 14 (KPI population) | overall | 6 modules run in both years | pooled counts, Newcombe interval | 12,076 | 0.4567 | 12,315 | 0.4215 | -0.0352 | -0.0476 | -0.0227 | yes |
| registered at day 14 (KPI population) | overall | 9 module x start-month pairs run in both years | pooled counts, Newcombe interval | 12,076 | 0.4567 | 10,900 | 0.4230 | -0.0337 | -0.0465 | -0.0208 | yes |
| registered at day 14 (KPI population) | overall | 9 module x start-month pairs run in both years | Mantel-Haenszel weighted over the pairs, Wald interval | 12,076 | 0.4567 | 10,900 | 0.4230 | -0.0307 | -0.0434 | -0.0179 | yes |
| all enrolments | overall | all runs (9 of 2013, 13 of 2014) | pooled counts, Newcombe interval | 13,529 | 0.5144 | 19,064 | 0.5376 | 0.0232 | 0.0122 | 0.0342 | yes |
| all enrolments | overall | 6 modules run in both years | pooled counts, Newcombe interval | 13,529 | 0.5144 | 14,630 | 0.5122 | -0.0022 | -0.0139 | 0.0095 | no |
| all enrolments | overall | 9 module x start-month pairs run in both years | pooled counts, Newcombe interval | 13,529 | 0.5144 | 13,103 | 0.5190 | 0.0047 | -0.0073 | 0.0167 | no |
| all enrolments | overall | 9 module x start-month pairs run in both years | Mantel-Haenszel weighted over the pairs, Wald interval | 13,529 | 0.5144 | 13,103 | 0.5190 | 0.0050 | -0.0069 | 0.0169 | no |

**By module (the six modules run in both years)**

| denominator | level | scope | method | n_2013 | rate_2013 | n_2014 | rate_2014 | difference_2014_minus_2013 | ci_low | ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| registered at day 14 (KPI population) | module | AAA | pooled counts, Newcombe interval | 370 | 0.2486 | 350 | 0.2771 | 0.0285 | -0.0357 | 0.0927 | no |
| registered at day 14 (KPI population) | module | BBB | pooled counts, Newcombe interval | 3,457 | 0.4585 | 3,080 | 0.3935 | -0.0650 | -0.0889 | -0.0410 | yes |
| registered at day 14 (KPI population) | module | DDD | pooled counts, Newcombe interval | 2,872 | 0.5352 | 2,529 | 0.4978 | -0.0373 | -0.0640 | -0.0106 | yes |
| registered at day 14 (KPI population) | module | EEE | pooled counts, Newcombe interval | 933 | 0.3483 | 1,640 | 0.3652 | 0.0169 | -0.0218 | 0.0550 | no |
| registered at day 14 (KPI population) | module | FFF | pooled counts, Newcombe interval | 3,518 | 0.4667 | 3,195 | 0.4460 | -0.0207 | -0.0445 | 0.0031 | no |
| registered at day 14 (KPI population) | module | GGG | pooled counts, Newcombe interval | 926 | 0.3607 | 1,521 | 0.3938 | 0.0331 | -0.0066 | 0.0723 | no |
| all enrolments | module | AAA | pooled counts, Newcombe interval | 383 | 0.2742 | 365 | 0.3068 | 0.0327 | -0.0323 | 0.0975 | no |
| all enrolments | module | BBB | pooled counts, Newcombe interval | 4,004 | 0.5317 | 3,905 | 0.5188 | -0.0129 | -0.0349 | 0.0091 | no |
| all enrolments | module | DDD | pooled counts, Newcombe interval | 3,241 | 0.5869 | 3,031 | 0.5807 | -0.0062 | -0.0306 | 0.0182 | no |
| all enrolments | module | EEE | pooled counts, Newcombe interval | 1,052 | 0.4211 | 1,882 | 0.4469 | 0.0258 | -0.0117 | 0.0629 | no |
| all enrolments | module | FFF | pooled counts, Newcombe interval | 3,897 | 0.5183 | 3,865 | 0.5418 | 0.0234 | 0.0012 | 0.0456 | yes |
| all enrolments | module | GGG | pooled counts, Newcombe interval | 952 | 0.3782 | 1,582 | 0.4172 | 0.0390 | -0.0004 | 0.0780 | no |

**By start month**

| denominator | level | scope | method | n_2013 | rate_2013 | n_2014 | rate_2014 | difference_2014_minus_2013 | ci_low | ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| registered at day 14 (KPI population) | start month, all modules | B | pooled counts, Newcombe interval | 4,323 | 0.5161 | 6,654 | 0.4959 | -0.0201 | -0.0393 | -0.0010 | yes |
| registered at day 14 (KPI population) | start month, modules run in both years | B | pooled counts, Newcombe interval | 4,323 | 0.5161 | 5,063 | 0.4685 | -0.0476 | -0.0678 | -0.0273 | yes |
| registered at day 14 (KPI population) | start month, paired runs | B | pooled counts, Newcombe interval | 4,323 | 0.5161 | 3,648 | 0.4912 | -0.0248 | -0.0468 | -0.0028 | yes |
| registered at day 14 (KPI population) | start month, all modules | J | pooled counts, Newcombe interval | 7,753 | 0.4236 | 9,331 | 0.4164 | -0.0072 | -0.0221 | 0.0076 | no |
| registered at day 14 (KPI population) | start month, modules run in both years | J | pooled counts, Newcombe interval | 7,753 | 0.4236 | 7,252 | 0.3887 | -0.0349 | -0.0505 | -0.0191 | yes |
| registered at day 14 (KPI population) | start month, paired runs | J | pooled counts, Newcombe interval | 7,753 | 0.4236 | 7,252 | 0.3887 | -0.0349 | -0.0505 | -0.0191 | yes |
| all enrolments | start month, all modules | B | pooled counts, Newcombe interval | 4,684 | 0.5527 | 7,804 | 0.5697 | 0.0170 | -0.0010 | 0.0350 | no |
| all enrolments | start month, modules run in both years | B | pooled counts, Newcombe interval | 4,684 | 0.5527 | 5,868 | 0.5407 | -0.0120 | -0.0311 | 0.0071 | no |
| all enrolments | start month, paired runs | B | pooled counts, Newcombe interval | 4,684 | 0.5527 | 4,341 | 0.5715 | 0.0188 | -0.0017 | 0.0393 | no |
| all enrolments | start month, all modules | J | pooled counts, Newcombe interval | 8,845 | 0.4941 | 11,260 | 0.5154 | 0.0213 | 0.0074 | 0.0352 | yes |
| all enrolments | start month, modules run in both years | J | pooled counts, Newcombe interval | 8,845 | 0.4941 | 8,762 | 0.4930 | -0.0010 | -0.0158 | 0.0137 | no |
| all enrolments | start month, paired runs | J | pooled counts, Newcombe interval | 8,845 | 0.4941 | 8,762 | 0.4930 | -0.0010 | -0.0158 | 0.0137 | no |

**By module x start-month pair run in both years**

| denominator | level | scope | method | n_2013 | rate_2013 | n_2014 | rate_2014 | difference_2014_minus_2013 | ci_low | ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| registered at day 14 (KPI population) | pair | AAA-J | pooled counts, Newcombe interval | 370 | 0.2486 | 350 | 0.2771 | 0.0285 | -0.0357 | 0.0927 | no |
| registered at day 14 (KPI population) | pair | BBB-B | pooled counts, Newcombe interval | 1,606 | 0.5006 | 1,289 | 0.4375 | -0.0631 | -0.0994 | -0.0265 | yes |
| registered at day 14 (KPI population) | pair | BBB-J | pooled counts, Newcombe interval | 1,851 | 0.4219 | 1,791 | 0.3618 | -0.0601 | -0.0916 | -0.0284 | yes |
| registered at day 14 (KPI population) | pair | DDD-B | pooled counts, Newcombe interval | 1,197 | 0.5748 | 1,050 | 0.5448 | -0.0300 | -0.0710 | 0.0111 | no |
| registered at day 14 (KPI population) | pair | DDD-J | pooled counts, Newcombe interval | 1,675 | 0.5069 | 1,479 | 0.4645 | -0.0424 | -0.0772 | -0.0074 | yes |
| registered at day 14 (KPI population) | pair | EEE-J | pooled counts, Newcombe interval | 933 | 0.3483 | 1,027 | 0.3340 | -0.0144 | -0.0564 | 0.0276 | no |
| registered at day 14 (KPI population) | pair | FFF-B | pooled counts, Newcombe interval | 1,520 | 0.4862 | 1,309 | 0.5011 | 0.0150 | -0.0220 | 0.0518 | no |
| registered at day 14 (KPI population) | pair | FFF-J | pooled counts, Newcombe interval | 1,998 | 0.4520 | 1,886 | 0.4077 | -0.0442 | -0.0752 | -0.0131 | yes |
| registered at day 14 (KPI population) | pair | GGG-J | pooled counts, Newcombe interval | 926 | 0.3607 | 719 | 0.3825 | 0.0218 | -0.0251 | 0.0689 | no |
| all enrolments | pair | AAA-J | pooled counts, Newcombe interval | 383 | 0.2742 | 365 | 0.3068 | 0.0327 | -0.0323 | 0.0975 | no |
| all enrolments | pair | BBB-B | pooled counts, Newcombe interval | 1,767 | 0.5456 | 1,613 | 0.5493 | 0.0037 | -0.0298 | 0.0373 | no |
| all enrolments | pair | BBB-J | pooled counts, Newcombe interval | 2,237 | 0.5208 | 2,292 | 0.4974 | -0.0234 | -0.0525 | 0.0057 | no |
| all enrolments | pair | DDD-B | pooled counts, Newcombe interval | 1,303 | 0.6086 | 1,228 | 0.6099 | 0.0013 | -0.0367 | 0.0393 | no |
| all enrolments | pair | DDD-J | pooled counts, Newcombe interval | 1,938 | 0.5722 | 1,803 | 0.5607 | -0.0115 | -0.0433 | 0.0202 | no |
| all enrolments | pair | EEE-J | pooled counts, Newcombe interval | 1,052 | 0.4211 | 1,188 | 0.4242 | 0.0031 | -0.0378 | 0.0440 | no |
| all enrolments | pair | FFF-B | pooled counts, Newcombe interval | 1,614 | 0.5155 | 1,500 | 0.5640 | 0.0485 | 0.0135 | 0.0834 | yes |
| all enrolments | pair | FFF-J | pooled counts, Newcombe interval | 2,283 | 0.5204 | 2,365 | 0.5277 | 0.0073 | -0.0214 | 0.0360 | no |
| all enrolments | pair | GGG-J | pooled counts, Newcombe interval | 952 | 0.3782 | 749 | 0.4072 | 0.0291 | -0.0176 | 0.0758 | no |
[saved] aq-1/results/year_comparison_all.csv  (50 rows x 14 columns)

**Sign of the year difference under each denominator**

| scope | registered at day 14 (KPI population) | all enrolments |
| :---- | :---- | :---- |
| all runs (9 of 2013, 13 of 2014) | -0.0072 | 0.0232 |
| 6 modules run in both years | -0.0352 | -0.0022 |
| 9 module x start-month pairs run in both years | -0.0337 | 0.0047 |
- registered at day 14 (KPI population): 2014 lower in 3 of 6 shared modules; interval excludes 0 in 2 (lower: 2, higher: 0)
- all enrolments: 2014 lower in 2 of 6 shared modules; interval excludes 0 in 1 (lower: 0, higher: 1)

**Share of enrolments not registered at day 14, by year (they are outside the KPI population and nearly all end in Fail or Withdrawn)**

| scope | enrolments_2013 | not_registered_2013 | share_not_registered_2013 | enrolments_2014 | not_registered_2014 | share_not_registered_2014 | difference_2014_minus_2013 | ci_low | ci_high | non_completion_among_not_registered_2013 | non_completion_among_not_registered_2014 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 13,529 | 1,453 | 0.1074 | 19,064 | 3,079 | 0.1615 | 0.0541 | 0.0467 | 0.0615 | 0.9938 | 0.9951 |
| 6 modules run in both years | 13,529 | 1,453 | 0.1074 | 14,630 | 2,315 | 0.1582 | 0.0508 | 0.0429 | 0.0587 | 0.9938 | 0.9944 |
| 9 module x start-month pairs run in both years | 13,529 | 1,453 | 0.1074 | 13,103 | 2,203 | 0.1681 | 0.0607 | 0.0525 | 0.0690 | 0.9938 | 0.9941 |
[saved] aq-1/results/not_registered_d14_by_year_all.csv  (3 rows x 12 columns)

### Three denominators per run: KPI population, all enrolments, KPI without flagged enrolments

| run | n_kpi | rate_kpi | ci_low | ci_high | n_all | rate_all | n_unflagged | rate_unflagged | shift_all_minus_kpi | all_outside_kpi_interval | shift_unflagged_minus_kpi | unflagged_outside_kpi_interval |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 0.249 | 0.207 | 0.295 | 383 | 0.274 | 370 | 0.249 | 0.026 | no | 0.000 | no |
| AAA-2014J | 350 | 0.277 | 0.233 | 0.326 | 365 | 0.307 | 350 | 0.277 | 0.030 | no | 0.000 | no |
| BBB-2013B | 1,606 | 0.501 | 0.476 | 0.525 | 1,767 | 0.546 | 1,605 | 0.500 | 0.045 | yes | -0.000 | no |
| BBB-2013J | 1,851 | 0.422 | 0.400 | 0.445 | 2,237 | 0.521 | 1,851 | 0.422 | 0.099 | yes | 0.000 | no |
| BBB-2014B | 1,289 | 0.438 | 0.411 | 0.465 | 1,613 | 0.549 | 1,288 | 0.437 | 0.112 | yes | -0.000 | no |
| BBB-2014J | 1,791 | 0.362 | 0.340 | 0.384 | 2,292 | 0.497 | 1,779 | 0.358 | 0.136 | yes | -0.004 | no |
| CCC-2014B | 1,591 | 0.583 | 0.559 | 0.607 | 1,936 | 0.658 | 1,591 | 0.583 | 0.074 | yes | 0.000 | no |
| CCC-2014J | 2,079 | 0.513 | 0.491 | 0.534 | 2,498 | 0.594 | 2,050 | 0.506 | 0.081 | yes | -0.006 | no |
| DDD-2013B | 1,197 | 0.575 | 0.547 | 0.602 | 1,303 | 0.609 | 1,194 | 0.574 | 0.034 | yes | -0.001 | no |
| DDD-2013J | 1,675 | 0.507 | 0.483 | 0.531 | 1,938 | 0.572 | 1,675 | 0.507 | 0.065 | yes | 0.000 | no |
| DDD-2014B | 1,050 | 0.545 | 0.515 | 0.575 | 1,228 | 0.610 | 1,048 | 0.544 | 0.065 | yes | -0.001 | no |
| DDD-2014J | 1,479 | 0.465 | 0.439 | 0.490 | 1,803 | 0.561 | 1,463 | 0.459 | 0.096 | yes | -0.006 | no |
| EEE-2013J | 933 | 0.348 | 0.318 | 0.379 | 1,052 | 0.421 | 932 | 0.348 | 0.073 | yes | -0.001 | no |
| EEE-2014B | 613 | 0.418 | 0.379 | 0.457 | 694 | 0.486 | 613 | 0.418 | 0.068 | yes | 0.000 | no |
| EEE-2014J | 1,027 | 0.334 | 0.306 | 0.363 | 1,188 | 0.424 | 1,023 | 0.331 | 0.090 | yes | -0.003 | no |
| FFF-2013B | 1,520 | 0.486 | 0.461 | 0.511 | 1,614 | 0.515 | 1,519 | 0.486 | 0.029 | yes | -0.000 | no |
| FFF-2013J | 1,998 | 0.452 | 0.430 | 0.474 | 2,283 | 0.520 | 1,997 | 0.452 | 0.068 | yes | -0.000 | no |
| FFF-2014B | 1,309 | 0.501 | 0.474 | 0.528 | 1,500 | 0.564 | 1,308 | 0.501 | 0.063 | yes | -0.000 | no |
| FFF-2014J | 1,886 | 0.408 | 0.386 | 0.430 | 2,365 | 0.528 | 1,862 | 0.400 | 0.120 | yes | -0.008 | no |
| GGG-2013J | 926 | 0.361 | 0.330 | 0.392 | 952 | 0.378 | 925 | 0.360 | 0.017 | no | -0.001 | no |
| GGG-2014B | 802 | 0.404 | 0.371 | 0.438 | 833 | 0.426 | 802 | 0.404 | 0.022 | no | 0.000 | no |
| GGG-2014J | 719 | 0.382 | 0.348 | 0.419 | 749 | 0.407 | 717 | 0.381 | 0.025 | no | -0.002 | no |
[saved] aq-1/results/denominators_by_run_all.csv  (22 rows x 13 columns)

**Pooled**

| denominator | enrolments | non_completers | rate |
| :---- | :---- | :---- | :---- |
| KPI (registered at day 14) | 28,061 | 12,700 | 0.453 |
| all enrolments | 32,593 | 17,208 | 0.528 |
| KPI without flagged | 27,962 | 12,602 | 0.451 |
[saved] aq-1/results/denominators_pooled_all.csv  (3 rows x 4 columns)

### Outcome shares (Pass, Distinction, Fail, Withdrawn), KPI population

[saved] aq-1/results/outcome_shares_all.csv  (136 rows x 8 columns)
| level | group | enrolments | Distinction | Pass | Fail | Withdrawn |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| pooled | all runs | 28,061 | 0.108 | 0.440 | 0.250 | 0.202 |
| module | AAA | 720 | 0.061 | 0.676 | 0.124 | 0.139 |
| module | BBB | 6,537 | 0.103 | 0.469 | 0.269 | 0.159 |
| module | CCC | 3,670 | 0.136 | 0.321 | 0.213 | 0.331 |
| module | DDD | 5,401 | 0.071 | 0.411 | 0.261 | 0.257 |
| module | EEE | 2,573 | 0.138 | 0.503 | 0.218 | 0.141 |
| module | FFF | 6,713 | 0.100 | 0.443 | 0.254 | 0.203 |
| module | GGG | 2,447 | 0.162 | 0.457 | 0.297 | 0.084 |

### Non-completion by audit attribute (description only; no model reads these columns)

| attribute | group | enrolments | events | rate | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gender | F | 12,573 | 5,462 | 0.434 | 0.426 | 0.443 |
| gender | M | 15,488 | 7,238 | 0.467 | 0.459 | 0.475 |
| disability | N | 25,385 | 11,230 | 0.442 | 0.436 | 0.449 |
| disability | Y | 2,676 | 1,470 | 0.549 | 0.530 | 0.568 |
| imd_band | 0-10% | 2,708 | 1,546 | 0.571 | 0.552 | 0.589 |
| imd_band | 10-20% | 2,890 | 1,533 | 0.530 | 0.512 | 0.549 |
| imd_band | 20-30% | 3,060 | 1,574 | 0.514 | 0.497 | 0.532 |
| imd_band | 30-40% | 3,055 | 1,398 | 0.458 | 0.440 | 0.475 |
| imd_band | 40-50% | 2,773 | 1,257 | 0.453 | 0.435 | 0.472 |
| imd_band | 50-60% | 2,740 | 1,217 | 0.444 | 0.426 | 0.463 |
| imd_band | 60-70% | 2,561 | 1,057 | 0.413 | 0.394 | 0.432 |
| imd_band | 70-80% | 2,550 | 1,071 | 0.420 | 0.401 | 0.439 |
| imd_band | 80-90% | 2,419 | 928 | 0.384 | 0.364 | 0.403 |
| imd_band | 90-100% | 2,268 | 809 | 0.357 | 0.337 | 0.377 |
| imd_band | Missing | 1,037 | 310 | 0.299 | 0.272 | 0.328 |
| age_band | 0-35 | 19,580 | 9,261 | 0.473 | 0.466 | 0.480 |
| age_band | 35-55 | 8,283 | 3,374 | 0.407 | 0.397 | 0.418 |
| age_band | 55<= | 198 | 65 | 0.328 | 0.267 | 0.396 |
[saved] aq-1/results/rates_by_audit_group_all.csv  (18 rows x 7 columns)

### Week of the first assessed task (TMA or CMA) due while enrolled and not submitted, KPI population

**Task calendar per run**

| run | first_task_due_day | first_task_due_week | tasks_due_by_day27 | tasks_in_run |
| :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 19 | 3 | 1 | 5 |
| AAA-2014J | 19 | 3 | 1 | 5 |
| BBB-2013B | 19 | 3 | 1 | 11 |
| BBB-2013J | 19 | 3 | 1 | 11 |
| BBB-2014B | 12 | 2 | 1 | 11 |
| BBB-2014J | 19 | 3 | 1 | 5 |
| CCC-2014B | 18 | 3 | 1 | 8 |
| CCC-2014J | 18 | 3 | 1 | 8 |
| DDD-2013B | 23 | 4 | 2 | 13 |
| DDD-2013J | 25 | 4 | 1 | 6 |
| DDD-2014B | 25 | 4 | 1 | 6 |
| DDD-2014J | 20 | 3 | 1 | 6 |
| EEE-2013J | 33 | 5 | 0 | 4 |
| EEE-2014B | 33 | 5 | 0 | 4 |
| EEE-2014J | 33 | 5 | 0 | 4 |
| FFF-2013B | 19 | 3 | 1 | 12 |
| FFF-2013J | 19 | 3 | 1 | 12 |
| FFF-2014B | 24 | 4 | 1 | 12 |
| FFF-2014J | 24 | 4 | 1 | 12 |
| GGG-2013J | 61 | 9 | 0 | 9 |
| GGG-2014B | 61 | 9 | 0 | 9 |
| GGG-2014J | 61 | 9 | 0 | 9 |
[saved] aq-1/results/task_calendar_by_run_all.csv  (22 rows x 5 columns)

Runs with no task due by day 27: 6 of 22: EEE-2013J, EEE-2014B, EEE-2014J, GGG-2013J, GGG-2014B, GGG-2014J

**First missed task by outcome**

| group | enrolments | ever_missed | share_ever_missed | median_first_missed_week | p25_week | p75_week | share_missed_by_week_4 | share_missed_by_week_8 | share_missed_by_week_12 | share_missed_by_week_16 | share_missed_by_week_20 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completers (Pass or Distinction) | 15,361 | 3,150 | 0.205 | 24.000 | 14.000 | 30.000 | 0.005 | 0.038 | 0.047 | 0.060 | 0.081 |
| Distinction | 3,022 | 393 | 0.130 | 23.000 | 5.000 | 32.000 | 0.001 | 0.043 | 0.046 | 0.054 | 0.060 |
| Fail | 7,027 | 5,816 | 0.828 | 12.000 | 6.000 | 19.000 | 0.150 | 0.335 | 0.424 | 0.529 | 0.636 |
| Non-completers (Fail or Withdrawn) | 12,700 | 9,532 | 0.751 | 9.000 | 5.000 | 18.000 | 0.168 | 0.351 | 0.430 | 0.532 | 0.619 |
| Pass | 12,339 | 2,757 | 0.223 | 24.000 | 14.000 | 29.000 | 0.006 | 0.036 | 0.047 | 0.062 | 0.086 |
| Withdrawn | 5,673 | 3,716 | 0.655 | 8.000 | 4.000 | 14.000 | 0.190 | 0.371 | 0.436 | 0.535 | 0.598 |
[saved] aq-1/results/first_missed_task_by_outcome_all.csv  (6 rows x 12 columns)

**Share with a first missed task by the end of week 4 (day 27), Wilson 95% interval**

| population | runs | year | group | enrolments | missed_by_week_4 | share | ci_low | ci_high |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | 9 | 2013 | Completers (Pass or Distinction) | 6,561 | 30 | 0.005 | 0.003 | 0.007 |
| all runs | 9 | 2013 | Non-completers (Fail or Withdrawn) | 5,515 | 1,080 | 0.196 | 0.186 | 0.207 |
| all runs | 13 | 2014 | Completers (Pass or Distinction) | 8,800 | 54 | 0.006 | 0.005 | 0.008 |
| all runs | 13 | 2014 | Non-completers (Fail or Withdrawn) | 7,185 | 1,053 | 0.147 | 0.139 | 0.155 |
| all runs | 22 | both years | Completers (Pass or Distinction) | 15,361 | 84 | 0.005 | 0.004 | 0.007 |
| all runs | 22 | both years | Non-completers (Fail or Withdrawn) | 12,700 | 2,133 | 0.168 | 0.162 | 0.175 |
| runs with a task due by day 27 | 7 | 2013 | Completers (Pass or Distinction) | 5,361 | 30 | 0.006 | 0.004 | 0.008 |
| runs with a task due by day 27 | 7 | 2013 | Non-completers (Fail or Withdrawn) | 4,856 | 1,080 | 0.222 | 0.211 | 0.234 |
| runs with a task due by day 27 | 9 | 2014 | Completers (Pass or Distinction) | 6,837 | 54 | 0.008 | 0.006 | 0.010 |
| runs with a task due by day 27 | 9 | 2014 | Non-completers (Fail or Withdrawn) | 5,987 | 1,053 | 0.176 | 0.166 | 0.186 |
| runs with a task due by day 27 | 16 | both years | Completers (Pass or Distinction) | 12,198 | 84 | 0.007 | 0.006 | 0.009 |
| runs with a task due by day 27 | 16 | both years | Non-completers (Fail or Withdrawn) | 10,843 | 2,133 | 0.197 | 0.189 | 0.204 |
[saved] aq-1/results/first_missed_by_week4_all.csv  (12 rows x 9 columns)

**Non-completers with a missed task by week 4: 2014 minus 2013**

| population | group | n_2013 | events_2013 | rate_2013 | n_2014 | events_2014 | rate_2014 | difference_2014_minus_2013 | ci_low | ci_high | interval_excludes_0 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| all runs | non-completers | 5,515 | 1,080 | 0.1958 | 7,185 | 1,053 | 0.1466 | -0.0493 | -0.0626 | -0.0360 | yes |
| runs with a task due by day 27 | non-completers | 4,856 | 1,080 | 0.2224 | 5,987 | 1,053 | 0.1759 | -0.0465 | -0.0617 | -0.0314 | yes |
[saved] aq-1/results/first_missed_by_week4_year_difference_all.csv  (2 rows x 12 columns)
[saved] aq-1/results/first_missed_task_cumulative_all.csv  (70 rows x 5 columns)

**Non-completers: first missed task by module**

| code_module | non_completers | share_ever_missed | median_first_missed_week | share_missed_by_week_4 | share_missed_by_week_8 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 189 | 0.603 | 12.500 | 0.122 | 0.302 |
| BBB | 2,797 | 0.795 | 8.000 | 0.212 | 0.423 |
| CCC | 1,994 | 0.725 | 5.000 | 0.204 | 0.447 |
| DDD | 2,796 | 0.712 | 8.000 | 0.212 | 0.366 |
| EEE | 924 | 0.753 | 10.000 | 0.000 | 0.281 |
| FFF | 3,067 | 0.753 | 13.000 | 0.169 | 0.340 |
| GGG | 933 | 0.807 | 17.000 | 0.000 | 0.000 |
[saved] aq-1/results/first_missed_task_by_module_all.csv  (7 rows x 6 columns)

