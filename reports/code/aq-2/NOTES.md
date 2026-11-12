# AQ2 – working notes

## Brief

- **Question (Level 1, Table 2.2).** Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module?
- **Level and task.** Diagnostic; association within module run. No causal claim.
- **Reader and decision.** D2, and the reasons shown with each name on the D1 list.
- **Population.** Enrolments registered at day 27: 11,811 in the 9 runs of 2013 (estimation), 15,724 in the 13 runs of 2014 (replication, after the AQ3 test; Change Log C14).
- **Baseline.** Unadjusted rate difference per sign. **Primary approach.** Logistic regression with run fixed effects, adjustment for previous attempts and credits, sign × module terms; average risk differences over the support of each sign.
- **Success criterion (Table 4.2).** Adjusted risk difference ≥ 5 points, interval excluding 0, same direction in ≥ two-thirds of the modules where the sign is defined. **Result: 5 of 5 signs consistent, in 2013 and in 2014, on the criterion as written. With clicks as a continuous adjustment (post hoc) the low-activity sign fails in both years; the other four hold.**
- **Status of the run.** Rerun of 12 November 2026, made after the first run of 11 November (commit `11f4aca`) and the Milestone 5 report had been read. The 2013 and 2014 results were known when P16, P17, P21 and P22 were revised.

## Lifecycle record (data-analyst skill, stages 1–10)

| Stage | Record |
| :---- | :---- |
| 1 Business understanding | Brief above; the signs become the reasons on a tutor's list |
| 2 Analytic approach | Diagnostic: adjusted risk difference per sign against the unadjusted difference; alternative that could fool the reader: signs overlap, a module mix creates a gap, a yes/no cut hides a graded effect. Tested by mutual adjustment, sign × module terms, and binned residuals with a continuous-activity run |
| 3 Data requirements | Signs at day 27, outcome, run, previous attempts, credits: available. A late TMA needs a TMA due by day 27: 14 of 22 runs. Conditional for the task signs |
| 4 Data collection | `features_d27.parquet` and `assessment_due.parquet` (task calendar) of OULAD-N04-prepared-1.0, hash-checked |
| 5 Data understanding | Both CCC runs set only a CMA by day 27; EEE and GGG set no task; in the CCC runs 86% and 89% of students have a late CMA (`results/sign_calendar_2014.csv`) |
| 6 Data preparation | Binary signs and sensitivity variants; five activity levels; log(1 + clicks). No row dropped |
| 7 Modeling | Main model, model without interactions (odds ratios), nine variants, subgroups; three figures |
| 8 Evaluation | Ledger below; unit tests of the support rule on synthetic data; comparison with the first run and with the Milestone 5 report |
| 9 Deployment | `README.md` (finding-led report); tables written from the result tables by `../common/fill_report_tables.py` |
| 10 Feedback | Received: the owner's comparison with the Milestone 5 report (findings 1, 3, 4, 5). Acted on in this rerun. Decision on the low-activity sign: pending with the team |

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| Binary definitions of the five signs as in `../PROTOCOL.md` P16; low activity stays at half the run median | Level 1 names the signs; a risk difference needs a yes/no definition. The Milestone 5 report uses the run median, which is a sensitivity row here |
| A late TMA is defined in the runs with a TMA due by day 27; a missed task in the runs with a TMA or CMA due | The calendar decides where a sign can occur. CCC sets only a CMA by day 27 |
| A risk difference is averaged over the support of the sign only, and printed with that n | A row without a slope has a difference of exactly 0 and dilutes the average (finding 1) |
| One slope per sign and module where ≥ 20 students have and ≥ 20 lack the sign; smaller cells with both sides present share a pooled slope; a module with one side empty has no term | Avoids separation in small cells; no cell needed pooling in either year |
| Direction count reported both ways: point estimates (Level 1 wording) and only modules whose interval excludes 0 | A value indistinguishable from 0 is not agreement (finding 4) |
| Replication judged by the change between years with its interval | Overlap of two intervals is not a test of their difference |
| Residuals by five activity levels and by tenths of predicted risk added | The three-level check is cut at the sign's own threshold (finding 3) |
| Sensitivity run with log(1 + clicks on days 0–27), labelled post hoc | Added after the misfit was seen; cannot change the Level 1 verdict |
| Risk differences by the delta method with HC1 robust standard errors, not clustered | Every run of the modules is observed, not sampled (Level 1, Section 3.2) |

## What the rerun changed against the first run, and what it found

