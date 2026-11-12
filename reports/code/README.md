# Milestone 4, Level 2 – Prototype Experiment (team N04)

*MTH045 The Science of Data Analytics · education analytics · prepared dataset OULAD-N04-prepared-1.0 · rerun of 12 November 2026 (UTC) with the repository's `data-analyst` skill*

This folder is deliverable G of the Milestone 4 brief: code, experiment log, preliminary results and reproducibility information for a controlled test of the Level 1 proposal. It tests whether the Level 1 choices are feasible and what they trade off. It is not a search for the best score, and the Level 1 report stays as submitted.

> **Result in one paragraph.** The prototype supports every primary approach chosen in Level 1, with two qualifications from the descriptive and diagnostic questions. Grouped rates answer the descriptive question, and both aggregation paths agree to the enrolment in all 22 runs: 45.3% of the 28,061 enrolments registered at day 14 do not complete. In the six modules that ran in both years that rate was −3.5 points (−4.8 to −2.3) in 2014 against 2013, and −0.2 points (−1.4 to +0.9) over all enrolments, because more students left before day 14 in 2014; the KPI can move by several points between years with no intervention. All five early signs meet the association criterion on the 2013 runs and again on the 2014 runs, and four of them still meet it when clicks enter as a continuous measure; the low-activity cut does not. The penalised logistic regression passes the single success gate S1 on the 13 test runs of 2014: its lists hold 72.6% of the non-completers a perfect list could hold, against 70.4% for the early-sign rule (0.726 against 0.704; difference +0.021, 95% interval +0.007 to +0.036, 11 of 13 runs won). The gain over the rule is small, and gradient-boosted trees add nothing measurable, so the simpler model stays. A list of 5 per tutor group of 20 reaches 41.5% of later non-completers against 25.1% for a random list, and the confirmatory fairness check finds 0 of 3 groups flagged. One Level 1 condition does not hold robustly: calibration meets its pooled bounds (calibration-in-the-large +0.124 and slope 0.873) but fails in 5 of 13 runs and in the team's earlier run, so the recommendation is to show tutors ranks and reasons, not probabilities.

## What this run is

**This is a rerun, made with the 2014 outcomes known.** The folder was first produced on 11 November 2026 (git commit `11f4aca`). That first run wrote its protocol before its first result, froze its models at 2026-11-11T23:18:16Z and read the 2014 outcomes once, from 2026-11-11T23:19:02Z. The team then compared its AQ1 and AQ2 reports with the Milestone 5 report of a team member and found five problems. The owner asked for the whole prototype to be regenerated end to end, so that every result table, log, figure, report and note comes from one run and agrees with the others. The pipeline was executed twice on 12 November: the first pass stopped at a checking step whose comparison rule was wrong, all its outputs were deleted, and the second pass ran every step again and is the source of everything here (`logs/process-log.md`, section 6). Three consequences:

1. **AQ3 and AQ4 are a reproduction of an unchanged design.** No model, grid, tuning criterion, tie-breaking rule, seed, bootstrap size, choice rule or fairness rule was changed (`PROTOCOL.md`, P01–P15, P19), so no 2014 outcome could shape the model choice. The rerun froze at 2026-11-12T15:58:51Z and its scripts first read the 2014 outcomes at 2026-11-12T15:58:53Z; that record shows the order in which the scripts ran, not a blind test. All 13 AQ4 result tables and 28 of the 30 AQ3 result tables are byte-identical to the first run's; the other 2 differ only in a column that records run time, and the 12 frozen model files have the same SHA-256 as in the first run (`logs/compare_first_run.md`).
2. **AQ1 and AQ2 changed, by decisions taken after their results were seen.** The changes are corrections of method and additions to reporting (`PROTOCOL.md`, P16–P18, P21, P22); the table below lists them. The Level 1 criteria and models are unchanged.
3. **The team should present one test.** The earlier team run (9 November), the first run of this folder (11 November) and this rerun (12 November) look at the same 13 test runs. They are one test and its reproductions.

