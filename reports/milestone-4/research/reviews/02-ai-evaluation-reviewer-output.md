# AI evaluation reviewer output (T11)

Scope: Appendix III (Tables A.8–A.12), Appendix IV (Tables A.13–A.14), Appendix V (Tables A.15–A.16), Appendix VI
(Table A.17), checked against the brief (`milestone-4.md`, sections 8 and 8.1) and `results/design_facts.md`. No data
file was opened and no performance figure is stated; every number below is either quoted from these files or is
arithmetic on them. Counts in Tables A.14 and A.15 match `design_facts.md` exactly (for example 5,245 / 23 = 228 events
per parameter; disability 1,123 / 602; test 15,724 = 10,801 + 4,923).

1. **Module coverage: the 2013 runs hold 6 modules, not 7.**
   - Passage: Table A.9, success criterion "same direction holds in at least 5 of the 7 modules"; validation "Estimated
     on the 2013 runs"; Table A.13 step 2 leave-one-run-out; Table A.14 "module and start-month dummies".
   - Problem: the 9 training runs in `design_facts.md` are AAA, BBB ×2, DDD ×2, EEE, FFF ×2 and GGG – six modules;
     CCC has no 2013 run. The AQ2 criterion cannot be evaluated on the data it is estimated on. For AQ3, the CCC runs of
     2014 carry a module level the model never saw, and in development the folds that hold out AAA-2013J, EEE-2013J or
     GGG-2013J (single-run modules) leave that module's dummy without any training rows.
   - Why it matters: an unattainable criterion is not falsifiable; an unseen dummy level is silently coded as the
     reference module, so CCC (and those three folds) are scored with another module's intercept.
   - Recommendation: restate the AQ2 rule for 2013 as "at least 5 of the 6 modules where the sign is defined" (or as
     a share), with CCC entering only in the 2014 replication. State in Table A.13 how an unseen module is scored
     (for example, the module term set to zero with a run-level base-rate offset, or no module dummies), apply the same
     rule in development folds, and report CCC runs separately in step 7.

2. **The decision is a per-tutor capacity; the metrics are per-run lists, and their "attainable" scale is not used.**
   - Passage: Appendix III intro "3 or 5 contacts per tutor group of about 20 students … that is 15% or 25% of the
     enrolments"; Table A.10 primary metric "read against the attainable recall of the run"; Table A.12.
   - Problem: (a) one run-wide top-k list can give one tutor group 12 names and another none, so the run-level list does
     not reproduce the stated capacity; OULAD has no tutor-group field to test this. (b) Attainable recall at k = 5/20
     ranges 0.457–1.0 across training runs at day 27, so raw pooled recall mixes runs on different ceilings, and no
     normalised recall is defined. (c) When |Y| ≥ k, recall ÷ attainable recall = TP/k = precision, so recall,
     precision, lift and normalised precision at fixed k are monotone transforms of the same count TP: the secondary
     metrics add no information on the trade-off. (d) Net benefit over threshold probabilities evaluates a "contact all
     above pt" policy, not a fixed-capacity policy.
   - Why it matters: the brief (8.1) asks for the metric that reflects the decision; the card currently implies more
     independent evidence than it has.
   - Recommendation: state that the run-level list approximates per-tutor capacity and is untestable in OULAD (add as a
     limitation and a risk). Define normalised recall = recall / attainable recall in Table A.12 and report it beside
     pooled recall. Label precision and lift as re-expressions of the same TP at fixed k; keep PR-AUC/ROC-AUC as
     threshold-free context; report net benefit at the capacity-implied threshold of each run or mark it as context only.

3. **S1 inference with 13 test runs is under-specified and probably anti-conservative.**
   - Passage: Table A.10 S1 "95% two-level bootstrap interval of the difference above 0 and … at least equal to the
     rule in at least 9 of the 13 test runs"; Appendix IV "two-level bootstrap that resamples runs and then enrolments".
   - Problem: percentile cluster bootstraps with 13 clusters of very unequal size (348–2,021) under-cover; it is not
     stated that the difference is computed on the same resample for model and rule (paired), nor how the top-k list is
     re-formed when resampled enrolments repeat. "At least equal" counts ties as wins, and ties are likely because both
     lists contain every inactive student. As a sign test, 9 of 13 has P(X ≥ 9 | p = 0.5) = 1,093 / 8,192 ≈ 0.13, so it
     is a consistency check, not evidence on its own. Pooled recall weights runs by non-completer count, so the 2–3
     largest runs can decide S1.
   - Why it matters: S1 is the main pass/fail gate; a mis-specified interval makes it either too easy or untestable.
   - Recommendation: specify a paired bootstrap of the per-run TP difference (lists re-formed by top-k within each
     resampled run, k fixed at 25% of the resampled n); add a run-level exact sign-flip (permutation) test on the 13
     per-run differences as a pre-specified companion; count ties separately ("wins / ties / losses"); report the
     unweighted mean of per-run differences beside the pooled one.

