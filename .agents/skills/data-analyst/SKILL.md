---
name: data-analyst
description: Turn datasets into clear, defensible answers, reports and dashboards. Use whenever the user wants to analyze data (CSV, Excel, SQL tables, dataframes, survey or log files), explore an unfamiliar dataset, define metrics/KPIs, explain why a number changed, analyze cohorts, funnels, experiments, surveys or time series, build an early-warning or risk-scoring analysis, or produce an analytical report or dashboard — even if they only say "look at this data" or "what does this tell us". Grills the user one question at a time when consequential context is missing, or when they say "grill me" about an analysis plan. Scales from a one-table answer to a full ten-stage project, and supplies the tools that run one: a project scaffold, a logged step runner, an input manifest, a holdout guard, report tables written from result files, a report check and a comparison with other implementations, beside report/dashboard templates, chart styling and statistics helpers.
---

# Data Analyst

Your product is an answer a busy reader can understand in two minutes and check in ten. Rigor is the floor, not the deliverable: correct populations, denominators and joins make the answer trustworthy, but the reader came for the finding, why it matters and what to do or look at next.

Two failure modes to avoid, both seen in practice:

- **Shallow**: correct totals and a profile of every column, but no real question answered.
- **Defensive**: careful analysis buried under table dumps, caveats on every sentence and process paperwork. The reader cannot find the point.

Aim for careful analysis told plainly.

## Start and scale

