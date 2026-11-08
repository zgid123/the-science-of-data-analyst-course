# Design decisions (T09) and their evidence

Working record behind Appendices I–VI and VIII. Claim IDs point to research/part*-claims.md; design facts to
results/design_facts.json (code/design_facts.py, logs/T08_design_facts.log).

| # | Decision | Evidence |
| :---- | :---- | :---- |
| D-01 | AQ1 descriptive: grouped rates with 95% intervals, no model | C1-002, C3-025, C3-024 |
| D-02 | AQ2 association: unadjusted comparison (baseline), logistic regression with run fixed effects (primary); mixed model rejected (7 modules); shallow tree as supplement | C2-002, C3-022, C3-023, C3-024; brief section 9 example |
| D-03 | AQ2 on 2013 runs, 2014 replication after AQ3 test (C14) | C4-036, C4-037, C4-048 |
| D-04 | AQ3 baseline = early-sign rule ranked by number of signs, ties by lower activity_ratio_run (stronger heuristic baseline); random list | C2-009, C2-010, C4-024 |
| D-05 | AQ3 primary = penalised logistic regression; challenger gradient-boosted trees; survival as later extension | C3-001, C3-002, C3-004, C3-005, C3-006, C3-007, C3-017, C3-018, C3-021; design facts EPP 228-240, Riley n 1,728-2,784 (C3-008, C3-031) |
| D-06 | Challenger adopted only if +0.03 mean recall at capacity and better in ≥ 7 of 9 folds; same for extended set | C3-026, C4-030, C4-047 |
| D-07 | Separate model per cut-off; one pooled model with module and start-month dummies, not per-module models | C3-012 (shrinkage does not rescue small samples), C3-015 (course differences → module terms), C3-014/C3-016 (train on previous presentations) |
| D-08 | Operating point k = 5 per 20 at day 27 (main), 3 per 20 and day 13 secondary | C1-013 (groups of about 20); M3 rule firing 28.8% at day 27; C4-022, C4-044 |
| D-09 | Primary metric recall at capacity vs attainable; lift; PR-AUC vs base rate; calibration intercept/slope; Brier; net benefit secondary | C2-011, C2-018, C4-003, C4-010–C4-016, C4-019, C4-020, C4-023 (T06 decision 1-2) |
| D-10 | Success S1 (beats rule, interval, 9 of 13 runs), S2 (halfway to attainable), S3 calibration 0.8-1.2 / ±0.2 for showing probabilities | C1-008, C4-030, C4-046, C4-012; M1 D1 threshold "higher recall than the simple rule" |
| D-11 | LORO folds with removal of overlapping students; nested tuning; refit preprocessing in folds; single logged test | C4-025, C4-026, C4-027–C4-029, C4-050, C4-051, C4-048, C4-049; design facts 121-129 students |
| D-12 | Two-level bootstrap (runs, students) plus per-run results | C4-052, C4-053 (T06 decision 5) |
| D-13 | Fairness: separation (recall at capacity) primary; ABROCA, calibration by group; gap rule 10 points with interval, groups ≥ 100 non-completers; small groups pooled | C5-010–C5-016, C4-039–C4-041, C4-013, C5-019, C5-020; design facts group sizes |
| D-14 | AQ4: top-k by risk with reasons; uplift ranking rejected; risk tiers as option; contact deferred to randomised pilot | C5-005–C5-008, C3-019, C3-020, C5-001–C5-004 |
| D-15 | Human oversight, override, reasons shown; legal classification before pilot | C5-022–C5-030, C5-044–C5-055 |