4. **S2 is ambiguous and its bar is unanchored.**
   - Passage: Table A.10 S2 "pooled precision at capacity at least halfway from the base rate to the attainable
     maximum"; Table A.12 normalised precision "(precision − b) / (min(1, |Y|/k) − b)".
   - Problem: the formula is per run, but S2 is "pooled": it is not said whether the per-run values are averaged or the
     pooled precision is normalised by a pooled b. With the training base rate 0.444 the pooled bar is precision ≥
     0.722 (lift ≈ 1.63); per run it ranges from 0.602 (AAA-2013J: b = 0.247, max = 91/95 = 0.958) to 0.777
     (DDD-2013B: b = 0.555). The halfway point is not linked to the rule or to any decision cost, and by point 2(c) it
     constrains the same TP as S1.
   - Why it matters: an arbitrary absolute threshold is what the brief warns against; nothing in the files shows
     whether 0.72 is easy or impossible for this cohort.
   - Recommendation: fix the aggregation (for example the TP-weighted mean of per-run normalised precision) and give a
     rationale for "halfway" (for example, the rule's normalised precision on 2013 as a floor fixed at the first
     freeze), or demote S2 to a reported quantity and keep S1 as the single gate.

5. **The primary test population for S1–S3 is not named among the step-7 variants.**
   - Passage: Table A.13 step 7 "with and without test enrolments of students seen in 2013 and the Withdrawn enrolments
     without a withdrawal day"; Table A.14 "Test enrolments of students seen in 2013: 1,586".
   - Problem: four populations (2 × 2), paired/unpaired runs and two cut-offs × two k values are reported, but the
     criterion does not say which one decides. The 1,586 repeat enrolments (about 10% of test) have their 2013 rows in
     the final training fit, a student-level dependency across the temporal split.
   - Why it matters: with several variants and no declared primary, the reported pass can be chosen after seeing the
     results – the forking-paths problem the first freeze is meant to prevent.
   - Recommendation: state in Table A.10 that S1–S3 are judged on all 13 runs, day 27, k = 5/20, all eligible test
     enrolments (the deployment-realistic population), and that every other variant is a sensitivity analysis that
     cannot change the verdict.

6. **Calibration criterion: definition, scope and the failure path conflict with the single test.**
   - Passage: Table A.10 S3 "slope between 0.8 and 1.2 and intercept between −0.2 and 0.2"; Table A.12 "Logistic
     recalibration of the outcome on the score's log-odds"; Table A.17 R4 check "recalibration when calibration fails".
   - Problem: (a) the intercept from a joint intercept–slope fit is not calibration-in-the-large; that needs the slope
     fixed at 1 (offset). (b) It is not stated whether the bounds apply to the point estimate or the interval, nor
     whether pooled or per run; training base rates span 0.247–0.555, so a pooled intercept can pass while several runs
     are off by much more. (c) R4's recalibration after a failed test check would refit on the test runs and then
     report on them, which breaks step 6. (d) No recalibration step exists in development, so a boosted-tree model
     reaches the test without any.
   - Why it matters: S3 decides whether tutors see probabilities; a failed or passed S3 must be interpretable, and the
     register promises a remedy that the protocol forbids.
   - Recommendation: define the intercept with slope fixed (offset), apply the bounds to the pooled point estimate and
     report per-run intercepts; add an optional recalibration fitted inside development (inner folds) before the second
     freeze; rewrite R4 so that a test failure leads to "ranks and reasons only" plus recalibration on a later run, not
     on the 2014 test.

7. **Model choice in step 4 uses the outer folds and a margin on a different aggregation from S1.**
   - Passage: Table A.13 step 4 "mean recall at capacity is at least 0.03 higher and higher in at least 7 of 9 folds";
     Table A.17 R3 control "Nested folds", residual "Low".
   - Problem: four configurations (LR/GBT × primary/extended) are compared on the outer fold results, so the chosen
     configuration's fold estimate is selected and optimistic; nesting only protects hyper-parameters. "Mean" (an
     unweighted mean of 9 fold recalls) differs from the pooled recall of S1, and a 0.03 absolute recall gain means
     different things on ceilings of 0.457 and 1.0. 7 of 9 corresponds to P ≈ 46 / 512 ≈ 0.09 under no difference. The
     inner leave-one-run-out loop must also remove overlapping students (121–129), which is stated only for the outer
     folds.
   - Why it matters: R3's "Low" residual is overstated if fold results are quoted as performance; inconsistent
     aggregation can make development and test disagree for arithmetic reasons.
   - Recommendation: use the same metric and aggregation as S1 (pooled, or normalised recall); state that fold results
     are for choice only and never reported as expected performance; apply the student-overlap removal in inner folds;
     justify 0.03 in students (for example, about 0.03 × 5,245 ≈ 157 more non-completers reached over the 9 runs).

