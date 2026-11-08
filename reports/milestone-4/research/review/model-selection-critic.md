# AI model-selection critic output (T10)

Role: "Model selection" reviewer under brief section 11. Inputs read: `final-project/milestones/04/milestone-4.md`,
`reports/milestone-4/report/10-01-briefs-full.md` (Tables A.1–A.4), `reports/milestone-4/report/10-02-candidate-comparison.md`
(Tables A.5–A.7 and the text after them), `reports/milestone-4/results/design_facts.md`. No data file, web source or
[Sxxx] source was opened; every number below is quoted from those files. The critic does not choose the model and
sets no metric thresholds. The team decides what to accept or reject.

1. **The AQ3 evaluation is pooled, but D1 acts within each run.**
   - Passage: Table A.3, "A risk score per enrolment at each cut-off"; Table A.7, "The k enrolments with the highest risk per run".
   - Problem: training base rates differ from 0.2486 to 0.5748 across runs at day 13 and from 0.2466 to 0.5547 at day 27 (`design_facts.md`). A model can score well on pooled discrimination just by separating high-rate runs from low-rate runs. That separation is no use to a tutor who ranks students inside one run. The early-sign rule is the only AQ3 baseline, and nothing measures how much of the score comes from module or run membership.
   - Why it matters: a pooled metric can favour the model over the rule for a reason D1 never uses. The comparison would then overstate the benefit to tutors.
   - Recommendation: name the primary AQ3 metric as a within-run measure, such as discrimination per run summarised across the 2014 runs, or precision at the capacity k per run. Add a second baseline that uses only module or run base rates and prior attempts, so the gain from engagement signs can be seen on its own.

2. **The validation does not yet match how the model will transfer to new runs.**
   - Passage: Table A.6, "penalty tuned in folds"; Table A.3, "train on 2013 runs, test once on 2014 runs".
   - Problem: (a) the files do not say how the folds are formed. Random folds over 11,811–12,080 rows mix rows from the same 9 runs into training and validation. The penalty is then tuned for within-run fit, but the stated risk is transfer to a later run. (b) 4 of the 13 test runs have no paired training run (`test_runs_paired` = 9; about 4,900–5,100 unpaired test rows). Table A.5 counts 7 modules, but the training table lists only 6 (AAA, BBB, DDD, EEE, FFF, GGG), so at least one test module was never seen in training. (c) Check whether a 2013 run's outcomes are known by the time a 2014 run reaches day 13 or 27. If a February 2014 run starts before the October 2013 run of the same module has ended, the planned training labels were not available when the score would have been needed.
   - Why it matters: each point can make the held-out result more optimistic than real deployment.
   - Recommendation: tune with folds grouped by run (leave one run out). Report paired runs, unpaired runs and the unseen module separately. Write down, for each test run, which training runs had finished before its cut-off, and either restrict training to those runs or state the gap as a limitation.

3. **The single test evaluation is shared by many comparisons.**
   - Passage: Table A.3, "an extended set of 10 predictors as an alternative"; Table A.6, gradient-boosted trees "stay as the challenger"; Table A.7, two baselines and two candidates.
   - Problem: "Test once on 2014 runs" holds only if one comparison is fixed before the test set is opened. As written, the 2014 runs would judge 2 cut-offs × 2 predictor sets × 2 model families × several list rules × 2 capacities. Picking the best of these after seeing test results is test-set selection.
   - Why it matters: the reported gain becomes a maximum over many tries, and the brief (section 8) rules out choosing the metric or model after seeing results.
   - Recommendation: in the Evaluation Design Card, name one primary comparison per cut-off (model against rule, one predictor set, one capacity). Make every choice among the alternatives using 2013 grouped folds only, and label all other test numbers as secondary or exploratory.

4. **The AQ2 method does not produce the per-module output the question asks for, and its data facts do not match the estimation sample.**
   - Passage: Table A.2, "within each module" and "direction of each association per module"; Table A.5, Candidate 1 "One model per cut-off, few terms" and Fit to data "22 runs, all large".
   - Problem: one model per cut-off with run fixed effects gives one pooled odds ratio per sign, adjusted for run. It does not give the per-module direction unless sign × module interactions or per-module models are added. Table A.2 also restricts estimation to the 2013 training runs, which are 9 runs and 6 modules, not 22 runs. In AAA-2013J, with 91–92 events, per-module estimates for 5 or more correlated signs will be wide. In addition, tasks due by day 27 exist in only 16 of 22 runs, so the "task missed" sign is undefined in some runs and is confounded with the run effect.
   - Why it matters: the primary approach answers a different question from the one stated, and the rejection of the mixed model ("Only 7 modules and 22 runs") rests on counts that are not the estimation counts.
   - Recommendation: either reword AQ2 to a pooled within-run association with a heterogeneity check, or state the per-module specification (interactions or separate fits) and report their intervals. Restate Fit to data for the 9 training runs. Say how the missed-task sign is coded in runs with no task due, and run a sensitivity analysis that drops those runs.

