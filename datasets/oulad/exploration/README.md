# OULAD exploration (1 November 2026)

Data understanding and descriptive analysis of all 7 OULAD tables, on the full data. Start with
[report.html](report.html) (charts, hover details, table views, appendices; opens offline) or its text source
[REPORT.md](REPORT.md).

## Pipeline

`code/run_all.sh` runs the stages in order. Each stage is one script with one job, reads only the raw CSVs in
`datasets/oulad/` and the outputs of earlier stages, and writes into `results/` or `evidence/`.

| Stage | Script | Job | Writes |
|---|---|---|---|
| 0 | `scripts/fetch-datasets/fetch_datasets.py --verify oulad` | check the raw CSVs against their pinned hashes | `logs/00_verify_dataset.log` |
| 1 | `code/01_profile.py` | structure, keys, per-column statistics, relationship and business-rule checks, quality follow-ups (duplicates, activity after unregistration, score heaping) | `results/overview.json`, `columns.json`, `columns.csv`, `checks.json`, `followups.json` |
| 2 | `code/02_features.py` | one row per enrolment: outcome, demographics, registration, clicks (total, days 0–27, de-duplicated), submissions, scores, first assessment | `results/enrolment_features.csv` |
| 3 | `code/03_describe.py` | outcome segments and Sections 5.1–5.5 (intervals, effect sizes, Simpson check, survival, temporal structure, signal ranking, registration, repeats, course design) | `results/segments.json`, `descriptive.json` |
| 4 | `code/04_multivariate.py` | Section 5.6: dimension associations, stratified gradients, interactions, PCA, trajectory clusters | `results/multivariate.json`, `trajectory_clusters.csv` |
| 5 | `code/05_crosscheck.py` | independent recount of the gender reversal from the raw `studentInfo.csv` | `logs/05_crosscheck.log` |
| 6 | `code/06_kdense_audits.sh` | independent profiles, leakage screen and distribution sensitivity with the `exploratory-data-analysis` skill | `evidence/*.json` (`*_first1M` = first 1,000,000 click rows) |
| 7 | `code/07_build_report.py` | render `REPORT.md` with charts, checkboxes and appendices | `report.html` |
| 8 | `validate_palette.js` (dataviz skill, optional) | colour-blindness and contrast check of the outcome and cluster palettes | `logs/08_palette_check.log` |
| 10 | `code/10_scope_feasibility.py` | scope feasibility for the Milestone 1 proposal (`reports/milestone-1`): cohorts still registered at days 14, 28, 60 and at each first assessment due day, their outcomes, withdrawal still ahead, assessments due, capacity-limited list sizes and, per temporal split, the most a perfect list of each capacity can cover; fairness group sizes; descriptive only, no comparator or method evaluated | `results/scope_feasibility.json`, `logs/10_scope_feasibility.log` |

Shared modules hold everything the stages reuse and no analysis of their own:

- `code/common.py` – paths, table keys, column roles, category orders (outcomes, `imd_band`, age, education), the CSV
  loader (`?` and empty fields become missing) and `write_json`.
- `code/stats.py` – Wilson intervals, bias-corrected Cramér's V, Cliff's delta, distribution shape and outliers,
  Gini concentration, Kaplan–Meier.
- `code/charts.py` – chart palette, SVG primitives and one function per chart in `report.html`.

`design-notes.md` records the page design of `report.html` (brief, palette, type, layout, review against
generic defaults) for the `frontend-design` skill.

`logs/` keeps one log per stage (UTC timestamp, command, full console output, exit status) and
`logs/09_render_check.log`, the record of the manual visual review of `report.html`.

## Run

From the repository root:

```bash
venv/bin/python scripts/fetch-datasets/fetch_datasets.py
venv/bin/pip install -r datasets/oulad/exploration/requirements.txt
bash datasets/oulad/exploration/code/run_all.sh
```

Each stage also runs on its own, for example `venv/bin/python datasets/oulad/exploration/code/03_describe.py`,
once the stages before it have written their outputs. Set
`DATAVIZ_VALIDATOR=<dataviz skill>/scripts/validate_palette.js` before `run_all.sh` to re-record the palette
check (stage 8).
