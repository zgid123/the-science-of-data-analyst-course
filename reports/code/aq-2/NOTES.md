# AQ2 – working notes

## Brief

- **Question (Level 1, Table 2.2).** Which signs recorded by the end of week 4 (missed and late tasks, inactivity,
  activity against the run's median) go with later non-completion, compared within each module?
- **Level and task.** Diagnostic; association within module run. No causal claim.
- **Reader and decision.** D2, and the reasons shown with each name on the D1 list.
- **Population.** Enrolments registered at day 27: 11,811 in the 9 runs of 2013 (estimation), 15,724 in the 13 runs of
  2014 (replication, after the AQ3 test; Change Log C14).
- **Baseline.** Unadjusted rate difference per sign. **Primary approach.** Logistic regression with run fixed
  effects, adjustment for previous attempts and credits, sign × module terms; average risk differences.
- **Success criterion (Table 4.2).** Adjusted risk difference ≥ 5 points, interval excluding 0, same direction in
  ≥ two-thirds of the modules where the sign is defined. **Result: 5 of 5 signs consistent, in 2013 and in 2014.**

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| Binary definitions of the five signs fixed in `../PROTOCOL.md` P16 before any result | Level 1 names the signs; a risk difference needs a yes/no definition |
| One model for all runs; task signs set to 0 and "not defined" in runs with no task due | Keeps one estimate per sign; task-sign estimates come only from the runs where the sign can occur |
| One slope per sign and module, estimated where ≥ 20 students have and ≥ 20 lack the sign | Avoids separation in small cells; none needed pooling in 2013 |
| Risk differences by the delta method with HC1 robust standard errors, not clustered | Every run of the modules is observed, not sampled (Level 1, Section 3.2) |
| Odds ratios from the model without sign × module terms | One readable odds ratio per sign beside the risk difference |
| 2014 run only after `aq-3/results/freeze.json` and the test | C14; enforced by `common/lib.py` |

## Methods checklist

- [x] Extraction of the association table – `extracted-datasets/aq2_signs_d27_2013.csv`, `aq2_signs_d27_2014.csv`
- [x] Unadjusted rate difference per sign with Newcombe interval – `results/associations_*.csv`
- [x] Adjusted risk difference per sign (run fixed effects, sign × module terms) – `results/associations_*.csv`
- [x] Module-specific risk differences – `results/associations_by_module_*.csv`
- [x] Verdict against the Level 1 criterion – `results/associations_*.csv` (column `verdict`)
- [x] Odds ratios – `results/odds_ratios_*.csv`
- [x] Correlation among signs; non-completion by number of signs – `results/sign_correlation_*.csv`, `non_completion_by_sign_count_*.csv`
- [x] Binned residuals by run and activity level – `results/binned_residuals_*.csv`
- [x] Sensitivity: de-duplicated clicks, late CMAs, flagged enrolments, runs with a task due, two activity thresholds – `results/sensitivity_*.csv`
- [x] Subgroups by gender, disability, deprivation band (description) – `results/subgroups_*.csv`
- [x] Replication on 2014 including CCC – `results/replication.csv`, `replication_by_module.csv`
- [x] Figures – `figures/fig-aq2-1-risk-differences.png`, `fig-aq2-2-replication.png`
- [ ] Mixed-effects model (Level 1 candidate 2, set aside: 6 modules are too few to estimate a between-module variance)
- [ ] Shallow tree as a supplement (Level 1 lists it as optional; not run)
- [ ] Concurrent-enrolment sign (Change Log C12: described for 2014 only; not part of the five signs)

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| Population | 11,811 enrolments, 5,245 non-completers (44.4%) in 2013 = Level 1 Table A.6 | PASS | `logs/01_extract_2013.md` |
| Convergence | Maximum-likelihood fit converged, 37 coefficients | PASS | `logs/02_associations_2013.md` |
| Cell size | Every estimated sign × module cell has ≥ 20 students with and without the sign | PASS (2013: no pooled cell) | `logs/02_associations_2013.md` |
| Fit | Observed − predicted by run and activity level within two standard errors | 25 of 27 cells in 2013 (GGG-2013J low and none: ±10 points); 39 of 39 in 2014 | `results/binned_residuals_*.csv` |
| Order | 2014 outcomes read only after the freeze | PASS: freeze 23:18:16, AQ2 2014 extraction 23:23:49 UTC | `../aq-3/logs/test-access.md` |
| Replication | Same direction in both years for every sign × module estimate | PASS, 26 of 26 | `logs/03_replication.md` |
| Cross-check | Earlier team run: missed task +40.8 (2013) and +39.3 (2014); this run +40.7 and +39.6 | Agree within 0.4 points | `../../milestone-4/package/results/aq2_replication.csv` |

The late-TMA estimate for 2014 differs between the two implementations (+16.2 here, +20.3 in the earlier run), which
use different sign and model specifications; both give the same verdict.

## Open issues

- GGG-2013J: the model overstates risk for low-activity students and understates it for students with no clicks by
  about 10 points; an activity sign with three levels would fit that run better.
- The signs are cuts of continuous behaviour; a dose-response view (risk by activity decile) would complement them.
