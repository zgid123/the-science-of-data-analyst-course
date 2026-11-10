## Appendix X – Specification of the Level 2 Prototype

This appendix supports Section 10. It gives what the specification of the unrun Level 2 prototype fixes, the configurations it would compare, its eight steps, the single logged test and the places in the project record that a run would change.

**What the prototype specification fixes.** The protocol leaves the person who implements it no modeling choice of their own: every choice was fixed before any result existed, so the prototype can confirm or refute the choices of Level 1 but cannot reshape them after its results. A result that argues for a different primary approach, predictor set or criterion would be recorded as a new entry of the Controlled Change Log, with the frozen proposal shown beside it, and a baseline that matches the candidate is an acceptable outcome that would be carried forward with its reasons. The prototype tests feasibility and trade-offs, not the best attainable score. Table A.25 gives the configurations it would compare.

**Table A.25. Configurations of the specified prototype**

| ID | Role | Method | Predictors |
| :---- | :---- | :---- | :---- |
| B1 | Baseline | Random list | – |
| B2 | Baseline | Early-sign rule (C10), ranked by number of signs, ties by lower activity ratio | Rule columns |
| B3 | Baseline | Background-only logistic model | Module, start month, previous attempts, credits, education, registration lead |
| M1 | Primary | Penalised logistic regression | Primary set |
| M2 | Challenger | Penalised logistic regression | Extended set |
| M3 | Challenger | Gradient-boosted trees | Primary set |
| M4 | Challenger | Gradient-boosted trees | Extended set |

Ties between configurations go to the simpler one. The protocol runs in eight steps: it reproduces the data input from OULAD-N04-prepared-1.0, checks every file against the hashes of the version manifest and stops on any mismatch; it fits the baselines first; it fits the candidates; it applies the split and folds of Section 9.1; it evaluates every configuration, reporting unfavourable results, including a baseline that matches or beats the primary model; it runs the error and subgroup analysis of Section 9.2; it compares the outcome with the Level 1 proposal; and it records scripts, seeds, package and data versions, folds and the test-access record in an experiment log. The model-ready matrices of the prepared dataset are not model input, because the protocol refits every transform inside each fold with deviation-coded modules (Section 7.1).

**One logged test.** The 13 runs of 2014 are the project's only independent test and can be used once, so they are kept for one complete run of the frozen protocol, from the baselines to the logged test: no model result on 2014 is seen before the model is frozen, and a partial early run would spend that test. The 2014 outcomes would be opened once, after the second freeze, with the access time and the hash of the frozen model written to the experiment log before any test metric is computed. Synthetic data may only test code paths, are labelled as synthetic and never feed a result. The outputs have fixed columns, covering the development folds, the model choice, the freeze, the test runs, the gate S1, the secondary metrics, calibration, fairness, and the sensitivity analyses; a column that does not apply holds an empty value, never a guess. The experiment log would record, for each run, the time in UTC, the command, the code commit, the exit status, the package versions, the prepared-data hashes, the random seeds, the folds and the test-access record.

**What a run would change.** If the prototype runs, the project record changes in four places only: the results part and its appendix, the verdict of the comparison with Level 1, the Change Log only if a choice changes, and the AI Decision Log; every other section stays as frozen. Section 11 turns to the findings that the project has reached and to the expected outputs of the questions that wait for this test.
