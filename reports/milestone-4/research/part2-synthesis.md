# Part 2 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 02-00-aq-task-mapping.md

**Claims:** C2-001, C2-002, C2-011, C2-017

**Outline:**
- Open with the purpose test per AQ: explanatory (causal), descriptive/associational, or predictive (C2-001, C2-002); the purpose fixes method and evaluation.
- Map AQ1 to aggregation (rates by group) and AQ2 to association within module, both descriptive in Shmueli's sense, no causal claim (C2-002).
- Map AQ3 to probability classification at day 13 and day 27 and AQ4 to ranking under the contact capacity of 3 or 5 per tutor group (C2-011, C2-017).
- State the prescriptive step (whom to contact) as decision support, with the contact decision deferred (C11/C13).

**Conflicts with the outline:**
- The outline labels the AQ1–AQ2 task "association (explain)". Shmueli (S200) reserves "explanatory" for testing causal hypotheses and calls association-only regression "descriptive". Since the AQ2 regression makes no causal claim, the report should either call it "descriptive/associational" or define "explain" explicitly as association within module. Human to decide the label.

**Gaps:** None.

## 02-01-modeling-briefs.md

**Claims:** C2-005, C2-019, C2-020, C2-021

**Outline:**
- Each brief names its expected output form (rate table, coefficient table, probability, ranked list), since each form needs its own metric (C2-005).
- AQ4 brief: the user is the tutor; the output is a ranked list per tutor group, as in the OU's own system (OU Analyse traffic-light list, C2-020) and educator-designed metrics (C2-019).
- Main constraint: contact capacity and human decision; prediction supports teachers, effect of contact not established (C2-021).

**Conflicts with the outline:** None.

**Gaps:** OU Analyse predicts next-assignment submission weekly, while the project predicts non-completion at day 13 and day 27 (S312); the brief should state the difference.

## 02-02-technical-tasks.md

**Claims:** C2-001, C2-002, C2-003, C2-004, C2-006, C2-007, C2-008, C2-005, C2-009, C2-010, C2-012, C2-011, C2-017, C2-018, C2-019, C2-015, C2-016, C2-013, C2-014

**Outline:**
- Explain versus predict: definitions, explanatory power is not predictive power, bias versus bias-plus-variance, predictive models judged on held-out data (C2-001–C2-004, C2-006, C2-007); Rashomon caution against reading predictive coefficients as explanation (C2-008).
- Output form per AQ and its metric family (C2-005).
- Decision first, baseline first: heuristic rule baseline, ML only once the rule would grow complex, simple first model, temporal testing (C2-009, C2-010, C2-012).
- Ranking under capacity as the AQ4 task: ranking quality over probability, ranked lists and precision at top k% because only a small share can be contacted (C2-011, C2-017, C2-018, C2-019).
- Survival alternative to a fixed horizon: discrete-time hazard via logistic regression, whether-and-when framing (C2-015, C2-016).
- Limits of complexity and feedback once outreach follows the ranking (C2-013, C2-014).

**Conflicts with the outline:** Same labelling issue as 02-00 ("explain" versus Shmueli's "descriptive").

**Gaps:** Huyen (2022, *Designing Machine Learning Systems*, O'Reilly) not fetched; Google's Rules of ML (S202) and Sculley et al. (S203) cover the same design points. Lakkaraju et al. (S205) full text not readable; precision at top k% is taken from the companion paper S206.
