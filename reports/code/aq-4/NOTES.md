# AQ4 – working notes

## Brief

- **Question (Level 1, Table 2.4).** Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability?
- **Level and task.** Prescriptive as decision support; ranking under capacity. The choice of contact and its effect are deferred to the pilot (Change Log C11).
- **Reader and decision.** Tutors: D1. They receive a ranked list with reasons and decide whom to contact.
- **Population.** The 13 test runs of 2014; lists of 3 or 5 per tutor group of 20, one per run.
- **Baselines.** Random list (expected recall k / n); rule-ranked list of the same length.
- **Primary approach.** Top-k per run from the frozen AQ3 scores, with reasons; risk tiers from capacity as the candidate form.
- **Success criterion (Table 4.4).** Gate S1 met by the list; confirmatory fairness check FR1 passes or its flags are reviewed; risk order = need order stated as untested; no statement about the effect of contact. **Result: S1 met; 0 of 3 groups flagged; age 55 or over not cleared.**
- **Status of the run.** Rerun of 12 November 2026: a reproduction of the first run of 11 November (commit `11f4aca`) with no AQ4 design choice changed (`../PROTOCOL.md` P03–P05, P14). The 2014 outcomes were known when the rerun started.

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| AQ4 fits nothing; it reads `../aq-3/extracted-datasets/aq3_test_scored_d*.csv` | Level 1: AQ4 reuses the AQ3 scores and adds only the capacity cut |
| Reasons = three largest positive contributions (coefficient × standardised value), module and start month excluded | Same equation that ranks; run-constant terms explain nothing within a run |
| Outcome columns of the contact list prefixed `EVALUATION_ONLY_` | A tutor's list would not hold them |
| Group recall summed over runs; bootstrap over runs then enrolments, 5,000 replicates; Holm over three groups | Level 1 Table A.8, made operational in `../PROTOCOL.md` P14 |
| Rule list audited beside the model list | Shows whether a gap comes from the model or from the signals |

## Methods checklist

- [x] Ranked lists, list flags at 3 and 5 per 20, tiers – `extracted-datasets/aq4_ranked_d27.csv`, `aq4_ranked_d13.csv`
- [x] Contact list with reasons – `extracted-datasets/aq4_contact_list_d27.csv`; reason frequency – `results/reason_frequency.csv`
- [x] Recall, attainable recall, normalised recall, precision, lift per run and pooled, against random and rule – `results/list_quality_by_run.csv`, `list_quality_pooled.csv`
- [x] Tiers – `results/tiers.csv`
- [x] Fail and Withdrawn on the list – `results/outcome_kind_on_list.csv`
- [x] Overlap with the rule list – `results/overlap_by_run.csv`
- [x] Students with no activity apart from active students – `results/active_vs_inactive.csv`
- [x] Confirmatory fairness check FR1 (three groups, Holm) and point gap for age 55 or over – `results/fairness_confirmatory.csv`
- [x] Selection rate, recall, precision by gender, disability, age band, deprivation band – `results/fairness_descriptive.csv`
- [x] Calibration by group – `results/fairness_calibration.csv`
- [x] ABROCA with shuffled-label reference – `results/fairness_abroca.csv`
- [x] Proxy check – `results/fairness_proxy.csv`
- [x] Figures – `figures/fig-aq4-1` to `fig-aq4-3`
- [ ] Per-tutor-group lists (OULAD has no tutor groups)
- [ ] Benefit ranking or uplift (rejected in Level 1: no contact data)
- [ ] Office scenario of 30 or 40 contacts per run (in the prepared capacity table; not part of the Level 1 cards)

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| List sizes | Places at 3 and 5 per 20 equal the capacity rule in every run, for model and rule lists | PASS (assert in `01_lists.py`) | `logs/01_lists.md` |
| Counts | Non-completers on the model and rule lists equal the S1 counts (2,870 and 2,786) | PASS | `../aq-3/logs/09_verify.md` (V3) |
| Reasons | Every listed student has at least one reason | PASS, 3,955 of 3,955 | `logs/01_lists.md` |
| Group sizes | Disability 1,488, band 0–10% 1,486, band missing 610, age 55 or over 118 test enrolments = Level 1 Table A.7 | PASS | `logs/03_fairness.md` |
| FR1 | Gap below −10 points and Holm-adjusted interval below 0 | No group meets both; 0 of 3 flagged | `results/fairness_confirmatory.csv` |
| Reproduction | Every AQ4 result table equals the first run (commit `11f4aca`) | PASS: 13 of 13 byte-identical; 18 of 18 AQ4 headline numbers equal | `../logs/compare_first_run.md` |
| Comparison with the earlier team run | Earlier team run: gaps +5.4, +1.7, −8.1 points, none flagged; here +5.4, +1.2, −6.9, none flagged | Agree on the verdict | `../aq-3/results/crosscheck_earlier_run.csv` |

## Open issues

- **Prior education as a reason** for 14.5% of listed students: in the score by Level 1, but not actionable and marked sensitive. Recommendation in the report, Section 3; a decision for the team.
- **Gender gap in recall** of 4.7 points (descriptive; not a confirmatory group in Level 1). Recommendation: add gender to the pilot's audit groups.
- **Missing deprivation band:** not flagged, but the interval reaches −16.8 points; 181 non-completers cannot clear it.
