# Milestone 4, Level 2 – Prototype Experiment (team N04)

*MTH045 The Science of Data Analytics · education analytics · prepared dataset OULAD-N04-prepared-1.0 · run
11 November 2026 (UTC) with the repository's `data-analyst` skill*

This folder is deliverable G of the Milestone 4 brief: code, experiment log, preliminary results and reproducibility
information for a controlled test of the Level 1 proposal. It tests whether the Level 1 choices are feasible and what
they trade off. It is not a search for the best score, and the Level 1 report stays as submitted.

> **Result in one paragraph.** The prototype supports every primary approach chosen in Level 1. Grouped rates answer
> the descriptive question, and both aggregation paths agree to the enrolment in all 22 runs. All five early signs
> meet the association criterion on the 2013 runs and again on the 2014 runs. The penalised logistic regression
> passes the single success gate S1 on the 13 test runs of 2014: its lists hold 72.6% of the non-completers a perfect
> list could hold, against 70.4% for the early-sign rule (difference +2.1 points, 95% interval +0.7 to +3.6, 11 of 13
> runs won). The gain over the rule is small, and gradient-boosted trees add nothing measurable, so the simpler model
> stays. A list of 5 per tutor group of 20 reaches 41.5% of later non-completers against 25.1% for a random list, and
> the confirmatory fairness check flags none of its three groups. One Level 1 condition does not hold robustly:
> calibration meets its pooled bounds in this run but fails in 5 of 13 runs and in the team's earlier run, so the
> recommendation is to show tutors ranks and reasons, not probabilities.

## Results at a glance

| AQ | Level 1 primary approach | Baseline | Main result | Level 1 criterion | Report |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 (descriptive) | Grouped rates with intervals | Pooled rate; second denominator | 45.3% of the 28,061 enrolments registered at day 14 do not complete; 24.9% to 58.3% by run; 16.8% of non-completers have missed a task by week 4 | Two aggregation paths agree to the enrolment: **met** (22 of 22 runs) | [aq-1/README.md](aq-1/README.md) |
| AQ2 (diagnostic) | Logistic regression with run fixed effects and sign × module terms | Unadjusted rate difference | Adjusted risk differences: missed task +41 points, late TMA +22, low activity +15, inactive +13, no pre-start activity +11 | ≥ 5 points, interval excluding 0, two-thirds of modules: **5 of 5 signs**, replicated on 2014 | [aq-2/README.md](aq-2/README.md) |
| AQ3 (predictive) | Penalised logistic regression, primary predictors | Early-sign rule; background-only model; random list | Pooled normalised recall 0.726 against 0.704 (rule), 0.567 (background-only), 0.439 (random); day 27, 5 per 20 | Gate S1: **met** (+0.021, interval +0.007 to +0.036, sign-flip p = 0.003). Challenger margin: **not met**, M1 stays. S3: met on pooled estimates, **not robust** | [aq-3/README.md](aq-3/README.md) |
| AQ4 (ranking) | Top-k per run from the AQ3 scores, with reasons | Random list; rule-ranked list | Recall 41.5% (ceiling 57.2%), lift 1.65; tier 1 holds 81% non-completers, tier 2 60% | S1 met by the list; fairness rule FR1: **0 of 3 groups flagged**; age 55 or over not cleared | [aq-4/README.md](aq-4/README.md) |

## How the eight prototype steps of the brief are met

| Brief step (section 10) | What was done | Where |
| :---- | :---- | :---- |
| 1. Reproduce data input | Every script loads OULAD-N04-prepared-1.0 through one loader that stops when a file's SHA-256 differs from the Milestone 3 manifest; nothing is written outside this folder; counts equal Level 1 Table A.6 | `common/lib.py`; `aq-3/logs/01_extract.md`; verification V7 |
| 2. Implement baseline | Random list, rule-ranked list and background-only model are scored on the same folds and runs as the candidates, first; AQ1 and AQ2 report their baselines beside the primary estimate | `aq-3/code/02_dev_folds.py`, `05_test.py`; `aq-1/results/denominators_*`; `aq-2/results/associations_*` |
| 3. Implement candidate | All four candidate configurations of the Candidate Solution Matrix (logistic and boosted trees, primary and extended predictors); no model outside the matrix | `aq-3/code/aq3_models.py` |
| 4. Split and fit correctly | Train 2013, test 2014; leave-one-run-out folds with repeat students removed; nested tuning; every transform fitted on training rows only; test rows extracted without outcomes until the freeze | `aq-3/code/02_dev_folds.py`, `04_freeze.py`; `aq-3/results/dev_fold_design.csv`; `aq-3/logs/test-access.md` |
| 5. Evaluate | The metrics of the four Evaluation Design Cards and the criteria S1, S2, S3, FR1, favourable or not | `aq-3/results/s1_gate.csv`, `secondary.csv`, `calibration.csv`; `aq-4/results/fairness_confirmatory.csv` |
| 6. Error / subgroup analysis | Errors by run, activity, attempts, registration, kind of non-completion and reach; list overlap and stability; fairness by group; calibration by run and group | `aq-3/results/errors_*.csv`, `list_*.csv`; `aq-4/results/fairness_*.csv` |
| 7. Compare to Level 1 expectation | A comparison table closes each report; two proposed Change Log entries (C15, C16) are stated for the team to decide | Each `aq-*/README.md`; AQ3 report, Section 7 |
| 8. Reproducibility | Scripts and runner, one seed (20261112), pinned packages, data version and hashes, folds, freeze record with model hashes, test-access record, experiment log, determinism rerun | `run_all.sh`, `requirements.txt`, `PROTOCOL.md`, `aq-3/results/freeze.json`, `logs/` |

