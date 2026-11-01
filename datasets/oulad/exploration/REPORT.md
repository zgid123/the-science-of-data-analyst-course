# OULAD is structurally sound and ready for a deep dive, with nine data issues to handle explicitly

- **Dataset:** OULAD (Open University Learning Analytics Dataset), all 7 tables, full data (10.9 million rows, no
  sampling).
- **Snapshot:** 1 November 2026.
- **Unit of analysis:** one student enrolment in one module presentation.

**Status: complete descriptive exploration (lifecycle stage 5, Data Understanding).** This report establishes
structure, keys, relationships, quality, candidate measures and the descriptive associations of the outcome with
student characteristics, early engagement, assessment behaviour and time (Section 5). Every method applied is
listed with its output file in Section 8. It tests no hypothesis and estimates no causal effect; that is the
deep-dive work it prepares (Section 7).

All 11 referential-integrity checks pass: every enrolment, assessment, VLE site and click record links to a valid
parent, and the enrolment key is unique in both student tables. The data can therefore be joined with confidence.
Nine issues need an explicit decision before analysis, because each changes a count, a denominator or a
comparison (Section 3).

## Findings at a glance

The table below lists the main findings with their size and the section that holds the evidence; issue numbers
refer to the data-issue table in Section 3.

| Finding | Size | Section |
|---|---|---|
| The seven tables join cleanly | 0 orphans in 11 referential-integrity checks | Section 2 |
| 7.39% of click rows are exact duplicates (issue 1) | 3.19% of clicks; the early-engagement effect changes by at most 0.004 | Section 3 |
| Exam scores exist for 2 of 7 modules only (issue 7) | 18 of 24 exams have no score records | Section 3 |
| Clicks and submissions continue after unregistration (issue 9) | 1,279 enrolments, 98,745 clicks | Section 3 |
| Success falls with deprivation | 35% in the most deprived decile against 58% in the least; −15.4 points within engagement strata | Section 5.1 |
| The gender gap in withdrawal reverses within modules | −1.2 points overall, +3.0 points within modules | Section 5.1 |
| Early registrants withdraw more often | 38.9% when more than 100 days early, 20.9% after day 0 | Section 5.1 |
| Early activity separates success | Cliff's delta 0.31 at equal exposure, 0.26–0.48 by module | Section 5.2 |
| Most withdrawn students never submitted the first assessment | 55.4% of Withdrawn against 1.0% of Pass | Section 5.2 |
| Withdrawal accumulates over the whole presentation | 23.7% of those enrolled on day 0 by the end; half by day 73 | Section 5.3 |
| Withdrawal rose from 2013 to 2014 | +0.7 to +9.9 points in all 9 module-semester pairs | Section 5.3 |
| Engagement forms a continuum, not types | 3 trajectory clusters, silhouette 0.26 | Section 5.6 |

## 1. Dataset map

The seven tables describe 22 presentations (7 modules × 2013B–2014J) and 32,593 enrolments. Dates are **day
offsets from the start of each presentation** (day 0), not calendar dates; negative values fall before the start.

| Table | Rows | One row per | Key (verified unique) | Role in analysis |
|---|---|---|---|---|
| `courses` | 22 | presentation | `code_module`, `code_presentation` | presentation length 234–269 days |
| `assessments` | 206 | assessment | `id_assessment` | 106 TMA, 76 CMA, 24 Exam; due day and weight |
| `vle` | 6,364 | VLE site (learning resource) | `id_site` | 20 activity types; planned weeks |
| `studentInfo` | 32,593 | enrolment | `code_module`, `code_presentation`, `id_student` | demographics, `final_result` (outcome) |
| `studentRegistration` | 32,593 | enrolment | same as `studentInfo`, matching 1:1 | registration and unregistration days |
| `studentAssessment` | 173,912 | student × assessment | `id_assessment`, `id_student` | submission day, score 0–100, banked flag |
| `studentVle` | 10,655,280 | logged visit (student × site × day, possibly several) | none | daily click counts |

Outcomes across all enrolments: Pass 12,361 (37.9%), Withdrawn 10,156 (31.2%), Fail 7,052 (21.6%) and
Distinction 3,024 (9.3%). 3,538 students hold more than one enrolment, so student-level and enrolment-level
counts differ.

## 2. Relationships

Every child table links to its parent without orphans, and every enrolment appearing in click or assessment data
exists in `studentInfo` (`results/checks.json`). Two coverage facts set denominators for later analysis:

- **3,365 enrolments (10.3%) have no VLE activity**, and **6,750 (20.7%) have no assessment submission**. An
  analysis restricted to active students therefore describes a selected population.
