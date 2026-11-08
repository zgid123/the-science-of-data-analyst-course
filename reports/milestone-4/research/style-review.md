# Style read-through (T20)

Scope: the English section files in `reports/milestone-4/report/` (00-0 to 10-08, `.vi.md` and `09-references.md`
excluded; citation numbers [1]–[53] used in the text all exist in `09-references.md`). Checked against CLAUDE.md
"Writing conventions" and section 6 of `.claude/skills/research-report/reference.md`, reading as someone who has only
the submitted report plus the Milestone 3 report and package. Kinds: (1) reader-only, (2) process history, (3) reads on
its own, (4) inconsistency, (5) unclear or awkward, (6) claim too strong for a proposal. The report files are unchanged.
Findings are ordered with the most important first.

Count by kind: (1) 1, (2) 6, (3) 7, (4) 10, (5) 13, (6) 3; total 40.

## Findings

1. **Kind 4. Parameter count of the primary model contradicts its predictor set.**
   - Location: 03-03-predictive.md:9–12; 10-01-briefs-full.md:44 (Table A.3); 02-01-modeling-briefs.md:15 (Table 2.1); 10-08-traceability-full.md:15; against 10-04-validation-protocol.md:47–49 (Table A.14).
   - Quote: "a penalised logistic regression on the 19 usable primary predictors and the weekly clicks … The 23 parameters face 5,245 to 5,519 training non-completers" (3.3). Table A.14: "Parameters, primary set (19 predictors, module and start-month terms) | 23 | 23" and "Parameters, primary and extended sets with weekly clicks | 35 | 37".
   - Problem: in Table A.14 the 23 parameters cover the 19 predictors with module and start-month terms but *no* weekly clicks; the weekly clicks (2 at day 13, 4 at day 27) appear only in the 35/37 count with the 10 extended predictors (23 + 10 + 2 = 35, 23 + 10 + 4 = 37). Section 3.3, Tables 2.1, A.3 and A.21 put the weekly clicks in the primary model. Either the primary model has 25/27 parameters (and events per parameter, Riley minimums and "about 230" change), or the weekly clicks belong to the extended set.
   - Replacement (if the counts in Table A.14 are right, 3.3): "The primary approach is a penalised logistic regression on the 19 usable primary predictors with module and start-month terms, one model per cut-off, 23 parameters in all; the weekly clicks enter with the extended set (Table A.14)." Make Tables 2.1, A.3 and A.21 say the same. If instead the weekly clicks are in the primary model, relabel the Table A.14 rows "Parameters, primary set with weekly clicks" (25 | 27) and recompute events per parameter and the Riley minimums.

2. **Kind 4. The confirmatory fairness rule (F1) is stated three different ways.**
   - Location: 04-03-metrics-success.md:25 (Table 4.2); 04-04-error-fairness.md:11–13; 10-05-fairness-spec.md:31 (Table A.16).
   - Quote: Table 4.2: "No eligible audit group with recall at capacity more than 10 points below the rest, Holm-adjusted". Section 4.4: "A shortfall of more than 10 points in recall at capacity against the rest, with a Holm-adjusted interval below 0, triggers a review". Table A.16: "a shortfall of more than 10 points, with a Holm-adjusted bootstrap interval below 0 across the three confirmatory groups".
   - Problem: Table 4.2 reads as a non-inferiority test against a 10-point margin (interval below −10), Section 4.4 and Table A.16 as two conditions (point gap > 10 *and* interval entirely below 0). "Points" is not "percentage points", and the confidence level is not given. A reader cannot tell what triggers a review.
   - Replacement (use in all three places): "A confirmatory group is flagged for review when its recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups, lies entirely below 0."