| Finding from the comparison with Milestone 5 | What the rerun does | What it finds |
| :---- | :---- | :---- |
| 1. The 2014 late-TMA average counted 3,521 CCC enrolments, where no student can have a late TMA, as differences of 0 | A risk difference is averaged only over rows where the sign has an estimated slope, with that n beside every estimate, in the main, module, sensitivity and subgroup tables; a unit test covers a sign absent from one module | +22.5 points (17.9 to 27.2), n = 9,064, in place of +16.2. The first run's story of a late-TMA gap that shrank by 5 points in 2014 was an artefact: the change is +0.9 points (−5.4 to +7.2). No other sign, module or variant had a module without a slope inside its average; the sensitivity and subgroup tables printed the wrong n and now print n per estimate |
| 2. The year comparison rested on overlapping intervals | 2014 − 2013 difference with a Newcombe interval, on both denominators, overall, for the six shared modules and the nine shared module × start-month pairs, per module and per start month, plus the share not registered at day 14 | Six shared modules, registered at day 14: −3.5 points (−4.8 to −2.3); all enrolments: −0.2 points (−1.4 to +0.9). 16.2% of 2014 enrolments against 10.7% of 2013 enrolments were not registered at day 14 |
| 3. The residual check could not see a graded activity effect | Binned residuals by five activity levels and by tenths of predicted risk; a sensitivity run with log(1 + clicks on days 0–27), labelled post hoc | 3 of 5 activity levels misfit in 2013 and 2 of 5 in 2014. With clicks continuous, low activity (half the median) falls to +2.9 and +0.8 points and fails the criterion in both years; at the median cut it fails in 2014; the other four signs hold |
| 4. Late TMA in AAA-2014J counted as "same direction" | Module estimates whose interval includes 0 are named as no detectable association; the direction count is given both ways | +0.2 points (−13.2 to +13.5), 53 students: no association in that run. 5 of the 30 module estimates of 2014 cannot be told from 0 |
| 5. Low-activity definition | Half the run median stays primary (P16); the run median is a sensitivity row | The Milestone 5 report uses the median cut; its +13.4 and +14.6 points equal the sensitivity row here |

## Results at a glance

| AQ | Level 1 primary approach | Baseline | Main result | Level 1 criterion | Report |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 (descriptive) | Grouped rates with intervals | Pooled rate; second denominator | 45.3% of the 28,061 enrolments registered at day 14 do not complete; 24.9% to 58.3% by run; same modules, 2014 − 2013: −3.5 points on the day-14 population, −0.2 over all enrolments; 16.8% of non-completers have missed a task by week 4 | Two aggregation paths agree to the enrolment: **met** (22 of 22 runs) | [aq-1/README.md](aq-1/README.md) |
| AQ2 (diagnostic) | Logistic regression with run fixed effects and sign × module terms | Unadjusted rate difference | Adjusted risk differences, 2013 / 2014: missed task +40.7 / +39.6, late TMA +21.7 / +22.5, low activity +14.7 / +14.8, inactive +13.5 / +15.4, no pre-start activity +11.3 / +9.2 | ≥ 5 points, interval excluding 0, two-thirds of modules: **5 of 5 signs** in both years; 4 of 5 with clicks as a continuous adjustment (post hoc) | [aq-2/README.md](aq-2/README.md) |
| AQ3 (predictive) | Penalised logistic regression, primary predictors | Early-sign rule; background-only model; random list | Pooled normalised recall 0.726 against 0.704 (rule), 0.567 (background-only), 0.439 (random); day 27, 5 per 20 | Gate S1: **met** (+0.021, interval +0.007 to +0.036, sign-flip p = 0.003). Challenger margin: **not met**, M1 stays. S3: met on pooled estimates, **not robust** | [aq-3/README.md](aq-3/README.md) |
| AQ4 (ranking) | Top-k per run from the AQ3 scores, with reasons | Random list; rule-ranked list | Recall 41.5% (ceiling 57.2%), lift 1.65; tier 1 holds 81% non-completers, tier 2 60% | S1 met by the list; fairness rule FR1: **0 of 3 groups flagged**; age 55 or over not cleared | [aq-4/README.md](aq-4/README.md) |

## How the eight prototype steps of the brief are met

