## 4.2. Data Gap Decisions and Synthetic Data

The brief separates a missing value, where a variable exists but some records lack it, from a missing variable,
which the dataset never collected and which must not be imputed or generated as if it were real [1]. Table 4.2
sorts the gaps of OULAD into these classes.

**Table 4.2. Missing values, recorded absences and missing variables**

| Class | Cases in OULAD | Handling |
| :---- | :---- | :---- |
| Missing value | imd_band, registration day, TMA score, withdrawal day of 93 Withdrawn | Category or indicator; no imputation in views |
| Recorded absence | No click or submission row; empty unregistration day | Zero counts; did not withdraw |
| Missing variable | Year of study, mode, attendance, leave, contacts, capacity, mark release day | Not imputed or simulated; questions narrowed or deferred |
| Missing target | None | Supervised target available |

No open dataset fills the missing variables, since none of the seven Milestone 2 candidates records contacts,
attendance or year of study, so the questions were narrowed and the contact part of AQ4 deferred, as the brief's order
of priority requires [1]. The only synthetic records are a few labelled test enrolments in the `tests/` folder of the Prepared Data Package that
check the feature formulas, the pipeline test data the brief allows [1]; they never enter a prepared view.