3. **Kind 4. Riley minimum quoted as 1,731 where the range starts at 1,728; events compared with enrolments.**
   - Location: 10-02-candidate-comparison.md:33 (Table A.6, Candidate 1, Fit to data); 03-03-predictive.md:12–14; against 10-04-validation-protocol.md:50 (Table A.14: "1,728 / 2,629 | 1,731 / 2,784").
   - Quote: "23 parameters against 5,245–5,519 training events, about 230 per parameter, well above the 1,731–2,784 enrolments the minimum sample size criteria require [14]".
   - Problem: the smallest Riley minimum in Table A.14 is 1,728 (day 13, primary), not 1,731; "2,784" is the full set at day 27, so the range mixes predictor sets. The sentence also compares training *events* (non-completers) with a minimum stated in *enrolments*, which invites a wrong reading. Section 3.3 has the same events-versus-enrolments contrast ("The 23 parameters face 5,245 to 5,519 training non-completers … while … require 1,731 enrolments").
   - Replacement (Table A.6 cell): "23 parameters against 5,245–5,519 training non-completers, about 230 per parameter; the 11,811–12,080 training enrolments are about seven times the 1,728–1,731 the minimum sample size criteria require for this set [14] (Table A.14)". In 3.3: "The 23 parameters have 5,245 to 5,519 training non-completers, about 230 per parameter, and the 11,811 training enrolments at day 27 are about seven times the 1,731 that the minimum sample size criteria of Riley et al. require under their default assumptions [14]."

4. **Kind 6. Sample-size argument draws a conclusion the evidence does not support.**
   - Location: 03-03-predictive.md:12–14; 10-02-candidate-comparison.md:42–43.
   - Quote: "… require 1,731 enrolments at day 27 under their default assumptions [14], so a flexible model has little room to gain." and "the 23 parameters leave about 230 events each, so data size gives a flexible model no advantage to exploit [14]".
   - Problem: Riley et al. give a *minimum* size for a stable model; ample data shows the primary model is not limited by sample size, but ample data is if anything what a flexible model needs, so it cannot show that a flexible model has "little room to gain". The statement predicts a comparative result before any model is fitted.
   - Replacement (3.3): "… under their default assumptions [14], so the size of the training data does not limit the logistic model, and any gain of a flexible model would have to come from non-linear effects, which the margin of Section 4.2 tests." (A.6 text): "the 23 parameters leave about 230 events each, so the training data are large enough for a stable logistic model [14], and whether a flexible model adds anything is left to the margin of Table A.13, step 4".

5. **Kind 4. "No student records shared with development" contradicts repeat students in the test runs.**
   - Location: 04-02-validation-strategy.md:3–4; against 10-04-validation-protocol.md:17 (step 6, "Data sharing no run with development") and :53 (Table A.14, "Test enrolments of students seen in 2013 | 1,637 | 1,586").
   - Quote: "Testing on data that share no student records with model development is the core requirement of TRIPOD+AI [21]".
   - Problem: the design's test runs hold 1,586 enrolments (day 27) of students who were in the 2013 training runs; they are removed only in a sensitivity analysis. Read next to Table A.14, the sentence says the design breaks the standard it cites.
   - Replacement: "Testing on data not used in model development is the core requirement of TRIPOD+AI [21]; the 2014 test runs share no run with development, and the 1,586 test enrolments of students already seen in 2013 are removed in a sensitivity analysis (Appendix IV)."

6. **Kind 4. Table A.21 disagrees with Table 8.1 on baselines and primary metrics.**
   - Location: 10-08-traceability-full.md:14–16; against 08-00-traceability.md:12–14 and 04-01-evaluation-cards.md:13.
   - Quote: AQ2 primary metric "Odds ratio and risk difference with interval"; AQ3 baseline "Early-sign rule ranked by signs; random list"; AQ3 primary metric "Recall at capacity (5 per 20, day 27)"; AQ4 primary metric "Recall against attainable; lift"; AQ2 primary approach "Logistic regression with run fixed effects".
   - Problem: the main text makes the risk difference the AQ2 primary metric with odds ratios beside it, gives AQ3 the background-only model as a baseline, and makes *normalised* recall at capacity the primary metric of AQ3 and AQ4. Lift is a secondary metric (Table A.11). The AQ2 approach omits the sign × module terms.
   - Replacement cells: AQ2 primary metric "Risk difference with interval (odds ratio beside it)"; AQ2 primary approach "Logistic regression with run fixed effects and sign × module terms"; AQ3 baseline "Rule-ranked list; background-only model; random list"; AQ3 primary metric "Normalised recall at capacity (day 27, 5 per 20)"; AQ4 primary metric "Normalised recall at capacity".

