# Execution Plan: From Modeling to Evaluation: Modeling Strategy, Method Selection and Evaluation Design

Plan date: 2026-11-06. Input outline: [reference.md](reference.md), derived from the instructor brief
`milestones/04/milestone-4.md`. Output: the Milestone 4 Modeling & Evaluation Proposal (Level 1), as
fine-grained sections in `report/` compiled to Word in English and Vietnamese by the build-report skill. No model is
fitted at this milestone. The machine-readable half of this plan is `plan.toml`; keep both in step.

## 1. Goal and Scope

The brief asks for a Modeling & Evaluation Proposal with seven deliverables (brief section 12). Each is mapped to its
place:

| Brief deliverable | Content required | Location |
| :---- | :---- | :---- |
| A. Updated Traceability Matrix | Goal → AQ → level → task → prepared data → approach → evaluation → decision | Part 8 (Table 8.1), Appendix VIII |
| B. AQ Modeling Briefs | One brief per retained AQ | Part 2 (Table 2.1), Appendix I |
| C. Candidate Solution Matrix | Baseline, candidate families, primary approach, rationale | Part 3 (Table 3.1), Appendix II |
| D. Evaluation Plan | Metrics, validation, baseline, error analysis, fairness, success criterion | Part 4 (Tables 4.1–4.2, Figure 4.1), Appendices III–V |
| E. Risk & Ethics Notes | Leakage, overfitting, interpretability, causal limits, fairness, high-stakes use | Part 5 (Table 5.1), Appendix VI |
| F. AI Decision Log | Prompt, suggestion, decision, verification, effect | Part 6 (Table 6.1), Appendix VII |
| G. Prototype code | Optional | Not delivered; Part 7 specifies its protocol (decision T02) |

Outline sections map one to one to report parts (brief section 13; Part 7 is a protocol, decision T02):

| Brief section 13 | Report part |
| :---- | :---- |
| 1 Project Context & Continuity | Part 1 |
| 2 AQ-to-Technical-Task Mapping | Part 2 |
| 3 Candidate Modeling Approaches | Part 3 |
| 4 Evaluation Design | Part 4 |
| 5 Risk, Ethics & Limitations | Part 5 |
| 6 Generative AI Usage | Part 6 |
| 7 Optional Prototype Results | Part 7, Prototype Protocol (specification, no results) |
| 8 Updated Traceability Matrix | Part 8 |

Rules:

- `CLAUDE.md` style; final state only; every section reads on its own; identifiers paired with their words.
- The reader has only the submitted report (and the Milestone 3 package already submitted): no repository paths, logs,
  source or claim IDs in the report.
- Level 1 only: no model is trained, tuned or scored; no performance number is stated or implied. Success criteria
  are fixed before any result exists (brief section 8, checklist "Evaluation Plan written before prototype").
- Facts about the data come from `code/design_facts.py` (reads the Milestone 3 prepared views, fits nothing) and are
  saved in `results/`; facts about methods come from the research trail.
- AI critics are AI on both sides, and team members verify; the report never calls them team-run.
- APA 7, `[Sxxx]` while drafting, `[n]` after T17. Main text 10–12 pages (decision T02). Submission 14 November 2026.

### 1.1 Core Rule: Record Every Crawl and Every Run on Disk

```
report sentence [n] → reference n → sources.md Sxxx → claim → comprehension.md → crawl.md
report number       → results/design_facts.* → code/design_facts.py → logs/T08_design_facts.log
design decision     → research/design/*.md → research/reviews/NN-ai-*-output.md (AI critique)
```

## 2. Tools Used

| Tool | Purpose |
| :---- | :---- |
| `WebSearch`, `fetch.py`, `WebFetch`, `trail.py` | Research tasks T05–T07 (one foreground subagent each, run as a wave) |
| polars (`./venv`), `code/design_facts.py` | Counts from the Milestone 3 prepared views (no model) |
| `Agent` (isolated, foreground) | AI model-selection critic (T10), AI evaluation reviewer (T11) |
| build-report | Checks, figures (`figures/milestone_4/`), Word build, Vietnamese twin |
| `progress.py`, `check_trail.py`, `check_drafts.py`, `finalize_refs.py`, `spot_check.py` | Ledger and gates |

## 3. Target File Map (`report/`)

Section, table and figure numbers are fixed here before writing.

