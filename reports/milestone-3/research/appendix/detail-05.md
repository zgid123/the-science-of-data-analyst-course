**Further decisions and reflection.**

The interpreter's suggestion on the OU policy of 2025 was also accepted in part: its reading of the 2025 policy gave a usable rule for
CMA marks, which appear within seven days, but its rule that a CMA cannot be submitted late does not hold in data
where 32,991 CMA submissions are late, so it was not applied.

**Reflection.** The reviews were most useful where the AI critic had to argue from the data rather than from general
advice: the duplicate test, the base-rate argument and the registration-day error each changed the pipeline, and each
was confirmed by a count before it was accepted.

**AI roles and verification.** The table below gives each of the seven roles, what AI did in it and how the result was
verified.

| Role (brief) | What AI did | How the result was verified |
| :---- | :---- | :---- |
| Data dictionary interpreter | Read the data descriptor, the OU's assessment policy and the IMD documentation | Each fact kept only with a verbatim quotation; the 2025 rule that a CMA cannot be late tested on the data and not applied |
| EDA and quality checklist partner | Proposed a test of whether duplicate click rows are copies | Test run on the data: 31.5% equal counts against 24.0% by chance |
| Code assistant | Drafted every script of the package | 13 figures equal to an independent recount; 9 unit tests; 6 features recomputed for every row without a difference; one row recounted by hand |
| Preparation critic | Reviewed the plan in isolation (12 critiques) and audited leakage (8 findings) | Each critique checked on the data or the code before a decision |
| Feature engineering ideator | Proposed recency, trend, a pre-start window, clicks by resource type and early submissions | Each feature computable from real fields before the cut-off; added as the extended set |
| Documentation assistant | Drafted the dictionary, lineage, package guide and transformation log | Generated from the code; V14 fails if a column lacks an entry |
| Synthetic-data assistant | Wrote small labelled test enrolments | Level A of the brief's policy only; never in a view or a finding |
