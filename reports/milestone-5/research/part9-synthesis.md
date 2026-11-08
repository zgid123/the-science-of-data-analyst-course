# Part 9 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 09-00-evaluation-design.md

**External sources (T07):**
- Claims: C9-029, C9-030, C9-031 (explain versus predict; rankings are predictions; explanatory power is not predictive power; S900).
- Outline: frame the evaluation design: AQ2 is diagnostic (association), AQ3 predictive (ranking judged out of sample).
- Conflicts with the outline: None.
- Gaps: None.

**Milestone evidence (T06):**
- Claims: C9-001, C9-002, C9-003, C9-004.
- Brief requirement (section 2, Part 9): metric, baseline, split/validation, success criterion, leakage/fairness/interpretability checks; evidence = Evaluation Plan; self-check "does the metric suit the goal and the class/data structure?".
- Outline: (1) evaluation fixed before any code runs, no metric chosen after results (C9-001); (2) the three properties of TRIPOD+AI (C9-002, with T07's C9-032–C9-034); (3) capacity and the main operating point 5 per 20 at day 27, close to the 28.8% rule rate (C9-003); (4) recall, precision and lift at fixed length replace F1 (C9-004).
- Conflicts with the outline: None.
- Gaps: None.

## 09-01-validation-success.md

**External sources (T07):**
- Claims: C9-032 (TRIPOD+AI 27-item checklist; S901), C9-033 (evaluation data separate from training, tuning and selection; S901), C9-034 (discrimination, calibration, utility; S901), C9-036, C9-037 (good discrimination is not enough; calibration slope 1, intercept 0; S902).
- Outline: justify the temporal split and the metric set (ranking metric plus calibration) by these reporting standards.
- Conflicts with the outline: None.
- Gaps: None.

**Milestone evidence (T06):**
- Claims: C9-005, C9-006, C9-007, C9-008, C9-043, C9-009, C9-014, C9-021, C9-010, C9-011, C9-022, C9-012, C9-013, C9-015, C9-016, C9-017, C9-018, C9-019, C9-020.
- Brief requirement: validation design and success criteria per AQ.
- Outline: (1) AQ1 card and success criterion: denominators, two aggregation paths agree, every rate with its interval (C9-005, C9-006); (2) AQ2 card: risk difference within run, 2013 estimation, 2014 replication only after the AQ3 test (C14), sensitivity runs; success = at least 5 points with an interval excluding 0 and same direction in two-thirds of modules (C9-007, C9-008, C9-043); (3) AQ3/AQ4 metric: normalised recall at capacity and its ceiling (46–100% per run) (C9-009, C9-014, C9-021); (4) success criteria fixed before testing: S1 single gate, S2 reported, S3 condition for probabilities, everything else sensitivity (C9-010, C9-011, C9-022, C9-012, C9-013); (5) validation design: unseen 2014 runs, repeat students kept, leave-one-run-out folds in 2013, challenger margin 0.03 and 7 of 9 folds, two freezes and one test, CCC and labels-available variant, paired two-level bootstrap and sign-flip test (C9-015–C9-020).
- Conflicts with the outline: None. Between milestones: the AQ1 card validates on 32,593 and 28,061 enrolments over all 22 runs (C9-005), while the Milestone 5 analysis (decision T04) uses the 9 runs of 2013; the AQ1 success criterion applies to the 2013 population, and the year comparison uses the 2014 outcome shares that Milestone 3 already published.
- Gaps: whether the AQ1 and AQ2 success criteria were met is a T08 result, not a T06 claim.

## 09-02-fairness-interpretability.md

**External sources (T07):**
- Claims: C9-035 (report performance with intervals per sociodemographic subgroup; S901), C9-038 (no audit without group membership data; S906), C9-039 (OULAD fairness study reproduced a 5–6 point gender disparity; S907).
- Outline: group audit of the ranking on OULAD's demographic fields is established practice and required by TRIPOD+AI.
- Conflicts with the outline: None.
- Gaps: None.

**Milestone evidence (T06):**
- Claims: C9-040, C9-041, C9-024, C9-025, C9-026, C9-023, C9-027, C9-028, C9-042.
- Brief requirement: leakage, fairness and interpretability checks.
- Outline: (1) leakage in evaluation: 2014 outcomes unopened until the single test, refitting inside folds, fold scores never reported as performance (C9-040, C9-041; data-side controls are in 07-01); (2) fairness: sensitive attributes only for audit because of proxies; separation as the one primary criterion; three confirmatory groups (disability 1,488, band 0–10% 1,486, missing band 610), 55+ "insufficient data, not cleared"; FR1 with Holm adjustment; a flag means human review (C9-024–C9-027); (3) error analysis slices (C9-028); (4) interpretability built in: reasons from the scoring model, no coefficient read as a cause, model card and datasheet (C9-042).
- Conflicts with the outline: None.
- Gaps: None.
