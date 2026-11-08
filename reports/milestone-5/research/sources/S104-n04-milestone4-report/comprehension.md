# S104 – N04 (2026). Milestone 4 report: modeling strategy and evaluation design (team's own submitted report)

## Summary in my own words

The Milestone 4 report is the team's Level 1 Modeling and Evaluation Proposal; it trains no model and states no model performance. For each question it writes a Modeling Brief, maps it to a technical task (AQ1 aggregation, AQ2 association within module run, AQ3 binary classification at day 13 and day 27, AQ4 ranking under capacity) and fills a Candidate Solution Matrix with baselines, candidate families and a primary approach chosen on eight criteria. The evaluation is fixed before any code runs: Evaluation Design Cards per question, leave-one-run-out development on the 9 runs of 2013, two freezes and a single logged test on the 13 runs of 2014, a single success gate S1 on normalised recall at capacity against the early-sign rule, S2 and S3 as non-gating reports, and a confirmatory fairness rule FR1 on three groups. It adds Change Log entry C14 (AQ2 on 2013 first), a risk register, the AI Decision Log and a protocol for the optional Level 2 prototype.

## Key facts

- Level 1 only – "This report covers Level 1 in full. Part 7 specifies how the optional prototype will run, as a protocol, and no model"
- No invented numbers – "every number in it is a count from the prepared data or a value we fixed in advance with its reason"
- Development data – "At day 27 the development runs hold 11,811 enrolments, of whom 5,245 (44.4%) did"
- C14 – "AQ2 estimated on the 9 runs of 2013; replicated on the 13 runs of 2014 only after the AQ3 model is frozen and scored"
- AQ2 primary approach – "Logistic regression with run fixed effects and sign × module terms"
- AQ3 baselines – "Early-sign rule ranked by signs; background-only logistic model; random list"
- AQ3 primary rule – "Candidate 1 on the primary predictors, unless Candidate 2 or the extended predictor set wins by a margin fixed in advance"
- Events per parameter – "about 230 events (non-completers) per parameter"
- Riley R. D. et al. minimum sample size criteria are cited for "about seven times the 1,731 that the" minimum requires (source not registered here)
- AQ2 success criterion – "A sign is a consistent association when its adjusted risk difference is at least 5 percentage points with an interval excluding 0"
- S1 – "S1 (single gate): on all 13 test runs, all eligible enrolments, day 27, k = 5 per 20"
- S3 – "S3 (condition for showing probabilities): calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2"
- Challenger margin – "replace the primary choice only with a gain of at least 0.03 in pooled normalised recall"
- Fairness criterion – "one primary criterion, separation, measured as equal recall at capacity across groups"
- Fairness groups – "missing deprivation band (610)"
- Prototype not run – "run the prototype, so it states no model performance"
- AI roles – "Three roles were used: a literature assistant that found and read sources, a model-selection"
- AI did not produce results – "produced a metric value, a threshold or a result"

## Used in

08-00-modeling-strategy.md, 08-01-candidate-methods.md, 09-00-evaluation-design.md, 09-01-validation-success.md, 09-02-fairness-interpretability.md, 10-00-experimental-status.md, 11-04-aq3-aq4-expected.md, 12-00-limitations.md, 12-01-future-work.md, 13-00-genai-reflection.md.

## Against reference.md

Confirms the outline's Part 8 chain ("AQ → analytics type → technical task → baseline → candidate methods → primary proposal → rationale") row by row in Table 3.1, and Part 9 ("Metrics, baselines, split and validation, success criteria, leakage, fairness and interpretability checks"). Confirms Part 10 ("the Level 2 prototype was not run; what its specification fixes"). Extends the outline's scope note on AQ1 ("AQ1 rates with intervals by module, run and start month"): the Milestone 4 AQ1 card computes rates over all 22 runs and a second denominator, while the outline (user decision 2026-11-08) restricts new results to the 2013 runs; this is the conflict already recorded in PROGRESS.md (T04).

## Reliability

Primary: the team's own submitted report (N04, MTH045), copied verbatim from the repository at commit 19d35a4. External sources it cites (TRIPOD+AI, Riley et al., Rudin, etc.) are summarised from its own trail and are not registered in this task. No citation traction applies (as of 2026-11-08).

## Open questions

- The AQ1 card expects rates over all 22 runs (both denominators 32,593 and 28,061), but Milestone 5 runs AQ1 on the 2013 runs only; the writer must state the narrower population (T08 methods note).
- Table A.12 links AQ4 to "Secondary KPIs 1 and 2", while Milestone 3 (S103, C08) measures secondary KPI 2 only in the pilot; the final traceability should say the KPI 2 link is pilot-only.