| File | Content | Tables / figures | Evidence |
| :---- | :---- | :---- | :---- |
| `00-0` | Brief's info table: team, members, title, M1 version, M2 dataset/version, M3 prepared version, 14 November 2026 | – | T04 |
| `00-1`, `00-2` | Abbreviations; terms (technical task, baseline, primary approach, prediction point, list at capacity, lift, attainable recall, calibration, …) | – | T16 |
| `01-00` | Part 1 intro: Milestone 4 question; Level 1 scope | – | S001 |
| `01-01` | Goal, SMART, KPIs, D1–D3; AQ1–AQ4 after C01–C13 | Table 1.1 AQs and decisions | T04 |
| `01-02` | Prepared dataset version, views, cut-offs, split; entry gate of brief section 3 | Table 1.2 entry gate | T04, T08 |
| `02-00` | Part 2 intro | – | – |
| `02-01` | AQ Modeling Briefs (8 attributes × 4 AQs) | Table 2.1 | T09 |
| `02-02` | Explain vs predict; task per AQ; ranking under capacity; prediction points and target timing | Figure 2.1 AQ → task → output → decision | T05, T09 |
| `03-00` | Part 3 intro | – | – |
| `03-01` | Eight criteria of brief 7.1; Candidate Solution Matrix | Table 3.1 | T05, T09, T10 |
| `03-02` | AQ1 rates with intervals; AQ2 unadjusted comparison and logistic regression within module, clustered errors; why no ML | – | T05, T08 |
| `03-03` | AQ3: rule and simple baselines; penalised logistic regression (primary); gradient-boosted trees; discrete-time survival as alternative; sample size, imbalance, calibration | – | T05, T08 |
| `03-04` | AQ4: top-k per run at capacity from AQ3 scores; rule ranked by number of signs; no causal or uplift claim | – | T05, T07, T08 |
| `04-00` | Part 4 intro | – | – |
| `04-01` | Evaluation Design Cards summary per AQ | Table 4.1 | T06, T09 |
| `04-02` | Time split, leave-one-run-out folds grouped by student inside 2013, nested selection, single test use, frozen plan | Figure 4.1 validation timeline | T06, T08 |
| `04-03` | Metrics: lift and recall at capacity, PR-AUC, calibration (intercept, slope, Brier), comparison with rule, clustered bootstrap intervals; success criteria fixed in advance | Table 4.2 success criteria | T06, T08 |
| `04-04` | Error analysis by threshold, run, module; subgroup and fairness checks (recall and calibration by group, ABROCA), small-group handling | – | T06, T07, T08 |
| `05-00` | Part 5 intro with Risk & Ethics Notes | Table 5.1 | T07, T09 |
| `05-01` | Leakage, overfitting, test reuse, interpretability | – | T06, T07 |
| `05-02` | Causal limits, deferred contact, future experiment; fairness; high-stakes use, human oversight; regulation | – | T07 |
| `06-00` | AI Decision Log summary and reflection | Table 6.1 | T10, T11 |
| `07-00` | Prototype protocol, brief section 10 steps 1–8 | Table 7.1 | T09 |
| `08-00` | Updated Traceability Matrix (brief 12.1 columns) | Table 8.1 | T09 |
| `09-references` | APA 7, first-citation order | – | T17 |
| `10-00…10-08` | Appendices I–VIII, generated by `code/build_appendices.py` from `research/design/` and `research/reviews/` | Tables A.1… | T15 |

## 4. Sequential Task Protocol

LOAD → DO → WRITE → VERIFY → DECIDE → CLOSE → FREE (research-report reference.md section 1). Resume with
`progress.py --base reports/milestone-4 next`. Source IDs: seeds S001–S002; Part 2 S200–S299 and Part 3 S300–S399
(T05); Part 4 S400–S499 (T06); Part 5 S500–S599 (T07).

**Wave 1** runs T05, T06, T07 and T08 together: the three research tasks write disjoint source blocks and claims
files (parts 2–3, 4, 5) through `trail.py`, and each works in its own scratch folder; T08 writes only
`code/design_facts.py`, `results/` and its log and reads no research file. Everything else runs one at a time.

## 5. Task Cards

**T01: Scaffold and register.** `scaffold.py build`, `scaffold.py register`; tasks.toml block like milestone-3
(glossaries, layout, figures package `figures.milestone_4`, abbreviations, people, output names
`N04_Milestone4_EN.docx` / `_VI.docx`).
- [ ] `scaffold.py check` 0 errors; `tasks.toml` has `[milestone-4]`.