8. **The fairness gate cannot fire for the groups most at risk, and its direction is inconsistent.**
   - Passage: Table A.16 "Gap above 10 points with an interval excluding 0, in a group with at least 100
     non-completers"; Table A.11 "no more than 10 points below the rest of the run"; Table A.15 age 55 or over "test
     enrolments 118".
   - Problem: requiring the interval to exclude 0 treats lack of power as evidence of fairness; age 55+ (118 test
     enrolments) cannot reach 100 non-completers, and IMD-missing (610 test enrolments; training rate 118/418 ≈ 0.28) is
     near the cut. Eligibility is counted on test outcomes, which are unseen at the freeze. Table A.11 is one-sided
     ("below"), Table A.16 is undirected ("above 10 points"). Across about 6 named groups (more if every IMD and age band
     is audited) × several metrics × 2 cut-offs × 2 k values, 95% intervals will produce chance flags.
   - Why it matters: Appendix V, citing [S526], already reports erratic bias for disabled students; the gate is blind exactly where
     the register (R7) says the residual risk is "Medium for small groups".
   - Recommendation: fix eligibility from enrolment counts at the freeze; make the rule one-sided (lower recall than the
     rest); for groups below the size threshold, trigger review on the point gap alone and report it as "insufficient
     data, not cleared"; name a confirmatory set (recall gap at day 27, k = 5/20, the four AQ4 groups) with a Holm
     adjustment, and label everything else descriptive.

9. **ABROCA's reading needs a reference and a role.**
   - Passage: Table A.16 "Threshold-free gap | ABROCA per group | Reported; read with the at-capacity checks"; Table A.10
     fairness row.
   - Problem: ABROCA is non-negative and unsigned, so sampling noise alone gives positive values, larger in small groups
     (smallest test runs hold 1–18 members); it integrates over all thresholds, while the decision acts at one rank
     per run; pooling ROC curves across runs with different base rates mixes run effects into the group gap.
   - Why it matters: an unreferenced ABROCA value will read as a fairness finding when it may be noise.
   - Recommendation: report ABROCA with a permutation reference (group labels shuffled within run) and the sign of the
     underlying AUC difference, compute it within run then pool, and state that it never triggers review on its own.

10. **AQ2: odds ratios at this base rate and a near-trivial threshold; AQ2–AQ3 coupling.**
    - Passage: Table A.9 primary "Odds ratio and average risk difference"; success "interval that excludes 1";
      error analysis "sensitivity … to the CMA-lateness variant of the rule".
    - Problem: with 44–46% non-completion, odds ratios are far from risk ratios and read as larger effects; with 11,811
      enrolments almost any sign will exclude 1, so the criterion separates little. The rule variant explored in AQ2 is
      also the AQ3 baseline; if AQ2 results on 2014 (step 8) inform the rule or the predictor set, the test is reused.
    - Why it matters: the criterion is close to trivially satisfied, and an unfrozen baseline undermines S1.
    - Recommendation: make the average risk difference the reported effect, with a smallest effect of interest fixed in
      advance (in percentage points); freeze the rule variant used as the AQ3 baseline at the first freeze; state that
      no 2014 AQ2 result may change AQ3.

11. **Error analysis gaps.**
    - Passage: Table A.10 and A.16 error rows (run, module, activity, Fail/Withdrawn).
    - Problem: missing are (a) non-completers who withdraw between the cut-off and list delivery, who count as caught
      but cannot be contacted; (b) the stability of list membership near rank k (students who enter or leave under
      bootstrap); (c) recall among active students only, where the model must add value over inactivity; (d) errors by
      prior attempts and late registration; (e) behaviour on the CCC runs (point 1).
    - Why it matters: (a) and (c) can make S1 look better than the actionable gain.
    - Recommendation: define "reachable non-completers" (no withdrawal before delivery) and report recall on them;
      report recall among active students as a pre-specified secondary result; add list-membership stability and the
      prior-attempt and late-registration slices.

12. **Risk register: missing risks and controls that do not match.**
    - Passage: Table A.17 R3, R4, R5, R6, R8.
    - Problem: missing risks are few-cluster inference (13 runs), unseen module at test (CCC), the run-list versus
      tutor-capacity mismatch, selective reporting across step-7 variants, and proxy features for the excluded
      attributes. R4's control conflicts with the single test (point 6); R3's residual is overstated (point 7); R5's
      control "many models fit equally well" is an argument, not a control; R6 and R8 have no check before a pilot.
    - Why it matters: the brief's rubric scores whether the important risks are identified in this context.
    - Recommendation: add rows for the five missing risks with the controls proposed above; reword R5's control as
      "association wording rule plus review"; give R6 and R8 a pre-pilot check (for example, a wording review of tutor
      materials and a scripted tutor walk-through).
