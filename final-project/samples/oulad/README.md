# OULAD: assessment behavior and early academic risk

Start with [the rendered report](report.html) and [the interactive local dashboard](dashboard/index.html). Open either file directly in a browser; both work offline. [REPORT.md](REPORT.md) is the editable source-format report. This is a static local snapshot, with no hosting or automatic refresh.

The study executes `../../prompts/generic-prompt.md` for OULAD. Status: **complete retrospective analysis within its declared first-attempt scope**. Live warning validity is conditional on unobserved submission/score/label availability, and failure-event lead time cannot be measured. Stakeholder acceptance is pending. No intervention was implemented.

Useful findings: missing due records are strongly associated with later Fail/Withdrawn within modules; behavior-only can outperform combined early signals after cohort shift; a review threshold leaves substantial risk unflagged and poorly calibrated high probabilities. Read the report for exact populations, magnitude, uncertainty and limits.

## Reproduce

Run from `the-science-of-data-analyst-course/final-project/`:

```bash
python3 -m venv /tmp/oulad-study-env
/tmp/oulad-study-env/bin/pip install -r samples/oulad/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/oulad-study-env/bin/python samples/oulad/code/analyze.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/oulad-study-env/bin/python samples/oulad/code/followup.py
/tmp/oulad-study-env/bin/python samples/oulad/code/supplement.py
/tmp/oulad-study-env/bin/python samples/oulad/code/build.py
/tmp/oulad-study-env/bin/playwright install chromium
/tmp/oulad-study-env/bin/python samples/oulad/code/browser_review.py
```

The existing execution used `/tmp/oulad-venv/`; exact installed versions are recorded in `evidence/environment.txt` (usable as a pinned requirements file for this environment). A machine lacking Chromium system libraries may need Playwright's documented `install --with-deps chromium` setup. Analysis uses only local CSVs and does not download another dataset. Browser installation is for verification only; dashboard viewing needs no Python dependencies.

Required files under `datasets/oulad/`: `courses.csv`, `assessments.csv`, `studentInfo.csv`, `studentRegistration.csv`, `studentAssessment.csv`. Hashes, sizes and exact row counts are in `results/source_manifest.csv`. VLE logs and the source archive are untouched and not needed for this assessment-focused study. Source attribution: Jakub Kuzilek, Martin Hlosta and Zdenek Zdrahal; OULAD, [UCI DOI 10.24432/C5KK69](https://doi.org/10.24432/C5KK69), CC BY 4.0. Verified metadata access: 13 October 2026; local original acquisition date is not inferred.

## Files and evidence

- `BRIEF.md`: prioritized questions, proposed definitions, pre-evaluation design and acceptance conditions.
- `code/analyze.py`: source checks, preparation, feature timing, grouped temporal evaluation, baselines, uncertainty and sensitivities.
- `code/followup.py`: executed investigation of the validation-to-test reversal, including paired behavior/combined AP and module/feature/schedule comparisons.
- `code/supplement.py`: full-cohort behavior tables and independent raw-record recalculation of primary test opportunity denominators/missing fractions.
- `code/build.py`: finding-led report, dashboard and static PNG figures from saved aggregate results.
- `code/browser_review.py`: Chromium interaction/display checks, local links, mobile overflow and source hash preservation.
- `prepared/`: regenerated enrollment-level features and test predictions. Contains anonymized student identifiers, stays local and is ignored by Git. No individual records appear in the dashboard.
- `results/`: aggregate analytical evidence and ledgers; all rates use eligible enrollment denominators, with undefined values retained as blank/“—”. See the report's timing table for definitions.
- `figures/`: exportable figures, generated using Matplotlib.
- `evidence/`: executed logs, dependency versions, screenshots and browser check records.
- `QUALITY_REVIEW.md`: evidence-backed criterion review, question-to-interface map, observed reviewer tasks and remaining gaps.
- `PROCESS.md`: gate decisions, corrective work, scope and stopping rationale.

Re-running writes study outputs, never source CSVs. All model fits use seed 20261013; historical train/validation student groups are fixed across cutoffs; thresholds use validation only; primary test excludes all students in 2013J. Prior holdout reuse outside this run is unknown. Read the report before interpreting scores as live probabilities or remaining course duration as time before failure.

A final event-time audit excluded one historical withdrawal outside scheduled follow-up. [Correction and before/after results](TIMING_CORRECTION.md); the approved baseline is preserved in evidence/approved-baseline-before-timing-audit.zip. Raw records are unchanged.
