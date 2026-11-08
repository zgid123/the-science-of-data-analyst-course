# Part 3 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 03-00-candidate-approaches.md

**Claims:** C3-021, C3-001, C3-002, C3-004, C3-006, C3-012, C3-016, C3-018, C3-028, C3-017

**Outline:**
- Candidate families for AQ3–AQ4 in order of complexity: rule baseline, (regularised) logistic regression, gradient-boosted trees, discrete-time survival (C3-021).
- Why logistic regression as primary: interpretable for a high-stakes, human-in-the-loop use, and no systematic accuracy loss on tabular data (C3-001, C3-002, C3-004).
- Why gradient boosting (not deep learning) as the flexible challenger (C3-006).
- Regularisation helps calibration on average but is not a fix for few events (C3-012).
- Survival framing: same tooling as logistic regression, adds "when" (C3-018, C3-028), with its independence assumption caveat (C3-017); training on earlier runs as the honest architecture (C3-016).

**Conflicts with the outline:** None.

**Gaps:** None.

## 03-01-criteria-matrix.md

**Claims:** C3-001, C3-003, C3-005, C3-008, C3-021, C3-026, C3-027

**Outline:**
- Interpretability and actionability: interpretable models preferred for high-stakes use; tutors combine scores with outside knowledge (C3-001, C3-003).
- Complexity vs baseline: tie goes to the simpler model (Rashomon, C3-026); maintenance and feedback risks count against complexity (C3-027); start simple (C3-021).
- Fit to data: sample-size criteria for the chosen predictor parameters (C3-008).
- Robustness: fair comparison under one frozen validation with calibration reported (C3-005).

**Conflicts with the outline:** None.

**Gaps:** None.

## 03-02-descriptive-diagnostic.md

**Claims:** C3-025, C3-024, C3-023, C3-022

**Outline:**
- AQ1–AQ2 are descriptive/associational, so no ML (C3-025).
- Report rate differences and odds ratios with confidence intervals, not significance alone; large n makes trivial gaps significant (C3-024).
- Within-module comparison by module fixed effects (C3-023); clustering of errors decided by the design, and conventional cluster-robust errors can be inflated when all clusters are observed (C3-022).

**Conflicts with the outline:** None. Note for the human: the card lists "cluster-robust or GEE errors, mixed models"; the evidence favours module (or module-presentation) fixed effects with a stated variance method, because OULAD holds all 22 runs of only 7 modules.

**Gaps:** No source fetched on the few-clusters problem (7 modules) for cluster-robust inference (e.g. Cameron & Miller 2015, Journal of Human Resources), nor on GEE versus mixed models; the report should state the 7-cluster limitation as a condition without a figure.

## 03-03-predictive.md

**Claims:** C3-002, C3-004, C3-005, C3-006, C3-007, C3-008, C3-009, C3-010, C3-011, C3-012, C3-013, C3-014, C3-015, C3-016, C3-017, C3-018, C3-030

**Outline:**
- Evidence on logistic regression versus ML on tabular risk data (C3-002, C3-004, C3-005); trees beat deep learning but the benchmark does not show trees beat logistic regression (C3-006, C3-007).
- Sample size: Riley criteria instead of 10 EPP, count parameters, compute on the 2013 training runs at the observed outcome proportion (C3-008–C3-011).
- Penalisation: ridge/lasso/elastic net for 20 correlated predictors, judged by calibration on 2014; bootstrap uniform shrinkage as an option (C3-012, C3-013).
- Prior OULAD/OU practice: models trained on previous presentations (C3-014, C3-016), course differences (C3-015), the OU's simple-model ensemble (C3-030).
- Survival variant as secondary candidate (C3-018, C3-017).

**Conflicts with the outline:** None.

**Gaps:** Riley et al. BMJ 2020 (S303) full text not readable: the report should cite the three criteria of S304 and not state the BMJ version's additional criterion. Hlosta et al. 2017 (S306) and Gašević et al. 2016 (S307) are abstract or title only: cite them only for what the abstract or title says.

## 03-04-ranking-capacity.md

**Claims:** C3-020, C3-019, C3-003, C3-030, C3-029

**Outline:**
- AQ4 output is a ranked list per tutor group; ranking quality at capacity matters more than the probability (C3-020).
- Precision at top k% and risk tiers as the educator-facing form (C3-019); capacity 3 or 5 per group of about 20 turns into k per group.
- The tutor decides with information outside the model (C3-003); the OU's own system is a teacher-facing risk list (C3-030), and engaged teachers were associated with better outcomes, without a causal claim for contact (C3-029).

**Conflicts with the outline:** None. S206 uses precision at top k%; the outline names "recall at capacity" (metrics are T06's): both are capacity-bound and can be reported together.

**Gaps:** None.
