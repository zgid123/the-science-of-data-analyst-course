# Milestone 3 report (team N04)

From understanding to preparation: data understanding, data quality assessment, AQ–data fit, the preparation plan,
a reproducible preparation pipeline, prepared-data validation and model readiness for OULAD, following
`milestones/03/milestone-3.md`. Baseline: the Milestone 1 proposal as revised by the Milestone 2 Change
Log (`reports/milestone-2/`); raw data: the Milestone 2 Data Collection Package.

- `reference.md`, `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md`: outline, plan and ledger (research-report skill).
- `package/`: the Prepared Data Package (deliverables C and D, with B, E and F in `package/data/metadata/`); see
  `package/README.md`. `data/raw`, `data/interim` and `data/processed` are rebuilt by `src/run_all.sh` and not committed.
- `research/`: frozen baseline (`baseline/`), AQ–data fit and Change Log entries (`fit/`), readiness (`readiness/`),
  AI critic and auditor prompts, outputs and decisions and the AI Decision Log (`review/`), tables moved to the
  appendices (`appendix/`), sources and claims of the web research (`sources/`, `part*-claims.md`), spot-check, style
  review, brief checklist (`brief-checklist.md`) and Vietnamese review logs (`vi-review/`).
- `report/`: English sections and Vietnamese twins (figures in `report/assets/figures/`, drawn by
  `figures/milestone_3/`); `build/`: `N04_Milestone3_EN.docx`, `N04_Milestone3_VI.docx`.
- `code/`: task scripts; `logs/`: run, check and build logs (UTC time, command, output, exit status).

## Commands (from the repository root)

```bash
venv/bin/python reports/milestone-3/code/freeze_baseline.py     # entry gate: baseline copy and checksums
bash reports/milestone-3/package/src/run_all.sh                 # rebuild the Prepared Data Package from raw (8 stages)
bash reports/milestone-3/code/check_rerun.sh                    # two runs from raw, compare output hashes
venv/bin/python reports/milestone-3/code/build_appendices.py    # Appendices I–VI from package and research files
venv/bin/python .claude/skills/build-report/scripts/render_figures.py milestone-3   # figures
venv/bin/python reports/milestone-3/code/measure_pages.py reports/milestone-3/build/N04_Milestone3_EN.docx  # main-text pages
make all TASK=milestone-3                                        # checks, EN and VI Word build, post-checks
```
