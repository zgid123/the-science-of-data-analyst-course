# Notes: {title}

One working record for the whole analysis. The report says what is true now; everything about how the work got there (decisions, reruns, corrections, reviews) lives here.

## Brief

- **Purpose and reader.**
- **Questions, in priority order.**
- **Scope:** population, period, grain, units.
- **Deliverable.**

## Inherited project record

What an existing design, protocol, change log, earlier report or teammate's implementation already fixes. Adopt it as given; list every departure as a proposed change.

| Item (definition, population, threshold, capacity, numbering) | Source | Adopted as given? | If not: what was done, why, result both ways |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

## Lifecycle record

One row per stage, filled when the stage is done. A stage is done when its gate is met and the evidence is named; a stage the task does not need is marked NOT APPLICABLE with the reason.

| # | Stage | What was done | Evidence (file, step log) | Gate |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Business Understanding |  |  |  |
| 2 | Analytic Approach |  |  |  |
| 3 | Data Requirements |  |  |  |
| 4 | Data Collection |  | `data-manifest.json`, `logs/00_verify_inputs.md` |  |
| 5 | Data Understanding |  |  |  |
| 6 | Data Preparation |  |  |  |
| 7 | Modeling |  |  |  |
| 8 | Evaluation |  | check ledger below, `logs/99_check_report.md` |  |
| 9 | Deployment |  |  |  |
| 10 | Feedback |  |  |  |

## Stage records

Fill each table when its stage is done; delete a table only if the stage is NOT APPLICABLE.

**Stage 2 – analytic approach**

| Question | Analytics type and method | Comparison and baseline | Main threat and how it is tested |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

**Stage 3 – data requirements**

| Question | Data needed | Available? | Status (answerable / conditional / unsupported) |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

**Stage 4 – source inventory**

| Source | Format, rows | Coverage (population, period) | Access and sensitivity |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

**Stage 5 – field meanings and data quality**

| Field or quality dimension | What was checked | Finding | Consequence for the analysis |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

**Stage 6 – preparation log**

| Step | Rows or entities affected | Reason |
| :---- | :---- | :---- |
|  |  |  |

**Stage 7 – follow-ups**

| Observation | Why follow up | Result | How the interpretation changed |
| :---- | :---- | :---- | :---- |
|  |  |  |  |

**Stage 10 – feedback**

| Feedback received (from whom, when) or PENDING | What it changed |
| :---- | :---- |
|  |  |

## Decisions

| Decision | Reason | Decided before or after the results were seen |
| :---- | :---- | :---- |
|  |  |  |

## Check ledger

| Check (quantity, population) | Expected condition | Method / evidence | Coverage (tables, values) | Observed | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
|  |  |  |  |  |  |

## Independent review

Who reviewed (not the author of the code), what they were given, what they recomputed, each demonstrated defect and its correction. If there was none: "self-checked".

## Open issues