5. **The reasons shown to tutors come from a different model than the score, and mutually adjusted odds ratios are being read as each sign's own effect.**
   - Passage: Table A.5, Actionability "Gives the signs listed as reasons on D1"; Table A.6, "Score plus the signs that raise it"; Table A.5, Assumptions "Additive log-odds".
   - Problem: the D1 list is ranked by the AQ3 score, but the reasons are labelled from AQ2 odds ratios. These are two models with different predictors and penalties, so a student's reasons may disagree with what drives that student's score. Inside AQ2, the signs overlap: "no platform activity in the last seven days", "activity relative to the run median" and "activity before the start" all measure clicks. Their mutually adjusted coefficients are partial effects that can shrink or flip sign. They are not the size of each sign's gap, and reading them that way is the "Table 2 fallacy". Additivity and the absence of sign × module interactions are assumed but not checked.
   - Why it matters: tutors could get reasons that contradict the score, or treat partial coefficients as the weight of each behaviour.
   - Recommendation: take per-student reasons from the same model that produces the score, or use the raw sign flags with no weights. Report AQ2 unadjusted and adjusted estimates side by side, check how strongly the click-based signs are correlated, and test a small set of pre-specified interactions (sign × module, sign × cut-off).

6. **The choice of logistic regression leans on published comparisons more than on this data, and no rule decides when the challenger wins.**
   - Passage: text after Table A.6, "comparisons at low risk of bias show no gain of machine learning over it", "complex classifiers often perform no better"; Table A.6, gradient-boosted trees "Suits tabular data of about 10,000 rows".
   - Problem: these are general findings, close to the reasoning by reputation that brief section 7 rejects. The data-specific reasons (tutors must read the reasons, the 23-parameter design, transfer across runs) are present but scattered. The plan also keeps gradient-boosted trees "as the challenger" without saying what result would justify a switch, or how the loss of interpretability would be weighed against it (brief section 10, "Prototype không phải cuộc thi").
   - Why it matters: without a decision rule written in advance, choosing between the two after the test becomes post hoc.
   - Recommendation: base the selection rationale on this data's constraints first, with the literature as support. Before any test run, write a team-set decision rule: which metric, measured on 2013 grouped folds, what size of difference counts as material, and what interpretability cost is acceptable. Do not borrow a threshold from the literature without saying why it fits D1.

7. **The survival candidate is a straw man: its stated assumption is wrong and its real mismatch goes unnamed.**
   - Passage: Table A.6, Candidate 3, "Independence of dropout across weeks, almost certainly violated" and "Needs person-week data and handling of censoring".
   - Problem: a discrete-time hazard model conditions on surviving to each week, and its main assumption is non-informative censoring given the covariates. It does not assume that weeks are independent in the sense stated. The stronger objection is never raised: the AQ3 target includes Fail, which is decided at the end of the run and is not a time-to-event outcome. Censoring is also nearly absent, except for the 89–90 test rows with an unknown withdrawal day.
   - Why it matters: rejecting a candidate on a false assumption weakens the "2–3 real candidate families" requirement and invites a reviewer challenge.
   - Recommendation: restate Candidate 3 correctly. It models time to withdrawal only, Fail would need a competing-risk or separate outcome, and it does not match the end-of-run composite target. Keep or drop it on those grounds.

8. **The sample-size argument covers rows, not runs, and its inputs and quoted figures need tidying.**
   - Passage: Table A.6, "about 230 events per parameter, far above the 1,728–2,784 enrolments the minimum sample size criteria require"; Table A.5, "at least 370 enrolments and 92 non-completers".
   - Problem: (a) the minimum-sample-size calculation (`riley_*` rows) depends on an anticipated Cox–Snell R² of about 0.112, and the files do not say where that value comes from. (b) Plenty of events per parameter protects against overfitting within the data. It says nothing about transfer, which rests on only 9 training runs, so performance on new runs is the real constraint. (c) 370 and 92 are the day-13 minimums. At day 27 they are 369 and 91 (`design_facts.md`).
   - Why it matters: "far above" can be read as settling robustness when it does not.
   - Recommendation: cite the source of the anticipated R² or run the calculation over a range of values. State that sample size is ample for estimation but that transfer is tested only by the run-level split. Quote the minimums per cut-off.