- **Withdrawal timing is recorded for nearly all withdrawals**: 10,063 of 10,156 Withdrawn enrolments carry a
  `date_unregistration`, and 3,097 enrolments unregistered on or before day 0, before teaching began.

Natural hierarchy for slicing: module → presentation → enrolment → assessment or VLE site → day.

## 3. Data quality issues to decide on before analysis

Each issue below states its size and the handling the deep dive should record. None justifies silently dropping
rows; the raw files stay unchanged.

| # | Issue | Size | Severity | Proposed handling |
|---|---|---|---|---|
| 1 | **Exact duplicate rows in `studentVle`** (same student, site, day and click count) | 787,170 rows, 7.39%; 3.8%–11.7% in every presentation; 70% of duplicated groups are single-click visits | High for click totals | Ambiguous: repeated short visits or duplicate records. Run click measures both raw and with exact duplicates collapsed; totals differ by 3.19% (39.6M vs 38.3M clicks). |
| 2 | **Several rows per student × site × day** beyond exact duplicates | 1,614,505 such groups covering 3,810,465 rows | Medium | Aggregate `sum_click` to student × day (or week) before modelling activity. |
| 3 | **Withdrawal record inconsistency** | 93 Withdrawn without `date_unregistration`; 9 Fail with one | Low | Keep `final_result` as the outcome; treat unregistration day as missing for the 93 and report the 9 separately. |
| 4 | **Assessment weights differ by module** | CCC 2014B and 2014J have two exams (exam weight 200); GGG's 3 presentations weight all TMA/CMA at 0 | Medium for weighted scores | Compute weighted scores per module rule; GGG coursework is formative, so its scores measure engagement, not graded attainment. |
| 5 | **Late and post-end submissions** | 49,318 submissions (28.8% of those with a due day) after the due day; 85 after the presentation ended (max day 608) | Medium for "on-time" features | Define lateness against the assessment's due day; 11 exams have no due day and need the presentation end as reference. |
| 6 | **Missing values in descriptive fields** | `imd_band` 1,111 (3.41%); `date_registration` 45; `score` 173; `vle.week_from/week_to` 82.4% | Low except `week_*` | Keep missing as its own category for `imd_band`: it is concentrated in North Region (40.1%) and Ireland (22.5%) and those enrolments succeed more often (65.7% against 46.6%), so it is not missing at random (Section 5.1). Use `week_*` only for the 1,121 sites that carry it. |
| 7 | **Exam scores absent for 5 of 7 modules** | 18 of 24 exams have no score records; only DDD (4 of 4) and CCC (2 of 4) have exam scores | High for score-based outcomes | `final_result` cannot be rebuilt from scores outside CCC and DDD; use `final_result` as recorded and describe exam performance for those two modules only. |
| 8 | **Two days without any click in every 2014B presentation** | days 218–219 in CCC, DDD, EEE, FFF and GGG 2014B; days 211–212 in BBB 2014B, whose presentation is 7 days shorter | Low | Consistent with a platform-wide logging gap (not verifiable: dates are offsets). Treat the two days as missing, not as zero activity, in daily series. |
| 9 | **Activity recorded after unregistration** | 1,279 of 10,072 unregistered enrolments have 29,440 click rows (98,745 clicks) after their unregistration day, up to 423 days later; 415 have 601 submissions after it | Medium for activity up to withdrawal | Count activity only up to the unregistration day when measuring engagement before withdrawal. The early-window measures in Section 5.2 are unaffected, because they cover days 0–27 of students still registered on day 28. |

Scores show round-number heaping, which reflects how they are marked rather than an error. All scores are
integers; 45.8% of computer-marked (CMA) scores and 17.4% of tutor-marked (TMA) scores fall on a multiple of 10,
against 10% without heaping, with 3.5 and 2.4 times the count of their neighbouring scores; exam scores show no
excess (`score_heaping` in `results/followups.json`). CMA scores therefore behave as coarse steps, and TMA scores
cluster at values markers round to.

Smaller observations: one `imd_band` label is `10-20` while the other nine read `NN-NN%` (normalise when
ordering bands); `studied_credits` reaches 655 against a 99th percentile of 240; 688,988 click rows (6.5%) fall
before day 0, which is genuine pre-start activity rather than an error.

## 4. Column profile highlights

Full per-column statistics (missing rate, distinct values, top and rare values, percentiles, zeros, negatives)
are in `results/columns.csv` and `results/columns.json`. The distributions that matter for modelling:

