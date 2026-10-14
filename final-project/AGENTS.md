# Final Project Agent Guide

## Task scope and skill selection

Use the dataset and analytical objective selected by the user. Work on one dataset at a time unless the user explicitly requests otherwise. If the dataset is not identified or its location cannot be resolved, ask before starting dependent work. Do not select other datasets or infer the task from neighboring files.

For analytical work, read `.agents/skills/data-analyst/SKILL.md`. Use `prompts/generic-prompt.md` when the user invokes it. The separate repository-root `skills/data-analyst/` copy may differ; do not substitute it for this installation. Paths in this guide are relative to `final-project/`; skill references are relative to the skill directory.

The current request determines the domain, questions, output format and language. Do not automatically load proposal, requirements or milestone files, or generate course submissions. Use those materials only when the user explicitly makes them relevant. Keep reusable analytical methods in the skill and dataset-specific decisions in the study.

Use the requested output location or default to `samples/<dataset>/`. Maintain relevant opening/reproduction instructions. A focused question can have a concise answer; a substantial study using the generic prompt calls for a report, dashboard, reproducible code and evidence. Documentation maintenance does not trigger analysis.

## Current structure

- `prompts/`: research brief and dataset acquisition instructions.
- `datasets/`: local educational datasets and archives; see `datasets/README.md` for the documented inventory.
- `requirements/` and `milestones/`: instructor guidance and team proposal/work; distinguish proposed assumptions from measurements and confirmed decisions.
- `.agents/skills/data-analyst/SKILL.md`: local analytical methodology and skill instructions.
- `.agents/skills/data-analyst/workflows/analytics-lifecycle.md`: detailed ten-stage lifecycle and verification gates.
- `.agents/skills/data-analyst/references/`: supporting analytical techniques and safeguards.
- `.agents/skills/data-analyst/references/investigation-and-synthesis.md`: question prioritization, follow-up, stopping and evidence-backed findings.
- `.agents/skills/data-analyst/references/analytical-quality.md`: anchored technical, analytical and communication review.
- `.agents/skills/data-analyst/evals/`: skill scenarios, synthetic fixtures and deterministic evaluator tests; these are not project research results.
- `samples/`: seven existing study folders, shared analysis/dashboard code, dependency manifest and saved verification evidence.
- `evaluations/`: local skill reviews and executed validation evidence.
- `skills-lock.json`: installed skill provenance.

Existing samples include `samples/_shared/`, dataset-specific wrappers, reports, dashboards and `samples/requirements.txt`; inspect them before choosing tools or adding a structure. Treat existing outputs as prior work to review, not accepted final-project results. Preserve them as baseline evidence when conducting comparisons; updating the skill does not retroactively validate or regenerate them. Dataset documentation can mention helper scripts that are absent; verify paths and commands before relying on them.

## Local skill workflow

Read `.agents/skills/data-analyst/SKILL.md` before analytical work. For an end-to-end study, also read `.agents/skills/data-analyst/workflows/analytics-lifecycle.md`, `.agents/skills/data-analyst/references/investigation-and-synthesis.md` and `.agents/skills/data-analyst/references/analytical-quality.md`. Follow the lifecycle gates and revisit earlier stages when evidence or feedback changes the question. Scale the workflow to focused requests; documentation-only maintenance does not require dataset analysis. Preserve concise evidence of gate decisions and corrections rather than forcing ten lifecycle headings into reports. A focused calculation does not require a dashboard or extensive rubric documentation.

Load supporting references only as the task requires them, using the local `.agents/skills/data-analyst/references/` directory:

| Task | Reference files |
|---|---|
| Research framing and definitions | `problem-definition.md`, `analytics-types.md`, `metrics-and-kpis.md` |
| Dataset suitability and preparation | `data-collection.md`, `data-quality.md`, `data-wrangling.md` |
| Exploration and uncertainty | `eda.md`, `statistics-and-inference.md` |
| Early-warning modeling and temporal evaluation | `predictive-analysis.md`, `time-series-analysis.md` |
| Dashboard creation and chart review | `dashboards-and-bi.md`, `visualization-and-storytelling.md` |
| Interpretation and reproducible handoff | `causal-reasoning.md`, `reproducibility-and-governance.md` |

Use the simplest method that answers the question. Keep predictive work at analyst depth, such as logistic regression and simple baselines; deep learning and production MLOps are outside the local skill's scope. Return to the earliest corrective stage when a verification gate fails, and record unresolved failures and their effect on confidence.

Use existing accessible dashboard tooling or portable HTML when none is established. A local artifact with opening instructions satisfies deployment; hosting or scheduled refresh requires a user request. Distinguish verified analytical results from stakeholder feedback and future intervention outcomes. Mark future outcome evaluation `PENDING`, or `NOT APPLICABLE` when no intervention exists; never invent approval or observed impact.

## Dataset selection and inspection

1. Inspect actual files, schemas, documentation, and coverage before making suitability claims. Treat documented counts and download instructions as expectations to verify.
2. Investigate the selected dataset on its own terms. Check whether supplied files or subsets overlap before treating them as independent evidence.
3. Map the requested questions to available concepts, populations, measures and time coverage. Do not force a particular domain or predictive target onto the dataset.
4. Validate consequential variable meanings using records and documentation rather than column names alone.
5. Preserve source files. Write cleaned tables and features to a separate generated directory, with lineage and documented transformations. Do not silently drop rows, impute values, or remove outliers.
6. Profile schemas and small samples first; use selected columns, chunked reads, or query engines for large logs. For sampled analysis, record the frame, seed, selection, exclusions and limits; assess stability when material. Avoid choosing a small sample solely to finish quickly. Respect the selected dataset scope.
7. Use `prompts/download-dataset-prompt.md` only when acquisition is needed. Check existing files before downloading, extracting, or regenerating data.

