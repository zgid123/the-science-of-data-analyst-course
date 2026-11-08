---
id: S106
url: reports/milestone-4/package/README.md
requested: reports/milestone-4/package/README.md
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (working tree read; verbatim, 1 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T06
part: 1
raw: raw.txt (8 KB)
conversion: verbatim copy of 1 file(s) from milestone-da at HEAD
---
===== reports/milestone-4/package/README.md @ HEAD =====
# Prototype Package – Milestone 4, Level 2 (team N04)

**Status: specification only. Nothing in this package has been run, and no result exists yet.**

This folder is the contract for the optional Level 2 prototype of the Milestone 4 brief (section 10; deliverable G in
section 12). The Level 1 report (`N04_Milestone4_EN.docx`, `N04_Milestone4_VI.docx`) is complete without it. Whoever
implements the prototype follows this file and the report sections it cites. They make no modelling choice of their
own: every choice below was fixed in the report before any result existed, and the brief requires that order (sections
8 and 15).

- Done before 14 November 2026: the package is submitted as deliverable G, and the report gains its results section
  (see "How results enter the report").
- Done later: the package belongs to the next stage of the project, and the Milestone 4 report stays as submitted.

## Rules the implementation keeps

1. **The report is frozen.** Parts 1–6 and 8 of the report do not change because of a result. A result that argues
   for a different primary approach, predictor set or criterion is recorded as a new Controlled Change Log entry (C15
   onwards), with its reason, and the frozen proposal stays visible beside it.
2. **The brief's eight steps.** The prototype follows report Table 7.1 (brief section 10) and the protocol of report
   Appendix III, Table A.5, steps 1–8, in that order.
3. **One test, logged.** The 2014 outcomes are opened once, at step 6, after the second freeze. The time of that
   access and the hash of the frozen model are written to the experiment log before any test metric is computed.
4. **Unfavourable results are reported.** That includes a baseline that matches or beats the primary model (report
   Section 7, "A baseline may win").
5. **Real data only.** Synthetic data may test code paths in `tests/`. It is labelled as synthetic and never feeds a
   result (brief section 11).

## Inputs

The inputs are the Milestone 3 prepared data package, version `OULAD-N04-prepared-1.0`.

- **Check before use.** Before reading any file, check the hashes against that package's
  `data/metadata/version_manifest.json`. A mismatch stops the run.
- **Files used:**
  - `data/processed/features_d13.parquet` and `features_d27.parquet`, the feature views;
  - `data/processed/capacity_by_run.parquet`, list lengths and ceilings;
  - `data/metadata/predictor_sets.json`, the only columns a model may read;
  - `data/metadata/data_dictionary.md`.
- **Files not used as model input:** `model_ready_d13.parquet` and `model_ready_d27.parquet`. Milestone 3 fitted them
  once on all 2013 runs, with one column per module level. The Milestone 4 protocol instead:
  - refits every transform inside each fold;
  - codes module as deviations from the average module;
  - gives an unseen module (CCC, or a module missing from a training fold) the average (report Appendix III).
- **Predictor sets:**
  - primary: 19 predictors, 23 parameters with the module and start-month terms;
  - extended: the primary set, 10 further predictors and the weekly click counts (2 columns at day 13, 4 at day 27);
  - the mean CMA score stays out of both (fewer than 10% of training rows have it).
- **Audit-only columns:** gender, disability, deprivation band, age band and region never enter a model.

## Preprocessing inside each fold

For the logistic models, every parameter in the table below is estimated on the training rows of the current fold
only. The results are then applied to that fold's validation rows, or, after the second freeze, to the 2014 test rows.
Gradient-boosted trees read the predictors untransformed.

| Predictor kind | Columns (from `predictor_sets.json`) | Transform for the logistic models |
| :---- | :---- | :---- |
| Nominal | module, start month | Deviation (sum) coding over the levels seen in the training fold; unseen level → all zeros, i.e. the average module |
| Ordinal | highest education | Ordered integer code (order in `data_dictionary.md`) |
| Boolean | `inactive_last7`, `registration_missing` | 0/1 |
| Non-negative counts | previous attempts, credits, banked results, every click, day, resource and task count, CMA marks known, weekly clicks | log(1 + x) |
| Not treated as counts | `registration_lead`, `activity_ratio_run`, `trend_last_week`, `days_since_last_click` | No log; standardised only |
| Missing values | any numeric column with nulls in the training fold | Training-fold median, plus a 0/1 missing-value indicator; registration lead takes no indicator in the primary set (its indicator is the extended predictor `registration_missing`) |
| All model columns | after the steps above | Standardised with the training-fold mean and standard deviation |

Tuning runs by nested leave-one-run-out cross-validation on the training runs of each fold. It tunes the penalty of
the logistic regression, and the depth, learning rate and number of trees of the boosted trees (report Appendix III,
step 3).

## Configurations and baselines

| ID | Kind | Model | Predictors |
| :---- | :---- | :---- | :---- |
| B1 | Baseline | Random list | – |
| B2 | Baseline | Early-sign rule (C10), ranked by number of signs, ties by lower activity ratio | Rule columns |
| B3 | Baseline | Background-only logistic model | Module, start month, previous attempts, credits, education, registration lead |
| M1 | Primary | Penalised logistic regression | Primary set |
| M2 | Challenger | Penalised logistic regression | Extended set |
| M3 | Challenger | Gradient-boosted trees | Primary set |
| M4 | Challenger | Gradient-boosted trees | Extended set |

A challenger replaces M1 only if it meets the margin of report Appendix III, step 4: a gain of at least 0.03 in
pooled normalised recall at day 27, at k = 5 per 20, and a gain in at least 7 of the 9 folds. Ties go to the simpler
model.

## Outputs with fixed columns

Every file is CSV in `results/`, one row per line of the key. Metric names and definitions are those of report
Appendix II. A column that does not apply holds an empty value, never a guess.

| File | Key | Columns |
| :---- | :---- | :---- |
| `dev_folds.csv` | config, cutoff, k, validation_run | n_enrolments, n_noncompleters, list_length, noncompleters_on_list, max_attainable, normalised_recall, precision, lift, roc_auc_within_run |
| `model_choice.csv` | config | pooled_normalised_recall_d27_k5, gain_vs_M1, folds_with_gain, chosen (yes/no), reason |
| `freeze.csv` | – | chosen_config, spec, parameter_file, model_sha256, first_test_access_utc |
| `test_runs.csv` | config, cutoff, k, test_run | the columns of `dev_folds.csv` |
| `s1_gate.csv` | – | pooled_nr_model, pooled_nr_rule, difference, boot_ci_low, boot_ci_high, signflip_p, wins, ties, losses, mean_per_run_difference, verdict |
| `secondary.csv` | config, cutoff, k | precision, base_rate, max_attainable_precision, pr_auc, roc_auc_within_run, net_benefit_by_threshold (file reference) |
| `calibration.csv` | config, cutoff | citl, slope, s3_verdict |
| `fairness.csv` | group, cutoff, k | n, n_noncompleters, recall_group, recall_others, difference, holm_ci_high, flagged |
| `sensitivity.csv` | variant, cutoff, k | the S1 columns of `s1_gate.csv` for that variant (paired, unpaired, CCC apart, without students seen in 2013, without Withdrawn lacking a day, labels-available, day 13, k = 3 per 20) |
| `aq2_replication.csv` | sign, module | estimate_2013, ci_2013, estimate_2014, ci_2014 |

## Experiment log

`logs/experiment_log.md` holds one entry per run:
- UTC time;
- command, git commit and exit status;
- Python and package versions (`requirements.txt` pinned);
- prepared-data version and hashes;
- random seeds;
- the folds used;
- for step 6, the test-access record.

Each script writes its console output to `logs/<step>.log`.

## Planned layout

```
package/
  README.md            this contract
  requirements.txt     pinned versions
  src/                 01_load_check, 02_baselines, 03_dev_folds, 04_choose, 05_freeze, 06_test, 07_fairness,
                       08_sensitivity, 09_aq2_replication; run_all.sh
  tests/               code-path tests on labelled synthetic fixtures
  results/             the CSV files above
  logs/                experiment_log.md and one log per step
```

## How results enter the report

When the prototype is run before submission, the report changes in four places only:
1. **Section 7.** It gains a part on the preliminary results, and an appendix holds the result tables, built from the
   CSV files above.
2. **Section 7, step 7 of Table 7.1.** It states whether the results support the Level 1 choice.
3. **Change Log.** It gains an entry only if a choice changes.
4. **AI Decision Log (Section 6).** It gains a row for each use of AI in the code.

Every other section stays as frozen.
