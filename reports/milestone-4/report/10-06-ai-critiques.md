## Appendix VI – Decisions on the AI Critiques and Prompts

The AI Decision Log of Section 6 (Table 6.1) records the significant AI contributions; this appendix gives the
team's decision on each critique of the two reviewers. Table A.10 covers the 12 critiques of the model-selection critic
and Table A.11 the 12 critiques of the evaluation reviewer, each with the evidence used to check it and its effect on
the proposal.

**Table A.10. Decisions on the model-selection critic's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | Pooled metrics can reward separating high-rate from low-rate runs | Accepted | Lists and normalised recall per run; ROC-AUC and PR-AUC within run; background-only baseline |
| 2 | Folds unspecified; unseen module; 2013 October labels not available for February 2014 | Accepted | Leave-one-run-out folds stated; module terms as deviations, CCC apart; labels-available variant for 2014 B runs |
| 3 | One test set judges many comparisons | Accepted | One primary comparison (S1); all variants are sensitivity analyses |
| 4 | AQ2 gives pooled, not per-module, associations; counts were not those of the 9 training runs | Accepted | Sign × module terms; fit stated for 9 runs and 6 modules; task signs only where a task is due |
| 5 | Reasons from AQ2 would contradict the AQ3 score; adjusted estimates are partial effects | Accepted | Reasons from the scoring model; unadjusted and adjusted estimates side by side; correlation check |
| 6 | Choice leans on literature; no switching rule | Accepted in part | Switching rule in Table A.5, step 4; rationale led by the project's constraints (Section 3.3) |
| 7 | Survival candidate rejected on a misstated assumption | Accepted | Fail is not a time-to-event outcome; non-informative censoring (follow-up stopping for reasons unrelated to the risk of withdrawal) stated as an assumption |
| 8 | Sample size says nothing about transfer; source of the anticipated R² | Accepted | Transfer tested by the run split; Riley default cited; minimums per cut-off |
| 9 | Ranks or probabilities for tutors not decided | Accepted | Ranks and reasons; probabilities only if S3 holds; tiers fixed from capacity |
| 10 | Fairness audit underpowered; dropping attributes is not enough | Accepted | Pooled confirmatory groups; proxy check; separation named |
| 11 | Risk order assumed to match need; recall has a ceiling | Accepted | Assumption stated as untested; normalised recall; Fail and Withdrawn split |
| 12 | Unknown withdrawal days and repeat students may leak | Accepted in part | Sensitivity analyses of Table A.5, step 7; previous attempts are recorded at registration and stay legitimate |

Table A.11 records the decision on each of the evaluation reviewer's 12 critiques.

**Table A.11. Decisions on the evaluation reviewer's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | 2013 runs hold 6 modules, not 7 | Accepted | AQ2 rule as a share of modules; unseen-module rule; CCC apart |
| 2 | Run lists stand in for tutor capacity; metrics re-express one count | Accepted | Limitation and risk R8; normalised recall defined; net benefit as context |
| 3 | S1 inference under-specified with 13 runs | Accepted | Paired two-level bootstrap with re-formed lists; sign-flip test; wins, ties and losses |
| 4 | S2 ambiguous and unanchored | Accepted | S2 reported, not a gate |
| 5 | No primary test population | Accepted | S1 on all 13 runs, all eligible enrolments, day 27, k = 5 per 20 |
| 6 | Calibration intercept ill-defined; failure path reuses the test | Accepted | Calibration-in-the-large defined as the intercept with the score's log-odds as offset (coefficient fixed at 1); bounds on the estimates pooled over all runs; recalibration only in development or on a run after the 2014 test runs |
| 7 | Model choice on another aggregation; overlap removal in inner folds | Accepted | Same metric as S1; margin of about 89 students; removal in all loops, outer and inner |
| 8 | Fairness gate blind for small groups; two-sided and one-sided rules | Accepted | Eligibility from enrolments; one-sided; Holm adjustment; "not cleared" for small groups |
| 9 | ABROCA without reference | Accepted | Within run, permutation reference, sign reported, descriptive only |
| 10 | Odds ratios overstate effects at this base rate; the threshold is too easy; AQ2 and AQ3 are coupled | Accepted | Risk difference with a 5-point smallest effect; rule frozen; 2014 AQ2 cannot change AQ3 |
| 11 | Error-analysis gaps | Accepted | Reachable non-completers, active students, list stability, history slices, CCC |
| 12 | Missing risks and mismatched controls | Accepted | Sixteen risks in Table A.9; controls of misreading coefficients as causes (R9), claiming that contact works (R10) and automation bias (R13) matched to their risks |

Each reviewer was a separate generative AI session that could read only the brief and the appendices named in its prompt, and team members checked every critique against the design facts before deciding. The prompts are given in English in abridged form, with documents named by their place in this report. The model-selection critic received this instruction:

> You act as the "Model selection" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the AQ Modeling Briefs (Section 2.1), the candidate comparison (Appendix I) and the
> sample sizes and counts from the prepared data (Appendix III). Do not search the web, do not open any data file, do
> not invent benchmark results, metric thresholds or performance numbers, and do not choose the model for the team.
> Challenge the model selection as a sceptical senior analyst would: (1) mismatch between each AQ's question, output
> and the chosen method; (2) whether each modeling AQ has a sensible baseline and 2–3 real candidate families, or a
> straw-man baseline; (3) whether the rationale is tied to the data facts and constraints, or rests on algorithm
> reputation; (4) assumptions the team has not checked; (5) causal overclaim or confusion between association,
> prediction and benefit; (6) leakage or test-set exposure risks created by the modeling plan; (7) anything that makes
> the choice hard to act on for tutors (decision D1) or unfair to groups. Write at most 12 numbered critiques, most
> important first, each with the passage, the problem, why it matters and a concrete recommendation.

The evaluation reviewer received this instruction:

> You act as the "Evaluation design" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the Evaluation Design Cards and metric definitions (Appendix II), the validation
> and test protocol (Appendix III), the error and fairness analysis (Appendix IV), the risk register (Appendix V) and the
> counts from the prepared data. Do not search the web, do not open any data file, do not invent results, benchmarks or
> performance numbers. Review the evaluation design as a sceptical methodologist: (1) whether each metric reflects the
> decision it serves and whether any metric is misleading for this base rate; (2) whether the success criteria are
> fixed in advance, falsifiable, internally consistent, and neither trivially easy nor impossible; (3) validation:
> leakage paths, test reuse, grouping of students across runs and years, nested tuning, the AQ2/AQ3 interaction; (4)
> uncertainty estimation with 9 training and 13 test runs; (5) calibration criteria and what happens when they fail;
> (6) fairness: choice of criterion, small groups, multiple comparisons, interpretation of ABROCA; (7) error analysis
> gaps; (8) risks missing from the register or controls that do not match their risk. Write at most 12 numbered
> critiques, most important first, each with the passage, the problem, why it matters and a concrete recommendation.
