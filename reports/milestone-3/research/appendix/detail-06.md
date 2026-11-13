**Why a ranking is needed.** The early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27,
while lists of 3 or 5 per group of 20 students hold 15% or 25% of them. The rule names more students than a list of 5
per 20 can hold in 7 of the 22 runs at day 13 and in 10 at day 27, and more than a list of 3 per 20 can hold in 15 runs
at day 13 and in all 22 at day 27. Staff therefore need an order of whom to contact first, which is what AQ3 and AQ4
provide; the rule alone cannot set it.

**Before-and-after checks explained.** The paragraphs below explain two results of Table 7.1 and the checks beyond it.

Two results need a word of explanation. The number of enrolments without a click row rises from 3,365 in the raw data
to 3,554 in the prepared view, because clicks after withdrawal are left out, so 189 students whose only activity came
after they unregistered now show none. The leakage check is built so that it can fail: if a feature used any click
after its cut-off, the feature would equal an unfiltered recount for every student, and the check would find no
difference for the students who clicked later.

Beyond the recount of every feature row, nine unit tests on synthetic test enrolments confirm each formula, and one
row was recounted by hand from the raw files: a TMA due on day 19 and submitted on day 24, with 168 clicks over 10
active days by day 27, matches the prepared view.

Table A.20 gives the state of each of the six conditions that the brief sets for starting Milestone 4.

**Table A.20. Entry conditions for Milestone 4**

| Condition | State |
| :---- | :---- |
| Core AQs have a prepared view with clear traceability | AQ1–AQ3 views ready; AQ4 ranking view ready, with the action part deferred (Appendix IV) |
| Target, features and dimensions stable | Defined in the feature specification and the data dictionary; 9 of 9 formula tests pass |
| Leakage and split defined for predictive tasks | Split and leakage specification; V11–V13 and V15 pass |
| Important quality issues handled or kept on purpose | DQ01–DQ19 each with a decision; residual risks stated (Section 7.3) |
| No synthetic data as evidence | Only labelled level A test enrolments |
| Prepared data reproducible from raw | Two runs from the raw files; 8 of 8 data files identical |

**Residual risks in full.** The paragraphs below explain the five residual risks that Section 7.3 lists.

(1) **Duplicate click rows.** The exact duplicate rows may be copies made by the logging system or repeated visits.
The de-duplicated twins of the click features bound their effect: they would remove 3.19% of all clicks.

(2) **Late CMAs and CMA marks.** The meaning of a late CMA in 2013–2014 is not documented, and the OU marking policy
on record dates from 2025 [3]. The early-sign rule therefore uses TMA lateness, and a variant that adds CMA lateness
is kept for comparison; with CMA lateness, the rule would flag 41.2% of enrolments at day 27 instead of 28.8%. CMA
marks known by the cut-off exist for only 1.4% of training rows at day 13 and 5.2% at day 27, below the 10% coverage
that we require before the CMA score enters the predictor set of Milestone 4, so the score is prepared but not
used.

(3) **Uncertain records.** 93 Withdrawn enrolments have no withdrawal day, and 1,962 test enrolments belong to students
seen in 2013. Both groups are flagged, so that test results can be reported with and without them.

(4) **The KPI is a proxy.** Completion of a module run stands for completion of a course, and leave or transfer cannot
be told apart from withdrawal in OULAD. The effect of the uncertain records on the KPI is small: without the 138
enrolments flagged for an unknown withdrawal day (93) or registration day (45), completion at day 14 is 54.9% instead
of 54.7%.

(5) **Assumed capacity.** The OU splits each module into tutor groups of a few tens of students [9], and the capacity
scenarios assume that one lecturer-advisor's caseload is one such group of 20 students. Each list then holds three or
five students per group, the weekly range that Milestone 1 sets for a lecturer-advisor, for the week after its review
point; for the support office, the scenarios use 30 or 40 students per run at each review point, the weekly range that Milestone 1 sets for
that office. The real caseload at the university may differ, so list sizes are scenarios,
not plans.