7. **Kind 2. Part 6 narrates how the design changed.**
   - Location: 06-00-genai-usage.md:17–20.
   - Quote: "The reviewers changed the design more than any source did. They found, for example, that the training runs cover 6 modules rather than 7, … ; each point was verified before it changed the plan."
   - Problem: "changed the design" and "before it changed the plan" describe revisions of the proposal. Part 6 may report what the AI suggested and what the team decided, without telling the reader the design was altered.
   - Replacement: "The two reviewers contributed the most consequential points of the design. They pointed out, for example, that the training runs cover 6 modules rather than 7, that the October 2013 runs end after the February 2014 runs need scores, and that a success rule requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be met by chance about 13% of the time; the team verified each point against the prepared data before adopting it."

8. **Kind 2. Appendix VII "Effect" column reports revisions.**
   - Location: 10-07-ai-decision-log.md:14–15 (Table A.18).
   - Quote: "Appendices I–II, IV–VI revised" and "Appendices III–VI revised; S2 no longer a gate".
   - Problem: "revised" and "no longer" tell the reader about earlier versions.
   - Replacement: "Appendices I–II and IV–VI" and "Appendices III–VI; S2 (precision at capacity) reported, not a gate".

9. **Kind 2 (with internal identifiers). Table A.20 refers to an earlier numbering of the risk register.**
   - Location: 10-07-ai-decision-log.md:53 (Table A.20, row 12).
   - Quote: "Five risks added; R5, R6 and R8 controls rewritten (now R9, R10, R13)".
   - Problem: "added", "rewritten" and "now" describe a revision, and "R5, R6 and R8" are identifiers from a register version the reader never sees.
   - Replacement: "Sixteen risks in Table A.17; controls of misreading coefficients as causes (R9), claiming that contact works (R10) and automation bias (R13) matched to their risks".

10. **Kind 2. Table A.19 "Change" column narrates earlier states.**
    - Location: 10-07-ai-decision-log.md:23, 28, 29, 34 (Table A.19, rows 1, 6, 7, 12).
    - Quote: row 1 "background-only baseline added"; row 6 "The switching rule existed (Table A.13, step 4); the rationale now leads with the project's constraints"; row 7 "Restated: Fail is not a time-to-event outcome"; row 12 "Already planned as sensitivity analyses".
    - Problem: "added", "existed", "now leads", "Restated" and "Already planned" are process history.
    - Replacement: rename the column "Where it is addressed" and use: row 1 "Lists and normalised recall per run; ROC-AUC and PR-AUC within run; background-only baseline"; row 6 "Switching rule in Table A.13, step 4; rationale led by the project's constraints (Section 3.3)"; row 7 "Fail is not a time-to-event outcome; non-informative censoring stated as an assumption"; row 12 "Sensitivity analyses of Table A.13, step 7; previous attempts are recorded at registration and stay legitimate".

11. **Kind 6. Model card and datasheet stated as existing.**
    - Location: 05-01-leakage-interpretability.md:16–18.
    - Quote: "The model and the prepared data are documented in a model card, which states intended and out-of-scope uses with performance by group [41], and a datasheet …".
    - Problem: no model exists yet, and a model card with "performance by group" implies results. The sentence must read as a commitment.
    - Replacement: "The final model will be documented in a model card, which states intended and out-of-scope uses with performance by group [41], and the prepared data in a datasheet, which records composition, collection and recommended uses [42]."

12. **Kind 6. Systematic-review finding generalised beyond its scope.**
    - Location: 10-02-candidate-comparison.md:44–45.
    - Quote: "comparisons at low risk of bias show no gain of machine learning over logistic regression on tabular risk data [18]".
    - Problem: Section 3.3 states it correctly (71 clinical comparisons, discrimination, author-reported); the appendix widens it to "tabular risk data" in general and drops the author-reported label.
    - Replacement: "a systematic review of 71 clinical prediction comparisons found no difference in discrimination between logistic regression and machine learning at low risk of bias (author-reported) [18]".

