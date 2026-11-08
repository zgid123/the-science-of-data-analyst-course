# 6. Generative AI Usage

**Roles.** Alongside the risks of Part 5, generative AI was used in the roles that the brief allows a modeling
partner: explaining methods, proposing and challenging candidate families, and reviewing metrics, splits, leakage,
class imbalance, calibration and fairness, while the final choice and the evidence for it remain the team's [1]. AI
agents worked on both sides of each review, as reviewer and as the drafter whose design was reviewed, and team members
verified every decision. Three roles were used: a literature assistant that found and read sources, a model-selection
critic that challenged the briefs and the candidate comparison, and an evaluation reviewer that challenged the cards,
the protocol, the fairness analysis and the risks.

**AI Decision Log.** Table 6.1 is the AI Decision Log in the brief's five columns, one row per significant AI
contribution: the prompt or goal, the AI's suggestion, the team's decision, the evidence used to verify it and its
effect on the proposal.

**Table 6.1. AI Decision Log**

| Prompt / goal | AI suggestion | Team decision | Evidence / verification | Effect on the proposal |
| :---- | :---- | :---- | :---- | :---- |
| Find well-known sources on method choice for each AQ (literature assistant) | Explain-versus-predict distinction; rule and simple baselines first; interpretable models for high-stakes use; sample size criteria; survival and ranking framings | Accepted after reading each source | Every statement checked against a saved copy of its source, with a verbatim quotation | Parts 2–3; Appendices I–II |
| Find sources on evaluation design (literature assistant) | TRIPOD+AI and the Prediction model Risk Of Bias ASsessment Tool for AI (PROBAST+AI); calibration; grouped folds; nested tuning; leakage types; pre-registration; hierarchical bootstrap; slicing analysis | Accepted; the imbalance argument for precision–recall curves not used, since non-completion is 44–46% | Same verification | Part 4; Appendices III–V |
| Find sources on risk, causality, fairness and regulation (literature assistant) | Target trials and uplift need treatment data; fairness criteria conflict; EU AI Act and Vietnam's AI law and high-risk list; performative prediction | Accepted; the EU Act used as a reference standard, Vietnamese law as binding on a Vietnamese pilot | Legal texts read in official copies where available; the EU text in a secondary copy | Part 5; Appendix VI |
| Review the model selection as a sceptical analyst (critic) | 12 critiques: within-run evaluation, run-grouped folds, one primary test comparison, AQ2 per-module output, reasons from the scoring model, rule for switching to the challenger, survival assumption, sample size versus transfer, ranks versus probabilities, fairness power, risk versus need, repeat students | 10 accepted, 2 accepted in part (Table A.19) | Each critique checked against the design facts and the run lengths | Appendices I–II and IV–VI |
| Review the evaluation design as a methodologist (reviewer) | 12 critiques: unseen module, per-run versus tutor capacity, S1 inference, S2 basis, primary population, calibration definition, model-choice aggregation, fairness gate, ABROCA reference, AQ2 effect measure, error-analysis gaps, missing risks | 12 accepted (Table A.20) | Arithmetic of each critique recomputed | Appendices III–VI; S2 (precision at capacity) reported, not a gate |

**Decisions on the critiques.** Tables 6.2 and 6.3 give the team's decision on each critique of the model-selection
critic and of the evaluation reviewer, with the evidence used to check it.