1. **Find the purpose and intended use.** Establish who will read this and what they need to decide or learn. Exploratory and informational work can start from its purpose and an inspection of the data and documentation; refine the questions from what they support. Establish a decision, population, grain, units, period and deliverable format when they affect the answer.
2. **Grill when context is missing.** If a decision that would change the answer is still open after that (outcome definition, population, period, cutoff, success criteria, deliverable), interview the user one question at a time using [grilling](./references/grilling.md), with your recommended answer for each. Summarize the settled brief and proceed; ask again only if the summary introduces a new consequential assumption or scope change. Also grill whenever the user asks ("grill me on this analysis"). Do not grill on facts you can look up or on focused calculations. When the user cannot answer (background run, "just do it"), record your recommendations as _proposed_ assumptions instead.
3. **Inherit before you define.** When the work continues a project — a team design, protocol, metric dictionary, change log, earlier report or someone else's implementation — read those first and adopt their populations, definitions, thresholds, operating points and numbering as given. Where the record is ambiguous, look at how the existing implementation resolved it and follow that. Depart only for a reason you can state, and treat each departure as a proposed change: what the record says, what you did, why, and the result both ways. When another implementation of the same question exists, reconcile your numbers with it and explain every difference before you report.
4. **Size the job.**
   - _Focused_ (one calculation, one comparison, a query): inspect the relevant inputs, compute, check once independently, answer with a compact table or a few sentences. No lifecycle headings, dashboard or model.
   - _Substantial_ (open-ended investigation, project, report/dashboard): follow the lifecycle below and read [the lifecycle workflow](./workflows/analytics-lifecycle.md). Check whether a [playbook](#playbooks) matches the problem before planning.
5. **Respect delivery preferences in order.** Follow the user's explicit format or required outline first. Otherwise use existing project or BI tooling. If neither applies, use the bundled report template and add the dashboard template when interactive exploration helps.

## The lifecycle (John Rollins, 10 stages)

The ten stages are mandatory for substantial work: every stage is worked in order and leaves a row in the lifecycle record of `NOTES.md`, with the evidence for its gate. Follow this order of reasoning. It is iterative: when evidence breaks an earlier decision, go back to that stage and say so. Scale the depth of each stage to the task; the gate is what matters, not a heading in the report.

| # | Stage | Question it answers | Produce | Gate to move on |
| --- | --- | --- | --- | --- |
| 1 | Business Understanding | What purpose does this serve, and what decision or learning question matters? | Brief: purpose, reader, questions, scope and deliverable; decision goals and KPIs when relevant | Questions are clear and answerable; decision success criteria are defined when needed |
| 2 | Analytic Approach | How can data answer it? | Analytics type and simplest method per question, with baselines | Method can actually answer the question |
| 3 | Data Requirements | What data do we need? | Outcome + context data → available? answerable / conditional / unsupported | Gaps trigger a narrower question or a pivot, not silence |
| 4 | Data Collection | Where does it come from, how do we get it? | Source inventory: source, coverage, access, sensitivity | Inputs trace to source; privacy handled; gaps disclosed |
| 5 | Data Understanding | Is the data representative of the problem? | Profile, descriptive stats, data quality by dimension | Meanings come from records and docs, not column names |
| 6 | Data Preparation | What work makes it usable? | Cleaned, blended, transformed tables; preparation log with counts | Keys, row counts, denominators and control totals reconcile |
| 7 | Modeling | How do we visualize or model the answer? | Comparisons, challenged hypotheses, models where justified; charts | Each finding has numbers, a comparison and a challenged alternative |
| 8 | Evaluation | Does it really answer the question? | Recomputed key numbers, check ledger, honest status | No critical failure; displayed values match verified results |
| 9 | Deployment | Can it be put into practice? | Report and/or dashboard; rollout plan when relevant | Rendered, inspected, findings visible in the artifact itself |
| 10 | Feedback | What do users and outcomes tell us? | Feedback log; outcome review plan, marked pending | Feedback is not invented; revisited stages re-verified |

## Run the work

The stages say what to decide; the tools below make the work executable and checkable. For substantial work, use them instead of writing equivalents, and do not report a number that no logged step produced. Exploring by hand to choose a definition is fine; note the choice in `NOTES.md`, then put the calculation in a script.

| When | Do | Tool |
| --- | --- | --- |
| Before stage 1 ends | Create the working folder: `NOTES.md` with the ten-stage record, `run_all.sh`, `tools/`, `code/`, `results/`, `figures/`, `logs/` | `python scripts/new_project.py <dir> --title "<title>"` |
| Right after | Prepare the environment from inside the folder and read what is available; if it cannot be prepared, continue with the standard-library tools and say so in `NOTES.md` | `python tools/setup_env.py` |
| Stage 4 | Record the input files once; every later run verifies them and stops on a changed file | `tools/data_manifest.py write <files>`, then `verify`; `checked(path, manifest)` in code |
| Stage 5 | Profile every input before trusting a field | `tools/profile_data.py` |
| Stages 6–7 | Run every script as a logged step, in `run_all.sh` order; a failing step stops the run. Scripts in `code/` start with `import _tools` to import from `tools/` | `tools/run_step.py <step> -- python code/<script>.py` |
| Stage 7, when a held-out set supports a performance claim | Freeze the choices, then read the holdout once; reruns read the saved scores. Cross-validation that only describes fit needs no freeze | `tools/holdout_guard.py freeze`; `open_holdout(...)` in every script that reads holdout outcomes |
| Stage 8 | Reconcile with any other implementation of the same question | `tools/compare_results.py mine.csv theirs.csv --keys … --cols … --tol …` |
| Stage 9 | Write report tables from `results/`; check references, tables, quoted numbers and run history | `tools/report_tables.py fill report.md`; `tools/check_report.py report.md --claims claims.json` |

Any dataset, any format: the tools assume nothing about the subject or the column names. When an input is not CSV (Excel, Parquet, JSON, a database), stage 4 extracts the tables the questions need to CSV under `data/` with a logged step, and the manifest pins both the original file and the extracts. A CSV input can stay where it is and be pinned by its relative path, or be copied into `data/`; prepared tables are not pinned, because the logged steps rebuild them.

The report tools work on Markdown reports, so for substantial work write `report.md` first; build the HTML report from it only when HTML is the requested format. For an HTML report, build its numbers from `results/` by script and say in the ledger how the displayed values were checked.

"Modeling" means whatever answers the question — often a well-chosen aggregation or comparison. Machine learning is optional and stays at analyst level (baselines, linear/logistic models).

## When the main question cannot be answered

Say so early and precisely (which linkage, timing, field or outcome is missing), then **pivot to the most valuable question the data can answer** that still serves the original purpose, and deliver that analysis properly. A feasibility verdict alone is a thin result; a feasibility verdict plus a real, related finding is useful. Label the pivot and the resulting status (partial analysis against the original aim). Never fabricate targets, timestamps or records to keep the original question alive.

## Integrity checklist

These protect the answer. Apply them silently; mention them in the report only where they change a conclusion.

- Inspect actual records and dictionaries before trusting a field's meaning. Preserve raw inputs.
- Define every metric by population, numerator/denominator, unit and window. Distinguish zero, missing and undefined.
- Validate join cardinality and reconcile control totals before aggregating.
- Respect time: no future information in features, account for censoring and incomplete periods.
- Respect design: survey weights, clustering, repeated observations of the same entity.
- Prefer distributions and comparisons over lone averages. Add uncertainty where inference is claimed; full-population totals do not need fake confidence intervals.
- Separate observation from interpretation. Associations are not causes without an identification strategy.
- Document material exclusions, deduplication and imputation with affected counts.
- Recompute decision-critical numbers independently. A check passes only when its stated condition was actually evaluated, over everything its wording covers: a check of "all rates" reads every table that holds a rate, and records how many values it read.
- For substantial work, your own re-check is not the independent one. Before delivery give the report, the result tables and the raw inputs — not your code or your expected values — to a fresh reviewer (a subagent or a colleague) who recomputes the headline numbers and reads each claim against its table. Fix what they demonstrate. With no such reviewer, say the work is self-checked.
- Score a holdout once. Fix the model, features, thresholds and operating points and record that freeze before the first read of holdout outcomes; save the scores; reruns, added views and report fixes read the saved scores. Anything chosen after the outcomes were seen is post hoc and is labelled so, beside the frozen result.
- Report status honestly: **complete analysis**, **partial analysis**, **feasibility assessment** or **unverified work**, with scope.

## Writing the findings

Read [visualization and storytelling](./references/visualization-and-storytelling.md) before writing a substantial report, and look at [the example report](./references/example-report.md) for the target voice.

- **Lead with the answer.** The first paragraph states the main finding with its key number, the population and what it means for the reader.
- **Headlines are claims.** "Students who missed an assignment due by day 60 were about 3.3 times as likely to fail or withdraw by course end" beats "Assessment behavior analysis". Chart titles are claims too.
- **One finding per section**: claim → evidence (one chart or one small table) → what it means → one sentence on its main limit.
- **Final state only.** The report says what is true now. Reruns, corrections, superseded figures and who checked what go in `NOTES.md`; a reader should not be able to tell how many attempts the result took.
- **Keep it short enough to be read.** The body of a substantial report, from the summary to the recommendations, fits in about 1,500 words of prose (tables not counted) and five findings. Method detail, definitions and further tables go in an appendix or stay in `results/`.
- **Caveats live once.** Put limitations in a dedicated section and next to the specific claim they weaken. Do not hedge every sentence.
- **Tables are evidence, not prose.** Keep the body to a few small tables with only the columns the claim needs. Move wide or exhaustive tables to an appendix or `results/`.
- **Plain words.** Explain technical metrics once in reader terms (e.g., what a precision of 60% means for a teacher's review list).
- **Recommend only what the evidence supports**, and say what would confirm it.

## Deliverables and files

For substantial work, default to this layout (adapt to the project's conventions or the user's requested location):

```text
<output>/
├── report.md          # finding-led report; its tables are filled and its numbers checked by the tools
├── report.html        # only when HTML is requested: built from report.md with assets/report-template.html
├── dashboard.html     # optional: when interactive exploration helps the reader
├── NOTES.md           # brief, inherited record, ten-stage lifecycle record, decisions, check ledger — one file
├── run_all.sh         # every step in order, each through tools/run_step.py
├── data-manifest.json # SHA-256 of every input file
├── claims.json        # numbers quoted in the prose, each tied to a cell of results/
├── tools/             # copies of this skill's scripts: the folder runs on its own
├── logs/              # one log per executed step, and experiment-log.md (failed drafting steps stay in it)
├── .venv/             # created by tools/setup_env.py; not part of what is handed over (requirements.lock is)
├── code/              # scripts that reproduce every number
├── results/           # result tables (CSV) behind each finding
└── figures/           # charts (PNG + SVG)
```

Keep process records in the single `NOTES.md`. Do not produce separate process, quality-review or self-scoring files; the reader judges the work by the report, and reviewers judge it by the code and ledger. Default to a report for substantial written analysis; add a dashboard when the reader needs to filter or explore. For focused questions, answer inline.

## Bundled assets and scripts

Use these instead of writing from scratch; they encode the house style.

| File | Use |
| --- | --- |
| [assets/report-template.html](./assets/report-template.html) | Self-contained report page: summary box, key-number tiles, finding sections, limitations, appendix. Light/dark, print-friendly. |
| [assets/notes-template.md](./assets/notes-template.md) | `NOTES.md` with the ten-stage lifecycle record, inherited project record, decisions, check ledger. Written by `new_project.py`. |
| [assets/reviewer-brief.md](./assets/reviewer-brief.md) | Brief to fill in and hand to the independent reviewer at stage 8: what they may read, what to recompute, what to report. |
| [assets/dashboard-template.html](./assets/dashboard-template.html) | Offline dashboard: embedded JSON data, filters, KPI tiles and dependency-free SVG bar/line/interval charts. |
| [scripts/chart_style.py](./scripts/chart_style.py) | Matplotlib house style: accessible palette, claim titles, direct labels, highlight-one-bar, PNG+SVG export. |
| [scripts/stats_helpers.py](./scripts/stats_helpers.py) | Wilson and difference-in-proportion intervals, (cluster) bootstrap, capacity/alert tables, calibration bins, weighted shares, like-for-like (standardised) rates. |
| [scripts/new_project.py](./scripts/new_project.py) | Working folder with `NOTES.md` (ten-stage record), `run_all.sh` and the tools copied in. |
| [scripts/setup_env.py](./scripts/setup_env.py) | Creates `.venv`, installs [requirements.txt](./requirements.txt), writes `requirements.lock`; `--check` reports what is available. |
| [scripts/run_step.py](./scripts/run_step.py) | Runs one step, logs command, time, exit status and output, appends the experiment log. |
| [scripts/data_manifest.py](./scripts/data_manifest.py) | Records and verifies the SHA-256 of input files; refuses a changed or unlisted input. |
| [scripts/holdout_guard.py](./scripts/holdout_guard.py) | Freeze record written once; blocks holdout reads before it and logs every read. |
| [scripts/report_tables.py](./scripts/report_tables.py) | Fills marked tables of a Markdown report from CSV results; empty cells stay empty, never 0. |
| [scripts/check_report.py](./scripts/check_report.py) | Checks file references, tables, quoted numbers (claims) and run-history phrases in a report. |
| [scripts/compare_results.py](./scripts/compare_results.py) | Compares a result table with another implementation's on key columns, with a tolerance. |
| [scripts/profile_data.py](./scripts/profile_data.py) | Fast first look at CSV/TSV/Parquet files: types, nulls, distinct counts, candidate keys, duplicates → Markdown. |

The run tools and `setup_env.py` use the Python standard library only (Python 3.9 or later; start analysis scripts with `from __future__ import annotations` if they use newer type hints). `wilson_ci`, `diff_proportions_ci` and the CSV profile also work without any package. The other statistics helpers and the charts need `pandas`, `numpy` and `matplotlib`: run `setup_env.py` first. Run `python scripts/<name>.py --help` for usage, or import them.

## Playbooks

Playbooks give the standard questions, charts and traps for common problem types. Read the matching one during Business Understanding.

| Problem | Playbook |
| --- | --- |
| Predict who is at risk early (dropout, churn, default, failure) | [Early warning](./playbooks/early-warning.md) |
| What goes with an outcome, and whether it is the same in each group (factors, drivers, associations) | [What goes with an outcome](./playbooks/drivers.md) |
| A metric moved — what changed and why | [Diagnose a change](./playbooks/diagnose-change.md) |
| Questionnaire or sampled survey data (weights, Likert items, country comparisons) | [Survey analysis](./playbooks/survey-analysis.md) |

## Reference routing

Load only what the current stage needs. Where a row names a companion skill, call the Skill tool with it when it is installed; it does the tool work, while this skill keeps the decisions and checks. If it is not installed, the reference is enough.

| Need | Reference |
| --- | --- |
| Stage activities, gates, verification ledger | [Analytics lifecycle](./workflows/analytics-lifecycle.md) |
| Interviewing the user when context is missing, "grill me" | [Grilling](./references/grilling.md) |
| Prioritizing questions, follow-up, pivoting, stopping | [Investigation and synthesis](./references/investigation-and-synthesis.md) |
| Review rubric before delivery | [Analytical quality](./references/analytical-quality.md); call the Skill tool with `validate-data` for an independent QA pass |
| Report voice, chart choice, storytelling | [Visualization and storytelling](./references/visualization-and-storytelling.md); call the Skill tool with `matplotlib` for chart types `chart_style.py` lacks, `create-viz` for interactive charts, `scientific-visualization` to audit a figure |
| Target voice and structure | [Example report](./references/example-report.md); call the Skill tool with `research-report` for a formal report from an outline with cited literature, `build-report` for its Word/`.pptx` build, `slidev` for a web deck |
| Dashboards, BI tools, readable delivery | [Dashboards and BI](./references/dashboards-and-bi.md); call the Skill tool with `frontend-design` and `theme-factory` to restyle a report or dashboard page, `build-dashboard` for a control the template lacks |
| Judgment illustrations | [Worked examples](./references/analytical-examples.md) |
| Ambiguity, audience, scope | [Problem definition](./references/problem-definition.md) |
| Decision trade-offs | [Data-driven business](./references/data-driven-business.md) |
| Descriptive / diagnostic / predictive / prescriptive | [Analytics types](./references/analytics-types.md) |
| Metric definitions, ratios, metric trees | [Metrics and KPIs](./references/metrics-and-kpis.md) |
| Sources, sampling, acquisition | [Data collection](./references/data-collection.md) |
| Distributions, relationships, anomalies | [EDA](./references/eda.md); call the Skill tool with `explore-data` for a table review, `exploratory-data-analysis` for missingness/leakage audits, `seaborn` for quick exploratory plots |
| Cleaning and reshaping | [Data wrangling](./references/data-wrangling.md); call the Skill tool with `polars` for tables of millions of rows |
| Joins, windows, funnels, cohorts in SQL | [SQL for analysis](./references/sql-for-analysis.md); call the Skill tool with `write-query` to draft a query, `sql-queries` for dialect and performance |
| Quality dimensions, reconciliation | [Data quality](./references/data-quality.md) |
| Uncertainty, tests, effect sizes | [Statistics and inference](./references/statistics-and-inference.md); call the Skill tool with `statistical-analysis` for test choice, `statsmodels` for fitting models, `pymc` for Bayesian or partially pooled estimates |
| Randomized experiments | [Experimentation](./references/experimentation.md); call the Skill tool with `experimental-design` and `statistical-power` when planning one |
| Confounding, causal identification | [Causal reasoning](./references/causal-reasoning.md) |
| Seasonality, temporal validation | [Time series](./references/time-series-analysis.md); call the Skill tool with `statsmodels` for ARIMA/SARIMAX |
| Baselines, leakage, classification metrics | [Predictive analysis](./references/predictive-analysis.md); call the Skill tool with `scikit-learn` for pipelines, `scikit-survival` for time-to-event, `shap` to inspect a model |
| Warehouses and pipelines | [Data engineering](./references/data-engineering.md) |
| Lineage, privacy, reruns | [Reproducibility and governance](./references/reproducibility-and-governance.md) |

Spatial comparisons: validate geographic units, boundary changes, exposure denominators and spatial dependence before ranking areas.
