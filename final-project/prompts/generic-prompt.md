# Final-project analysis prompt: Early Warning of Academic Risk through Student Assessment Behavior Analytics

Use the data-analyst skill to analyze **the single dataset I name in my accompanying request** for my final project, **“Early Warning of Academic Risk through Student Assessment Behavior Analytics.”** Investigate whether assessment behaviors observable early in learning can identify students at risk of a later adverse academic outcome, with enough lead time to inform supportive action. Deliver substantial, reproducible findings with a useful report and dashboard.

Keep this purpose fixed across datasets. Adapt questions, features and methods to verified data availability; do not replace the project with a general education overview, institutional ranking, survey profile or unrelated prediction task. A working dashboard or high retrospective classification score alone does not demonstrate early-warning value.

## Inputs and scope

- Use my request to identify the dataset, its location, the specific questions within this project purpose, audience and any constraints. Do not select additional datasets or launch a batch analysis.
- If I have not identified a dataset or its location cannot be resolved, ask for that information before starting dependent work.
- If I select a dataset without a specific question, inspect its schema, records and metadata, then prioritize supported questions about assessment behavior, subsequent academic risk and warning timeliness. Label dataset-specific definitions and choices as proposed operationalizations, not as requirements I supplied.
- If my request specifies a narrower deliverable or focused calculation, scale the work accordingly; do not force a dashboard or a long report onto a simple question.
- Follow applicable `AGENTS.md` instructions. In this workspace, use `final-project/.agents/skills/data-analyst/SKILL.md` (or `.agents/skills/data-analyst/SKILL.md` when already in `final-project/`). For substantial work, read the skill's `workflows/analytics-lifecycle.md`, `references/investigation-and-synthesis.md` and `references/analytical-quality.md`. Load other references only when relevant.
- Use my requested output location. Otherwise, write under `final-project/samples/<dataset>/`, resolving the path from the workspace rather than creating a nested `final-project/` directory. Keep code, prepared outputs, supporting tables/figures, report and dashboard organized separately.
- Use the language I request; otherwise use the language of my analytical request. Preserve source field names and useful technical terms.

The project purpose above governs this prompt unless I explicitly change it. My accompanying request specifies the dataset and any narrower scope. Do not infer a risk target, cohort, cutoff, KPI, model, language or submission format from unrelated previous analyses or neighboring files. Use relevant dataset documentation and codebooks to establish semantics, not to silently replace the project objective.

Inspect existing work before changing it. Reuse verified components without inheriting unsupported assumptions or generic layouts. Preserve raw data and unrelated changes. Keep baseline evidence when comparing versions. Do not edit the skill as part of the analysis unless I ask.

## 1. Frame answerable questions

Establish the population, unit of analysis, coverage, intended reader and prioritized questions. Define relevant metrics, denominators, units, periods, comparisons and what would constitute an adequate answer.

Map each question to required evidence and actual fields/tables. Classify it as supported, conditional or unsupported. Distinguish the local snapshot from any larger upstream dataset.

Begin with an explicit suitability assessment for this project's purpose. Check for student-level linkage, assessment events or submissions, event/availability times or ordered observation periods, assessment opportunities or deadlines where needed, and a later measurable academic outcome. Identify which evidence is present in the selected local files. Distinguish direct early-warning evidence, partial evidence about assessment behavior, contextual evidence and unsupported use; educational relevance alone is insufficient.

Prioritize these questions where answerable:

1. Which early assessment behaviors are associated with later academic risk, and how large and consistent are those differences?
2. How early do useful signals emerge, and how do warning quality, student coverage and available support time change across justified cutoffs?
3. Do behavior features add value beyond simple prior-score or course-prevalence baselines?
4. Which students or course/cohort groups are missed or falsely flagged, and what alert volume would educators need to review?

Define academic risk using a documented future outcome, such as course failure, withdrawal or later assessment underperformance, only when supported. Explain the educational meaning and treatment of outcome categories; do not silently combine withdrawal and failure. A proxy must be labeled and justified, with its limits stated. Missing activity is not itself a confirmed adverse outcome. Define the student-course or other justified analytical unit, enrollment eligibility, observation cutoff, future outcome window and minimum follow-up. Exclude or separately analyze students whose adverse outcome already occurred by the cutoff. State the intended support decision and useful lead time as assumptions when no stakeholder requirement exists.

Resolve consequential meanings using actual records, dictionaries and authoritative documentation. Ask only about ambiguities that materially affect validity and cannot be resolved from available evidence. Continue independent work while clarification is pending.

If direct early warning is unsupported, explain the precise missing linkage, behavior, timing or outcome evidence. Conduct a bounded feasibility assessment or relevant assessment-behavior investigation when possible, and identify the additional evidence needed. Contextual datasets may inform background only within this purpose; do not substitute an unrelated analysis or present contextual associations as student-level warning evidence. Do not fabricate targets, timestamps, missing concepts or results to preserve an unsupported question.

