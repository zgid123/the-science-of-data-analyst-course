## 7.1. Before-and-After Checks

Preparation changes no outcome and no count without an explicit rule. Table 7.1 shows each comparison that the brief
asks for, with the value in the raw data, the value in the prepared data and the result.

**Table 7.1. Before-and-after checks**

| Check | Before (raw) | After (prepared) | Status |
| :---- | :---- | :---- | :---- |
| Enrolments, students, outcome mix (V01) | 32,593 enrolments; 28,785 students; 12,361 Pass, 10,156 Withdrawn, 7,052 Fail, 3,024 Distinction | Identical; no row dropped | PASS |
| Populations (V01, C09) | 32,593 enrolments | 28,061 at day 14; 28,069 at day 13; 27,535 at day 27, equal to the profile | PASS |
| Non-completion in the feature views (V01) | 12,708 at day 13; 12,156 at day 27 in the profile | Identical | PASS |
| Clicks (V04) | 39,605,099 | 39,506,354 kept plus 98,745 after withdrawal; weekly view sums to the same total | PASS |
| Missing values (V02) | imd_band 1,111; registration day 45; score 173 | Identical, not imputed | PASS |
| Keys (V03) | Unique in the six keyed tables | Unique in every prepared view | PASS |
| Categories and ranges (V05, V07) | Score 0–100; credits 30–655 | Same ranges; every label in its expected set | PASS |
| Time order (V08) | Activity after withdrawal present | No week counted after the withdrawal week | PASS |
| Joins (V09, V10) | – | 25 joins, rows in equal rows out; 3,554 enrolments without a click row kept with zero | PASS |
| Derived features (V11) | – | 6 features (clicks before and after day 0, active days, resources, missed and late tasks) recomputed from raw by separate code for all 55,604 feature rows: 0 differences | PASS |
| Leakage (V13) | – | A recount of the click features without the date filter changes them only for the 26,755 (day 13) and 25,663 (day 27) enrolments that clicked after the cut-off, so the filter works; no target-derived column in a view | PASS |
| Fitted transforms (V12) | – | Parameters identical with test rows altered | PASS |
| Documentation and split (V14, V15) | – | Every column documented with a role; 9 training and 13 test runs, none in both | PASS |

The number of enrolments without a click rises from 3,365 to 3,554 because the 189 students whose only clicks came
after they unregistered now show none, and the leakage check is built so that it would fail if any feature used a
later click. Beyond the recount of every feature row, nine unit tests on synthetic test enrolments confirm each formula,
and one row recounted by hand from the raw files matches the prepared view; Appendix VI explains these checks in full.
