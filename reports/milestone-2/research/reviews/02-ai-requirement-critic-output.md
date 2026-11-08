# AI requirement critic output (T07)

Role: "Requirement critic" (brief section 12). Inputs read: `final-project/milestones/02/milestone-2.md`,
`research/baseline/m1-baseline.md`, `research/requirements/data-requirements.md`. No dataset, exploration result
or web source was consulted. The team decides on each point and records its rationale.

1. **Withdrawal date is required by AQ3 but only nice-to-have in the gates.**
   Passage: AQ3 "plus the date of withdrawal to tell who is still enrolled at each cut-off"; section 5 "Nice-to-have: several courses; withdrawal date".
   Problem: AQ3's population ("students still enrolled at the data cut-off"), the section 3 leakage rule ("activity logged after a student's own withdrawal date") and AQ1's minimum variables all depend on the withdrawal date. G1 asks only for a final result that separates withdrawal, so a dataset with a withdrawal label but no date passes every gate.
   Why it matters: without the date, the cut-off population cannot be built. Students who had already withdrawn by week 2 would count as easy positives, which inflates recall against the simple rule. Either make a dated withdrawal part of G1/G2, or state in advance that AQ3 drops to Partial coverage without it.

2. **G2 accepts "dated activity" alone, so a passing dataset could lack the AQ3 comparator and KPI 1.**
   Passage: G2 "dated assessed tasks and submissions, or dated activity".
   Problem: the AQ3 benchmark ("two or more assessed tasks missed") and Secondary KPI 1 ("two or more tasks missed or late by week 4") both need task due dates and submission dates. Activity logs alone cannot produce either. The gate also does not require that any assessed task falls due before the end of week 2 or week 4.
   Why it matters: a dataset with clicks but no early-due tasks passes G2, yet AQ3's comparison against the simple rule cannot be made and KPI 1 cannot be computed. Consider splitting G2 into "dated tasks and submissions" (must-have) and "dated activity" (must-have for AQ2's activity sign). Add the condition "tasks due within the first four weeks".

3. **The KPI denominator is not fully specified, and the gates do not check it.**
   Passage: AQ1 "Optional variables: … student status (approved leave, transfer) to apply the withdrawal definition"; section 4 "the right denominator (enrolled after add-drop)".
   Problem: the primary KPI is "Passed ÷ enrolled after add-drop … leave and transfers excluded". This needs two inputs that are missing or optional: (a) the add-drop deadline and each enrolment's registration and unregistration dates, to know who was enrolled after add-drop; (b) a way to tell course withdrawal apart from leave or transfer. Neither appears in the minimum variables or in G1.
   Why it matters: if withdrawals that are really leave or transfer stay in the data, or early drops are counted, non-completion is overstated, and the 70% baseline that AQ1 is meant to recount is wrong. At minimum, list "enrolment start and end dates relative to the add-drop deadline" as a minimum variable. Record in advance that any leave/transfer distinction left out is a known deviation from the KPI definition.

4. **Year of study and delivery mode are optional, but the frozen AQs and the AQ4 constraint require them.**
   Passage: AQ1 "Optional variables: Delivery mode; year of study"; AQ3 "Optional variables: Year of study (first-year against later-year comparison)".
   Problem: the frozen AQ1 asks for shares "by course, delivery mode and year of study". AQ2 asks whether differences hold "across … delivery modes and years of study". AQ3 compares first-year and later-year students. AQ4 has the hard limit "keep first-year recall within ten points of later-year recall".
   Why it matters: if these are optional, a dataset without them passes and parts of three AQs, plus one AQ4 constraint, become unanswerable without being flagged. Mark them as minimum for the AQs that name them, or record now which AQ clauses become Partial without them, so the outcome is a controlled revision and not a silent one.

5. **G3 (three semesters) conflicts with AQ1 (four semesters) and does not require time order.**
   Passage: G3 "at least three semesters (or course runs) of the same courses"; AQ1 "At least four consecutive semesters".
   Problem: the frozen AQ1 covers "the four semesters of 2024–2025 and 2025–2026", but the gate admits three. In addition, "or course runs" accepts runs that may be parallel and not sequential, while AQ3's time-based validation needs a run that starts later than the training runs.
   Why it matters: a three-run dataset passes, but AQ1's trend over four semesters is only partly covered. Parallel runs also allow a train/test split with no real time ordering. State the AQ1 consequence of three runs, and require "ordered in time, with at least one later run for testing".

6. **Some leakage paths are not in section 3.**
   Passage: section 3 "Features allowed before the point … Fields unavailable / leakage risk …"; AQ2/AQ3 "LMS activity per week relative to the course's own average".
   Problem: the following are missing:
   (a) the "course's own average" computed over the whole semester or the whole cohort (including test-run students and later weeks) leaks information from after the cut-off;
   (b) a task due before the cut-off can have its mark or grading date after the cut-off, so the concept "date the score became known" is needed, not only the due date and submission date;
   (c) "study load" and concurrent courses measured at semester end include drops that happen after the cut-off;
   (d) "background known at enrolment" may be values updated later;
   (e) normalisation or encoding fitted on all semesters before the time split.
   Why it matters: each one raises held-out recall without being visible, and section 16 of the brief requires an explicit leakage check. Add these lines to the "Fields unavailable" column.