Record material changes to definitions or scope with their rationale and effect on conclusions. Do not invent stakeholder agreement.

## 2. Understand and prepare the data

Inspect schema and representative records before choosing transformations. Establish entities, keys, join cardinality, variable meanings, units, category codes, time semantics, provenance and coverage.

Assess relevant quality issues with evidence:
- Missingness and its patterns across meaningful groups or periods; distinguish missing values from absent concepts.
- Duplicate records versus legitimate repeated observations, unmatched keys and join fanout.
- Invalid codes, impossible dates, unusual values, skewness, dispersion and zero inflation.
- Outcome balance, temporal gaps, follow-up duration, selection effects and representativeness where applicable.

Investigate anomalies rather than automatically dropping or imputing them. Document consequential transformations, exclusions and affected row/entity counts. Preserve source data and create reproducible analysis-ready views with source-to-derived-variable lineage.

Create assessment-behavior features only from supported fields: submission timing relative to deadlines, completion of due assessments, overdue non-submission, attempt frequency, spacing or regularity, time since the last assessment event, response duration, and early score trajectories where available. Treat these as candidates, not required columns. Separate behavior features from performance features and supplementary engagement/context features. Do not infer attempts, active working time or procrastination from records that cannot establish them. Distinguish an assessment not yet due, a confirmed missed obligation, an absent log and an unavailable score. Compute opportunity-based denominators only from assessments applicable and due for that student by the cutoff; document exceptions, registration changes and resit rules when available.

Validate keys, joins, counts, control totals and denominators. Distinguish zero, missing and undefined values. Use efficient reads or a justified reproducible sample for large data; record the sampling frame, seed, scope and limitations, and assess sampling stability when material.

Use existing data first. Retrieve relevant metadata where needed and accessible, but do not acquire additional datasets or expand the scope without justification and authorization. Record actual sources and access evidence; do not invent historical acquisition dates.

## 3. Investigate beyond profiling

Execute a coherent set of analyses that answer the prioritized questions. Choose appropriate distributions, comparisons, relationships, temporal patterns, decompositions or other methods based on the data and objective.

Keep assessment behavior central: compare early behavior distributions and trajectories across later outcome groups, then investigate relevant differences in assessment opportunities, prior performance and course/cohort context. Compare behavior-only, performance-only and combined signals where feasible. Evaluate stability across justified periods or cohorts and test sensitivity to material choices such as cutoff, risk definition and missing-record handling. Report associations without claiming that a behavior causes failure or that changing it will improve outcomes.

For each material initial finding:
1. Explain what remains uncertain and which alternative explanation could change its interpretation.
2. Choose and execute a discriminating follow-up or sensitivity check when feasible.
3. Record the result and how it strengthens, changes or limits the conclusion.

A list of proposed analyses does not replace feasible investigation. Use the simplest defensible methods; do not add models for appearance, slice indiscriminately or hunt significance. Quantify effect sizes and uncertainty when warranted by the question and study design. Respect dependence, sampling design, confounding, multiplicity and incomplete observation where relevant.

Stop when priority questions have supported answers or concrete blockers, material contradictions are resolved or bounded, and further feasible work is unlikely to change the scoped interpretation. Disclose partial work if constraints prevent that point.

## 4. Evaluate early-warning value when supported

Early-warning evaluation is a priority when the selected data supports temporal prediction. If required evidence is absent, document the blocker and complete the supported investigation without manufacturing a model. When prediction is feasible:

- Define the target, eligible population, prediction point, observation window and future outcome window before modeling.
- Verify that predictors and historical training labels are available at the required times. Exclude future information, target-derived variables and retrospective aggregates.
- Check recording and release delays as well as event dates: a submitted assessment's score is usable only if it would have been available at the warning cutoff. Exclude final grades, later withdrawal/completion records, post-cutoff submissions and full-course summaries from predictors. If availability times are unknown, state and test a conservative assumption or omit the affected features.
- Choose entity/group and temporal separation appropriate to the intended generalization claim.
- Prefer evaluation on later course presentations/cohorts when available. Keep repeated snapshots of the same enrollment together; handle students appearing in multiple courses according to the claimed generalization setting. Ensure historical training outcomes were known before the simulated deployment point. If only within-cohort evaluation is feasible, disclose that it does not establish performance on future cohorts.
- Fit preprocessing and feature selection on training data only. Select models and thresholds on training/validation evidence. Reserve test data for final evaluation and disclose prior holdout reuse.
- Compare simple baselines before adding complexity. Justify methods using the question, data, assumptions and interpretability needs.
- Include a prevalence/no-skill reference, a simple assessment-behavior rule and a prior-score baseline where supported. Start with interpretable analyst-level methods such as logistic regression. Compare behavior-only, score-only and combined models on the same eligible population and splits to assess the added value of behavior.
- Choose metrics appropriate to the task, including error analysis, uncertainty and relevant subgroup or threshold trade-offs. A single favorable score is insufficient.
- For binary risk, report prevalence, precision-recall performance, recall and precision at a validation-selected threshold, false positives/false negatives, alert volume and calibration when risk probabilities are shown. Report how many students receive warnings and the lead time before the outcome or relevant support deadline; disclose unmeasurable lead time. Compare justified early cutoffs using equivalent eligibility rules, showing coverage and sample counts. Select thresholds using a stated support-capacity or error-cost assumption and disclose uncertainty; do not optimize on test outcomes.
- Explain practical consequences and limitations. Predictive importance or explanations do not establish causality.

