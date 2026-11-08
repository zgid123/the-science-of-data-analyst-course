## 4.1. Evaluation Design Cards

Each question has a card with the seven items of the brief: primary and secondary metrics, validation strategy,
baseline, error analysis, fairness or subgroup check and success criterion [1]. The metric follows the decision:
recall matters for cheap contacts and precision for costly ones [23], and when only a limited number of top-ranked
cases can be examined, performance among those cases is the practical measure [24]. Table 4.1 summarises five items of the four
cards; the full cards, with secondary metrics and error analysis, are in Appendix III (Tables A.8–A.11).

**Table 4.1. Evaluation Design Cards (summary)**

| Item | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- |
| Primary metric | Rates with 95% intervals | Risk difference within run, with interval | Normalised recall at capacity, day 27, 5 per 20 | Normalised recall at capacity |
| Validation | Two aggregation paths; known totals | 2013 runs; replication on 2014 after the AQ3 test | Leave-one-run-out on 2013; single test on 2014 | As AQ3 |
| Baseline | Pooled rate; second denominator | Unadjusted rate difference per sign | Rule-ranked list; background-only model; random list | Random and rule-ranked lists |
| Fairness / subgroup | Rates by group, descriptive | Associations by group, descriptive | Confirmatory recall check by group (Section 4.4) | Same, by deprivation band and disability |
| Success criterion | Paths agree; every rate with interval | At least 5 percentage points, interval excluding 0, same direction in two-thirds of modules | Single gate S1: pooled normalised recall above that of the rule-ranked list, interval above 0 (Section 4.3) | Gate S1 met by the list; confirmatory fairness check passed or reviewed (Section 4.4) |