## Three things a reader should know before relying on these results

1. **The gain of the model over the rule is real and small.** 84 more non-completers on 3,955 list places, about one
   per nine tutor groups. The rule alone delivers 97% of the model's hits. Level 1 expected that a baseline may come
   close; it did.
2. **The calibration condition S3 depends on an implementation detail.** Tuning the penalty on log loss (this run)
   meets S3; tuning it on recall at capacity (the team's earlier run) fails it; the ranking is the same in both. The
   safe reading is the Level 1 fallback: ranks and reasons only.
3. **This is a second look at the 2014 runs.** The team's earlier prototype (`reports/milestone-4/package/`) opened
   the 2014 outcomes on 9 November 2026. This prototype is an independent implementation of the same frozen design,
   built without reading the earlier results, with its own freeze (23:18:16 UTC) before its first test access
   (23:19:02 UTC). The two runs agree on S1 to within one non-completer. They should be presented as one test and its
   replication, and the team decides which code is submitted as deliverable G.

## Folder layout

```text
reports/code/
├── README.md              this overview
├── PROTOCOL.md            implementation choices P01–P20, fixed before any result
├── run_all.sh             every step in protocol order
├── requirements.txt       pinned package versions
├── common/                shared code: loader with hash check, test-outcome guard, list metrics, bootstrap, runner, unit tests
├── logs/                  process-log.md (what was done and why), experiment-log.md (automatic, one row per step),
│                          ai-decision-log.md, tests_lib.md, determinism hashes
└── aq-1/ … aq-4/          one folder per analytical question
    ├── README.md          finding-led report
    ├── NOTES.md           brief, decisions, methods checklist, check ledger, open issues
    ├── code/              scripts, numbered in run order
    ├── extracted-datasets/ tables extracted from the prepared dataset (and scores derived from them), CSV
    ├── results/           result tables behind every number in the report, CSV
    ├── figures/           PNG and SVG
    └── logs/              one Markdown log per executed step: time, command, exit status, full console output
```

AQ4 fits nothing of its own: it reads the frozen scores in `aq-3/extracted-datasets/`. `common/` sits outside the
question folders because all four share it.

## How to run

```bash
cd reports/code
../../venv/bin/pip install -r requirements.txt     # the repository's shared environment
../../venv/bin/python common/tests/test_lib.py     # 17 code-path tests on labelled synthetic inputs
bash run_all.sh                                    # about 20 minutes on 10 cores
```

`run_all.sh` stops at the freeze step when `aq-3/results/freeze.json` exists, because the results here come from one
freeze and one test. A single step can be rerun through the runner, for example
`../../venv/bin/python common/run_step.py aq-4 03_fairness -- python aq-4/code/03_fairness.py`. To reproduce the whole
run on a clean copy, remove `aq-3/results/freeze.json` and `aq-3/logs/test-access.md` first; that is a reproduction of
this run, not a new test. Inputs: `reports/milestone-3/package/data/` (override with `OULAD_PREPARED_DIR`) and, for the
AQ1 cross-path, the raw tables in `datasets/oulad/` (`OULAD_RAW_DIR`).

## Reproducibility record

| Item | Value |
| :---- | :---- |
| Prepared dataset | OULAD-N04-prepared-1.0, created 2026-11-06T15:24:17Z; five files hash-checked at every load |
| `features_d27.parquet` SHA-256 | `4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347` |
| `features_d13.parquet` SHA-256 | `c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6` |
| Seed | 20261112 (tie-breaking, bootstrap, boosted trees, shuffles) |
| Python and packages | Python 3.14.5; scikit-learn 1.9.1, statsmodels 0.15.0, polars 2.1.0, numpy 2.5.4, scipy 1.18.1, matplotlib 3.11.2 |
| Git commit at run time | `5c1f96f` (this folder untracked at the time of the run) |
| Folds | Leave-one-run-out over the 9 runs of 2013; `aq-3/results/dev_fold_design.csv` |
| Second freeze | 2026-11-11T23:18:16Z; 12 model files with SHA-256 in `aq-3/results/freeze.json` |
| First test access | 2026-11-11T23:19:02Z; every access in `aq-3/logs/test-access.md` |
| Determinism | Development folds rerun: 5 output files byte-identical (`logs/determinism_*.sha256`); refit of the chosen model reproduces the saved test scores (V1) |
| Checks | AQ1 C1–C5, AQ3 V1–V7 and V1b, 17 unit tests: all pass; ledgers in each `NOTES.md`. Report check: 304 file references resolve and the quoted S1, S3, sensitivity, list-quality, fairness, AQ2 and AQ1 numbers equal the result tables (`logs/check_reports.md`) |

## Before submitting

- **Read and rerun the code.** The brief does not accept AI-written code that the team cannot explain (section 11).
  This prototype was written and run by an AI assistant; `logs/ai-decision-log.md` offers the rows for the team's AI
  Decision Log, with the "Team decision" column left for the team.
- **Decide the two proposed Change Log entries** (C15 tuning criterion, C16 ranks and reasons only) and which
  prototype run is deliverable G.
- **Language and build.** Reports are in English, like the Level 1 section sources; the Vietnamese twin and the Word
  build belong to the team's `build-report` flow. A submitted report should cite these results in words and not by
  repository path.
- **Scope of every claim.** OULAD is a stand-in for the university's records: the results show that the design is
  feasible, not what it will achieve in the pilot. No result says that contacting a student changes the outcome.
