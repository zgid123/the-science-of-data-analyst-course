## Appendix I – Data Understanding, Profiling and Quality Details

Figure A.1 shows the seven OULAD tables with their row counts and the keys that link them; each link was checked on the data (`understanding.json`).

![Figure A.1. Tables, row counts and keys of OULAD](assets/figures/fig-2-1-tables.png)

Figure A.2 shows weekly clicks per enrolled student by start month, with the two cut-offs at the end of weeks 2 and 4 (`fig_weekly_activity.csv`).

![Figure A.2. Weekly clicks per enrolled student by start month, with the two cut-offs](assets/figures/fig-3-2-weekly.png)

The inputs required by the brief, checked before preparation began, are listed in Table A.1 with their status.

**Table A.1. Inputs from Milestone 2 and their status**

| Input (brief) | Content in this project | Status |
| :---- | :---- | :---- |
| Milestone 1 baseline | Business Goal, SMART Goal, KPIs, AQ1–AQ4, analytics types and decisions, frozen with a SHA-256 checksum of each file; all 8 source files unchanged | Complete |
| Updated traceability matrix | KPI → AQ → data requirement → file → actual variables → coverage → decision | Complete |
| Raw data package | Seven CSV tables of OULAD, figshare version 1, DOI 10.6084/m9.figshare.5081998.v1, each matching its pinned SHA-256 | Complete, 7 of 7 match |
| Metadata and data dictionary | Column definitions from the data descriptor, license CC BY 4.0, citation | Complete |
| Collection evidence | Web address, DOI, access date 6 November 2026 (UTC+7), version, checksums, collection log | Complete |
| Controlled Change Log | C01–C08 with old and new content and data evidence | Complete |

Table A.2 sets out what each day field and measure of OULAD means and when it becomes known; the meanings come from the data descriptor and the OU's assessment policy, the counts from `understanding.json`.

**Table A.2. Meaning and timing of the key fields**

| Field | Meaning | Unit and scale | Known at |
| :---- | :---- | :---- | :---- |
| date_registration, date_unregistration | Days the student registered and unregistered; empty unregistration = did not withdraw | days from the start | the day itself |
| assessments.date | Cut-off (due) day of the assessment | days | from the start of the run |
| date_submitted | Day the student submitted; all 1,909 banked results carry −1, a placeholder | days | the day itself |
| is_banked | Result carried over from an earlier run | 0/1 | registration |
| score | Mark, 0–100; below 40 is a fail | points | TMA: tutor marking, usually within ten working days of the cut-off; CMA: automatic, within 7 days |
| weight | Share of the grade; exams 100, other assessments together 100 | % | from the start |
| sum_click | Number of interactions with one resource on one day | count | the day itself |
| studied_credits | Credits of all modules studied at the same time; 60 a year is part-time, 120 full-time | credits | registration |

Table A.3 lists the six sensitive attributes with their codes, smallest group and the number of module-run groups with fewer than 20 students.

**Table A.3. Sensitive attributes**

| Attribute | Codes | Smallest group | Run groups below 20 | Nature |
| :---- | :---- | :---- | :---- | :---- |
| gender | F, M | F: 14,718 | 0 | Personal |
| age_band | 0-35, 35-55, 55<= | 55<=: 216 | 18 | Personal |
| disability | Y, N (declared) | Y: 3,164 | 1 | Health-related |
| imd_band | ten deciles, blank | blank: 1,111 | 11 | Socio-economic, area-level |
| region | 13 regions | Ireland: 1,184 | 11 | Location |
| highest_education | five levels | Postgraduate: 313 | 29 | Socio-economic |

The Data Quality Issue Log in Table A.4 gives the full evidence of every issue of Table 3.1; P. refers to sections of `data/metadata/profile.json` and U. to `understanding.json`.

**Table A.4. Data Quality Issue Log with evidence**

