## 6.2. Integration and Feature Construction

**Integration.** Integration starts from the enrolment table, which holds one row for each of the 32,593 enrolments,
and adds every other table through left joins after summing it to the enrolment, so that no enrolment is lost and no
row is multiplied. Each join is checked: the pipeline asserts that the number of rows after the join equals the
number before it, and all 25 joins kept their input rows. Clicks are summed by enrolment and day, then by week, as
the OU itself summarises clicks by week and by type of content for its early-warning work [9].

**Timing rule.** Every feature uses only records dated on or before its cut-off. A legitimate model may only build on
information that existed before its target was known, and records that are updated later without a time stamp are a
common route for information from the future to reach a model [10]. Activity before day 0 is kept as its own window,
because it is known before teaching starts. Features that need a mark use only CMA marks, for submissions made at
least seven days before the cut-off, since a CMA score is expected within seven days [3], a rule of 2025 assumed to hold for 2013–2014, while a TMA mark has no
release day in the data.

**Derived variables.** The derived variables cover the target, non_completion, a final result of Fail or Withdrawn
observed at the run end and never used as a feature; the populations enrolled at days 13, 14 and 27; the clicks before
day 0 and from day 0 to the cut-off c (13 or 27), the active days, the inactivity in the seven days ending at c and the
activity ratio against the run's median; the missed and late tasks by type; the mean score of CMAs submitted by c − 7;
the early-sign rule of C10 with a variant that adds CMA lateness; and the week of the first missed task for AQ1.
Appendix III (Table A.13) gives each with its formula, source fields and timing rule.

A task counts as missed only if it fell due on or after the student's registration day, and the activity ratio
compares a student with the median of the same run up to the same day, without any outcome. The feature views hold 20
primary and 10 extended predictors plus the weekly click counts; every other column is an identifier, the target, a
flag for evaluation, the rule or an audit attribute, and demographic attributes serve mainly the fairness audit,
because adding them to activity and assessment data did not significantly improve the prediction of students at risk
at the OU [9]. Appendix III explains these choices and lists the predictor sets.