**T02: HC, scope inputs.** Decided in conversation 2026-11-06 (Decisions).

**T03: R, seeds.** S001 brief (local, verbatim copy); S002 OULAD descriptor (crawl reused from the Milestone 3
trail). R1–R8.

**T04: Entry gate.** `code/freeze_baseline.py` copies from the Milestone 3 report and package verbatim: goal, SMART,
KPIs, decisions, Table 1.1 (AQs), Table 4.1 (fit), Table 8.1 (readiness), C09–C13, predictor sets, split
specification, version manifest; records SHA-256 of each source → `research/baseline/m4-baseline.md`; checks the
five entry conditions of brief section 3.
- [ ] Baseline written; each entry condition has evidence and a status.

**T05: R, modeling strategy and method selection (Parts 2–3).** Research questions:
1. Explain versus predict: how the purpose (explanatory association vs predictive accuracy) changes method choice
   and evaluation (e.g. Shmueli 2010, Statistical Science; Breiman 2001 "two cultures").
2. ML system design guidance on starting from the decision, simple heuristics and baselines first, and when added
   complexity is justified (e.g. Google "Rules of Machine Learning"; Huyen 2022 *Designing Machine Learning
   Systems*; Sculley et al. 2015 hidden technical debt).
3. Interpretable models for high-stakes decisions (Rudin 2019, Nature Machine Intelligence) and evidence on logistic
   regression versus ML for tabular risk prediction (e.g. Christodoulou et al. 2019; Grinsztajn et al. 2022 on
   tree ensembles for tabular data).
4. Sample size for prediction models: events per variable and Riley et al. (2019/2020) minimum sample size criteria;
   penalised regression (ridge/lasso/elastic net) under limited events.
5. Early-warning prediction in education and on OULAD/OU Analyse: prediction from previous presentations, course-
   specific vs general models (e.g. Hlosta et al. 2017; Gašević et al. 2016 "one size does not fit all"; Herodotou et
   al. 2019/2020 OU Analyse use by teachers; Gardner & Brooks 2018 review of student success prediction).
6. Survival / time-to-event framing of dropout (discrete-time hazard models) as an alternative to fixed-horizon
   classification.
7. Ranking under a fixed capacity (top-k selection, precision/recall at k) as the output form for limited outreach.
8. Explanatory regression for clustered data: module fixed effects, cluster-robust or GEE errors, mixed models; effect
   sizes rather than p-values.
Each answer anchored in a primary source; current versions checked (as of November 2026). R1–R8.

**T06: R, evaluation design (Part 4).** Research questions:
1. Reporting and evaluation standards for prediction models: TRIPOD+AI (Collins et al. 2024, BMJ) and PROBAST+AI
   (2025) items on validation, calibration, fairness, sample size.
2. Calibration as part of evaluation: Van Calster et al. 2019 ("Achilles heel"), calibration intercept and slope,
   Brier score; Steyerberg & Vergouwe 2014 ABCD.
3. Precision–recall versus ROC under imbalance (Saito & Rehmsmeier 2015); threshold and decision-cost based
   evaluation; decision curve analysis (Vickers & Elkin 2006).
4. Validation with temporal and grouped structure: temporal/external validation; grouped and blocked
   cross-validation (Roberts et al. 2017, Ecography); scikit-learn GroupKFold / LeaveOneGroupOut, nested
   cross-validation and selection bias (Varma & Simon 2006; Cawley & Talbot 2010).
5. Leakage taxonomy and test reuse: Kapoor & Narayanan 2023 (Patterns) leakage and reproducibility; Kaufman et al.
   2012.
6. Comparing two models or a model and a rule with uncertainty: paired bootstrap, cluster bootstrap; McNemar or
   DeLong where relevant; Dietterich 1998.
7. Evaluating predictive models of student success: temporal evaluation and inference (Gardner, Brooks & Baker
   2019; Gardner & Brooks 2018), slicing analysis and ABROCA for fairness (Gardner, Brooks & Baker 2019, LAK).
8. Pre-specifying success criteria and avoiding metric shopping (pre-registration / analysis plans for ML).
R1–R8.

**T07: R, risk, causal limits, fairness and use (Part 5).** Research questions:
1. Why predictive models cannot estimate the effect of an intervention; what causal data and designs are needed
   (target trial, randomised experiment, uplift needs treatment variation): e.g. Hernán & Robins *Causal Inference:
   What If*; Athey & Imbens; Kohavi et al. 2020 *Trustworthy Online Controlled Experiments*.