13. **Kind 4. Title page misstates the Milestone 1 version and Change Log range.**
    - Location: 00-0-title-page.md:22; against 01-01-goal-decisions-aqs.md:14–15 and 10-08-traceability-full.md:18–19.
    - Quote: "Milestone 1 proposal version | Proposal of 14 November 2026, Change Log C01–C14".
    - Problem: the date equals this report's submission date, and C14 is the Milestone 4 entry (Table A.22), whereas Section 1.1 and Appendix VIII state that C01–C13 come from Milestones 2 and 3.
    - Replacement: "Milestone 1 proposal version | Proposal of [Milestone 1 submission date], with Change Log entries C01–C13 of Milestones 2 and 3 (entry C14 in Appendix VIII)" (insert the real Milestone 1 date).

14. **Kind 3. Change Log identifiers used bare.**
    - Location: 01-01-goal-decisions-aqs.md:27 "(C10)" and :29 "(C13)"; 01-02-prepared-data-entry-gate.md:15 "(C11, C13)"; 03-02-descriptive-diagnostic.md:19 "(C14)"; 03-03-predictive.md:4 "the early-sign rule of C10"; 04-02-validation-strategy.md:25 "(C14)"; 04-03-metrics-success.md:6 "(C13)"; 05-01-leakage-interpretability.md:7 "(C14)"; 10-03-evaluation-cards-full.md:43 "as frozen in C10"; 10-04-validation-protocol.md:12 "the early-sign rule of C10".
    - Problem: each section must read on its own, and "C10" or "C14" does not say it is a Change Log entry or what it decided.
    - Replacement pattern: "(Change Log entry C10)"; in 3.3:4 "the early-sign rule (Change Log entry C10, Section 1.1)"; in 3.2:19, 4.2:25 and 5.1:7 "(Change Log entry C14, Appendix VIII)"; in 4.3:6 "(Change Log entry C13)"; in Table 1.2 "AQ4 as ranking, contact deferred (Change Log entries C11 and C13)".

15. **Kind 3. "Extended predictor set" used in the main text without definition.**
    - Location: 04-02-validation-strategy.md:15.
    - Quote: "Gradient-boosted trees or the extended predictor set replace the primary choice only with a gain of at least 0.03 …".
    - Problem: the extended set is defined only in Appendix I (Table A.3, "an extended set of 10 predictors"); the main text never introduces it.
    - Replacement: "Gradient-boosted trees, or an extended set of 10 further predictors (Appendix I, Table A.3), replace the primary choice only with a gain of at least 0.03 …".

16. **Kind 3. S1 used before it is defined.**
    - Location: 04-01-evaluation-cards.md:17 (Table 4.1, Success criterion row).
    - Quote: "S1: beats the rule (Section 4.3)" and "S1 for the list; fairness check passed or reviewed".
    - Problem: S1 is defined in Table 4.2 of the next section; Table 4.1 is the reader's first meeting with it.
    - Replacement (AQ3 cell): "Single gate S1: pooled normalised recall above that of the rule-ranked list, with an interval above 0 (Section 4.3)"; (AQ4 cell): "Gate S1 met by the list; confirmatory fairness check passed or reviewed (Section 4.4)".

17. **Kind 1. "AI agents" in Appendix VII.**
    - Location: 10-07-ai-decision-log.md:55–57.
    - Quote: "Both reviewers worked as isolated AI agents that could read only the brief and the appendices named in their prompt".
    - Problem: "agents" is tool vocabulary; the reader needs the condition, not the mechanism.
    - Replacement: "Each reviewer was a separate generative AI session that could read only the brief and the appendices named in its prompt, and team members checked every critique against the design facts before deciding."

18. **Kind 5. Labels-available variant lacks its reason in the main text.**
    - Location: 04-02-validation-strategy.md:22–24.
    - Quote: "and the 2013 J runs last 261–268 days, so a labels-available variant scores the 2014 B runs with a model trained on the 2013 B runs only."
    - Problem: the step that makes the "so" follow is missing; Appendix IV has it ("they had not ended when the 2014 B runs reached their cut-offs").
    - Replacement: "and the 2013 J runs last 261–268 days, so their outcomes are not yet known when the 2014 B runs reach their cut-offs; a labels-available variant therefore scores the 2014 B runs with a model trained only on the 2013 B runs."