**Table 6.2. Decisions on the model-selection critic's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | Pooled metrics can reward separating high-rate from low-rate runs | Accepted | Lists and normalised recall per run; ROC-AUC and PR-AUC within run; background-only baseline |
| 2 | Folds unspecified; unseen module; 2013 October labels not available for February 2014 | Accepted | Leave-one-run-out folds stated; module terms as deviations, CCC apart; labels-available variant for 2014 B runs |
| 3 | One test set judges many comparisons | Accepted | One primary comparison (S1); all variants are sensitivity analyses |
| 4 | AQ2 gives pooled, not per-module, associations; counts were not those of the 9 training runs | Accepted | Sign × module terms; fit stated for 9 runs and 6 modules; task signs only where a task is due |
| 5 | Reasons from AQ2 would contradict the AQ3 score; adjusted estimates are partial effects | Accepted | Reasons from the scoring model; unadjusted and adjusted estimates side by side; correlation check |
| 6 | Choice leans on literature; no switching rule | Accepted in part | Switching rule in Table A.13, step 4; rationale led by the project's constraints (Section 3.3) |
| 7 | Survival candidate rejected on a misstated assumption | Accepted | Fail is not a time-to-event outcome; non-informative censoring stated as an assumption |
| 8 | Sample size says nothing about transfer; source of the anticipated R² | Accepted | Transfer tested by the run split; Riley default cited; minimums per cut-off |
| 9 | Ranks or probabilities for tutors not decided | Accepted | Ranks and reasons; probabilities only if S3 holds; tiers fixed from capacity |
| 10 | Fairness audit underpowered; dropping attributes is not enough | Accepted | Pooled confirmatory groups; proxy check; separation named |
| 11 | Risk order assumed to match need; recall has a ceiling | Accepted | Assumption stated as untested; normalised recall; Fail and Withdrawn split |
| 12 | Unknown withdrawal days and repeat students may leak | Accepted in part | Sensitivity analyses of Table A.13, step 7; previous attempts are recorded at registration and stay legitimate |

**Table 6.3. Decisions on the evaluation reviewer's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | 2013 runs hold 6 modules, not 7 | Accepted | AQ2 rule as a share of modules; unseen-module rule; CCC apart |
| 2 | Run lists stand in for tutor capacity; metrics re-express one count | Accepted | Limitation and risk R8; normalised recall defined; net benefit as context |
| 3 | S1 inference under-specified with 13 runs | Accepted | Paired two-level bootstrap with re-formed lists; sign-flip test; wins, ties and losses |
| 4 | S2 ambiguous and unanchored | Accepted | S2 reported, not a gate |
| 5 | No primary test population | Accepted | S1 on all 13 runs, all eligible enrolments, day 27, k = 5 per 20 |
| 6 | Calibration intercept ill-defined; failure path reuses the test | Accepted | Calibration-in-the-large with offset; pooled bounds; recalibration only in development or on a later run |
| 7 | Model choice on another aggregation; overlap removal in inner folds | Accepted | Same metric as S1; margin of about 89 students; removal in all loops |
| 8 | Fairness gate blind for small groups; two-sided and one-sided rules | Accepted | Eligibility from enrolments; one-sided; Holm adjustment; "not cleared" for small groups |
| 9 | ABROCA without reference | Accepted | Within run, permutation reference, sign reported, descriptive only |
| 10 | Odds ratios overstate effects at this base rate; the threshold is too easy; AQ2 and AQ3 are coupled | Accepted | Risk difference with a 5-point smallest effect; rule frozen; 2014 AQ2 cannot change AQ3 |
| 11 | Error-analysis gaps | Accepted | Reachable non-completers, active students, list stability, history slices, CCC |
| 12 | Missing risks and mismatched controls | Accepted | Sixteen risks in Table A.17; controls of misreading coefficients as causes (R9), claiming that contact works (R10) and automation bias (R13) matched to their risks |

**Reflection.** The reviewers made the most consequential points. They showed, for example, that the training runs
cover 6 modules rather than 7, that the October 2013 runs end after the February 2014 runs need scores, and that a
success rule requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be met by chance
about 13% of the time; the team verified each point against the prepared data before adopting it. The reviews were
most useful where the AI had to argue from the counts of the prepared data rather than from general advice. No AI
produced a metric value, a threshold or a result: every number in this proposal is a count from the prepared data or a
value fixed by the team with its reason, as the brief requires [1].
