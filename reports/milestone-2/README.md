# Milestone 2 report (team N04)

From requirements to collection: data requirements, open dataset search and selection, reproducible collection of
OULAD and structural verification, following `milestones/02/milestone-2.md`. Baseline: the Milestone 1
proposal in `reports/milestone-1/report/`.

- `reference.md`, `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md`: outline, plan and ledger (research-report skill).
- `research/`: baseline freeze (`baseline/`), data requirements (`requirements/`), dataset search (`search/`, sources
  `sources/S3xx-*`), selection (`selection/`), coverage and Change Log (`coverage/`), AI critic prompts and decisions
  (`review/`), Vietnamese review logs (`vi-review/`).
- `package/`: the Data Collection Package (README, `src/collect.py`, `src/verify_structure.py`, `metadata/`);
  `package/data/raw/` is re-created by the script and not committed.
- `report/`: English sections and Vietnamese twins; `build/`: `N04_Milestone2_EN.docx`, `N04_Milestone2_VI.docx`.
- `code/`: task scripts; `logs/`: check and build logs.

## Commands (from the repository root)

```bash
venv/bin/python reports/milestone-2/code/freeze_baseline.py              # freeze the Milestone 1 baseline (checksums)
venv/bin/python reports/milestone-2/package/src/collect.py [--compare-mirror]   # download, verify, extract OULAD
venv/bin/python reports/milestone-2/package/src/verify_structure.py      # Task 6 structural checks
venv/bin/python reports/milestone-2/code/compare_mirrors.py UCI_ZIP       # compare the UCI copy with the collected files
venv/bin/python reports/milestone-2/code/build_appendices.py             # Appendices I–VI from research and package files
make all TASK=milestone-2                                                 # checks, EN and VI Word build, post-checks
bash reports/milestone-2/code/measure_move.sh STEP [--blocks]             # rebuild EN and VI, log pessimistic pages (logs/R22_*)
bash reports/milestone-2/code/check_pair.sh STEP FILE.md ...              # parity, sync record and pre-checks of edited pairs
venv/bin/python reports/milestone-2/code/putback_test.py MOVE             # put-back test of one appendix move (m1, m4, m7–m11; as run 2026-11-13)
```
