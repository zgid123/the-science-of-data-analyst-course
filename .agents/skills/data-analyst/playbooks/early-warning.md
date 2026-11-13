# Playbook: early warning and risk scoring

Use when the goal is to flag entities (students, customers, accounts, patients, loans) **before** a bad outcome so someone can act: dropout, course failure, churn, default, readmission.

The question is never just "can we predict the outcome?" — a model scored on the whole period can look excellent and be useless. The question is: **how early, how well, for whom, and at what review workload?**

## Frame it (stages 1–3)

Pin these down in the brief. Each one changes the answer.

| Decision | Ask | Typical trap |
| --- | --- | --- |
| Unit | One row = student-course, customer-month, loan? | Mixing repeat enrollments with first attempts |
| Outcome | Exactly which event, recorded where? Keep distinct outcomes apart (fail vs withdraw; churn vs downgrade) unless the action is the same | Merging outcomes with different meanings and timing |
| Prediction time (cutoff) | When would the warning be issued? Use 2–3 cutoffs justified by the calendar (e.g., after the first assessment) | Using information from after the cutoff |
| Eligibility at cutoff | Who is still "at risk" at the cutoff? Remove those whose outcome already happened | Counting already-withdrawn students as correct predictions |
| Outcome window | How long after the cutoff do we observe? Is follow-up complete for everyone? | Censored entities treated as negatives |
| Action and capacity | Who acts, how many cases can they review (10%? 20%?), how much lead time do they need? Use the capacities the brief or project design names before any default | Reporting AUC with no workload translation; evaluating at shares nobody asked for |
| Baselines | What would a reader use without a model? Base rate, a single simple rule, prior-performance only | Comparing only against "no model" |

**A snapshot with no dates** (one row per entity, attributes and a final outcome, no event times) cannot support an early-warning claim: nothing says the attributes were recorded before the outcome. Say so, then do the two things the data does support and label them for what they are: (1) describe which attributes go with the outcome, like for like; (2) a _hindsight ranking_: a score fitted on part of the entities and tested once on a random holdout of the rest, compared with a random list and the best one-line rule at the same list size. Report it as how well these attributes separate the two groups in this file, not as how early or how well a warning would work.

If the data lacks a timed outcome, a cutoff-able behaviour record, or entity linkage, the early-warning question is unsupported. Say exactly which piece is missing, then pivot (see SKILL.md) to the best related analysis — for example, describing which early behaviours differ between later outcome groups in a dataset that has outcomes but no usable timing.

## Features (stage 6)

- Build every feature from records **available at the cutoff**. If you do not know when a value became visible (e.g., when a grade was released), assume a realistic delay and test it. For large activity logs (millions of click or event rows), call the Skill tool with `polars` to filter to the cutoff before aggregating.
- Separate **behaviour** (submissions, lateness, attendance, activity recency) from **performance** (scores) and **context** (course, demographics). This lets you answer "does behaviour add anything beyond scores?"
- Use opportunity-based denominators: "missed 1 of 2 assignments due by day 30", not "missed 1 assignment". An entity with nothing due has an _undefined_ rate, not zero.
- Distinguish not-yet-due, missed, no record, and unavailable score.
- Describing outcome rates by demographic group is a finding and belongs in the report; using the group as an input of the score is the part to avoid. Demographics are for fairness audit, not prediction, unless the user explicitly wants otherwise and the ethics are discussed.

## Analysis sequence (stage 7)

Run these in order; each is a finding candidate.

1. **Signal**: compare early behaviour between later outcome groups at each cutoff. Show rates with denominators (e.g., risk among students with vs without a missed assignment). Check the gap within segments (course, cohort) so composition does not create it.
2. **Simple rule**: how well does the single best rule do (e.g., "any missed assignment")? Readers can adopt a rule without a model.
3. **Models**: baseline-first. Context-only → behaviour → performance → combined, all logistic or similar, all evaluated on the **same** entities. Train on earlier cohorts, test on a later cohort (temporal holdout) whenever more than one cohort exists. Call the Skill tool with `scikit-learn` to build each model as a pipeline fitted on the training cohorts only.
4. **Timing**: how does quality change across cutoffs, and how much lead time remains before the outcome for flagged entities? For time until the outcome (such as days until withdrawal, with students still enrolled treated as censored), call the Skill tool with `scikit-survival`.
5. **Workload**: at the review capacities the brief or design names (otherwise 10/20/30%), how many are flagged, what share of flags are true (precision), what share of at-risk entities are caught (recall), how many are missed? Use `stats_helpers.capacity_table`.
6. **Who is missed**: precision, recall and flag rates by segment (course, cohort, demographic audit fields). Small groups are descriptive.
7. **Calibration**: if probabilities will be shown to people, do predicted risks match observed rates? Use `stats_helpers.calibration_table`.
8. **Order the work around the holdout**: choose features and model on the development part only; freeze; score the holdout once; only then describe the whole population, because a description of everyone reads holdout outcomes and would otherwise steer the model.
9. **Freeze, then test once**: before the first read of the later cohort's outcomes, record the chosen model, features, tuning values, capacities and success criteria (a timestamped freeze file or commit). Score the later cohort once and save the scores. Every later rerun, extra capacity, lead-time view or report fix reads the saved scores; it does not refit. A choice changed after the outcomes were seen is post hoc: report it beside the frozen result, never instead of it. If several people or implementations scored the same cohort, say how many looks it has had.
10. **Stress tests**: assumed release delays, alternative outcome definitions, the later-cohort shift. Report what changed.

## Metrics, in reader terms

| Metric | Say it as |
| --- | --- |
| Precision at capacity | "Of the students on the list, X in 10 were really at risk" |
| Recall at capacity | "The list caught X% of the students who later failed or withdrew" |
| Missed (false negatives) | "N at-risk students were not flagged" |
| Average precision (AP) | Ranking quality across all thresholds; compare with the base rate (no-skill AP = prevalence) |
| Calibration | "Students given a 90% risk actually ended at-risk 59% of the time" |

Lead with precision, recall and counts at a stated capacity. Use AP/AUC as supporting ranking measures, never alone.

## Charts that work

- Risk rate by early-behaviour status, small multiples by course or cohort.
- Precision and recall vs review capacity, one line per model.
- AP by cutoff, one line per feature set, base rate as a reference line.
- Lead-time distribution (days from warning to outcome) for flagged entities.
- Calibration: predicted vs observed risk by bin, with the diagonal.
- Recall by segment at the reference capacity (horizontal bars).

## Report shape

Summary: how early, how well at what workload, and the main gap ("At day 60, reviewing 20% of students catches 42% of those who later fail or withdraw; 6 in 10 flagged students are truly at risk; about 1,100 at-risk students are still missed"). Then findings: the strongest early signal → whether it holds within groups → how early warnings become useful → workload and who is missed → what would make it deployable.

## Traps checklist

- Outcome already occurred at the cutoff (leakage through eligibility).
- Features computed over the whole period, or scaled using test data.
- Random split across cohorts when a temporal split is possible.
- Threshold tuned on the test set, or a model swapped for one that did better on it.
- The test cohort rescored on every rerun instead of read from the frozen scores.
- Same entity in train and test (repeat enrollments).
- Reporting only accuracy on imbalanced outcomes.
- Treating missing activity as a confirmed outcome.
- Claiming that changing a behaviour will change the outcome (association only).