9. **The plan has not decided whether D1 needs a calibrated probability or only a ranking.**
   - Passage: Table A.3, "readable as a probability only if calibration holds"; Table A.7, Candidate 2 "risk tiers" with "Tier cut points".
   - Problem: top-k within a run needs only the ordering within that run. Risk tiers, or any wording that tells tutors a probability, need calibration in each new run. Base rates differ by about 0.33 between training runs, so a model trained on pooled data will be miscalibrated in some runs, and the plan contains no recalibration step. The source of the tier cut points is also not stated: capacity, risk level or practice.
   - Why it matters: miscalibrated probabilities shown to tutors mislead, and tiers whose cut points are fixed after viewing the test data leak.
   - Recommendation: state which output D1 receives. If it is only a rank, report calibration as secondary and do not show probabilities to tutors. If it is tiers or probabilities, add calibration per run (calibration slope and intercept on the test runs) and fix the cut points from capacity or 2013 data before testing.

10. **The fairness audit is underpowered in each run and assumes that leaving out a sensitive attribute is enough.**
    - Passage: Table A.7, "Audit of recall and precision at capacity by group"; Table A.6, "no sensitive predictor"; Baseline "Treats all equally by construction".
    - Problem: the audit groups are tiny in some runs. The smallest-run test counts are disability = Y 18, IMD 0–10% 17, IMD missing 1 and age 55+ 1, so audit results for a single run would be noise. Leaving out a sensitive attribute does not stop proxies: activity, previous attempts and credits can all carry deprivation or disability. The baseline's equal weights do not give equal error rates. The disability group's training event rate (636/1157 at day 13) is above the overall rate (0.4569), so equal recall and equal precision cannot both hold, and the team has not said which one matters for D1.
    - Why it matters: a fairness claim without power, or one that rests on dropping the attribute, does not protect the group the brief asks about.
    - Recommendation: audit on pooled test runs with intervals and report the group sizes. Choose the fairness criterion for D1 in advance, with its reason: for example, equal recall if missing a struggling student is the main harm. Check proxies by comparing scores across groups, and drop the rule baseline's "treats all equally" claim.

11. **The AQ4 list rests on two unchecked assumptions, and its metric has a ceiling set by capacity.**
    - Passage: Table A.7, Candidate 1 Assumptions "Risk order matches need"; Table A.4, "with which gain over chance and recall".
    - Problem: the target puts Fail and Withdrawn together, and the list ranks by risk of either. Students who withdraw early and students who fail may need different contact, or may be unreachable, so "risk order matches need" is assumed rather than tested. The text after Table A.7 rightly separates risk from benefit, but the assumption is still in the primary approach. Recall at capacity also has a hard ceiling that varies by run: maximum recall for 3 per 20 runs from 0.2616 to 0.6196 at day 13 (`design_facts.md`). Raw recall therefore penalises high-rate runs for the size of the list, not for the model.
    - Why it matters: comparing runs, or reporting "recall" with no ceiling, misstates list quality. The composite target hides which outcome the list actually finds.
    - Recommendation: report recall at k as a share of the maximum possible in each run, or lead with precision at k. Break down the listed true positives into Fail and Withdrawn. State "risk order matches need" as an untested assumption, to be checked only by the randomised study the team already defers to.

12. **Some cohort-definition and repeat-student cases could leak or bias the comparison.**
    - Passage: Table A.3, "Enrolment registered at the cut-off"; Table A.2, adjustment for "previous attempts".
    - Problem: (a) 89–90 test rows have an unknown withdrawal day. If some of them withdrew before the cut-off, the evaluation includes students whose outcome was already known at prediction time. (b) 1,586–1,637 test rows belong to students who also appear in training, and 121–129 training students appear in several runs. Their earlier outcome can be learned through the student's identity or a previous-attempts feature, and the test then partly measures memory of the student, not generalisation. (c) For AQ1, the brief requires a baseline or cross-check (brief section 8, descriptive row: reconcile counts and totals), and Table A.1 names none.
    - Why it matters: (a) and (b) inflate held-out performance, and (c) leaves a required element missing.
    - Recommendation: rerun the test with the unknown-withdrawal-day rows excluded and then included as non-completers. Report test results for repeat students and for new students separately. Check that no feature draws on a previous run's outcome after its end date. Add the count reconciliation for AQ1 to its brief.