For supported nonpredictive questions within the project, use appropriate descriptive, diagnostic or inferential methods. Clearly distinguish candidate early signals from validated warnings. Do not invent labels or force classification metrics onto contextual data.

## 5. Deliver findings, not just files

For a substantial analysis, deliver:

1. **An evidence-backed report:** lead with the supported answers and scope. Explain questions, key findings, follow-up results, magnitude, uncertainty, interpretation and implications where relevant. Include methods, preparation and limitations without letting them dominate the findings.
2. **Purposeful visual analysis:** use suitable comparisons, distributions or trajectories with clear captions, units, denominators, populations, periods and sources. Choose the number of figures by analytical need, not a quota.
3. **A usable local dashboard:** organize it around the actual questions and findings. Provide meaningful views and interactions; generic cards and one bar chart are not sufficient when the investigation needs richer explanation. Respect any alternative format I request.
4. **Reproducible code and supporting results:** scripts or notebooks, dependency/setup instructions, seeds and split definitions where applicable, variable definitions, preparation decisions, saved result tables and figures.
5. **Verification evidence and opening instructions:** record what was checked, observed results, unresolved gaps and exact commands to reproduce and inspect the work.

Make the report explicitly answer what assessment behaviors were studied, which future risk they relate to, when they become observable, whether they improve warning quality, and what lead time and review workload the evidence supports. If a question is blocked, state that beside the answer. Include a compact feature/target timing table with source fields, formulas, availability assumptions and cutoff rules.

For direct early-warning studies, organize dashboard views around risk prevalence and eligible coverage, assessment-behavior comparisons and trajectories, warning performance by cutoff, threshold trade-offs, alert volume, lead time and error/subgroup analysis where supported. Label observed outcomes, retrospective model estimates and proposed support actions distinctly. Explain alert drivers as associations and show uncertainty or data gaps. If only feasibility or contextual evidence is available, make that limitation prominent and show relevant evidence gaps instead of simulated risk scores. Avoid exposing identifiable student records in shared outputs.

Make each major finding traceable through **question → population/comparison → method → numerical evidence → uncertainty/limits → interpretation → relevant implication**. Use natural prose and visuals rather than repeating rigid headings. Separate facts, hypotheses and recommendations; recommendations are optional when the task only asks for description.

Use existing tooling or portable HTML when appropriate. Inspect rendering, readability, relevant filters and empty/missing states; reconcile displayed values with saved results. Save actual inspection evidence and clearly identify unperformed checks. Do not add hosting or unrelated infrastructure.

Protect sensitive data and avoid unsupported judgments about individuals. A local analytical deliverable does not authorize external messages or real-world interventions.

Any suggested outreach or support is a proposal for educator review. Do not claim that alerts prevent failure or that an intervention works without observed intervention evidence. Mark future intervention evaluation `PENDING`, or `NOT APPLICABLE` when no intervention exists.

## 6. Review analytical quality before stopping

Follow lifecycle gates while working and preserve concise evidence of decisions and corrections. Do not claim compliance merely because reports contain lifecycle terminology.

For substantial work, apply the skill rubric separately to technical correctness, analytical completeness and communication. Every material applicable criterion must be at least adequate (2), with no unresolved critical failure, before declaring the scoped analysis complete.

Check source preservation, keys, joins, exclusions, denominators, transformations, statistical assumptions, relevant leakage/split rules, important calculations, visual encodings and question coverage. Independently recompute critical findings where practical.

Review alignment with the project purpose explicitly: assessment behavior is central; academic risk has a defensible future outcome definition; every feature is available by its cutoff; enrollment eligibility and outcome follow-up are valid; baselines test behavior's added value; warning timing and review burden are assessed; and feasibility/contextual work is not presented as validated early warning. An unresolved timing/leakage failure prevents a validated early-warning claim even if predictive scores are high.

Record each material check's quantity, population, unit, expected condition, executed method, observed evidence, status and consequence. A related quantity cannot verify the quantity actually being tested. Passing code tests, file-existence checks or dashboard interactions alone does not establish analytical depth.

Correct fixable gaps before delivery. Otherwise report the precise blocker and classify the work as **complete analysis**, **partial analysis**, **feasibility assessment** or **unverified work**, with its scope. Missing evidence is not NOT APPLICABLE. Future feedback or intervention outcomes are not observed results.

Finish with links to the report/dashboard, the most important findings, reproduction/opening instructions, executed checks and remaining gaps. Execute the supported investigation; do not stop at a plan, inventory or dashboard shell.
