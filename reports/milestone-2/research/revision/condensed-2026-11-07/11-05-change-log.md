## Appendix V – Controlled Change Log and Full Traceability

The Milestone 1 baseline was frozen before the search: Table A.8 lists the proposal files it was copied from, with their SHA-256, so any later edit to them is detectable. Table A.9 records every change to the baseline with its data evidence, in the format of the brief (section 3.1).

**Table A.8. Frozen Milestone 1 files**

| File | SHA-256 |
| :---- | :---- |
| 03-01-business-goal.md | 39cd541f2c1ce4c21df2e194cd857df03d09003ddfbeecbb7f7f05354d6ece34 |
| 03-02-smart-goal.md | 4402d67f291aff3a4c29fa776b45ffe4315c3408cdd621a2d15013b366bf78d0 |
| 03-03-kpis.md | 13c18d601d8aa87a8d89c8eb0f6a57dad67a40625edd445890a977f6968f9e29 |
| 04-01-four-level-questions.md | 404bcc2ae5cfae66d3866fa10ebd78b617146db7e5ecbcf70bb21eefbe9a34e2 |
| 05-00-analytic-approach.md | 67e8b7510dcb23675f5d79116ce6aa59d6b550b9d31208f788118bca72e1f584 |
| 06-01-data-requirements.md | a1022c224669eb4f81a460bf396573bb2738c4d503bc8c2dc68f3a03a784582f |
| 07-00-decision-value.md | 49ff783b35dbba1d3f6d7863fd349188b419193eefc3d3c7cd50de5bb6440945 |
| 09-00-traceability-matrix.md | da18b3430886d9be3332405c95442112e4326dc49c065dc61c936a5a5777a8a9 |

Table A.9 gives each change with the old and new content, the data evidence and its effect on the questions, KPIs and decisions.

**Table A.9. Controlled Change Log**

| ID | Old content (Milestone 1) | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- |
| C01 | The program's online and blended courses at a Vietnamese university | OULAD module runs (UK Open University, distance learning, 2013–2014) as an open stand-in for the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses was found; OULAD is the only candidate passing the gates | All AQs answered on stand-in data; results describe OULAD and must be re-checked on the university's data before D1–D3 |
| C02 | Course and semester; weeks 1–5 of a 15-week semester | Module run (`code_presentation`), about nine months; days counted from day 0 of the run; week n = days 7(n−1) to 7n−1 | Dates in OULAD are days from the run start; runs last 234–269 days | Cut-offs become day 13 (week-3 list) and day 27 (week-5 list); the semester-length difference is a stated limit |
| C03 | Denominator: students enrolled after the add-drop period; withdrawal as in Circular 83/2026 | Enrolments still registered at day 14 (registration closes two weeks after the start); leave and transfer cannot be told apart | `date_registration`, `date_unregistration` exist; no status field for leave or transfer | Primary KPI computed as a proxy on 28,119 enrolments; deviation from the Circular 83 rule recorded |
| C04 | Comparisons by delivery mode and year of study; AQ4 limit on first-year against later-year recall | Comparisons by module and run; the fairness limit is checked across IMD band and disability | No delivery-mode or year-of-study field; all modules are distance learning | AQ1–AQ3 narrowed; AQ4 limit re-expressed on available groups |
| C05 | AQ2 sign: attendance at in-class sessions (blended courses) | Dropped | No in-class sessions or attendance in OULAD | AQ2 uses missed and late tasks, activity and concurrent runs |
| C06 | AQ3 week-3 list from assessment and activity signs | Week-3 list (day-13 cut-off) from activity only; assessment signs start with the week-5 list | A non-exam task is due by day 13 in 1 of 22 runs, by day 27 in 16 | Secondary KPI 1 (early-sign rule) applies at the week-4 cut-off in 16 of 22 runs |
| C07 | AQ3 tested on a later semester of the same pilot courses | Train on 2013 runs, test on 2014 runs of the same module and start month (9 pairs); CCC, EEE-B and GGG-B only as later runs | B and J runs should be analysed separately; each module has at most two runs of one start month | Time-based validation feasible but with one earlier run per pair |
| C08 | AQ4 action and outcome; secondary KPI 2 and the contact part of secondary KPI 1 measured from a contact record | Kept as a future decision requirement; AQ4 limited to ranking under assumed capacity | No contact, capacity or intervention data in any candidate | No prescriptive or causal claim; secondary KPI 1 (contact part) and secondary KPI 2 measured only in the pilot |

Table A.10 is the full traceability matrix of deliverable B: every row serves the Business Goal of improving successful course completion by identifying students who stop taking part early enough to support them within the semester, and links its KPI, question, data requirement, files, actual variables, coverage and decision.

**Table A.10. Full traceability from goal to decision with coverage**

| Business Goal / SMART Goal / KPI | AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completion rate in pilot courses, assumed 70% → 75% by end 2027–2028 (primary KPI) | AQ1 | Descriptive | Outcome by course and time; first missed task | studentInfo, studentRegistration, assessments, studentAssessment | final_result, date_unregistration, assessments.date, date_submitted | Partial | D2, D3 |
| Primary KPI; secondary KPI 1, early-sign contact rate (sign part) | AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | + studentVle, vle | sum_click, studentVle.date, date_submitted | Partial | D2; reasons in D1 |
| Secondary KPI 1 (sign part) | AQ3 | Predictive | Target and features by the cut-off; later run for testing | as AQ2 | as AQ2 + num_of_prev_attempts, studied_credits, imd_band, disability | Partial | D1 |
| Secondary KPI 2, follow-up rate; secondary KPI 1 (contact part) | AQ4 | Prescriptive | Ranking within capacity; contact record | AQ3 outputs | none for contacts | Partial / None | D1 |