19. **Kind 5. "Test … below 0.05" omits what is below 0.05.**
    - Location: 04-03-metrics-success.md:22 (Table 4.2, S1); 10-03-evaluation-cards-full.md:46 (Table A.10).
    - Quote: "a one-sided sign-flip test on the 13 per-run differences below 0.05".
    - Problem: reads as if the differences are below 0.05.
    - Replacement: "a one-sided sign-flip test on the 13 per-run differences with a p-value below 0.05".

20. **Kind 5. "A rule of 9 wins in 13 runs" is opaque.**
    - Location: 06-00-genai-usage.md:19.
    - Quote: "a rule of 9 wins in 13 runs would occur by chance about 13% of the time".
    - Problem: the reader never meets this rule elsewhere and cannot tell whose rule it is. The figure is correct (P(X ≥ 9 | 13, 0.5) = 1,093/8,192 = 13.3%).
    - Replacement: covered by the text proposed in finding 7: "a success rule requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be met by chance about 13% of the time".

21. **Kind 4. Random list missing from the AQ3 baselines in two tables.**
    - Location: 03-01-criteria-matrix.md:20 (Table 3.1); 08-00-traceability.md:13 (Table 8.1); against 04-01-evaluation-cards.md:15, 07-00-prototype-protocol.md:12 and 10-03-evaluation-cards-full.md:43.
    - Quote: Table 3.1 "Early-sign rule ranked by signs; background-only logistic model"; Table 8.1 "Rule-ranked list; background-only model".
    - Problem: Tables 4.1, 7.1 and A.10 give AQ3 three baselines, including the random list.
    - Replacement: "Early-sign rule ranked by signs; background-only logistic model; random list" (Table 3.1) and "Rule-ranked list; background-only model; random list" (Table 8.1).

22. **Kind 5. "Replace … only by the margin" is ungrammatical.**
    - Location: 03-03-predictive.md:22; 10-02-candidate-comparison.md:47–48.
    - Quote: "They replace the primary approach only by the margin fixed in Section 4.2." / "they replace logistic regression only by the margin fixed in Appendix IV (Table A.13, step 4)".
    - Problem: a model cannot replace another "by a margin"; the condition is not stated.
    - Replacement: "They replace the primary approach only if they beat it by the margin fixed in Section 4.2: at least 0.03 in pooled normalised recall and a gain in at least 7 of the 9 folds."

23. **Kind 3. Decision D1 named without its words.**
    - Location: 02-02-technical-tasks.md:17; 03-03-predictive.md:5; 04-03-metrics-success.md:22 (Table 4.2, Role).
    - Quote: "but D1 acts at fixed cut-offs"; "which Milestone 1 named as the comparison for D1"; "Single gate for AQ3 and AQ4 (decision D1)".
    - Problem: D1 is defined only in Section 1.1.
    - Replacement: "but the listing decision (D1) acts at fixed cut-offs"; "the comparison for deciding who is listed for contact (D1)"; "Single gate for AQ3 and AQ4 (who is listed, D1)".

24. **Kind 4. AQ4 analytics level labelled three ways.**
    - Location: 01-01-goal-decisions-aqs.md:24 "Prescriptive (ranking)"; 08-00-traceability.md:14 and 10-08-traceability-full.md:16 "Prescriptive (decision support)"; 10-01-briefs-full.md:53 "Prescriptive, narrowed to decision support (ranking)".
    - Problem: one level, three labels.
    - Replacement: "Prescriptive, as decision support (ranking)" everywhere, or keep "Prescriptive (ranking)" from Table 1.1 in Tables 8.1 and A.21.

25. **Kind 3. Group-size threshold and the age-55 exclusion lack their reason in Section 4.4.**
    - Location: 04-04-error-fairness.md:10–13.
    - Quote: "the three groups that AQ4 names and that hold at least 400 test enrolments: … the most deprived band (1,486) … students aged 55 or over (118) are reported as a point gap".
    - Problem: the sentence does not say that the age group is excluded *because* it falls below 400, the band is not named (Table A.15: "0–10%"), and the 400 threshold carries no reason anywhere in the report.
    - Replacement: "… the most deprived band, 0–10% (1,486) … ; students aged 55 or over (118 test enrolments, below the 400 threshold) are reported as a point gap, …". Add the basis of the 400-enrolment threshold in the same paragraph (for example, the smallest group in which a 10-point recall gap can be detected at the stated power), if the team has one.

