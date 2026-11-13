# AQ1–AQ4 on OULAD 2013–2014 (team N04)

Answers the four Analytical Questions of the Milestone 4 design on the prepared dataset OULAD-N04-prepared-1.0, and serves as the Milestone 4 Level 2 prototype and the results of the Final Report.

- **Read first:** [report.md](report.md) – the findings, figures and tables.
- **Against the Milestone 4 experiment:** [comparison.md](comparison.md) – same answers to every AQ; calibration S3 and the strength of the S1 test differ, both traced to the tuning criterion.
- **How the work was done and checked:** [NOTES.md](NOTES.md) – brief, inherited design, ten-stage lifecycle record, decisions, check ledger, independent review.

## Run

```bash
cd reports/experiment
../../venv/bin/pip install -r requirements.txt   # the repository's shared environment
bash run_all.sh                                  # every step in order, about 15 minutes on 10 cores
```

Inputs: `../milestone-3/package/data/` (prepared views and raw OULAD tables), pinned in `data-manifest.json`; override the location with `OULAD_PREPARED_DIR`. Each step writes `logs/<step>.md`; `logs/experiment-log.md` lists every executed step.

The 2014 test runs are protected: `results/freeze.json` records the frozen choices and model files, every read of a 2014 outcome is appended to `logs/holdout-access.md`, and the 2014 scores are written once to `scores/` (later runs read them). To run the test from scratch on a clean copy, delete `models/`, `scores/`, `results/freeze.json` and `logs/holdout-access.md` first; that is a reproduction of the same test, not a new one.

## Layout

| Path | Content |
| :---- | :---- |
| `code/` | Scripts in run order: `02_prepare` (populations), `03_aq2` (AQ2, per year), `04_aq3_dev` (development and final models), `06_aq3_score` (single scoring of 2014), `07_aq3_evaluate`, `08_aq4_lists`, `10_aq2_compare`, `11_aq1`, `12_recompute` (second code path), `13_compare_prior` (earlier team implementation), `16_compare_m4` (Milestone 4 experiment), `14_headlines`, `15_figures`; `common.py` and `models.py` (frozen) are shared |
| `results/` | Every result table behind the report (CSV), the frozen choices and freeze record |
| `models/`, `scores/` | Frozen models (2013) and the saved 2014 scores |
| `figures/` | PNG and SVG of the seven report figures |
| `evidence/` | Result tables of the earlier team implementation (git commit 7516b83) and of the Milestone 4 experiment, used for the comparisons |
| `tools/` | Copies of the `data-analyst` skill's run, check and chart tools |
| `claims.json`, `comparison-claims.json` | Each number quoted in the report and the comparison, tied to a result cell |
