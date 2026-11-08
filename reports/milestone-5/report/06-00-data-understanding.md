# 6. Data Understanding and Data Quality

The requirement–data fit of Section 5 established that OULAD can carry the four final questions once each is measured on module runs and enrolments; before any question is answered, the data themselves must be understood well enough to know which of their features could change a conclusion. Milestone 3 profiled every raw table for this purpose (Milestone 3, Sections 2–3), and its findings are restated here in the terms the analysis uses: the unit, the outcome, time, the balance of the outcome and the shape of the main measures. Section 6.1 then turns the profile into quality findings, and Section 6.2 covers temporal coverage, representativeness and the sensitive fields.

**Unit and keys.** OULAD holds 22 module runs of seven Open University (OU) modules from 2013 and 2014, with 32,593 enrolment records that belong to 28,785 distinct students. The unit of analysis is the enrolment, one student in one module run, because the outcome, the dates and the assessed tasks are all recorded per enrolment; finer tables, such as the daily click records, are summed to the enrolment before they are joined to it. The six tables that carry a key have no duplicate key, and no row of a child table lacks its parent row; only the click table, which records platform activity, has no key at all. The profile ran on all 10.9 million rows of the seven raw tables rather than on a sample, and thirteen of its figures were recounted independently by separate code, with all thirteen in agreement.

**Outcome and time.** The final result is recorded at the end of each run as Pass (12,361 enrolments), Withdrawn (10,156), Fail (7,052) or Distinction (3,024). We define non-completion as Fail or Withdrawn and completion as Pass or Distinction, so the target joins two different ways of not finishing. The joint target is kept because the primary KPI counts both a fail and a withdrawal as non-completion (Section 2.1), and AQ1 reports the two outcomes separately (Section 11.2). Time is counted in days from day 0, the official start of each run, and week n covers days 7(n−1) to 7n−1. The two data cut-offs of decision D1, whom the course lecturers, lecturer-advisors and the support office contact first at each review point, are therefore day 13, the end of week 2, and day 27, the end of week 4.

**Outcome balance.** Of the 28,061 enrolments still registered at day 14, the population of the primary key performance indicator (KPI), 54.7% completed. Among the enrolments registered at the cut-offs, non-completion is 45.3% at day 13 and 44.2% at day 27, and it ranges from 24.9% to 58.3% between runs in the KPI population; even the smaller class holds at least 92 enrolments in every run. The classes are therefore close in size, and no resampling or reweighting is needed for any question. The mix of non-completion differs by module: withdrawal is highest in the CCC runs, at 43–46%, while GGG has the fewest withdrawals but the most failures, so a single non-completion rate hides different patterns that AQ1 reports separately.

**Distributions.** Activity is strongly skewed: the median enrolment has 602 clicks, 3,365 enrolments have none, 2,503 lie beyond the upper fence of the interquartile range, and a single record of one student on one resource on one day reaches 6,977 clicks. Scores lean the other way, with a median of 80, and 45.8% of computer-marked assessment (CMA) scores against 17.4% of tutor-marked assignment (TMA) scores fall on a multiple of ten, which reflects how the two kinds of task are marked. Study load reaches 655 credits against a 99th percentile of 240. These shapes decide the encoding of Section 7.1: counts enter models as logarithms, and no value is removed.

**The development population.** The analyses of Milestone 5 and the proposed models use the 9 runs of 2013 as development data and keep the 13 runs of 2014 for a single test (Section 9.1). Table 6.1 gives the populations that every later number refers to, with the outcome share where it is used.

**Table 6.1. Populations of the 2013 development runs and the 2014 test runs**

| Population | Definition | Enrolments | Non-completers | Used by |
| :---- | :---- | :---- | :---- | :---- |
| All 2013 enrolments | Every enrolment of the 9 runs of 2013 | 13,529 | 6,959 (51.4%) | AQ1, second denominator |
| 2013, registered at day 14 | KPI population rule applied to 2013 | 12,076 | 5,515 (45.7%) | AQ1, primary denominator |
| 2013, registered at day 13 | Population at the first cut-off | 12,080 | 5,519 | AQ3 development, day 13 |
| 2013, registered at day 27 | Population at the second cut-off | 11,811 | 5,245 (44.4%) | AQ2; AQ3 development, day 27 |
| 2013, day 27, runs with a task due | The 7 runs of 2013 with a task due by day 27 | 9,960 | – | AQ2 task-based signs |
| 2014 test, registered at day 13 | 13 runs of 2014 | 15,989 | not opened | AQ3 and AQ4 test, day 13 |
| 2014 test, registered at day 27 | 13 runs of 2014 | 15,724 | not opened | AQ3 and AQ4 test, day 27 |

The 2014 outcomes stay unopened in every row, because they form the independent test of the predictive question (Section 9.1). Which data problems could change a conclusion drawn from these populations is the question Section 6.1 answers, issue by issue.