2. Algorithmic fairness in education: Baker & Hawn 2022; Kizilcec & Lee 2022; group fairness criteria and their
   incompatibility (Chouldechova 2017; Kleinberg et al. 2017; Barocas, Hardt & Narayanan 2023).
3. High-stakes use and human oversight: EU AI Act (Regulation (EU) 2024/1689) Annex III education as high-risk and
   Article 14 human oversight; NIST AI RMF 1.0 (2023); model cards (Mitchell et al. 2019); datasheets (Gebru et al.).
4. Learning analytics ethics and institutional practice: e.g. Jisc code of practice for learning analytics; Slade &
   Prinsloo 2013; OU policy on ethical use of student data for learning analytics.
5. Vietnam's current rules relevant to AI-based decisions on students (law on AI or digital technology, personal data
   protection decree/law), checked current as of November 2026.
6. Self-fulfilling and feedback effects of early-warning lists (performative prediction; Perdomo et al. 2020) and
   monitoring after deployment.
R1–R8.

**T08: Design facts.** `code/design_facts.py` reads the Milestone 3 prepared views and metadata (no model):
training and test rows and events per cut-off; events per candidate parameter for the primary set (after one-hot);
Riley minimum sample size inputs; per-run base rates and list sizes for capacities 3 and 5 per 20; attainable recall
per run; subgroup sizes and expected positives in test runs (disability, deprivation band incl. Missing, age band,
gender); number of leave-one-run-out folds; paired/unpaired test runs. Writes `results/design_facts.json`, `.md`.
- [ ] Script runs, log saved; totals equal the Milestone 3 validation summary; every number used later is in the file.

**T09: Design documents.** `research/design/`: `modeling-briefs.md` (B), `candidate-matrix.md` and
`candidate-comparison.md` (C, eight criteria × candidates), `evaluation-cards.md` (D, seven card rows per AQ, metric
definitions with formulas), `validation-protocol.md`, `fairness-spec.md`, `risk-register.md` (E),
`prototype-protocol.md` (brief 10 steps), `traceability.md` (A). Every rationale cites a claim or a design fact.
- [ ] Every AQ has a brief and a card; every modeling AQ has a baseline and ≥ 2 candidates; success criteria fixed
  with reasons; no performance number appears.

**T10: AI model-selection critic.** Isolated agent with the brief's suggested prompts (section 11), reading only the
briefs, candidate matrix and comparison and the design facts; returns numbered critiques. Decisions with evidence in
`research/reviews/`; design files updated.

**T11: AI evaluation reviewer.** Isolated agent reading the evaluation cards, validation protocol, fairness spec and
risk register: mismatch with the AQ, metric fit, causal overclaim, imbalance, leakage, test reuse. Decisions; AI
Decision Log `research/ai-decision-log.md` (all AI roles, brief 11.1 columns).

**T12: F, figures.** `figures/milestone_4/`: Figure 2.1 AQ → technical task → output → decision; Figure 4.1
validation timeline (2013 runs: leave-one-run-out folds grouped by student; freeze; 2014 runs used once; paired and
unpaired subsets). F1–F5.

**T13–T15: W, writing.** Parts 1–2; Parts 3–4; Parts 5–8 and appendices (`code/build_appendices.py`). W1–W10.

**T16–T24: finishing.** Front matter; references; full gates; spot-check; style read-through; build EN and measure
pages (10–12); Vietnamese twin (build-report flow: terms, translators, native review, consistency, reader test,
rewrite); build every language; final review.

## 6. Human Checkpoints

| When | Why it stops |
| :---- | :---- |
| Any unticked checklist item | The user decides how to continue |
| Any conflict between a source and the brief or the Milestone 3 baseline | The user decides |
| Final review (T24) | Acceptance |

The user asked for the plan to run straight through (decision T02); part reviews are folded into the final review.

## 7. Deliverables

| Deliverable | Location |
| :---- | :---- |
| Plan and ledger | `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md` |
| Report sections | `report/*.md`, `report/*.vi.md` |
| Word reports | `build/N04_Milestone4_EN.docx`, `build/N04_Milestone4_VI.docx` |
| Design documents and reviews | `research/design/`, `research/reviews/` |
| Design facts | `code/design_facts.py`, `results/`, `logs/` |
