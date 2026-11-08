# Milestone 4 report outline: from modeling to evaluation (team N04)

Derived on 2026-11-06 from the instructor brief `final-project/milestones/04/milestone-4.md` [1], which fixes the two
levels (section 2), the entry gate (section 3), the seven-step Level 1 process (section 4), the AQ-to-method guide
(section 5), Task 1 AQ Modeling Brief (section 6), Task 2 Candidate Solution Matrix and its eight criteria (section 7),
Task 3 Evaluation Plan and the Evaluation Design Card (section 8), the worked example (section 9), the AI policy and
AI Decision Log (section 11), deliverables A–G (section 12), the report structure (section 13), the rubric (section 14)
and the checklist (section 15). The baseline is the Milestone 3 report and its Prepared Data Package
(`reports/milestone-3/`, prepared dataset `OULAD-N04-prepared-1.0`), with AQ1–AQ4 as revised by Change Log C01–C13.

## Scope and rules

- Level 1 only: a reasoned Modeling & Evaluation Proposal. No model is fitted, tuned or scored, and the report
  states no model performance; Part 7 specifies the Level 2 prototype as a protocol that a later run follows.
- Method choice starts from the question, the output it needs, the data and the decision; machine learning only where
  the question is predictive; descriptive and diagnostic questions keep simple methods.
- Every AQ gets a baseline; AQ3 and AQ4 get 2–3 candidate families and a primary approach chosen against the brief's
  eight criteria (fit to question, fit to data, assumptions, interpretability, complexity vs baseline, robustness and
  reproducibility, ethics and fairness, actionability).
- The evaluation is specified before any result exists: metrics, validation, baseline, error analysis, subgroup and
  fairness checks, and success criteria fixed in advance.
- Design reasoning rests on well-known sources on modeling strategy and evaluation (ML system design, prediction-model
  reporting standards, calibration, validation under temporal and grouped structure, leakage, interpretability,
  fairness in education, causal limits), retrieved current as of November 2026, and on OULAD-specific prior work.
- Facts about the data (sizes, class balance, group sizes, list sizes) come from the Milestone 3 prepared views,
  recomputed by a script; no number is invented.
- AI as modeling partner: an isolated model-selection critic and an evaluation reviewer (the brief's two suggested
  prompts); every suggestion decided and verified in the AI Decision Log.
- Readers have only the submitted documents: no repository paths, logs or internal IDs in the report.
- Deliverables A–F inside the report (main tables, full versions in appendices); G specified as a protocol only.
- Main text 10–12 pages, appendices excluded. English source,
  Vietnamese twin. Submission date 14 November 2026.

## 1. Project Context and Continuity

- Business Goal, SMART Goal, KPIs and decisions D1–D3; OULAD and the prepared dataset version; AQ1–AQ4 after C01–C13
  and their Milestone 3 readiness; entry gate of brief section 3.

## 2. AQ-to-Technical-Task Mapping

- AQ Modeling Briefs (Task 1): level, decision, unit, target, inputs and window, expected output, main constraint.
- Technical task per AQ: aggregation, association (explain), classification and ranking under capacity (predict),
  decision support without causal claim (prescriptive); explain-versus-predict distinction.

## 3. Candidate Modeling Approaches

- Selection criteria applied (brief 7.1); Candidate Solution Matrix (Task 2).
- AQ1 and AQ2: rates with intervals, comparison and explanatory regression within module; why no ML.
- AQ3 and AQ4: rule and simple baselines; regularised logistic regression; tree ensembles; survival framing;
  sample size, imbalance, calibration, interpretability; primary approach and rationale.

## 4. Evaluation Design

- Evaluation Design Cards (Task 3) per AQ.
- Validation: time split, grouped folds inside the training years, single use of the test runs, frozen plan.
- Metrics and success criteria: gain over base rate and recall at capacity, discrimination, calibration, comparison
  with the rule, uncertainty.
- Error analysis, subgroup and fairness checks.

## 5. Risk, Ethics and Limitations

- Leakage, overfitting and test reuse; interpretability; causal limits and the deferred contact decision; fairness and
  high-stakes use with human oversight; data constraints and transfer to the university.

## 6. Generative AI Usage

- AI Decision Log (prompts, suggestions, decisions, verification, effect) and short reflection.

## 7. Prototype Protocol (Level 2)

- The brief's eight prototype steps as a specification: data version, baseline first, candidate, split and fitting
  rules, metrics from Part 4, error and subgroup analysis, comparison with the Level 1 choice, reproducibility record.

## 8. Updated Traceability Matrix

- Business Goal → AQ → level → technical task → prepared data → primary approach → primary metric → validation →
  decision supported.

## Appendices

- Full AQ Modeling Briefs; candidate comparison per AQ against the eight criteria; full Evaluation Design Cards with
  metric definitions; validation and test protocol; error and fairness analysis specification; risk register; AI
  Decision Log and prompts; full traceability.

## References

[1] MTH045 – The Science of Data Analytics. (2026). Milestone P4: From modeling to evaluation [Course brief].
[2] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. Scientific Data, 4, 170171. https://doi.org/10.1038/sdata.2017.171