| Brief step (section 10) | What was done | Where |
| :---- | :---- | :---- |
| 1. Reproduce data input | Every script loads OULAD-N04-prepared-1.0 through one loader that stops when a file's SHA-256 differs from the Milestone 3 manifest; nothing is written outside this folder; counts equal Level 1 Table A.6 | `common/lib.py`; `aq-3/logs/01_extract.md`; verification V7 |
| 2. Implement baseline | Random list, rule-ranked list and background-only model are scored on the same folds and runs as the candidates, first; AQ1 and AQ2 report their baselines beside the primary estimate | `aq-3/code/02_dev_folds.py`, `05_test.py`; `aq-1/results/denominators_pooled_all.csv`; `aq-2/results/associations_2013.csv` |
| 3. Implement candidate | All four candidate configurations of the Candidate Solution Matrix (logistic and boosted trees, primary and extended predictors); no model outside the matrix | `aq-3/code/aq3_models.py` |
| 4. Split and fit correctly | Train 2013, test 2014; leave-one-run-out folds with repeat students removed; nested tuning; every transform fitted on training rows only; test rows extracted without outcomes until the freeze | `aq-3/code/02_dev_folds.py`, `04_freeze.py`; `aq-3/results/dev_fold_design.csv`; `aq-3/logs/test-access.md` |
| 5. Evaluate | The metrics of the four Evaluation Design Cards and the criteria S1, S2, S3, FR1, favourable or not | `aq-3/results/s1_gate.csv`, `secondary.csv`, `calibration.csv`; `aq-4/results/fairness_confirmatory.csv`; `aq-2/results/replication.csv`; `aq-1/results/year_comparison_all.csv` |
| 6. Error / subgroup analysis | Errors by run, activity, attempts, registration, kind of non-completion and reach; list overlap and stability; fairness by group; calibration by run and group; AQ2 residuals by activity level and predicted risk | `aq-3/results/errors_by_run.csv`, `errors_by_slice.csv`, `list_overlap.csv`; `aq-4/results/fairness_descriptive.csv`; `aq-2/results/binned_residuals_activity5_2013.csv` |
| 7. Compare to Level 1 expectation | A comparison table closes each report; two proposed Change Log entries (C15, C16) and one open design question (the low-activity sign) are stated for the team to decide | Each `aq-*/README.md`; AQ3 report, Section 7; AQ2 report, Section 4 |
| 8. Reproducibility | Scripts and runner, one seed (20261112), pinned packages, data version and hashes, folds, freeze record with model hashes, test-access record, experiment log, determinism rerun, comparison with the first run | `run_all.sh`, `requirements.txt`, `PROTOCOL.md`, `aq-3/results/freeze.json`, `logs/` |

## Four things a reader should know before relying on these results

