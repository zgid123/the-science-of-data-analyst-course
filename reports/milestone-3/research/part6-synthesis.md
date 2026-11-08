# Part 6 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 06-02-integration-features.md

**Claims:** C6-005, C6-006, C6-008, C6-010

**Outline:**
- Weekly VLE features follow the Open University's own design: daily clicks aggregated to weekly counts per activity type and weekly active/inactive flags (C6-005, S602).
- Every feature is computed only from records dated before the prediction point (day 13 or day 27): the no-time-machine requirement (C6-008, S606).
- Fields filled or updated after the cut-off without their own time-stamp (for example the unregistration date, final result, late assessment rows) are excluded or truncated at the cut-off, because untime-stamped updates are the usual route for leakage (C6-010, S606).
- Demographic fields enter as candidate features and audit attributes; earlier OU work found little predictive gain from demographics over VLE and assessment data (C6-006, S602, reporting Wolff et al. 2013), which supports keeping them mainly for the fairness audit (Part 9).

**Conflicts with the outline:** None.

**Gaps:** The OU's exact feature list for OU Analyse (Kuzilek et al. 2015, S601) is not readable; S602 is an earlier (LAK '14) description. Feature specifics in the report must come from the team's own scripts.

## 06-03-split-leakage.md

**Claims:** C6-007, C6-011, C6-008, C6-009, C6-001, C6-002, C6-003, C6-004, C6-013, C6-014, C6-012

**Outline:**
- Define leakage: information about the target that would not legitimately be available at prediction time; it inflates estimated performance (C6-007, S606; C6-011, S607).
- Cut-off rule: features use only data from before day 13 / day 27 (C6-008); avoidance by time-stamps and a learn-predict separation, which in the time case is a cut in time between training and evaluation data; leakage can also enter through training examples (C6-009).
- Time split mirrors the OU practice: OU Analyse trains and validates on previous presentations and predicts the running one, weekly, against the next assignment (C6-001, C6-002, C6-003); Ouroboros (C6-004, S600) is the exception for courses without a previous run. The team's train 2013 runs → test 2014 runs follows the same logic.
- Entity rule: a student with several registrations is a group; keep all of a student's rows on one side (C6-013) and evaluate on future observations rather than random folds (C6-014).
- Transforms (imputation, scaling, encoding, selection) are fitted on the training partition only, after the split, inside a Pipeline (C6-012, S607).

**Conflicts with the outline:** None. Note for the human (not a conflict): the OU trains on the previous presentation of the same module and predicts the next one, while the team's split pools all 2013 runs for training and all 2014 runs for testing; this is consistent in spirit but not identical (some modules have no 2013 run).

**Gaps:** The OU sources on disk do not explain why legacy data may differ from the current presentation (drift); the Ouroboros full text (S600), which would, is blocked (HTTP 403). No education-specific source on time-based validation was fetched; S608 is general scikit-learn guidance.
