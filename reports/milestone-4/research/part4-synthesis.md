# Part 4 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 04-00-evaluation-design.md

**Claims:** C4-001, C4-031, C4-035, C4-042, C4-037, C4-048, C4-049

**Outline:**
- Open with the standard: TRIPOD+AI (2024) replaces TRIPOD 2015 and frames evaluation as discrimination, calibration and utility on data never used for development (C4-001).
- State why the design is fixed before modelling: leakage is widespread and inflates results, and corrected comparisons often erase claimed gains of complex models (C4-031, C4-035).
- Name the realistic architecture for student-success models: information available at the cut-off, testing on a later, disjoint run (C4-042).
- Introduce the two-step freeze (before training; before scoring the 2014 runs) and the self-control rule of not looking past the separation point (C4-048, C4-037, C4-049).
- Point to the cards (04-01), validation (04-02), metrics and success criteria (04-03), error and fairness checks (04-04).

**Conflicts with the outline:** None.

**Gaps:** Hofman et al. (S416) is an arXiv preprint (v1, 2023); present it as a proposal with a small qualitative study, not as a standard.

## 04-01-evaluation-cards.md

**Claims:** C4-003, C4-012, C4-016, C4-022, C4-024, C4-044, C4-039

**Outline:**
- Each Evaluation Design Card states, per AQ, the measures and their rationale, as TRIPOD+AI requires (C4-003).
- AQ3 card (risk scores): discrimination plus calibration intercept and slope, i.e. the ABCD set (C4-012, C4-016).
- AQ4 card (top-k at capacity): early-retrieval performance – recall and precision among the 3–5 flagged per group – chosen because contact is costly (C4-022, C4-044).
- Comparison row on every card: model against the rule and against contact-all/contact-none (C4-024).
- Fairness row: slicing by subgroup (C4-039), detailed in 04-04.

**Conflicts with the outline:** None.

**Gaps:** The card template itself comes from the course brief (S001), not from these sources.

## 04-02-validation-strategy.md

**Claims:** C4-002, C4-017, C4-042, C4-043, C4-025, C4-026, C4-051, C4-050, C4-027, C4-028, C4-029, C4-007, C4-009, C4-008, C4-032, C4-033, C4-034, C4-036, C4-037, C4-049, C4-005

**Outline:**
- Time split as temporal (external) validation: train on 2013 runs, test on 2014 runs, the stronger test of transportability; future-run performance is usually lower than same-run, so the 2014 estimate is the honest one (C4-002, C4-017, C4-042, C4-043).
- Grouped folds inside 2013: students are nested in runs, random folds underestimate error; leave-one-run-out (each block its own fold) via LeaveOneGroupOut, with the extrapolation caveat (C4-025, C4-026, C4-051).
- Tuning and selection only inside the folds, with preprocessing in a pipeline; nested selection because the tuned fold score is optimistic (C4-050, C4-027, C4-028, C4-029, C4-007).
- Leakage checklist mapped to the design: L1 separation, L2 predictor legitimacy at day 13/27, L3 temporal order and non-independence (C4-009, C4-008, C4-032, C4-033, C4-034, C4-036).
- Single use of the test runs and frozen plan (C4-037, C4-049); evaluation sample size stated (C4-005).

**Conflicts with the outline:** EXECUTION_PLAN line for 04-02 says "leave-one-run-out folds grouped by student inside 2013". The sources (C4-051, C4-034) require that no group appear in both training and validation folds; OULAD students can register on more than one module run, so leave-one-run-out folds alone may place the same student in training and validation folds (and in both 2013 training and 2014 test). The team should decide whether to group by run, by student, or check and report the overlap.

**Gaps:** No learning-analytics study comparing grouped and random folds was fetched (evidence is ecological, S406). The size of the selection bias with thousands of students is not quantified (S408 is a 40-sample setting).

## 04-03-metrics-success.md

**Claims:** C4-003, C4-010, C4-011, C4-019, C4-012, C4-013, C4-014, C4-015, C4-006, C4-020, C4-021, C4-022, C4-044, C4-018, C4-023, C4-024, C4-038, C4-045, C4-052, C4-053, C4-030, C4-046, C4-047, C4-004, C4-048

**Outline:**
- Measures and rationale (C4-003, C4-010): discrimination is not enough; calibration (intercept, slope, curve; Brier score) because a base-rate model is perfectly calibrated but useless (C4-011, C4-019, C4-012–C4-015); recalibration after any imbalance correction (C4-006).
- Gain over base rate and recall at capacity: precision and PR-AUC read against the base rate P/(P+N); top-k (early retrieval) because contacts are limited and costly (C4-020, C4-021, C4-022, C4-044).
- Comparison with the rule: usefulness over a range of thresholds, net benefit against contact-all/none and the rule (C4-018, C4-023, C4-024).
- Uncertainty: paired comparison on the same students (McNemar for one-shot decisions), run-then-student bootstrap for intervals because students are nested (C4-038, C4-045, C4-052, C4-053).
- Success criteria fixed in advance with a minimum practically relevant gain; small average gains are not wins (C4-030, C4-046, C4-047, C4-048); intervals reported overall and by subgroup (C4-004).

**Conflicts with the outline:** (1) The card framed RQ3 as "precision–recall versus ROC under imbalance"; with non-completion near 44–45%, the OULAD target is close to balanced, so Saito & Rehmsmeier's imbalance argument (C4-021) applies weakly; PR-AUC and precision are still justified by the base-rate baseline and by top-k contact (C4-020, C4-022). (2) Net benefit and decision curves (C4-023) are defined over probability thresholds, while the AQ4 action is a fixed top 3–5 per tutor group; using net benefit needs a stated exchange rate between a missed and an unnecessary contact.

**Gaps:** DeLong's test for correlated AUCs (card RQ6) was not fetched (paywalled Biometrics 1988); AUC comparison uncertainty can come from the paired cluster bootstrap (S418). Behaviour of the bootstrap with only 13 test runs is not studied in S418. No source gives a numeric minimum gain for education early warning; the team must set and justify it.

## 04-04-error-fairness.md

**Claims:** C4-039, C4-040, C4-041, C4-004, C4-013, C4-052

**Outline:**
- Aggregate metrics hide subgroup effects; slicing analysis evaluates the frozen model per subgroup (C4-039).
- ABROCA as the threshold-free summary of differential discrimination, with why AUC differences can cancel (C4-040); unfairness varies with algorithm and features, with no strict trade-off (C4-041).
- Add operating-point checks at capacity (subgroup recall and precision at top 3–5) and subgroup calibration, with intervals (C4-004).
- Small-group handling: a calibration curve needs about 200 events and 200 non-events; below that report only intercept and slope or merge groups (C4-013); intervals by run-then-student bootstrap (C4-052).

**Conflicts with the outline:** ABROCA (C4-040) is threshold-free, whereas the decision uses one operating point (top 3–5 per group); the outline's "subgroup and fairness checks" should therefore pair ABROCA with subgroup recall/precision at capacity. Also, S413 states ABROCA's range is "practically restricted to the interval [0 .5, 1]", which is inconsistent with its definition as the area between two ROC curves; the report should not repeat that range.

**Gaps:** No fetched source gives sampling uncertainty or a significance threshold for ABROCA. Fairness criteria theory (which parity notion to target) belongs to T07 (Part 5).
