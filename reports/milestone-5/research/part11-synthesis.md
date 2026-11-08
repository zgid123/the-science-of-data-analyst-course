# Part 11 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 11-00-findings-overview.md

**External sources (T07):**
- Claims: C11-006 (regression used to capture association is descriptive, not causal; S900).
- Outline: supports the interpretation rules by analytics level (brief section 5): diagnostic findings stated as associations.
- Conflicts with the outline: None.
- Gaps: None.

## 11-03-aq2-findings.md

**External sources (T07):**
- Claims: C11-007, C11-008 (p-value is not effect size; decisions not on a threshold alone; S903).
- Outline: report AQ2 associations with effect sizes and intervals; p-values only as support.
- Conflicts with the outline: None.
- Gaps: None.

**Milestone evidence (T06):**
- Claims: C11-014.
- Outline: the 2014 replication of AQ2 is defined by the prototype contract (estimates and intervals per sign and module for 2013 and 2014) and happens only after the AQ3 test (C14; C9-043), so Section 11.3 reports the 2013 estimates only and names the replication as pending.
- Note: the AQ1 and AQ2 findings themselves come from task T08 (code/aq_analysis.py → results/), not from T06 claims; the AQ2 success criterion to apply is C9-008 and the AQ1 criterion C9-006.
- Conflicts with the outline: the sign "tasks missed in several modules at once" (C12) is described for the 2014 runs only, because only 12 of the 1,382 concurrent enrolments fall in 2013; with 2014 untouched it cannot be described in Milestone 5 and should be named "deferred with the 2014 replication".
- Gaps: None from T06.

## 11-05-decision-support.md

**External sources (T07):**
- Claims: C11-009, C11-010 (effectiveness needs a randomised or emulated trial; emulation fails without baseline confounders; S904), C11-011 (the OU's own evaluation warns against causal reading; S112).
- Outline: prescriptive options (D1–D3) are presented as hypotheses to test, e.g. by a randomised pilot of the contact decision.
- Conflicts with the outline: None.
- Gaps: None.

## 11-04-aq3-aq4-expected.md

**Milestone evidence (T06):**
- Claims: C11-001, C11-002, C11-003, C11-012, C11-004, C11-005, C11-013.
- Brief requirement (section 5; 4.2): AQ-by-AQ answers at the evidence level reached; for Level 1, AQ3 and AQ4 get "expected output" in the proposal tense, no metric.
- Outline: (1) AQ3 expected output: a risk score per enrolment at day 13 and day 27, used as a rank within the run, a probability only if S3 holds (C11-001); (2) AQ4 expected output: a ranked list per run of the size capacity allows with the signs behind each name; tutors decide (C11-002); (3) what result would answer them: gate S1 (model lists reach more non-completers than rule lists, interval above 0, sign-flip p < 0.05) and how it would be reported (C11-003, C11-012); (4) when probabilities may be shown (S3 bounds about 40–49% average risk) (C11-004); (5) AQ4 extra conditions: FR1 passes or flags reviewed, risk-need assumption untested, no claim about contact; fairness and sensitivity outputs (C11-005, C11-013).
- Conflicts with the outline: None.
- Gaps: None.

## 11-01-traceability-matrix.md

**Milestone evidence (T06):**
- Claims (cross-part, for the matrix columns): C8-031 and C8-013 (task, baseline, primary approach per AQ), C9-010 and C9-008 (evaluation per AQ), C8-001 (readiness), C7-012 and C7-009 (prepared variables), C12-009 (AQ4 decision supported without contact plan).
- Conflicts with the outline: Milestone 4's full traceability links AQ4 to "Secondary KPIs 1 and 2", while Milestone 3 (C08) measures secondary KPI 2 only in the pilot; the final matrix should mark the KPI 2 link as pilot-only (GAP for OULAD).
- Gaps: Final Status per AQ (Answered/Partial/Deferred/Dropped) is a team decision for T09.

## 11-02-aq1-findings.md

**Milestone evidence (T06):**
- Claims: C9-005, C9-006 (AQ1 card and success criterion), C8-009 (AQ1 expected output), C6-015 (KPI population and the 24.9–58.3% range by run, all 22 runs).
- Outline: the AQ1 results come from task T08 (code/aq_analysis.py → results/), not from T06; T06 supplies only the plan they must follow and the criterion they are judged by.
- Conflicts with the outline: the Milestone 4 AQ1 plan covers all 22 runs and both denominators (32,593 and 28,061), while the Milestone 5 decision (T04) computes new AQ1 rates on the 9 runs of 2013 only and compares years with the 2014 outcome shares that Milestone 3 already published; the section must state the narrower population and that the year comparison rests on published shares, not on new 2014 computation.
- Gaps: None from T06.