| Item | First run (commit `11f4aca`) | Rerun |
| :---- | :---- | :---- |
| Late TMA, 2014, adjusted | +16.2 (12.9 to 19.6), averaged over 12,585 rows, 3,521 of them CCC rows without a slope | +22.5 (17.9 to 27.2), n = 9,064. The first run's value is reproduced as 22.5 × 9,064 ÷ 12,585 (`results/late_tma_average_check.csv`) |
| Late TMA, 2014, unadjusted | +14.4, with CCC students in the comparison group | +17.3 (12.5 to 22.0), n = 9,064 |
| Late TMA, change between years | Reported as a fall of 5 points and as the sign that varies most between years | +0.9 points (−5.4 to +7.2): no change the data can show |
| Other signs, other years | – | Same adjusted values as the first run for the missed task, the three click signs and every 2013 estimate (`../logs/compare_first_run.md`) |
| The same error elsewhere | – | None found. Every sign, module and variant was checked in `results/sign_support_*.csv` (no module with a sign defined and one side empty) and `results/sign_calendar_*.csv`. The sensitivity and subgroup tables printed the row count of the whole table, not of the estimate; they now print n per estimate. The model without sign × module terms (odds ratios) had the same CCC rows in its late-TMA term; corrected by the same rule |
| Late TMA in AAA-2014J | Counted as one of "26 of 26 in the same direction" | +0.2 (−13.2 to +13.5), 53 students: no association in that run; named as such |
| Residual check | By run and three activity levels: 2 of 27 and 0 of 39 cells outside the band | The same, plus five activity levels (3 of 5 and 2 of 5 outside) and tenths of predicted risk (2 of 10 and 0 of 10) |
| Low activity with clicks as a continuous adjustment | Not run | +2.9 (−0.2 to +6.0) in 2013, +0.8 (−1.9 to +3.4) in 2014: criterion not met. At the median cut: +5.9 and +5.9, met in 2013, not met in 2014 (4 of 7 modules). The Milestone 5 report finds 5.8 and 5.9 with the same verdicts |

## Methods checklist