| ID | Variable / table | Evidence | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: exact duplicate rows | 787,170 rows (7.39%) repeat another row in every column; 3.82–11.73% per run; 69.8% of duplicated groups are single-click; collapsing them removes 3.19% of clicks (P.duplicates). In two-row student-site-day groups, 31.5% have equal counts against 24.0% expected by chance from each site's own counts (Table A.6) | Click measures of AQ2 and AQ3 | Medium | Cause not decidable from the data: keep every row in the primary click measures (the table's record grain) and build a de-duplicated variant of each click feature for sensitivity |
| DQ02 | studentVle: grain differs from the documentation | 1,614,505 student-site-day groups hold several rows (3,810,465 rows), 1,179,074 of them with different click counts; up to 10 rows in one group (P.shape) | Any join or count at row level would mistake records for days | Medium | Aggregate clicks to enrolment × day and enrolment × week before any join; count active days, not rows |
| DQ03 | studentVle, studentAssessment: activity after unregistration | 29,440 click rows (98,745 clicks) by 1,279 enrolments, up to 423 days after unregistering; 588 non-banked submissions by 411 enrolments (P.validity) | Engagement up to withdrawal (AQ1, AQ2); none at a cut-off for students still registered | Medium | Truncate engagement measures at the unregistration day; feature views contain only students still registered at the cut-off, so no post-withdrawal event enters them |
| DQ04 | final_result × date_unregistration | 93 Withdrawn enrolments without an unregistration day, 87 of them in October 2014 runs; 9 Fail enrolments with one, 8 of them on or before day 0 (U.outcome, P.validity) | Populations at day 14, 13 and 27; time to withdrawal | Low | Keep final_result as the outcome; keep the recorded day; flag both groups (`withdrawal_day_missing`, `unregistered_not_withdrawn`); the 93 stay in every population because no record shows them leaving before a cut-off, and an evaluation flag lets test metrics be reported with and without them |
| DQ05 | studentRegistration: registration after day 14 | 58 enrolments registered on days 16–167, after the two-week sign-up window of the descriptor; 16 of them later unregistered (P.validity, check log T08) | KPI denominator and populations at cut-offs | Low | Define "enrolled at day d" as registered by day d (or registration day unknown) and not unregistered by day d; late registrants enter only the populations of later days |
| DQ06 | studentRegistration: departures before teaching | 3,097 enrolments unregistered on or before day 0; one unregistration on day 444 of a 268-day run (U.outcome) | KPI denominator | Low | Not an error: these students left before the run began and are outside the day-14 KPI population; the day-444 record is kept with a flag |
| DQ07 | studentAssessment: banked results | All 1,909 banked results carry date_submitted = −1, a placeholder for a result carried over from an earlier run (P.validity) | Timeliness and missed-task measures (AQ1–AQ3) | Medium | Exclude banked rows from submission timing, lateness and missed-task counts; keep a per-enrolment count of banked results, known at registration |
| DQ08 | assessments, studentAssessment: exams | 18 of 24 exams have no result rows (scores only for CCC 2 and DDD 4); 11 exams have no due day (P.missing, U.time) | "First missed assessed task" (AQ1); task signs (AQ2, AQ3) | High (exams) | Count missed and late tasks over TMA and CMA only; the outcome stays final_result; exam scores are not used |
| DQ09 | assessments: weights | Coursework weights sum to 0 in the three GGG runs and to 100 elsewhere; FFF CMAs weigh 0; CCC 2014 runs hold two exams (total 200) (P.validity, U.measurement) | Weighted score features | Medium | Build no weighted grade; count tasks unweighted (formative tasks are still due) and keep weight as a column |
| DQ10 | studentAssessment: late and post-run submissions | 49,318 of 169,138 non-banked submissions with a due day are late (29.2%; median 3, 99th percentile 29 days): 16,320 of 97,088 TMA and 32,991 of 69,956 CMA, although the OU's current (2025) policy accepts no CMA after its cut-off day; 85 fall after the run ended, up to day 608 (P.validity) | Late-task signs (AQ1, AQ2, early-sign rule) | Medium | Keep every submission; lateness = date_submitted − due day, counted separately for TMA and CMA because the meaning of a late CMA in 2013–2014 is not documented; post-run submissions fall after both cut-offs |
| DQ11 | studentAssessment.score | 173 missing scores, all TMA (P.missing); 45.8% of CMA scores are multiples of 10 against 17.4% of TMA (P.distribution) | Score features | Low | Keep the submission, leave the score missing; scores enter features only where the mark is known at the cut-off (decision matrix, row "Derived feature") |
| DQ12 | studentInfo.imd_band | 1,111 missing (3.41%), 40.1% of North Region and 22.5% of Ireland; success 65.7% when missing against 46.6% when present, so not missing at random; one label "10-20" lacks the % sign (P.missing, P.validity) | AQ4 fairness check by deprivation; background features | Medium | Normalise the label to "10-20%"; keep missing as its own category "Missing"; no imputation |
| DQ13 | studentRegistration.date_registration | 45 missing, 39 of them Withdrawn (P.missing) | Registration-lead feature | Low | Keep null with an indicator; any filling is fitted on the training runs only |
| DQ14 | vle.week_from, week_to | 82.4% missing; filled for 1,121 of 6,364 sites (P.missing, U.time) | None | Low | Not used |
| DQ15 | studentVle: days without any click | In all six February 2014 runs two consecutive days carry no click (days 218–219; days 211–212 in BBB) (P.temporal) | Daily activity series after week 30 | Low | Treat the two days as missing, not as zero activity, in daily series; both lie after the cut-offs |
| DQ16 | Outliers: clicks and credits | One row of 6,977 clicks; clicks per enrolment skewness 3.03, 2,503 enrolments beyond the upper interquartile-range fence; studied_credits up to 655 against a 99th percentile of 240 (P.distribution) | Scale-sensitive methods | Low | Keep every value (heavy users and students on several modules are real); log or rank transforms are applied in modelling, fitted on training runs |
| DQ17 | Enrolments without any activity or submission row | 3,365 enrolments without a click row (2,988 Withdrawn; 2,390 left by day 0); 6,750 without a submission (P.missing) | Counts would drop these students under an inner join | Medium | Absence of a row records no activity (descriptor: no submission, no result row): fill counts with 0 after left joins from the enrolment table |
| DQ18 | assessments: tasks due by the cut-offs | A non-exam task is due by day 13 in 1 of 22 runs and by day 27 in 16; two or more are due by day 27 in 1 run only (P.temporal) | AQ3 comparison rule and secondary KPI 1 ("two or more tasks missed or late by week 4") can fire in 1 run of 22 | High | Task 3 decision (AQ–Data fit): rule restated on the tasks actually due (Change Log C10) |
| DQ19 | Population and module mix | Seven UK distance-learning modules of 2013–2014, selected partly for many failing students; women 11.5% of EEE and 88.4% of BBB; completion in the day-14 population from 45.7% (CCC) to 73.8% (AAA) (P.representativeness) | Generalisation of every AQ; group comparisons | High (claims) | State the scope; compare groups within module; results describe OULAD and are re-checked on the university's data before decisions D1–D3 |

