## 7.1. Before-and-After Checks

Preparation changes no outcome and no count without an explicit rule, as Table 7.1 shows for each comparison the brief
asks for.

**Table 7.1. Before-and-after checks**

| Check | Before (raw) | After (prepared) | Status |
| :---- | :---- | :---- | :---- |
| Enrolments, students, outcome mix | 32,593; 28,785; four outcomes | identical; no row dropped | PASS |
| Populations (C09) | 32,593 enrolments | 28,061 at day 14; 28,069 at day 13; 27,535 at day 27 | PASS |
| Clicks | 39,605,099 | 39,506,354 kept + 98,745 after withdrawal | PASS |
| Missing values | 1,111 / 45 / 173 | identical, not imputed | PASS |
| Keys, ranges, time order | unique; score 0–100; credits 30–655 | unique in every view; same ranges; no week after withdrawal | PASS |
| Derived features | – | 6 features recomputed from raw for 55,604 rows: 0 differences | PASS |
| Leakage | – | features change only for the 26,755 (day 13) and 25,663 (day 27) enrolments that clicked after the cut-off | PASS |

Beyond the recount of every feature row, nine unit tests on synthetic fixtures confirm each formula, and one row
recounted by hand from the raw files, a TMA due on day 19 and submitted on day 24 with 168 clicks over 10 active days
by day 27, matches the prepared view.