7. **AQ1 and AQ2 timing does not handle withdrawal occurring before the sign (reverse order and censoring).**
   Passage: AQ1 "week of the first missed assessed task"; AQ2 "Missed and late assessed tasks in weeks 1–4".
   Problem: after a student withdraws, every later task is "missed" by definition. For withdrawers, the first missed task can therefore be a result of withdrawal and not an early sign, and AQ2 associations then partly measure the outcome itself. The requirements give no rule for counting only tasks due before the student's withdrawal date, or for excluding students who withdrew within weeks 1–4.
   Why it matters: AQ2's ranking of signs, and AQ1's comparison of the first missed week between groups, would be biased toward the "missed task" sign. This also reinforces critique 1: the withdrawal date matters for the descriptive and diagnostic AQs too.

8. **Week numbering and the data delay are not specified as concepts.**
   Passage: AQ2 "Weeks 1–4 of each semester at day or week granularity"; section 3 "End of week 2 (data cut-off; list reaches staff in week 3)".
   Problem: "week 1" needs a course or semester start date (an anchor) so that event dates can be converted to weeks, and that anchor is not in any minimum variable list. The baseline also records "About one week of delay (DO4)", but section 3 treats data up to the end of week 2 as available when the list is built.
   Why it matters: without an anchor, cut-offs cannot be applied the same way across runs. If the one-week delay is ignored, the offline evaluation uses fresher data than staff will have, which overstates AQ3 accuracy. Add "course start date" as a minimum variable, and either state the delay assumption or evaluate a delayed cut-off as a sensitivity case.

9. **No gate requires stable, linkable identifiers across tables, courses and semesters.**
   Passage: AQ2 "missed tasks in several courses in the same semester … course membership of each student in the same semester"; AQ3 "prior attempts, study load".
   Problem: concurrent-course signs and prior attempts need the same pseudonymous student identifier across courses and semesters. Joining results, tasks and activity also needs shared keys. G5 asks only for pseudonymised data, and pseudonymisation done per course or per file would break these links.
   Why it matters: one AQ2 sign and two AQ3 features would disappear even though the dataset passes every gate. Add the linkage condition to G1 or as a separate gate. Otherwise, record now that these features are conditional.

10. **No requirement covers volume or target distribution.**
    Passage: section 4 "Labelled outcome, predictors timestamped … enough semesters".
    Problem: the brief's predictive row asks for "đủ historical cases; target distribution". AQ3 reports recall and precision by group (first-year against later-year, by course), and AQ4 sets a precision ≥ 50% and a ten-point recall gap. No minimum number of enrolments, or of non-completers per group and test run, is stated.
    Why it matters: a small dataset could pass every gate but give unstable group recall, so the AQ4 fairness constraint cannot be checked. State a minimum count (for example of non-completers per group in the test run) as a requirement, or as a condition attached to the AQ3/AQ4 claims.

11. **AQ4 mixes data with assumptions and leaves out who contacts whom.**
    Passage: AQ4 "Minimum variables: AQ3 outputs; capacity figures; a contact record …"; "Decision inputs: … routing options".
    Problem:
    (a) capacity (3–5 per lecturer-advisor, 30–40 for the support office) is a baseline assumption, not a data requirement, and should be labelled that way;
    (b) applying the capacity limit needs the assignment of each student to a lecturer-advisor, which is not listed;
    (c) the AQ3 unit (student–course–semester) and the AQ4 unit (student per review point) differ, with no rule for students listed in several pilot courses;
    (d) the contact record is listed as minimum even though the baseline says it "does not exist (AD7, VCL4)", so the gap should be declared up front (brief section 11.1: keep as a future decision requirement);
    (e) routing to student affairs for "financial or personal support" implies sensitive attributes that the ethics row does not cover.
    Why it matters: without these, AQ4 can be overclaimed as prescriptive, against the brief's warning in section 6, and D1's list-length logic cannot be evaluated.

12. **Some wording still reads as columns or system names, not concepts.**
    Passage: AQ1 "withdrawal flag and date"; AQ3 "registration information"; AQ2 "dated LMS activity".
    Problem: "flag" describes a field type, not a concept (the concept is "course withdrawal event and its date, as distinct from leave or transfer"). "Registration information" is vague: does it mean the enrolment date, the add-drop status or the number of attempts? "LMS" names a system, where the concept is "online learning activity events". The pass/fail/withdrawal outcome also does not say how any additional outcome grades (such as a pass with merit) map to completion.
    Why it matters: vague or system-flavoured terms let a candidate dataset's fields be matched loosely, which is the backward-fitting the brief forbids in section 5. A precise concept also makes the Task 7 traceability "Coverage" judgement defensible.
