# AI Decision Log – rows offered for the Level 2 prototype

The Milestone 4 brief (section 11.1) requires a log of what a generative AI suggested, what the team decided, how it
was verified and how it affected the proposal. This prototype was written and run by an AI coding assistant (Claude,
through Claude Code, with the repository's `data-analyst` skill) on 11 November 2026 (UTC), at the request of a team
member. The rows below record what the assistant did and chose. **The column "Team decision" is left for the team:**
the brief makes the team responsible for the final decision, and the assistant cannot fill it.

| Prompt / goal | AI suggestion (what the assistant did) | Team decision | Evidence / verification | Effect on the proposal |
| :---- | :---- | :---- | :---- | :---- |
| "Use the data-analyst skill to do the Level 2 requirement of Milestone 4; results under `reports/code`, grouped by `aq-<number>`, with extracted datasets, logs and Markdown" | Built one folder per AQ with code, extracted datasets, results, figures, logs, a report and notes; followed the eight prototype steps of the brief and the frozen Level 1 protocol | *to be recorded by the team* | `logs/experiment-log.md`; every step log in `aq-*/logs/` | None on Level 1; adds deliverable G |
| Implementation details that Level 1 leaves open (penalty type, grids, tuning criterion, tie-breaking, binary sign definitions, bootstrap sizes) | Fixed 20 choices in `PROTOCOL.md` before the first result (P01–P20) | *to be recorded by the team* | File written before `aq-1/logs/01_extract_2013.md` (first row of the experiment log) | Proposed Change Log entry C15 (tuning criterion = log loss) |
| Keep the 2014 outcomes closed until the model is frozen | Wrote a guard in `common/lib.py` that refuses 2014 outcomes before `freeze.json` exists and records every later read | *to be recorded by the team* | `aq-3/logs/test-access.md`; verification V6 | None |
| Choose between logistic regression, the extended set and boosted trees | Applied the Level 1 rule (+0.03 and 7 of 9 folds) to the development folds; no challenger qualified; kept M1 | *to be recorded by the team* | `aq-3/results/model_choice.csv` | Confirms the Level 1 primary approach |
| Judge gate S1 | Computed the gate exactly as written in Level 1 Table 4.5; reported it as met with a small margin (+0.021; 84 students on 3,955 places) | *to be recorded by the team* | `aq-3/results/s1_gate.csv`; recomputed by a second code path (V2); earlier team run agrees | Supports D1 as designed |
| Judge S3 (show probabilities or not) | Reported S3 as met on the pooled estimates, and recommended ranks and reasons only, because 5 of 13 runs and two audit groups are outside the bounds and the earlier team run fails S3 | *to be recorded by the team* | `aq-3/results/calibration*.csv`, `crosscheck_earlier_run.csv` | Proposed Change Log entry C16 |
| Fairness check FR1 | Ran the confirmatory check as specified (three groups, Holm); 0 flagged; reported age 55 or over as not cleared and a descriptive gender gap | *to be recorded by the team* | `aq-4/results/fairness_confirmatory.csv`, `fairness_descriptive.csv` | Suggestion: add gender to the pilot's audit groups |
| Reasons shown with each name | Derived reasons from the frozen equation; pointed out that prior education is the first reason for 14.5% of listed students and is not actionable | *to be recorded by the team* | `aq-4/results/reason_frequency.csv` | Suggestion for the next stage: show behavioural reasons only |
| Check the assistant's own work | Unit tests on labelled synthetic inputs; verification ledger V1–V7; determinism rerun; cross-check against the team's earlier run, opened only after all results existed | *to be recorded by the team* | `logs/tests_lib.md`, `aq-3/results/verification.csv`, `logs/determinism_*.sha256`, `aq-3/results/crosscheck_earlier_run.csv` | None |

## What the brief asks of the team for AI-written code

- The brief does not accept AI-generated code that members cannot explain (section 11, "Coding prototype"). Each
  script is short and commented; `README.md` in this folder lists what each one does. The team should read and rerun
  them before submitting.
- No metric, threshold, plot or result in this folder was written by hand or generated as an expectation: every
  number in the reports is printed by a script into a step log and saved under `results/`.
- No synthetic record or label was used as evidence. Synthetic toy inputs appear only in `common/tests/test_lib.py`,
  labelled as such, to test code paths.