- [x] Extraction of the association table and the task calendar – `extracted-datasets/aq2_signs_d27_2013.csv`, `aq2_signs_d27_2014.csv`, `results/sign_calendar_*.csv`
- [x] Support of each sign by module – `results/sign_support_*.csv`
- [x] Unadjusted rate difference per sign with Newcombe interval, on the support – `results/associations_*.csv`
- [x] Adjusted risk difference per sign (run fixed effects, sign × module terms), with n – `results/associations_*.csv`
- [x] Module-specific risk differences with a flag for intervals including 0 – `results/associations_by_module_*.csv`
- [x] Verdict against the Level 1 criterion, both readings of the direction count – `results/associations_*.csv` (columns `verdict`, `verdict_strict`)
- [x] Odds ratios – `results/odds_ratios_*.csv`
- [x] Correlation among signs on rows where both are defined; non-completion by number of signs – `results/sign_correlation_*.csv`, `non_completion_by_sign_count_*.csv`
- [x] Binned residuals by run and three activity levels – `results/binned_residuals_by_run_*.csv`
- [x] Binned residuals by five activity levels and by tenths of predicted risk – `results/binned_residuals_activity5_*.csv`, `binned_residuals_decile_*.csv`
- [x] Sensitivity, with n and verdict per estimate: de-duplicated clicks, late CMAs, flagged enrolments, runs with a task due, two activity thresholds – `results/sensitivity_*.csv`
- [x] Post hoc sensitivity: continuous activity, at both low-activity cuts – `results/sensitivity_*.csv` (status `post hoc`)
- [x] Subgroups by gender, disability, deprivation band (description), with n – `results/subgroups_*.csv`
- [x] Replication on 2014 including CCC, with the change and its interval – `results/replication.csv`, `replication_by_module.csv`, `replication_sensitivity.csv`
- [x] Late-TMA average over the support against the diluted average – `results/late_tma_average_check.csv`
- [x] Figures, titles built from the result tables – `figures/fig-aq2-1-risk-differences.png`, `fig-aq2-2-replication.png`, `fig-aq2-3-residuals-by-activity.png`
- [ ] Mixed-effects model (Level 1 candidate 2, set aside: 6 modules are too few to estimate a between-module variance)
- [ ] Shallow tree as a supplement (Level 1 lists it as optional; not run)
- [ ] Concurrent-enrolment sign (Change Log C12: described for 2014 only; not part of the five signs)
- [ ] Activity as a dose-response curve (risk by activity decile within run) instead of one log term

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| Population | 11,811 enrolments, 5,245 non-completers (44.4%) in 2013 = Level 1 Table A.6; 15,724 in 2014 | PASS | `logs/01_extract_2013.md`, `logs/01_extract_2014.md` |
| Calendar | "A task is due by day 27" from the feature view equals the task table's calendar in every run; no sign occurs where it is not defined | PASS (asserts in `01_extract.py`) | `results/sign_calendar_2013.csv`, `sign_calendar_2014.csv` |
| Support | No row outside the support of a sign enters its average (assert in `aq2_model.py`); the unadjusted and adjusted differences use the same rows (assert in `02_associations.py`) | PASS, both years, all nine variants | `logs/02_associations_2013.md`, `logs/02_associations_2014.md` |
| Same error elsewhere | No module where a sign is defined by the calendar and one side is empty | PASS: 0 such modules in either year | `results/sign_support_2013.csv`, `sign_support_2014.csv` |
| Convergence | Maximum-likelihood fit converged: 37 coefficients (2013), 45 (2014) | PASS | `logs/02_associations_2013.md`, `logs/02_associations_2014.md` |
| Cell size | Every estimated sign × module cell has ≥ 20 students with and without the sign | PASS (no pooled cell in either year) | `results/sign_support_2013.csv`, `sign_support_2014.csv` |
| Fit (a) | Observed − predicted by run and three activity levels within two standard errors | 25 of 27 cells in 2013 (GGG-2013J none and low: ±10 points); 39 of 39 in 2014 | `results/binned_residuals_by_run_2013.csv`, `binned_residuals_by_run_2014.csv` |
| Fit (b) | The same by five activity levels | **Not met:** 3 of 5 levels outside in 2013, 2 of 5 in 2014. Reported as a limit of the yes/no activity signs | `results/binned_residuals_activity5_2013.csv`, `binned_residuals_activity5_2014.csv` |
| Fit (c) | The same by tenths of predicted risk | 8 of 10 within the band in 2013 (largest residual 3.3 points); 10 of 10 in 2014 | `results/binned_residuals_decile_2013.csv`, `binned_residuals_decile_2014.csv` |
| Order | 2014 outcomes read by the scripts only after the freeze of the rerun (2026-11-12T15:58:51Z; AQ2 2014 extraction 2026-11-12T16:00:22Z). Order only: the outcomes were known | PASS | `../aq-3/logs/test-access.md` |
| Replication | Verdict of each sign equal in both years; change between years with its interval | 5 of 5 verdicts equal; 5 of 5 change intervals include 0 | `logs/03_replication.md` |
| Late-TMA arithmetic | The first run's +16.2 equals the new estimate × 9,064 ÷ 12,585 | PASS: 0.2254 × 9,064 ÷ 12,585 = 0.1623 | `results/late_tma_average_check.csv` |
| Unit tests | Support rule with a sign absent from one module, pooled small cell, direction counts, residual band | PASS, 21 of 21 | `../logs/tests_aq2_model.md` |
| Reproduction | Estimates that the changes should not touch equal the first run: every 2013 estimate, and the missed-task and click signs of 2014 | PASS (`aq-2` rows of the headline table) | `../logs/compare_first_run.md`, `../logs/compare_first_run_headlines.csv` |
| Milestone 5 | Low activity at the median cut: +13.4 (2013), +14.6 (2014) in both analyses; with continuous clicks +5.9 and +5.9 here against 5.8 and 5.9 there, same verdicts | Agree | `reports/milestone-5/report/16-13-aq2-results.md` |
| Earlier team run | Missed task +40.8 (2013) and +39.3 (2014) there; +40.7 and +39.6 here | Agree within 0.4 points | `../../milestone-4/package/results/aq2_replication.csv` |

No step failed in the final pass. The late-TMA estimates of the Milestone 5 report (+20.2 and +20.3) differ from those here (+21.7 and +22.5) because the two models differ in their background terms; both give the same verdict.

## Open issues

- **The low-activity sign.** It meets the Level 1 criterion as written and adds nothing once the amount of activity is in the model. Whether the reasons on the D1 list should show the amount of activity instead is a decision for the team; it would need a Change Log entry.
- **No pre-start activity in 2014.** Meets the criterion on point estimates (7 of 7 modules) but only 4 of 7 module intervals exclude 0.
- **GGG-2013J.** The model overstates risk for low-activity students and understates it for students with no clicks by about 10 points.
- **The continuous-activity run is post hoc.** It was chosen after seeing the misfit in both years, so its result should be confirmed on other data.