1. **The gain of the model over the rule is real and small.** 84 more non-completers on 3,955 list places, about one per nine tutor groups. The rule alone delivers 97% of the model's hits. Level 1 expected that a baseline may come close; it did.
2. **The calibration condition S3 depends on an implementation detail.** Tuning the penalty on log loss (this folder) meets S3; tuning it on recall at capacity (the team's earlier run) fails it; the ranking is the same in both. The safe reading is the Level 1 fallback: ranks and reasons only.
3. **The KPI moves between years without any intervention.** In the same modules the day-14 non-completion rate was 3.5 points lower in 2014 while the rate over all enrolments did not change, because more students left before day 14. The pilot should be judged against tutor groups of the same run, and the share not registered at day 14 should be reported beside the KPI.
4. **"Low activity" is a coarse summary, not a separate sign.** It meets the Level 1 criterion as written and adds nothing once the amount of activity is known. Showing tutors the amount of activity may serve them better than a yes/no flag; that is a decision for the team.

## Folder layout

```text
reports/code/
├── README.md              this overview
├── PROTOCOL.md            implementation choices P01–P23 and the status of the rerun
├── run_all.sh             every step in protocol order
├── requirements.txt       pinned package versions
├── common/                shared code: loader with hash check, test-outcome guard, list metrics, bootstrap, runner, unit tests,
│                          report tables built from result tables, report check, comparison with the first run
├── logs/                  process-log.md (what was done and why), experiment-log.md (automatic, one row per step),
│                          ai-decision-log.md, unit-test logs, determinism hashes, comparison with the first run, report check
│                          attempt-1/ = record of the first pass of the rerun, which stopped at a checking step
└── aq-1/ … aq-4/          one folder per analytical question
    ├── README.md          finding-led report
    ├── NOTES.md           brief, lifecycle record, decisions, methods checklist, check ledger, open issues
    ├── code/              scripts, numbered in run order
    ├── extracted-datasets/ tables extracted from the prepared dataset (and scores derived from them), CSV
    ├── results/           result tables behind every number in the report, CSV
    ├── figures/           PNG and SVG
    └── logs/              one Markdown log per executed step: time, command, exit status, full console output
```

AQ4 fits nothing of its own: it reads the frozen scores in `aq-3/extracted-datasets/`. `common/` sits outside the question folders because all four share it.

## How to run

```bash
cd reports/code
../../venv/bin/pip install -r requirements.txt     # the repository's shared environment
../../venv/bin/python common/tests/test_lib.py          # 17 of 17 code-path tests of the list metrics, synthetic inputs
../../venv/bin/python common/tests/test_aq2_model.py    # 21 of 21 code-path tests of the AQ2 support rule and the year comparison
bash run_all.sh                                    # about 25 minutes on 10 cores
```

`run_all.sh` stops at the freeze step when `aq-3/results/freeze.json` exists. To run the whole pipeline again on a clean copy, remove `aq-3/results/freeze.json` and `aq-3/logs/test-access.md` first; that is a reproduction, not a new test, which is what this rerun is. A single step can be rerun through the runner, for example `../../venv/bin/python common/run_step.py aq-4 03_fairness -- python aq-4/code/03_fairness.py`. `REPORT_CHECK=0 bash run_all.sh` leaves out the last three steps, which build the report tables from the result tables, write them into the reports and check the reports; they are run after the prose is written. Inputs: `reports/milestone-3/package/data/` (override with `OULAD_PREPARED_DIR`) and, for the AQ1 second path, the raw tables in `datasets/oulad/` (`OULAD_RAW_DIR`).

## Reproducibility record

| Item | Value |
| :---- | :---- |
| Prepared dataset | OULAD-N04-prepared-1.0, created 2026-11-06T15:24:17Z; five files hash-checked at every load |
| `features_d27.parquet` SHA-256 | `4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347` |
| `features_d13.parquet` SHA-256 | `c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6` |
| Seed | 20261112 (tie-breaking, bootstrap, boosted trees, shuffles) |
| Python and packages | Python 3.14.5; scikit-learn 1.9.1, statsmodels 0.15.0, polars 2.1.0, numpy 2.5.4, scipy 1.18.1, matplotlib 3.11.2 |
| Git commit at run time | `11f4aca` (the first run; the rerun's files are uncommitted changes on top of it) |
| Folds | Leave-one-run-out over the 9 runs of 2013; `aq-3/results/dev_fold_design.csv` |
| Freeze of the first run (history) | 2026-11-11T23:18:16Z; first test access 2026-11-11T23:19:02Z |
| Freeze of this rerun | 2026-11-12T15:58:51Z; 12 model files with SHA-256 in `aq-3/results/freeze.json` |
| First test access of this rerun | 2026-11-12T15:58:53Z; every access in `aq-3/logs/test-access.md` |
| Reproduction of the first run | All 13 AQ4 result tables and 28 of the 30 AQ3 result tables are byte-identical to the first run's; the other 2 differ only in a column that records run time, and the 12 frozen model files have the same SHA-256 as in the first run |
| Determinism | Development folds rerun inside the pipeline: 5 output files byte-identical (`logs/determinism_before.sha256`, `logs/determinism_after.sha256`); refit of the chosen model reproduces the saved test scores (V1) |
| Checks | AQ1 C1–C7, AQ3 V1–V7 and V1b, 17 of 17 and 21 of 21 unit tests: all pass; ledgers in each `NOTES.md`. Report check: every table row of the four reports equals the row built from the result tables, and the quoted numbers, the times of this run and the file references are checked (`logs/check_reports.md`) |

## Before submitting

- **Read and rerun the code.** The brief does not accept AI-written code that the team cannot explain (section 11). This prototype was written and run by an AI assistant; `logs/ai-decision-log.md` offers the rows for the team's AI Decision Log, with the "Team decision" column left for the team.
- **Decide the two proposed Change Log entries** (C15 tuning criterion, C16 ranks and reasons only), the open question on the low-activity sign, and which prototype run is deliverable G.
- **Align with the Milestone 5 report.** Its AQ1 year comparison agrees with this folder. Its AQ2 uses the run median as the low-activity cut and a slightly different model, so its late-TMA numbers (+20.2 and +20.3 points) differ from the +21.7 and +22.5 here; the verdicts agree.
- **Language and build.** Reports are in English, like the Level 1 section sources; the Vietnamese twin and the Word build belong to the team's `build-report` flow. A submitted report should cite these results in words and not by repository path, and should describe the final state without the history of runs told here.
- **Scope of every claim.** OULAD is a stand-in for the university's records: the results show that the design is feasible, not what it will achieve in the pilot. No result says that contacting a student changes the outcome.