Thirteen figures of the profile were recounted by an independent exploration of the same files with separate code (`profile_crosscheck.csv`); Table A.5 shows the 13 measures compared, all equal.

**Table A.5. Cross-check with an independent recount**

| Measure | Independent recount | Milestone 3 profile | Equal |
| :---- | :---- | :---- | :---- |
| studentVle exact duplicate rows | 787,170 | 787,170 | yes |
| clicks raw | 39,605,099 | 39,605,099 | yes |
| clicks after collapsing duplicates | 38,343,063 | 38,343,063 | yes |
| repeated student-site-day groups | 1,614,505 | 1,614,505 | yes |
| rows in repeated groups | 3,810,465 | 3,810,465 | yes |
| enrolments without activity | 3,365 | 3,365 | yes |
| enrolments without submission | 6,750 | 6,750 | yes |
| late submissions | 49,318 | 49,318 | yes |
| submissions after run end | 85 | 85 | yes |
| click rows after unregistration | 29,440 | 29,440 | yes |
| enrolments with clicks after unregistration | 1,279 | 1,279 | yes |
| submissions after unregistration (incl. 13 banked rows dated day -1) | 601 | 601 | yes |
| click rows before day 0 | 688,988 | 688,988 | yes |

The chance test of duplicate click rows compares, in the 1,311,841 student-resource-day groups with exactly two rows, the share with equal click counts (31.5%) with the share expected by chance from each resource's own counts (24.0%) or from each activity type's counts (21.7%). Table A.6 gives the observed share for the six activity types with the most such groups.

**Table A.6. Equal counts in two-row groups by activity type**

| Activity type | Two-row groups | Equal counts observed |
| :---- | :---- | :---- |
| forumng | 895,551 | 32.8% |
| oucontent | 279,561 | 32.2% |
| quiz | 71,751 | 11.5% |
| ouwiki | 21,555 | 7.7% |
| questionnaire | 14,694 | 6.0% |
| oucollaborate | 11,921 | 59.6% |