26. **Kind 5. Overlong sentence on model-choice overfitting.**
    - Location: 05-01-leakage-interpretability.md:9–11.
    - Quote: "Overfitting also enters through model choice: a tuned fold score is optimistic [28], so fold results serve only the choice, and comparisons of machine learning with logistic regression, often biased by validation flaws and silent on calibration [18], are answered by a frozen validation that reports calibration."
    - Problem: three ideas in one sentence; "are answered by" is vague.
    - Replacement: "Overfitting also enters through model choice: a tuned fold score is optimistic [28], so fold results serve only the choice and are never reported as performance. In addition, published comparisons of machine learning with logistic regression are often biased by validation flaws and silent on calibration [18]; the frozen validation of Section 4.2 avoids both and reports calibration."

27. **Kind 2. "Fixed now".**
    - Location: 10-05-fairness-spec.md:8.
    - Quote: "and eligibility for the confirmatory check is fixed now from enrolment counts."
    - Problem: "now" is time-relative to the writing.
    - Replacement: "and eligibility for the confirmatory check is fixed in this proposal from enrolment counts, before any test outcome is opened."

28. **Kind 5. "Earlier models" is ambiguous and differs from Appendix V.**
    - Location: 04-04-error-fairness.md:14; against 10-05-fairness-spec.md:42.
    - Quote: "On OULAD, earlier models reproduced and slightly amplified a gap in favour of male students" vs "most at-risk models reproduced and slightly amplified".
    - Problem: "earlier models" can read as this team's earlier models, and "most" is dropped.
    - Replacement: "On OULAD, most published at-risk models reproduced and slightly amplified a gap in favour of male students and showed erratic bias for students with a declared disability (author-reported) [37]".

29. **Kind 5. "Four configurations" not named.**
    - Location: 10-04-validation-protocol.md:15 (Table A.13, step 4).
    - Quote: "Four configurations compared on pooled normalised recall at day 27".
    - Problem: the reader has to infer the four.
    - Replacement: "Four configurations, penalised logistic regression and gradient-boosted trees each with the primary and with the extended predictor set, compared on pooled normalised recall at day 27, …".

30. **Kind 3. "Full" set undefined in Table A.14.**
    - Location: 10-04-validation-protocol.md:49–50.
    - Quote: "Events per parameter, primary / full" and "Minimum development size (Riley criteria), primary / full".
    - Problem: the row above calls it "primary and extended sets with weekly clicks"; "full" is never defined.
    - Replacement: "Events per parameter, primary set / primary and extended sets with weekly clicks" (same for the Riley row), or define "full" in the sentence before the table.

31. **Kind 3. AQ1 population "registered at day 14" unexplained in Table 2.1.**
    - Location: 02-01-modeling-briefs.md:13.
    - Quote: "Enrolment registered at day 14; assessment task".
    - Problem: day 14 differs from the day-13 cut-off, and the table does not say that it is the KPI population after the add-drop period (stated only in Table A.1).
    - Replacement: "Enrolment registered at day 14, after the add-drop period (the KPI population); assessment task".

32. **Kind 4. AQ2 baseline named four ways.**
    - Location: 03-01-criteria-matrix.md:19 "Unadjusted rate difference per sign"; 04-01-evaluation-cards.md:15 and 10-02-candidate-comparison.md:14 "Unadjusted comparison"; 08-00-traceability.md:12 "Unadjusted rate difference".
    - Replacement: "Unadjusted rate difference per sign" in every table.

33. **Kind 2. "Now" in the Part 3 opening.**
    - Location: 03-00-candidate-approaches.md:3.
    - Quote: "The technical tasks of Part 2 now receive their methods."
    - Replacement: "With the technical task of each question fixed in Part 2, each question receives its methods."

34. **Kind 5. Vague "well-known guidance".**
    - Location: 03-01-criteria-matrix.md:5.
    - Quote: "Well-known guidance on prediction systems decides most ties:".
    - Replacement: "Four findings on prediction systems settle most ties between candidates:".

