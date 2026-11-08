## 5.1. Requirement–Data Fit and Question Status

The tables of Section 5 meet the core requirements of every question but none in full, so each question had to be set
against the real data before any analysis. The fit was rated twice, in sequence. Milestone 2 rated coverage from the
documentation and the structural check: Full when the data answer the question as stated, Partial when they answer its
core but not every clause, and None when they cannot answer it; all four questions were Partial, and the action part of
AQ4 was None. Milestone 3 then rated each question against the claim it carries after profiling the data: GREEN when
the variables, population, time window and quality are enough to answer it, YELLOW when the question must be narrowed,
its claim changed or data added, and RED when a key concept, variable, target or intervention is missing.

**The fit matrix.** Table 5.3 is the AQ–Data Fit Matrix in its final form. For each question it gives what the data
support, what is missing or weak, how the gap is handled, the revision action on the brief's scale and the final
status of Section 3.

**Table 5.3. AQ–Data Fit Matrix**

| AQ | Supported by OULAD | Missing or weak | Handling | Action | Final status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Final result of all 32,593 enrolments in 22 runs; due days of 182 TMA and CMA tasks and their submissions; registration and unregistration days | Year of study and delivery mode (every run is distance learning); exam results in only 2 of 7 modules | First missed task derived over TMA and CMA; comparisons by module, run, start month and year; population rule at day 14 (C09); computed on 2013 with the published 2014 counts (C15) | Modify + Defer | Partial |
| AQ2 | Daily click records; tasks due by day 27 in 16 of 22 runs; 1,382 enrolments in two runs at once, 1,370 of them in 2014 | Attendance; year of study and delivery mode; the several-modules sign in 2013 | Each sign derived with a formula and a time window; task signs only in runs with a task due; several-modules sign for 2014 only (C12); replication on 2014 after the AQ3 test (C14) | Modify + Defer | Partial |
| AQ3 | Target for every enrolment; 28,069 enrolled at day 13 and 27,535 at day 27; 9 module and start-month pairs in both years | A task-only rule fires in 1 run at day 13 and 16 at day 27; no day on which a TMA mark was released; one earlier run per module and start month | Early-sign rule restated with an inactivity part (C10); CMA marks used only when known by the cut-off; train on 2013, test once on all 13 runs of 2014 (C16) | Modify | Deferred |
| AQ4 | Ranking from the AQ3 scores; enrolment counts for capacity scenarios | Contacts, contact types, staff capacity and outcomes after contact | No compatible open dataset; rewritten to the ranking part (C11); judged by lift and normalised recall (C13); contact choice deferred to the pilot | Modify + Defer | Deferred |

**Kinds of gap and how each is handled.** Not every empty cell in OULAD is a gap of the same kind, and each kind
needs a different response. Table 5.4 sorts the gaps into four classes. A missing value is a variable that exists but
is empty for some records; a recorded absence is a missing row that itself records an event, such as no click or no
submission; a missing variable is something the dataset never collected, which must not be imputed or generated as if
it were real; and a missing target means no outcome for supervised prediction.

**Table 5.4. Classes of gap in OULAD and their handling**

| Class | Cases in OULAD | Handling |
| :---- | :---- | :---- |
| Missing value | Deprivation band (1,111 enrolments); registration day (45); TMA score (173); withdrawal day of 93 Withdrawn enrolments; due day of 11 exams | A "Missing" category for the deprivation band; indicators; no imputation in the prepared views; exams left out of task counts |
| Recorded absence | No click row; no submission row; empty unregistration day of students who stayed | Zero counts after joins; an empty unregistration day means the student did not withdraw |
| Missing variable | Year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity, the day a TMA mark was released | Not imputed or simulated; questions narrowed (AQ1–AQ3) or the contact part deferred (AQ4) |
| Missing target | None: the final result is present for every enrolment | Supervised target available |

**Why no other dataset is added.** Adding a compatible open dataset closes none of these gaps. None of the seven
candidates screened in Section 4.1 records contacts, attendance or year of study for the same students, and joining
data of other students only because they share a variable name would create links that do not exist. Synthetic data
are used only as small hand-made test records that check each feature formula in the code; they never enter a prepared
view, a statistic or a finding.

**Status entering the analysis.** After Milestone 3 every question had a prepared view, a fixed target and fixed time
rules: AQ1 and AQ3 were ready, AQ2 was ready for association only, and AQ4 was ready as a ranking with its contact part
deferred, so all the entry conditions for modeling held. The prepared data are split by year: the 9 runs of 2013 are
for development and the 13 runs of 2014 for the single final test. At day 27 the development runs hold 11,811
enrolments, of whom 5,245 (44.4%) did not complete, and the test runs hold 15,724 enrolments, whose outcomes remain
unopened until the AQ3 test.

**Which questions the data cannot support.** Three parts of the proposal cannot be answered with OULAD and need the
university's own records. The first is the contact part of AQ4: which contact, a message from a lecturer, a call from
the support office or a referral, works for which student, and whether contact raises completion; it is deferred to a
randomised pilot in which contacts and outcomes are logged. The second is every comparison by year of study, delivery
mode or attendance, which AQ1–AQ3 replace by comparisons by module, run and start month, and which the pilot can
restore. The third is secondary KPI 2 with the contact part of secondary KPI 1, which need the contact record. Within
OULAD, the several-modules sign of AQ2 exists only in 2014 and is deferred with the 2014 replication. No question is
dropped, because each keeps a core that the data answer. Section 6 examines the data behind these supported cores in
detail.