| Measure | Median | Middle 50% | Tail | Shape |
|---|---|---|---|---|
| `score` (0–100) | 80 | 65–90 | 329 zeros; 0.1% missing | left-skewed; mean 75.8 below median |
| `sum_click` per row | 2 | 1–3 | 99th pct 34, max 6,977 | heavy right tail; use medians or log scale |
| `date_registration` (day) | −57 | −100 to −29 | −322 to 167 | most students register 1–3 months early |
| `num_of_prev_attempts` | 0 | 0–0 | max 6 | 87% first attempts |

Total clicks per enrolment separate the outcome groups strongly: median 89 for Withdrawn (29.4% with no clicks),
317 for Fail, 1,343 for Pass and 1,896 for Distinction (`results/segments.json`). This is a descriptive
association: withdrawn students are enrolled for less time, so click totals partly measure exposure. Comparisons of
engagement should use activity within a fixed early window for every enrolment; Section 5.2 does this for
days 0–27.

The gap is visible from the first week of teaching. In week 0 (days 0–6), enrolments that later withdrew
averaged 34.7 clicks against 44.7 for Fail, 81.1 for Pass and 113.6 for Distinction, so early activity is a
candidate early signal worth testing within modules (deep-dive analysis 1).

Withdrawal rates differ widely by module, from 11.5% (GGG) and 16.8% (AAA) to 44.5% (CCC), so module is a
required control in any outcome comparison.

## 5. Outcome relationships, time and withdrawal

This section describes how the outcome (`final_result`) varies with student characteristics, early engagement,
assessment behaviour and time. It uses one row per enrolment (`results/enrolment_features.csv`, 38 columns) and
the summaries in `results/descriptive.json`, written by `code/02_features.py` and `code/03_describe.py`. Because the data hold
32,593 enrolments, almost any difference passes a significance test; the section therefore reports effect sizes
and 95% intervals instead of p-values. Success means Pass or Distinction. Every statement is a descriptive
association, not a cause.

### 5.1 Student characteristics

Success rate rises steadily with socio-economic advantage, prior education and age, and falls with repeat
attempts and disability. The table below gives the lowest and highest group for each characteristic with Wilson
95% intervals, plus two association sizes: bias-corrected Cramér's V against the four-class outcome overall, and
its median within the seven modules. Each association is weak on its own (V 0.06–0.12), but it keeps its size
within modules, so module mix does not explain it.

| Characteristic | Lowest success | Highest success | Cramér's V overall / within module |
|---|---|---|---|
| `imd_band` (deprivation decile) | 0–10%: 35.2% (33.6–36.8) | 90–100%: 57.5% (55.6–59.4) | 0.082 / 0.087 |
| `highest_education` | No formal quals: 29.7% (25.1–34.7) | Post-graduate: 65.5% (60.1–70.6) | 0.102 / 0.105 |
| `num_of_prev_attempts` | 2 or more: 27.5% (24.6–30.6) | none: 49.3% (48.7–49.9) | 0.088 / 0.065 |
| `disability` | Y: 38.2% (36.5–39.9) | N: 48.2% (47.6–48.8) | 0.065 / 0.058 |
| `age_band` | 0–35: 45.0% (44.4–45.7) | 55 and over: 61.6% (54.9–67.8) | 0.058 / 0.053 |
| `region` | North Western: 40.2% (38.4–42.0) | Ireland: 54.9% (52.1–57.7) | 0.065 / 0.070 |
| `code_module` | CCC: 37.8% (36.4–39.3) | AAA: 71.0% (67.6–74.1) | 0.121 / – |

The deprivation gradient is monotone apart from two small steps whose intervals overlap (30–40% to 40–50% and
60–70% to 70–80%), which makes `imd_band` usable as an ordinal measure (Spearman ρ with the ordered outcome 0.13).

