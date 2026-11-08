# Milestone 5 report outline: Final Integration & Project Report (team N04)

Derived on 2026-11-08 from the instructor brief `milestones/05/milestone-5.md` [1], which fixes the role of
Milestone 5 (section 1: integrate, reconcile, trace), the integration rules (1.1), the inputs required from Milestones
1–4 (1.2), the Final Report structure with the source, aim, content, evidence and self-check of each part (section 2),
the Final Project Traceability Matrix and the AQ Revision Log (section 3 and 3.1), the narrative and the suggested
length of each part (4, 4.1), the two cases of Milestone 4 (4.2), the AQ-by-AQ answer table and its interpretation
rules (section 5), the use of Generative AI and the minimum AI Decision Log (6, 6.1), the Final Project Package
(section 7), the rubric (section 8) and the checklist before submission (section 9). The baseline is the four
submitted reports of Milestones 1–4 and their packages (OULAD [2], prepared dataset `OULAD-N04-prepared-1.0`,
Change Log C01–C14 and onwards).

## Scope and rules

- One project story, rewritten: the report reads as a single project from stakeholder problem to decision support,
  never as four milestone reports placed side by side; earlier reports are evidence and input.
- Final versions only: the final Business Goal, SMART Goal, KPIs, AQs and dataset version; every change since
  Milestone 1 is stated with its reason in the AQ Revision Log and the Change Log.
- Proposal kept apart from experiment: Milestone 4 reached Level 1, so modeling and evaluation for AQ3 and AQ4 are
  written in the proposal tense with no model metric; Section 10 states that no Level 2 experiment was run and what
  the prototype specification fixes.
- New evidence for AQ1 and AQ2 (user decision 2026-11-08): a scripted analysis on the 2013 training runs only,
  following the Milestone 4 plan fixed before any result (AQ1 rates with intervals by module, run and start month,
  week of first missed task; AQ2 within-module associations of the early signs with later non-completion); the 2014
  test runs stay untouched. Each number comes from that script's output.
- Every conclusion has evidence; associations are never read as causes; prescriptive statements stay decision
  options for the pilot to test.
- Limitations stated as conditions and scope; deferred and partial questions named as such.
- AI as writing and review partner (brief section 6): consistency check, structure review and a challenge of the
  reasoning by isolated reviewers; every suggestion decided and verified in the AI Decision Log.
- Readers have only the submitted documents: no repository paths, logs or internal IDs in the report.
- Main text up to 25 pages (user decision 2026-11-08), appendices excluded: written in full first, then detail moved
  to appendices against the brief's required structure. English source, Vietnamese twin. Submission date
  14 November 2026.

## Abstract / Executive Summary

- Problem; data; final AQs; proposed and implemented analysis; key AQ1 and AQ2 results; educational value;
  limitations. 150–250 words, nothing not in the report.

## 1. Introduction & Educational Context

- Context of early disengagement in online and blended courses; motivation; stakeholders and their needs; scope;
  project objective.

## 2. Business Understanding & Success Criteria

- Business Goal; SMART Goal; primary and secondary KPIs; decisions D1–D3 and their needs; final SMART/KPI table.

## 3. Analytical Questions & Analytics Levels

- Final AQ1–AQ4 with level, scope and decision; AQ quality check (clear, specific, scoped, data-oriented, answerable);
  AQ Revision Log from Milestone 1 to the final versions.

## 4. Data Requirements & Dataset Selection

- Unit of analysis, outcome, variables, time, population; candidate datasets and the selection rationale;
  provenance, version and licence of OULAD.

## 5. Dataset Description & Requirement–Data Fit

- Tables, keys, sizes, variables, coverage and gaps; AQ–Data Fit and the status of each AQ (keep, modify, defer, drop).

## 6. Data Understanding & Data Quality

- Distributions, missingness, duplicates, invalid values, outliers, imbalance, temporal coverage, representativeness,
  sensitive fields; the quality findings that could change a conclusion.

## 7. Data Preparation & Analytic-ready Data

- Cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control; final prepared
  dataset and version; reproducible pipeline.

## 8. Modeling / Analysis Strategy

- AQ → analytics type → technical task → baseline → candidate methods → primary proposal → rationale.

## 9. Evaluation Design

- Metrics, baselines, split and validation, success criteria, leakage, fairness and interpretability checks.

## 10. Experimental Implementation & Results

- Status: the Level 2 prototype was not run; what its specification fixes and how its results will be reported.

## 11. Findings, Discussion & Decision Support

- AQ-by-AQ answers at the evidence level reached: AQ1 and AQ2 results from the 2013 analysis, AQ3 and AQ4 expected
  outputs; educational meaning, uncertainty, decision support for D1–D3; interpretation rules by analytics level.

## 12. Limitations & Future Work

- Dataset gaps, generalisability, observational and causal limits, model limits, deferred decisions, next data
  needed; "no evidence found" kept apart from "no data to test".

## 13. Generative AI Use & Reflection

- AI used for, suggestions, verification, accepted and rejected, final human decisions across Milestones 1–5.

## 14. Conclusion

- What was asked, what the data supported, what analysis is appropriate, what can and cannot be concluded, next step.

## Appendices

- Full Final Project Traceability Matrix; AQ Revision Log in full; Change Log; AQ1 and AQ2 result tables; data
  dictionary summary; preparation decisions; evaluation protocol; AI Decision Log with prompts; Final Project Package
  contents.

## References

[1] MTH045 – The Science of Data Analytics. (2026). Milestone P5: Final integration & project report [Course brief].
[2] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. Scientific Data, 4, 170171. https://doi.org/10.1038/sdata.2017.171
