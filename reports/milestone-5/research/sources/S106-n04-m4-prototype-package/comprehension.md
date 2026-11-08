# S106 – N04 (2026). Milestone 4 prototype package contract (team's own specification)

## Summary in my own words

The Milestone 4 prototype package is a contract for the optional Level 2 experiment, explicitly marked as a specification that has not been run. It freezes the report: any result that argues for a different choice becomes a new Change Log entry from C15. It fixes the inputs (OULAD-N04-prepared-1.0 checked against its manifest), the preprocessing refitted inside each fold, the seven configurations (baselines B1–B3, primary M1, challengers M2–M4), the switching margin, the fixed-column CSV outputs (from dev folds to the S1 gate, calibration, fairness, sensitivity and the AQ2 replication), the experiment log and the four places where results would enter the report.

## Key facts

- Status – "Status: specification only. Nothing in this package has been run, and no result exists yet."
- No new choices – "every choice below was fixed in the report before any result existed"
- Frozen report – "for a different primary approach, predictor set or criterion is recorded as a new Controlled Change Log entry (C15"
- One test – "The 2014 outcomes are opened once, at step 6, after the second freeze."
- Unfavourable results – "Unfavourable results are reported."
- Hash check – "A mismatch stops the run."
- Primary configuration – "| M1 | Primary | Penalised logistic regression | Primary set |"
- Ties – "Ties go to the simpler"
- No guessing – "A column that does not apply holds an empty value, never a guess."
- S1 output columns – "pooled_nr_model, pooled_nr_rule, difference, boot_ci_low, boot_ci_high, signflip_p, wins, ties, losses, mean_per_run_difference, verdict"
- AQ2 replication output – "estimate_2013, ci_2013, estimate_2014, ci_2014"
- Report changes – "the report changes in four places only"

## Used in

10-00-experimental-status.md, 11-03-aq2-findings.md, 11-04-aq3-aq4-expected.md.

## Against reference.md

Confirms the outline's Part 10 ("Status: the Level 2 prototype was not run; what its specification fixes and how its results will be reported") and the scope rule "Section 10 states that no Level 2 experiment was run and what the prototype specification fixes". Extends Part 7: the contract does not use the Milestone 3 model-ready matrices as model input, because transforms are refitted inside each fold with deviation-coded modules; Part 7 should present those matrices as prepared but superseded by in-fold transforms for modeling.

## Reliability

Primary: the team's own specification, copied verbatim from the working tree (HEAD), not from commit 19d35a4 like S101–S105. No citation traction applies (as of 2026-11-08).

## Open questions

- The contract was copied from the working tree; the writer should confirm it matches the submitted Milestone 4 package before citing it as submitted material.