**The gender comparison reverses once module is taken into account (Simpson's paradox).** Overall, women
withdraw slightly less often than men (30.5% against 31.7%, −1.2 percentage points). Within modules, women
withdraw more often in 6 of 7 modules (+1.4 to +7.7 points; GGG −2.4), and the module-standardised gap is
+3.0 points. The reversal follows from module mix: women make up 88% of BBB and 81% of GGG, and GGG has the
lowest withdrawal rate (11.5%). As a result, any gender comparison needs module as a control. An independent
recount from the raw `studentInfo.csv` gives the same figures (`code/05_crosscheck.py`,
`logs/05_crosscheck.log`). The other contrasts keep their direction and size after standardising by module:
disability −10.0 points crude against −9.9 standardised, most against least deprived −18.8 against −19.1,
repeat against first attempt −16.2 against −14.1 (`simpson` in `results/descriptive.json`).

Missing `imd_band` is not random. It is concentrated in North Region (40.1% of its enrolments) and Ireland
(22.5%), giving a Cramér's V of 0.54 between missingness and region, and enrolments with a missing band succeed
more often (65.7% against 46.6%). Keeping missing as its own category (issue 6) is therefore necessary, and that
category partly stands for region.

Registration timing relates to withdrawal in an unexpected direction. Enrolments registered more than 100 days
before the start withdraw in 38.9% of cases, against 30.3% for 31–100 days early, 25.6% for the last 30 days and
20.9% for the 234 registered after day 0, while success changes less (43.2% to 50.4%). The 45 enrolments without
a registration day withdraw in 86.7% of cases. One hypothesis for the deep dive: students who enrol far ahead
lose momentum before teaching starts (`registration_timing`).

### 5.2 Early engagement and assessment behaviour

To compare engagement on equal exposure, clicks are counted in the same early window, days 0–27, for every
enrolment still registered on day 28 (27,553 of 32,593). The table below gives the median and middle 50% of
early clicks, the median number of active days and the share with no early click, by outcome.

| Final result | Enrolments | Median clicks, days 0–27 (middle 50%) | Median active days | No early click |
|---|---|---|---|---|
| Withdrawn (still registered on day 28) | 5,124 | 141 (52–298) | 8 | 5.9% |
| Fail | 7,044 | 103 (27–235) | 6 | 10.1% |
| Pass | 12,361 | 217 (96–421) | 11 | 1.6% |
| Distinction | 3,024 | 299 (130–575) | 14 | 1.0% |

Successful enrolments click more in the first four weeks than unsuccessful ones, with a Cliff's delta of 0.31
for clicks and 0.34 for active days (delta is the probability that a successful enrolment ranks higher minus the
probability that it ranks lower; about 0.33 is conventionally a medium effect). The effect holds in every module,
from 0.26 (AAA) to 0.48 (EEE), and collapsing exact duplicate rows (issue 1) changes it by at most 0.004, so the
duplicates do not affect this measure. In addition, module alone explains 21% of the variance of log early
clicks (η²), which confirms module as a required control. One pattern is worth a hypothesis: students who later
withdraw are more active early than students who later fail (median 141 against 103 clicks), so low early
activity marks future Fail more than future withdrawal among students still enrolled at day 28.

The chart below ranks the measures by how strongly they separate successful from unsuccessful enrolments across
all 32,593 enrolments (Cliff's delta; `signal_ranking`). Measures counted over the whole presentation lead
(assessments submitted 0.83, active days 0.80, total clicks 0.75), but they partly record the outcome, because
students who withdraw stop clicking and submitting. Among measures known by day 27, active days (0.50) and clicks
(0.47) in days 0–27 lead, followed by clicks before day 0 (0.36), which are available before teaching starts, and
the first assessment score (0.34). Background measures separate weakly: prior education 0.16, IMD band 0.15 and
studied credits −0.14 (a heavier workload goes with lower success). The early-window deltas here are larger than
the 0.31 of the equal-exposure comparison above, because they include students who left before day 28.

The first assessment is the clearest early signal. Of Withdrawn enrolments, 55.4% never submitted the first
TMA or CMA of their presentation, against 20.9% of Fail, 1.0% of Pass and 0.2% of Distinction; among those who
submitted, the first score separates success with a Cliff's delta of 0.34. This comparison mixes warning and
consequence: 3,089 Withdrawn enrolments left on or before day 0, and 22.8% of the withdrawals during the
presentation happen before the first due day, so their non-submission follows from leaving. A clean early-warning
measure counts non-submission only among students still registered on the due day (deep-dive analysis 3).

Assessment data have three further properties to plan around. First, only 6 of 24 exams have any score records
(DDD all four, CCC two of four), so exam performance is observable for two modules only (issue 7). Second, the
computer-marked assessments of BBB and GGG sit at a ceiling (median score 100), so their scores separate
students poorly. Third, late submissions are mostly a few days late: median 3 days, 90th percentile 9, 99th
percentile 29 (`assessments` in `results/descriptive.json`).

The mix of activity differs only slightly by outcome. Forum use (`forumng`) takes 28.8% of successful students'
early clicks against 24.6% for unsuccessful ones (+4.2 points), while quizzes (−1.7) and subpages (−2.0) take a
larger share for unsuccessful students (`activity_mix`).

### 5.3 Withdrawal over time

Withdrawal is spread over the whole presentation rather than concentrated at the start. Of the 29,403 enrolments
still registered on day 0, the Kaplan–Meier estimate shows 6.7% withdrawn by day 28, 10.7% by day 60, 16.1% by
day 120 and 23.7% by the end, with the rest censored at the presentation end; the 3,097 who left on or before
day 0 and the 93 withdrawals without a date are outside this curve (`survival`). Half of the in-presentation
withdrawals happen by day 73 (quartiles at days 26 and 142). Retention at day 60 ranges from 81.4% in CCC to
97.4% in GGG, and at the end from 62.9% to 91.0%.

Daily activity follows a weekly rhythm and peaks around assessments. Across the 22 presentations, the median
autocorrelation of daily clicks at a 7-day lag is 0.53, and the three days ending on a TMA or CMA due day carry
2.2 times the clicks of other days (median; 1.7–3.2 across presentations, highest in CCC) (`temporal`).

Withdrawal rose from 2013 to 2014 in all 9 module-semester pairs observed in both years, by 0.7 to 9.9 points
(largest in GGG J), while success changed by between −4.9 and +2.3 points (`temporal.year_on_year`). Year is
therefore a required control or split: a model fitted on 2013 and tested on 2014 faces a higher base rate of
withdrawal. B (February) presentations also succeed less than J (October) ones, 5.7 points crude and 3.9 points
within modules.

### 5.4 Repeat enrolments and course design

Of the 3,538 students with more than one enrolment, 1,081 pairs of enrolments run in the same presentation
period (concurrent modules) and 2,727 follow one another, 1,201 of them a repeat of the same module. The attempt
counter `num_of_prev_attempts` rises at every same-module repeat (1,201 of 1,201), so it is consistent with the
enrolment history. A repeat after Withdrawn or Fail ends in success 27.6% of the time (25.2–30.2%), well below
the 47.2% of all enrolments, and 615 of the 1,322 enrolments that follow a withdrawal (46.5%) end in withdrawal
again (`repeat_transitions`).

Use of the learning environment is concentrated in few sites. Of 6,364 VLE sites, 96 (1.5%) were never clicked,
while the top 10% of sites draw 86.9% of all clicks (Gini 0.90). Content pages (`oucontent`, 28.3% of clicks),
forums (20.1%), quizzes (17.6%) and the homepage (17.6%) carry most activity, whereas `resource` sites make up 42%
of all sites (2,660) but draw 2.8% of clicks. Presentations also differ in design, for example 5 TMA and CMA in
AAA against 11 in BBB 2013B, so site and assessment counts describe the module rather than the student
(`course_design`).

### 5.5 Distribution shape, correlation and redundancy

Activity is concentrated in a minority of enrolments: the top 10% generate 43% of all clicks (Gini 0.63), total
clicks have a skewness of 3.0, and 2,503 enrolments (7.7%) lie beyond the interquartile-range fence. These are
heavy users rather than errors, so the deep dive should keep them and use medians, ranks or a log scale; the log
transform over-corrects (skewness −1.2) because of the zero-click enrolments (`univariate`).

Three features duplicate one another or the outcome. Total clicks and active days correlate at Spearman ρ 0.95
(0.91 within the early window), so one of each pair is enough. The number of submitted assessments correlates
with the ordered outcome at ρ 0.74, but it partly records the outcome itself (withdrawn students stop
submitting), so it is usable as a predictor only when counted inside a fixed early window. In the source tables,
no column is constant, no text label differs only by case or spacing, and `vle.week_to` equals `week_from` for
99.1% of the sites that carry a week, so one of the two is enough (`structure`, `correlations`).

### 5.6 Confounding, interactions and multivariate structure

This subsection uses `results/multivariate.json` and `results/trajectory_clusters.csv`, written by
`code/04_multivariate.py`. The student and course dimensions are largely independent of one another, with two
exceptions that matter for comparisons (`dimension_associations`). Module and gender are strongly associated
(Cramér's V 0.60), which produces the gender reversal in Section 5.1. Module and year are moderately associated
(0.35), because not every module ran in both years (CCC only in 2014), so year comparisons need module as a
control. Of the 45 pairs, 9 reach V 0.10, and all except these two stay below 0.17.

The deprivation gradient is not explained by engagement or prior education. Among students registered on day 28,
the most deprived fifth succeed 17.9 points less often than the least deprived fifth; within tertiles of early
clicks the gap is 14.7 to 16.5 points (15.4 after standardising), and within education levels it is 14.2 to 24.9
points. Early engagement therefore accounts for about a seventh of the gap at most. The disability gap behaves
similarly (−10.7 points crude, −9.5 within engagement tertiles), except among the least engaged, where it narrows
to −5.1 (`stratified_gradients`).

The gradients differ in size between modules but not in direction: the deprivation gap ranges from −5.7 points
(AAA, the smallest module) to −22.2 (BBB), and the disability gap from −4.8 (GGG) to −19.7 (AAA). Year and
semester change them little (deprivation −20.5 in 2013 against −17.6 in 2014), and the early-engagement effect
is the same in both years (Cliff's delta 0.31 and 0.32) (`interactions`).

The measures known by day 27 carry several separate dimensions rather than one. A principal component analysis
on the ranks of 10 such measures needs four components to explain 64% of the variance: early engagement with
first-assessment submission (30%; it separates success with a Cliff's delta of 0.55), workload and history
(13%: studied credits, previous attempts, earlier registration; −0.14), background (11%: education, IMD band, age;
0.02) and registration timing with previous attempts (10%). As a result, background and engagement measures add
information to each other in a model rather than repeating it (`pca`).

Clustering the weekly click trajectories gives three groups, shown in the chart below (`trajectories`; k-means on
log clicks in weeks 0–37, with k chosen as the highest silhouette among 3–6 before the clusters were inspected).
A low-activity group (42% of enrolments) fades out within the first weeks and succeeds 8.6% of the time, a middle
group (33%) succeeds 63.2% and a sustained high-activity group (24%) succeeds 92.7%. The clusters describe a
continuum rather than distinct types (silhouette 0.26; k = 2 scored 0.36 but only separates active from inactive
students), and because the trajectories run to the end of the presentation they partly record withdrawal itself
(Cramér's V with the outcome 0.52). They therefore summarise engagement descriptively; an early-warning version
would cluster weeks 0–3 only.

## 6. Recommended dimensions and measures

- **Dimensions** (3–50 values): `code_module` (7), `code_presentation` (4), `assessment_type` (3),
  `activity_type` (20), `region` (13), `highest_education` (5), `imd_band` (10 + missing), `age_band` (3),
  `gender` (2), `disability` (2).
- **Outcome**: `final_result` (4 classes), often grouped as Pass/Distinction vs Fail/Withdrawn.
- **Measures**: assessment `score`, submission lateness (days after due), clicks per student × day aggregated to a
  window, days of activity, `num_of_prev_attempts`, `studied_credits`.
- **Time**: day offsets in `date`, `date_submitted`, `date_registration`, `date_unregistration`.
- **Join keys**: enrolment (`code_module`, `code_presentation`, `id_student`); `id_assessment`; `id_site`.

## 7. Recommended deep-dive analyses

1. **Early engagement and outcome, within module**: model success on days 0–27 active days and clicks with module
   and year as controls; the descriptive effect (Cliff's delta 0.26–0.48 by module, Section 5.2) sets the size
   to expect. Test the hypothesis that low early activity marks Fail more than withdrawal.
2. **Time to withdrawal**: extend the Kaplan–Meier description (Section 5.3) to a Cox or discrete-time model on
   `date_unregistration`, with Pass/Fail censored at the presentation end, module and year as strata, and
   first-assessment submission as a time-varying covariate (skills: `scikit-survival`, `statsmodels`).
3. **Assessment behaviour as an early signal**: missing or late first TMA/CMA against later Fail/Withdrawn,
   respecting module weighting rules (issue 4) and the due-day definition (issue 5).
4. **Socio-economic gradient**: outcome by `imd_band` and `highest_education`, controlling for module and
   region, with the missing band kept as a category; report the gender gap only within module, given the Simpson
   reversal (Section 5.1; `statistical-analysis`).
5. **Repeat attempts**: outcomes of the 3,538 students with several enrolments, separating prior attempts
   (`num_of_prev_attempts`) from banked results.

## 8. Descriptive methods applied

The checklist below records every descriptive method applied in this exploration, grouped by the `explore-data`
workflow step it serves, with the file that holds its output. Ticked items ran on the full data unless the item
says otherwise; unticked items are methods still to run before or during the deep-dive analyses (Section 7).

**Structure** (`results/overview.json`)

- [x] Row and column counts for all 7 tables, full read without sampling.
- [x] Grain and key uniqueness at the declared grain; exact duplicate full rows per table.
- [x] Column role classification (identifier, dimension, metric, temporal, boolean) for all 43 columns.
- [x] Range of every day-offset column (`temporal_ranges`).

**Column profile** (`results/columns.json`, `results/columns.csv`)

- [x] Missing count and rate, empty fields, `?` placeholder count, completeness band (complete ≥ 99%, mostly
  complete 95–99%, incomplete 80–95%, sparse < 80%).
- [x] Distinct count and cardinality ratio; top 10 and rarest 5 values for text columns.
- [x] Numeric summary: min, max, mean, standard deviation, percentiles 1/5/25/50/75/95/99, zeros, negatives,
  non-integers, mean-to-median ratio as a skew indicator.
- [x] Text format checks: length range and whitespace padding; label pattern of `imd_band` (`results/followups.json`).
- [x] Independent re-profile with K-Dense `tabular_profile.py` (`evidence/kdense_profile_*.json`; `studentVle` on
  its first 1,000,000 rows).
- [x] Distribution sensitivity of `score` (full) and `sum_click` (first 1,000,000 rows) to outliers and
  transformation (`evidence/kdense_sensitivity_*.json`).

**Quality and business rules** (`results/checks.json`, `results/followups.json`)

- [x] Duplicate characterisation of `studentVle`: exact duplicates, share by presentation, single-click share,
  click totals raw against collapsed.
- [x] Repeated student × site × day groups.
- [x] Range rules: score 0–100, activity before day 0 and after the presentation length.
- [x] Cross-column rules: Withdrawn against `date_unregistration`, unregistration before registration.
- [x] Assessment rules: weight sums per presentation and type, submissions after the due day and after the
  presentation end, assessments without a due day.
- [x] Missingness by group as a leakage screen (K-Dense `missingness_leakage_audit.py`,
  `evidence/kdense_leakage_studentInfo.json`).

**Relationships** (`results/checks.json`)

- [x] Referential integrity: 11 parent–child checks.
- [x] 1:1 alignment of the two enrolment tables.
- [x] Coverage: enrolments without VLE activity or assessment submission; students with several enrolments.

**Segments** (`results/segments.json`)

- [x] Outcome distribution overall, by module and by presentation period.
- [x] Total clicks per enrolment by outcome: median, interquartile range, zero-click count.
- [x] Weekly clicks per enrolment by outcome (week = day offset // 7).
- [x] Enrolments per presentation.

**Outcome relationships, time and withdrawal** (`results/descriptive.json`, `results/enrolment_features.csv`;
`code/02_features.py`, `code/03_describe.py`)

- [x] Enrolment-level feature table: one row per enrolment with outcome, demographics, registration, total and
  early-window (days 0–27) clicks and active days, raw and de-duplicated, submissions, scores, first assessment.
- [x] Univariate shape: skewness, excess kurtosis, log-transform skewness, outliers by the interquartile-range
  fence and by robust z-score (median absolute deviation) (`univariate.shape`).
- [x] Concentration of activity: Gini coefficient, top 10% and top 1% share of clicks (`univariate`).
- [x] Zero-variance columns, case or whitespace label collisions, redundant columns (`structure`).
- [x] Correlation matrix, Pearson and Spearman, of 17 enrolment measures (`correlations`).
- [x] Outcome by every dimension: row counts, success and withdrawal rates with Wilson 95% intervals,
  bias-corrected Cramér's V overall and within each module, Spearman ρ for ordinal dimensions
  (`outcome_by_dimension`).
- [x] Simpson's paradox check: crude against module-standardised gaps for six contrasts, with per-module gaps
  (`simpson`); the gender reversal recounted independently (`code/05_crosscheck.py`, `logs/05_crosscheck.log`).
- [x] Early engagement on equal exposure: by outcome, Cliff's delta overall and per module, robustness to
  duplicate rows, η² of module (`early_engagement`).
- [x] Assessment behaviour: score by module and type, submission rate by type, exams with scores, lateness
  quantiles, first assessment by outcome (`assessments`).
- [x] Activity-type mix of early clicks, successful against unsuccessful (`activity_mix`).
- [x] Daily series per presentation: days without activity, autocorrelation at lags 1, 7 and 14, click ratio
  around assessment due days (`temporal.per_presentation`).
- [x] Presentation drift: success and withdrawal by presentation and year-on-year change (`temporal.drift`,
  `temporal.year_on_year`).
- [x] Time to withdrawal: Kaplan–Meier retention overall and by module, withdrawal-day quantiles, withdrawals
  before the first due day (`survival`).
- [x] Missingness mechanism of `imd_band`: by region, against outcome (`imd_missingness`).
- [x] Measures ranked by separation of success, overall and within module, labelled by measurement window
  (`signal_ranking`).
- [x] Registration timing: registration day by outcome, outcome by registration band (`registration_timing`).
- [x] Repeat enrolments: concurrent and sequential pairs, attempt-counter consistency, outcome transitions
  (`repeat_transitions`).
- [x] Course design: sites by activity type, sites never used, click concentration across sites, assessment
  schedule (`course_design`).

**Cross-table consistency and accuracy** (`results/followups.json`; `code/01_profile.py`)

- [x] Clicks and submissions dated after the unregistration day (`activity_after_unregistration`).
- [x] Round-number heaping of scores by assessment type (`score_heaping`).

**Multivariate structure and confounding** (`results/multivariate.json`, `results/trajectory_clusters.csv`;
`code/04_multivariate.py`)

- [x] Association matrix of all student and course dimensions, bias-corrected Cramér's V (`dimension_associations`).
- [x] Stratified gradients: deprivation and disability gaps within engagement tertiles and education levels
  (`stratified_gradients`).
- [x] Interactions: deprivation gap, disability gap and early-engagement effect by module, year and semester
  (`interactions`).
- [x] Principal component analysis of the measures known by day 27, on ranks (`pca`).
- [x] K-means clustering of weekly click trajectories, k chosen by silhouette, clusters against outcome
  (`trajectories`).

**Still to run** (outside descriptive exploration; for the deep dive)

- [ ] Early-warning clustering on weeks 0–3 only, so that clusters do not record withdrawal itself.
- [ ] Calendar alignment of the 2014B two-day gap (issue 8) with an external source, if one exists.
- [ ] Inferential estimates with module, year and region as controls (Section 7).

## 9. Verification ledger

| Check | Expected | Method and evidence | Observed | Status |
|---|---|---|---|---|
| Source files are the pinned OULAD release | SHA-256 match | `scripts/fetch-datasets` verify against milestone 2 hashes | 7 of 7 CSVs match | PASS |
| Row counts read in full | no sampling | polars full read, `results/overview.json` | 10,900,970 rows across 7 tables | PASS |
| Key uniqueness at declared grain | 0 duplicates | `results/overview.json` | 0 for all six keyed tables | PASS |
| Referential integrity | 0 orphans | 11 checks, `results/checks.json` | 0 orphans in all 11 | PASS |
| Enrolment tables align | 1:1 | anti-joins both directions | 0 and 0 | PASS |
| Score range | 0–100 | `results/checks.json` | 0 out of range | PASS |
| Independent profile agrees | same counts | K-Dense `tabular_profile.py`, `evidence/kdense_profile_*.json` | rows and missing counts match (e.g. `imd_band` 1,111) | PASS |
| Leakage screen on enrolment table | report group missingness gaps | K-Dense `missingness_leakage_audit.py`, `evidence/kdense_leakage_studentInfo.json` | `imd_band` missingness differs by up to 5.5 pp across modules; split leakage not assessable without a split column | PASS (screen only) |
| Duplicate click rows characterised | size and spread known | `code/01_profile.py`, `results/followups.json` | 7.39% of rows, all 22 presentations, 3.19% of clicks | PASS; cause NOT VERIFIED |
| Simpson reversal (gender, withdrawal) | same figures from two code paths | `code/03_describe.py` against `code/05_crosscheck.py` on raw `studentInfo.csv` | per-module gaps equal to 0.01 point; crude 30.5% vs 31.7% | PASS |
| Duplicate rows do not drive the engagement effect | delta changes < 0.01 | early-window Cliff's delta raw vs exact duplicates collapsed, `results/descriptive.json` | 0.3112 vs 0.3093 overall; ≤ 0.004 per module | PASS |
| Survival population adds up | events = Withdrawn − no date − left by day 0 | `survival.population` | 10,156 − 93 − 3,089 = 6,974 | PASS |
| Attempt counter matches enrolment history | rises at each same-module repeat | `repeat_transitions` | 1,201 of 1,201 | PASS |
| Cluster count chosen before inspection | rule fixed in code | `code/04_multivariate.py` (highest silhouette, k = 3–6, seed 0) | k = 3, silhouette 0.26 | PASS (weak structure) |
| 2014B zero-click days are a logging gap | external calendar | same two days in all six 2014B presentations | consistent pattern | NOT VERIFIED (hypothesis) |

## Reproduce

From the repository root:

```bash
venv/bin/python scripts/fetch-datasets/fetch_datasets.py                       # OULAD, hash-verified
venv/bin/pip install -r datasets/oulad/exploration/requirements.txt
bash datasets/oulad/exploration/code/run_all.sh                   # every step, output in logs/
```

`run_all.sh` runs the pipeline stage by stage: dataset check, `code/01_profile.py` (structure, columns,
checks), `code/02_features.py` (one row per enrolment), `code/03_describe.py` (segments and Sections 5.1–5.5),
`code/04_multivariate.py` (Section 5.6), `code/05_crosscheck.py`, `code/06_kdense_audits.sh` (writes `evidence/`)
and `code/07_build_report.py` (writes `report.html`). It saves each stage's command, timestamp and console output in `logs/<stage>.log`; the stage
table is in `README.md`.

Skills applied: `data-analyst` (lifecycle stage and verification ledger), `explore-data` (structure, profile,
quality framework, relationships, recommendations) and `exploratory-data-analysis` (scripted profiles, leakage
and distribution-sensitivity audits in `evidence/`).
