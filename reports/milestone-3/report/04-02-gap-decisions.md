## 4.2. Data Gap Decisions and Synthetic Data

**Kinds of gap.** The brief separates three kinds of gap [1]. A missing value is a variable that exists but is empty
for some records, which can be analysed, kept as a category or imputed with a reason. A missing variable or concept is
something the dataset never collected, which must not be imputed or generated as if it were real; it calls for another
valid source or a revised question. A missing target means no outcome for supervised prediction. OULAD adds a fourth
case that looks like missing data but is not: a recorded absence, where a missing row itself records an event, such as
no click or no submission. Table 4.2 sorts the gaps of OULAD into these classes with the handling of each.

**Table 4.2. Missing values, recorded absences and missing variables**

| Class | Cases in OULAD | Evidence | Handling |
| :---- | :---- | :---- | :---- |
| Missing value | imd_band (1,111); registration day (45); TMA score (173); withdrawal day of 93 Withdrawn; due day of 11 exams | DQ04, DQ08, DQ11–DQ13 | "Missing" category for imd_band; indicators; no imputation in the prepared views; filling fitted on training runs only in model matrices; exams left out of task counts |
| Recorded absence | No click row; no submission row; empty unregistration day of students who stayed | DQ17; data descriptor | Zero counts after left joins; an empty unregistration day means the student did not withdraw |
| Missing variable | Year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity, the day a TMA mark was released | C04, C05, C08 | Not imputed or simulated; questions narrowed (AQ1–AQ3) or the contact part deferred (AQ4) |
| Missing target | None: final_result is present for every enrolment | Section 2.2 | Supervised target available |

**Adding another dataset.** The third step of the procedure, adding a compatible open dataset, does not close any
gap. None of the seven candidate datasets screened in Milestone 2 records contacts, attendance or year of study for
the same students, and joining a dataset of other students only because it shares a variable name is what the brief
rules out [1]. The questions were therefore narrowed and the contact part of AQ4 deferred, which is the brief's order
of priority [1].

**Synthetic data.** Of the five levels of synthetic data in the brief's policy, this project uses only level A, small
labelled test data for code [1]: a few hand-made test enrolments in the `tests/` folder of the Prepared Data Package
check that each feature formula gives the expected value. They never enter a prepared view, a statistic or a finding,
and no augmentation is planned; Appendix IV sets out the five levels and their conditions.