## Research design and leakage prevention

Define the unit of analysis, eligible population, measures, comparisons and observation period from the current question. For prediction, additionally define the target, prediction point and future outcome window. Verify information availability, appropriate group/temporal splits and training-label timing. Fit learned preprocessing on training only, select thresholds on validation, and disclose prior holdout reuse.

Document derived variables, source fields, formulas and timing assumptions. Validate keys, join cardinality and exclusions. Distinguish recorded absence from a confirmed event or obligation. Choose analyst-level methods and baselines appropriate to the task; prediction is optional.

## Analysis and interpretation

Before substantial analysis, record prioritized questions, evidence requirements, answerability, intended comparisons and task-specific acceptance criteria. Distinguish supplied requirements from proposed assumptions. An inventory or a working dashboard is not an analytical success criterion.

Start with data-quality checks and exploratory analysis. Define metric grains, denominators, time windows, missingness, and sample counts. Analyze only concepts and relationships supported by the data and requested objective.

Compare simple baselines before adding analyst-level predictive methods. Use task-appropriate metrics, uncertainty, error analysis and relevant subgroup or threshold comparisons. Explain practical trade-offs rather than relying on one favorable score.

Keep descriptive associations, held-out predictive evidence, and causal claims distinct. Disclose uncertainty and protect sensitive identifiers. If the requested analysis is unsupported, identify the missing evidence and any justified narrower alternative without silently replacing the objective.

For material findings, record the observation, why a follow-up could change its interpretation, the executed comparison or sensitivity check, and the resulting interpretation. Link each major finding to its population, method, magnitude, uncertainty and supporting results. Stop when priority questions are adequately answered or concretely blocked, not after producing a fixed number of charts.

When required evidence is absent, explicitly revise scope and pursue relevant supported questions. Do not present coverage-only work as a completed broader investigation. Use verified codebooks and substantive fields for survey/contextual studies; respect survey design, overlapping exports, reporting cohorts and appropriate denominators. Do not stop at identifier counts or weight availability when meaningful supported analysis is feasible. Domain-specific assumptions belong in each study, not in the general-purpose skill.

The user has already reported that the existing reports and dashboards lack analytical depth. Record this as actual feedback requiring review of framing, investigation, evaluation and presentation; stakeholder acceptance remains unconfirmed.

## Deliverables and reproducibility

Produce the following for each selected dataset when executing the analysis brief:

- A usable dashboard organized around the supported analytical questions and findings.
- A finding-led research report answering prioritized questions with evidence, interpretation, limitations and implications relevant to the requested objective; keep extensive inventories and methodology in supporting material.
- Reproducible preparation and analysis code, feature and label definitions, supporting result tables, and verification evidence.
- A study README with dependency setup, dataset requirements, exact execution commands, and dashboard opening instructions.
- Update the relevant local index when useful; cross-dataset comparison is outside a single-dataset task unless requested.

The generic prompt requests a report and dashboard for substantial studies; explicit user format constraints take precedence. Explain any evidence-blocked scope and organize reports around findings. Design views around actual comparisons and findings; reusing infrastructure does not justify identical analytical layouts for every dataset.

Keep preparation, analysis, generated outputs, and dashboard code separate as the project grows. Declare dependencies when adding runnable code, use relative paths or explicit configuration, and record seeds, split definitions, dataset versions, and transformation decisions. Keep large source data, generated caches, and secrets out of version control; inspect existing ignore rules before changing them.

## Verification and completion

Verify schema assumptions, key uniqueness, join cardinality, row counts, label coverage, feature cutoff compliance, and train/test separation. Reconcile reported metrics and dashboard values with saved result tables.

Run the implemented pipeline and check that the dashboard opens, renders, and supports its documented interactions. Include a compact verification ledger in substantial analytical deliverables with the check, expected condition, executed method, evidence, and status (`PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE`). Explicitly report checks that were not run.

Apply the skill rubric separately to technical correctness, analytical quality and communication. For every material criterion, record evidence, score, consequence and corrective work. Complete delivery requires at least adequate (2) on each material applicable criterion, the explicit deliverables met, and no unresolved critical failure. Do not average away weak analytical depth with successful technical checks.

Record question coverage and status as **complete analysis**, **partial analysis**, **feasibility assessment** or **unverified work**, with scope and blockers. Lifecycle headings do not prove compliance; retain gate decisions and corrections as work happens. The ledger must record the actual quantity, population, unit and condition checked by code. Missing evidence is NOT VERIFIED, not NOT APPLICABLE.

For documentation-only edits, check paths, consistency with the research brief, and the resulting diff; model training or dataset downloads are unnecessary. Preserve unrelated user changes and report what changed and any remaining limitations.

## Evaluating the installed skill

From `final-project/`, run the bundled evaluator regression tests with:

```bash
python3 -m unittest discover -s .agents/skills/data-analyst/evals -v
```

The bundled evaluation README refers to paths in the upstream source repository. Here, resolve `skills/data-analyst/` to `.agents/skills/data-analyst/`; do not assume upstream `scripts/validate_skills.py` is installed. Evaluation fixture paths in `evals.json` are relative to the skill directory.

Passing evaluator tests validates those checks, not model behavior or research quality. For behavioral comparisons, freeze skill/input versions, use fresh contexts with matched model/settings/tools/budgets, preserve outputs and traces separately from existing samples, and review all three rubric dimensions. Do not expose expected answers to the task runner. Keep held-out fixtures unopened during development. Record unavailable comparisons as NOT RUN and do not claim improvement without observed evidence.