35. **Kind 5. Vague opening of Part 8.**
    - Location: 08-00-traceability.md:3.
    - Quote: "The parts above end in one chain per question, from goal to decision."
    - Replacement: "Parts 1 to 7 give each question one chain from the Business Goal to the decision it supports."

36. **Kind 5. Overlong first sentence of Section 1.2.**
    - Location: 01-02-prepared-data-entry-gate.md:3–5.
    - Quote: "The prepared dataset OULAD-N04-prepared-1.0 holds one row per enrolment and two feature views at the cut-offs, the ends of day 13 and day 27 (weeks 2 and 4), each keeping enrolments still registered and information dated on or before the cut-off; the target non_completion is a final result of Fail or Withdrawn."
    - Replacement: "The prepared dataset OULAD-N04-prepared-1.0 holds one row per enrolment and two feature views, one for each cut-off at the end of day 13 (week 2) and day 27 (week 4). Each view keeps the enrolments still registered at its cut-off and only information dated on or before it, and the target non_completion is a final result of Fail or Withdrawn." Also at :7, "whose 15,724 outcomes" → "whose 15,724 outcomes at day 27".

37. **Kind 5. Terse cells in Table 5.1.**
    - Location: 05-00-risk-ethics.md:18–19.
    - Quote: "classification before a pilot"; "CCC apart".
    - Replacement: "risk classification under Vietnamese AI law before a pilot"; "module CCC reported separately".

38. **Kind 4. Capitalisation of assessment types.**
    - Location: 00-1-abbreviations.md:10 and :21; 01-01-goal-decisions-aqs.md:27.
    - Quote: "Computer-marked assessment" vs "Tutor-Marked Assignment".
    - Replacement: "Tutor-marked assignment", matching "Computer-marked assessment".

39. **Kind 5. "Points" without unit.**
    - Location: 04-01-evaluation-cards.md:17 (AQ2 success criterion); 04-04-error-fairness.md:12; 04-03-metrics-success.md:25.
    - Quote: "At least 5 points, interval excluding 0"; "more than 10 points".
    - Replacement: "At least 5 percentage points, interval excluding 0"; "more than 10 percentage points".

40. **Kind 5. Calibration sentence cites [31] twice and runs on.**
    - Location: 04-03-metrics-success.md:9–12.
    - Quote: "Calibration is assessed because risks can be unreliable even when discrimination is good [31], by the intercept with the slope fixed (target 0) and the slope (target 1) [31], but it cannot be a success criterion alone, since …".
    - Replacement: "Calibration is assessed because risks can be unreliable even when discrimination is good, using the calibration-in-the-large, with the slope fixed (target 0), and the calibration slope (target 1) [31]. Calibration cannot be a success criterion alone, since a model giving everyone the base rate is perfectly calibrated and useless [25]."

## Checked and consistent

- 0.03 × 2,976 = 89.3, so "about 89 more non-completers" matches (04-02:16, Table A.13 step 4, Table A.20 row 7); "7 of 9 folds" matches in all three places.
- 5,245 / 11,811 = 44.4%; 5,519 / 12,080 = 45.7%; 5,245 / 23 = 228; 5,519 / 23 = 240; 5,245 / 37 = 142; 5,519 / 35 = 158 (Table A.14).
- Table A.15 sums to the totals: training 5,697 + 6,114 = 11,811 and 2,488 + 2,757 = 5,245; test 6,666 + 9,058 = 15,724. Paired and unpaired test runs 10,801 + 4,923 = 15,724 and 10,902 + 5,087 = 15,989.
- Training enrolments are about seven times the Riley minimum (11,811 / 1,731 = 6.8; 12,080 / 1,728 = 7.0).
- 13 test runs, 9 training runs, 6 training modules, 400 eligibility threshold, S1–S3 and F1 operating point (day 27, 5 per 20), sixteen risks (R1–R16), 12 + 12 critiques with 10 + 2 and 12 accepted: consistent across main text and appendices.
- The glossary terms (normalised recall, attainable recall, background-only model, labels-available variant) agree with their uses.
- Citation numbers [1]–[53] all resolve in 09-references.md; [2] supports the tutor-group size of about 20 (OULAD paper).
