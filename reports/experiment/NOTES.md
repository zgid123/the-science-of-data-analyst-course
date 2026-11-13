# Notes: AQ1–AQ4 on OULAD 2013–2014 (Milestone 4 Level 2 prototype, results for the Final Report)

One working record for the whole analysis. The report (`report.md`) says what is true now; everything about how the work got there lives here.

## Brief

- **Purpose and reader.** Answer the four Analytical Questions of team N04 (MTH045) on the prepared OULAD dataset, deeply and readably, for the team and the instructor; the results feed Section 10 (experimental results) and Section 11 (findings) of the Milestone 5 Final Report. The decisions supported are D1 (whom tutors contact at the week-3 and week-5 review points), D2 (where advisors' time goes) and D3 (whether to extend after the pilot).
- **Questions, in priority order.** AQ3 (can a model beat the early-sign rule at day 13 and day 27, trained on 2013, tested on 2014) and AQ4 (who tops a list of fixed capacity, with what gain, recall and fairness) carry decision D1; AQ1 (non-completion by module, run, start month and year; week of the first missed task) and AQ2 (which day-27 signs go with non-completion within module run) carry D2, D3 and the reasons shown with each name.
- **Scope.** 22 runs of 7 OULAD modules, 2013 and 2014; unit = enrolment (one student in one module run); non-completion = Fail or Withdrawn; time = days from the run start; cut-offs day 13 and day 27.
- **Deliverable.** A finding-led report (`report.md`) with figures, all numbers from `results/`, plus this record; requested location `reports/code/`, renamed `reports/experiment/` on 2026-11-13 (the Level 2 prototype experiment).
- **Why this folder was rebuilt.** The owner reported that a teammate was disappointed with the earlier version of this folder (four reports of 2,700–6,400 words each, process history and protocol IDs in every summary). Reading it against the skill: the analysis was rigorous, the communication was the "defensive" failure mode (findings buried under rerun history and caveats), and it answered the questions without the decision-level depth (when students leave, what the model adds over the rule and for whom, the yield of each extra contact, what tutors would see). This version keeps the inherited design and rigour, adds those analyses, and tells the result in one report of about 2,000 words of body text. Proposed reading of the feedback, not confirmed with the teammate (stage 10).

## Inherited project record

The Milestone 4 Level 1 report (`reports/milestone-4/report/`) fixes the design. Everything below is adopted as given.

| Item | Source | Adopted as given? | If not: what was done, why, result both ways |
| :---- | :---- | :---- | :---- |
| AQ wording, analytics levels, decisions D1–D3 | M4 Section 1.1, Table 1.1 | Yes | – |
| Populations: KPI = registered at day 14 (28,061); day-13 and day-27 feature views | M4 Table 2.1–2.4, Table A.6 | Yes | Counts asserted in `code/02_prepare.py` (19 checks, all PASS) |
| Five AQ2 signs, where each is defined (run calendar), criterion ≥ 5 points, interval > 0, two-thirds of modules | M4 Table 4.2; design P16–P17 of the team's earlier implementation | Yes | – |
| AQ2 model: run fixed effects, log prior attempts, log credits, sign × module terms with the 20/20 support rule, HC1, delta-method average risk difference | M4 Table 4.2; earlier implementation P17 | Yes | Reproduces the earlier estimates to 4 decimals in both years |
| Predictor sets (19 primary, extended + weekly clicks), `cma_score_mean_c` left out | `predictor_sets.json`; M4 Table 2.3 | Yes | – |
| Candidates B3, M1–M4; grids; log-loss tuning; ties to the stronger penalty / smaller model; choice margin 0.03 and 7 of 9 folds | M4 Section 3.3, Appendix III; earlier P06–P11 | Yes | Same choice (M1) and the same 10 tuned settings as the earlier implementation |
| Leave-one-run-out folds removing students also in the validation run | M4 Table A.5 step 2 | Yes | – |
| Capacity k = 5 × ⌈n/20⌉ (3 × for sensitivity); rule-ranked list by number of signs, then lower activity; fixed tie-breaker seed 20261112 | M4 Section 4.1; earlier P03–P05 | Yes | Rule lists identical to the earlier implementation in all 4 cut-off × capacity views |
| Gate S1 (bootstrap 2,000, sign-flip exact), S2, S3 bounds, FR1 (3 groups, 5,000 replicates, Holm, −10 points) | M4 Table 4.5, Section 4.4 | Yes | – |
| Order of work: AQ2 2013 → AQ3 development → freeze → test → AQ4 → AQ2 2014 → AQ1 | M4 Appendix III; earlier P02 | Yes | `run_all.sh` follows it; `logs/holdout-access.md` |

Not carried over (scope, not departures): the labels-available variant, net benefit, ABROCA and the proxy check of the Milestone 4 error/fairness list. They are descriptive extras in the design that cannot change any verdict; listed under Open issues.

## Lifecycle record

| # | Stage | What was done | Evidence (file, step log) | Gate |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Business Understanding | Read the M4 and M5 briefs, the M4 Level 1 design and the earlier implementation; wrote the brief above, including the teammate feedback as the reason for the rebuild | Brief above; `milestones/04`, `milestones/05`; M4 report Sections 1–2 | Met: four AQs pass the Clear/Specific/Scoped/Data-oriented/Answerable test as written in M4; decisions and success criteria fixed |
| 2 | Analytic Approach | One line per AQ (stage 2 table); the alternative explanation for each named and tested | Stage 2 table | Met: simplest adequate method per AQ, each with a baseline |
| 3 | Data Requirements | Mapped each AQ to the prepared views | Stage 3 table | Met: all four answerable; AQ4 answerable as a ranking only (no contact record) |
| 4 | Data Collection | Prepared dataset OULAD-N04-prepared-1.0 (Milestone 3 package) and 5 raw OULAD tables pinned by SHA-256; hashes equal the M3 version manifest | `data-manifest.json`; `logs/00_verify_inputs.md` | Met |
| 5 | Data Understanding | Profile of the four prepared views; field meanings from the M3 data dictionary checked against records (registration days, first missed week, task calendar) | `results/profile.md`; `logs/01_profile.md`; stage 5 table | Met |
| 6 | Data Preparation | No new cleaning: populations asserted against the design; signs derived in code from the prepared features | `results/prep_reconciliation.csv`; `logs/02_prepare.md` | Met: 19 of 19 reconciliation checks PASS |
| 7 | Modeling | AQ2 2013; AQ3 development, freeze, single scoring of 2014; AQ3 evaluation; AQ4 lists, yield, reasons, fairness; AQ2 2014; AQ1; seven figures | `results/aq*`; `figures/`; logs 03–11, 15 | Met: every finding has numbers, a comparison and a tested alternative (stage 7 table) |
| 8 | Evaluation | Second code path from raw CSVs and saved scores (8 checks PASS); reconciliation with the earlier team implementation; holdout order check; report check; independent reviewer | `results/check_recompute.csv`; `results/compare_prior.csv`; `logs/14_holdout_order.md`; `logs/99_check_report.md`; Independent review below | Met: no critical failure; ledger below |
| 9 | Deployment | `report.md` with 14 tables written from `results/`, 82 quoted numbers checked; figures viewed one by one and corrected (order, overlaps, one overstated title) | `logs/98_fill_tables.md`, `logs/99_check_report.md` | Met: report check PASS; read top to bottom |
| 10 | Feedback | Teammate feedback on the earlier version recorded and routed to stages 7 and 9; feedback on this version PENDING | Stage 10 table | Met: observed feedback separated from plans |

## Stage records

**Stage 2 – analytic approach**

| Question | Analytics type and method | Comparison and baseline | Main threat and how it is tested |
| :---- | :---- | :---- | :---- |
| AQ1 | Descriptive: grouped rates with Wilson intervals; exit-timing bands; first missed week | Second denominator (all enrolments); like-for-like year comparison (shared modules, shared module × month pairs, Mantel–Haenszel) | Denominator and run mix create a year difference → both denominators and like-for-like sets; second code path from raw tables |
| AQ2 | Diagnostic: logistic association model within run (design P17) | Unadjusted difference on the same rows; replication on 2014 | Overlapping activity signs and a graded activity effect → sign correlations, fit check by five activity levels, continuous-clicks sensitivity |
| AQ3 | Predictive: penalised logistic, temporal split 2013 → 2014 | Rule-ranked list, background-only model, random list | Gain within noise → paired two-level bootstrap and sign-flip test; transfer → paired/unpaired runs, CCC apart, repeat students out |
| AQ4 | Prescriptive (ranking): top-k per run from frozen scores | Random and rule-ranked lists of the same length | Risk ≠ benefit, unfair reach → fairness FR1; yield per contact; reachability |

**Stage 3 – data requirements**

| Question | Data needed | Available? | Status |
| :---- | :---- | :---- | :---- |
| AQ1 | Outcome, registration and withdrawal days, run, task calendar and submissions | `enrolment.parquet`, `assessment_due.parquet` | Answerable |
| AQ2 | Day-27 behaviour signs, run, prior attempts, credits | `features_d27.parquet` | Answerable (association only) |
| AQ3 | Pre-cut-off predictors at day 13 and 27; outcome; year | `features_d13/27.parquet` | Answerable |
| AQ4 | AQ3 scores, audit fields, withdrawal day | Saved scores; `features_d27`; `enrolment` | Answerable as a ranking; effect of contact unsupported (no contact data) |

**Stage 4 – source inventory**

| Source | Format, rows | Coverage | Access and sensitivity |
| :---- | :---- | :---- | :---- |
| OULAD-N04-prepared-1.0 (`../milestone-3/package/data/processed/`) | Parquet: enrolment 32,593; features_d13 28,069; features_d27 27,535; assessment_due 286,898 | 22 runs, 7 modules, 2013–2014 | Open data (CC BY 4.0); student IDs pseudonymised by the provider; audit fields (gender, disability, IMD, age) used for fairness only |
| Raw OULAD tables (`../milestone-3/package/data/raw/`) | CSV: studentInfo 32,593; studentRegistration 32,593; assessments; studentAssessment; courses | Same | Same; used only for the second code path |

**Stage 5 – field meanings and data quality**

| Field or dimension | What was checked | Finding | Consequence |
| :---- | :---- | :---- | :---- |
| `enrolled_d14` | Recomputed from raw registration and withdrawal days | 28,061 = registered by day 14 (or day missing, 7 rows) and not withdrawn by day 14; 58 late registrants excluded | KPI denominator agreed in all 22 runs (`check_recompute.csv`) |
| Withdrawal day | Missing for 93 Withdrawn rows | 0.5% of non-completers | Own band in the exit timing; sensitivity row in AQ3 |
| Task calendar | Tasks due by day 27 per run | 16 of 22 runs have a task due; 10 students in those runs had nothing due | Task signs defined per run (design); not "no missed task" where nothing was due |
| `first_missed_week` | Meaning from the dictionary; null when no task missed | 75.1% of non-completers miss one eventually | Shares by week computed over all KPI enrolments |
| Profile | `results/profile.md` | No duplicate keys; audit fields complete; `imd_band` "Missing" 610 at day 27 (test) | Missing band kept as a fairness group |
| Outcome shares in the profile | The profile prints pooled final-result shares (both years) | Read before the freeze | No AQ3 choice depends on it; the design was fixed in M4 |

**Stage 6 – preparation log**

| Step | Rows or entities affected | Reason |
| :---- | :---- | :---- |
| None beyond the prepared dataset | – | Milestone 3 already cleaned and documented; this analysis only derives signs, lists and populations in code |

**Stage 7 – follow-ups**

| Observation | Why follow up | Result | How the interpretation changed |
| :---- | :---- | :---- | :---- |
| AQ2 fit check misfits by activity level (3 of 5 levels outside the band in 2013) | The yes/no low-activity sign may proxy a graded effect | With log clicks as a continuous adjustment, low activity falls to +2.9 / +0.8 points and fails the criterion; the other four signs hold | Report says low activity matters as an amount, not a flag |
| The model beats the rule by only 82 listed non-completers | Who makes the difference? | Swap analysis: model-only picks are active students with prior attempts (59.7% non-completion) vs rule-only picks with a sign (50.6%) | Gain is real and explicable, not noise; rule is a fair fallback |
| Recall only 41.5% | Where are the missed non-completers? | 60.7% of non-completers look normally active at day 27; lists reach 19.1% of them | Recommendation for a later review point (as a hypothesis) |
| Lists are fixed at 5 per 20 | Is that the right capacity? | Yield by contact slot: 92.4% first, 57.6% fifth, 47.3% seventh vs 44.0% base | Capacity recommendation (≈ 6 per 20 limit) |
| Reasons per name | What would tutors see? | 14.2% of listed students are listed mainly for prior education | Recommend showing behavioural reasons only |
| Exit timing | Can a list reach non-completers at all? | 25.9% gone before day 14; 70.2% still enrolled after day 27 | Adds a pre-day-14 contact to D2 |
| Year difference −3.5 points on the day-14 population | Real change or denominator? | All enrolments: −0.2; share leaving before day 14 rose from 10.7% to 15.8% | KPI recommendation for D3 |

**Stage 10 – feedback**

| Feedback received (from whom, when) or PENDING | What it changed |
| :---- | :---- |
| Owner, 2026-11-13: the teammate was disappointed with the earlier `reports/code` result; asked to redo AQ1–AQ4 deeply and evaluate carefully | Stage 7: added exit timing, swap analysis, blind spot, contact yield, reasons; stage 9: one finding-led report, history kept here |
| Teammate and instructor feedback on this version | PENDING |
| Pilot outcome (KPI, effect of contact) | PENDING: needs the pilot; recommendation 5 in the report proposes randomised contact |

## Decisions

| Decision | Reason | Decided before or after the results were seen |
| :---- | :---- | :---- |
| Adopt the M4 design unchanged, including grids, tie rules and seeds | Inherit before you define; S1 is only meaningful for a fixed design | Before (the design dates from M4) |
| Keep the rule fallback in the recommendations | The rule delivers 97.1% of the model's hits | After AQ3 test results |
| Report ranks and reasons, not probabilities | S3 met pooled but only 5 of 13 runs within bounds | After (S3 is the design's own condition) |
| Exit timing, swap analysis, blind spot, yield per contact, reasons: added views | Decision-level depth requested; none can change S1 or FR1 | Added after the test scores existed; descriptive, labelled as views, not gates |
| Reasons map coefficient × standardised value to predictor groups; module and start-month terms are "course context", not shown | Tutors act on behaviour; course context is the same for the whole run | Before reading AQ4 results |
| Install pyarrow in the shared venv | The skill profiler needs it for Parquet | Before any result |

## Check ledger

| Check (quantity, population) | Expected condition | Method / evidence | Coverage | Observed | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Input files unchanged | SHA-256 equal to manifest | `tools/data_manifest.py verify` | 11 files | All equal | PASS |
| Population counts | Equal to M4 design values | `code/02_prepare.py` | 19 counts | 19 equal | PASS |
| KPI population and non-completers per run from raw tables | Equal to prepared path | `code/12_recompute.py` | 22 runs × 2 values + totals | All equal | PASS |
| Exit-timing counts from raw tables | Equal | `code/12_recompute.py` | 2 bands | Equal | PASS |
| Listed non-completers, M1 and rule, day 27, 5 per 20, separate ranking code | Equal to `aq3_test_pooled.csv` | `code/12_recompute.py` | 2 values | 2,868 and 2,786 equal | PASS |
| Holdout order | Freeze before the first 2014 outcome read | `tools/holdout_guard.py status` | 9 reads | Frozen 09:15:37Z, first read 09:15:39Z | PASS |
| Reconciliation with earlier team implementation, AQ1 run rates | Equal within 1e-6 | `code/13_compare_prior.py` | 22 runs, 44 cells | 0 differences | PASS |
| Same, AQ2 adjusted risk differences and supports, both years | Within 0.0005 | same | 5 signs, 20 cells | 0 differences | PASS |
| Same, AQ3 development normalised recall, 6 rankings | Within 0.0005 | same | 6 cells | 0 differences | PASS |
| Same, AQ3 test lists, 6 rankings × 2 cut-offs × 2 capacities | Equal | same | 48 cells | Rule: all equal; models: 7 cells differ by 1–3 listed students of 2,373–4,030 | PASS with explained difference: the two implementations transform the overlapping late-task counts (tasks_late = TMA late + CMA late) differently, which moves coefficients of those three columns; no verdict changes |
| Same, AQ4 fairness recalls | Within 0.0005 | same | 3 groups | 2 group recalls differ by one listed student (follows from the list difference above) | PASS with explained difference |
| Report tables equal result files | Equal | `tools/report_tables.py` + `check_report.py` | 14 tables | Equal | PASS |
| Numbers quoted in prose | Equal to their result cell after rounding | `check_report.py --claims claims.json` | 82 numbers (summary, headings, findings, recommendations) | All found; two typing errors (30.0% → 30.2%, 95.1% → 95.3%) caught and corrected before delivery | PASS |
| Figure titles | Numbers read from result tables | `code/15_figures.py` builds titles from results | 7 figures | Titles generated; one title (Figure 2) overstated a gap whose interval included 0 for one module, rewritten to "5 of 6 modules" | PASS |
| Run history phrases absent from the report | None | `check_report.py` | 7 phrases | None | PASS |
| Independent recomputation | Headline numbers agree; defects fixed | Fresh subagent with the report, results, scores and raw inputs only | All headline numbers of the summary and 4 findings | All agree; 6 wording or population defects, fixed (see Independent review) | PASS after fixes |
| Clean-copy reproduction | `run_all.sh` runs from zero; results identical | Folder copied without models, scores, results or logs; inputs copied; full run in a scratch folder | 55 result CSVs, test scores | First attempt exposed 2 issues: the manifest/symlink skill defect, and `14_headlines` missing from `run_all.sh` (added as step 14b). After the fix: exit 0, report check PASS, 55 of 55 tables and the scores byte-identical | PASS |
| Comparison with the Milestone 4 experiment (`reports/milestone-4/package/`) | Every quantity compared from result files | `code/16_compare_m4.py`; `comparison.md` checked by `check_report.py` | 42 quantities, 13 runs | Same verdict on every AQ; S3 differs (C = 0.001 tuned on recall vs C = 10 tuned on log loss); GGG-2014J changes winner | PASS (differences explained) |
| Final run | Every step exit 0 in one run | `bash run_all.sh` in place | 20 steps | All 0; report check PASS (87 numbers, 15 tables) | PASS |

## Independent review

Reviewer: a fresh subagent that had not seen the code, notes, logs or claims. It was given `report.md`, `results/`, the saved 2014 scores, the prepared parquet views with their dictionary, and the raw OULAD CSVs, using the brief in `tools/reviewer-brief.md`. 2026-11-13.

**What it recomputed with its own code:**

- every headline number of the summary and the four findings, including the KPI population rebuilt from the raw CSVs;
- all list counts, both calibration numbers and the sign-flip p;
- the contact yields and the fairness recalls;
- its own AQ2 logit for the missed-task sign in 2013: +40.65 points, against +40.7 reported.

All agree after rounding. All seven figure titles match their result tables.

**Demonstrated defects and corrections:**

| # | Defect | Correction |
| :---- | :---- | :---- |
| 1 | "Median week 9" was attributed to the normally active 2014 non-completers; it is the median for all KPI non-completers. For the blind-spot group it is week 13, and 32.4% never miss a task | New result `results/aq1_blind_spot_timing.csv` (step 11_aq1). Summary and recommendation 2 rewritten with week 13 and 32.4%; recommendation 2 now says the later review point needs signs beyond missed tasks |
| 2 | "Model's own picks are mostly … a previous attempt" read as if most had one (30.7%) | Already rewritten before the review result arrived ("more often have a previous attempt … 30.7%, against 6.4%") |
| 3 | Year rows of Table 1 shown as "2,013" / "2,014" | `11_aq1.py` writes "2013 (9 runs)"; it is a skill observation (report_tables formats numeric labels) |
| 4 | 15.8% / 10.7% referred to Table B.2, which shows only differences; "had left" also covers 1.4% late registrants | Table B.9 added from `aq1_not_registered_d14.csv`; wording "no longer (or not yet) registered at day 14" |
| 5 | "module and start month move the rate" is causal wording on a descriptive table | "the rate varies most by module and start month" |
| 6 | Recommendation 3 implied a contact before day 14 could reach all 25.9%; 15.6 of those points left before the run started, and no effect of contact is shown | Split into 15.6% before the start and 10.3% in days 0–13; recommends testing a welcome contact before and at the start; "whether such a contact keeps anyone is untested" |

Non-defect note from the reviewer: the correlation 0.45 is the 2014 value (2013: 0.50); the report now says "in 2014".

## Open issues

- Not run (descriptive extras of the M4 error/fairness list that cannot change a verdict): labels-available variant, net benefit, ABROCA, proxy check, list stability under the bootstrap. The earlier team implementation (commit 7516b83) has them.
- Skill defects found here, fixed in the `data-analyst` source repository on 2026-11-13 and copied into `.agents/skills/data-analyst/scripts/` and `tools/` (each covered by a new test that fails on the old script):
  - `profile_data.py` reads Parquet only through pandas + pyarrow, and fails without pyarrow even when polars is installed.
  - `data_manifest.checked()` resolves symlinks while `verify` does not, so an input reached through a symlinked folder passes `verify` and is then rejected by `checked()`. This was found by the clean-copy reproduction.
  - `report_tables.py` prints negative whole numbers with a hyphen ("-1") but negative decimals with a minus sign ("−0.002"); cosmetic, not fixed.
  - `report_tables.py` formats numeric label cells such as years with a thousands separator ("2,013").
- Corrected in this folder during drafting: `common.pooled` cast the random list's expected count to an integer (1,737.9 shown as 1,737); it now keeps the value.
- AQ4 fairness bootstrap (5,000 two-level replicates in pure Python) takes several minutes; vectorising it would shorten `run_all.sh`.
