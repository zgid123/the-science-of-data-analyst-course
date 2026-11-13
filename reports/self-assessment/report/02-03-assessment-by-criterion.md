## Appendix III – Self-Assessment against the Grading Criteria

Each subsection below takes one milestone and assesses its submitted report against every grading criterion of its brief, with the rating of Table A.4 (met, mostly met, partly met, not applicable). The evidence column names where the work is found in that milestone's report, and the last column states the limitation that keeps a criterion from a full rating. Section, table and appendix numbers in both columns refer to that milestone's report, not to this document.

### 1. Milestone 1: requirement analysis and project proposal

The Milestone 1 brief grades the proposal on eight criteria, from stakeholder requirement gathering to the responsible use of generative AI. Table A.5 assesses each of them; the report's main text runs to about 19 pages in English and 21 in Vietnamese, against the brief's recommended 6–10.

**Table A.5. Self-assessment of Milestone 1 against its grading criteria**

| Criterion | Rating | Evidence in the Milestone 1 report | Limitation |
| :---- | :---- | :---- | :---- |
| Stakeholder requirement gathering | Mostly met | Five stakeholders (the brief asks for at least three), each interviewed with seven or eight open questions and follow-ups (Section 2.1, Table 2.1; Section 2.2; Appendices I and II). | Generative AI played both the stakeholders and the interviewer, as the brief's simulated-stakeholder setting allows; no real person was interviewed, so the requirements still need confirming with real university staff. |
| Synthesis and prioritisation | Met | Six requirement themes ranked by priority; three conflicts and one constraint resolved; a validation round in which every stakeholder confirmed, corrected and added requirements (Sections 2.3 and 2.4, Table 2.2; Appendix III). | – |
| Business Goal, SMART Goal and KPI | Met | A goal stated as an outcome, a SMART Goal that raises course completion from 70% to 75% by the end of the 2027–2028 academic year with its 70% baseline marked as an assumption about the scenario university, not a measured figure, and one primary and two secondary key performance indicators, each with its rationale (Sections 3.1–3.3). | – |
| Analytical Question Ladder | Met | Four analytical questions, one at each level from descriptive to prescriptive, each checked against the five criteria clear, specific, scoped, data-oriented and answerable, with two before-and-after refinements (Sections 4.1 and 4.2, Tables 4.1 and 4.2). | – |
| Analytics type and candidate technique family | Met | Analytics type, technique family, expected output and user for each question, with no algorithm named before the data are known (Section 5, Table 5.1). | – |
| Data requirements, feasibility, privacy and ethics | Met | Four data sources with granularity, timing and availability for each question, five data quality risks, and the Vietnamese personal data protection rules that apply (Sections 6.1 and 6.2, Table 6.1). | – |
| Decision supported and expected value | Met | Three decisions, each with the person who takes it, its level (from day-to-day operation to strategy) and whether it can be reversed (Section 7, Table 7.1). | – |
| Responsible GenAI use and proposal quality | Mostly met | Four roles given to generative AI, and twelve reviewer critiques, of which nine were accepted, two partly accepted and one rejected with its reason (Section 8, Table 8.1; Appendix IV); a traceability matrix links goal, questions and decisions (Section 9, Table 9.1). | The main text is about twice the recommended length. |

### 2. Milestone 2: data requirements, dataset search and collection

The Milestone 2 brief grades nine criteria, from the link with Milestone 1 to the verified use of generative AI, and asks for a Data Collection Package beside the report. Table A.6 assesses each criterion; the main text runs to about 19 pages in English and 21 in Vietnamese, against the recommended 6–10.

**Table A.6. Self-assessment of Milestone 2 against its grading criteria**

| Criterion | Rating | Evidence in the Milestone 2 report | Limitation |
| :---- | :---- | :---- | :---- |
| Link with Milestone 1, scope consistency and Change Log | Met | The Milestone 1 baseline restated, with eight recorded changes, each backed by data evidence; goal, SMART Goal and decisions unchanged (Sections 1.1 and 1.2, Table 1.1; Appendix V). | – |
| Data Requirement Specification for each question | Met | Unit, outcome, variables, time window and decision point for each question, and the must-have gates a dataset has to pass (Section 2.1, Table 2.1). | – |
| Data requirements by analytics level | Mostly met | The data gap of the prescriptive question declared before the search, and, for each planned contact list (day 13 and day 27 of the course), the prediction point and a leakage check (Sections 2.2 and 2.3). | The brief grades the table of data requirements by analytics level, but that table sits in Appendix VII and the main text carries only its summary. |
| Search strategy, at least three candidate datasets and Search Log | Met | Sixteen search-log entries (eleven searches and five further sources that those searches led to, rejected sources included), yielding seven candidate datasets (Section 3, Table 3.1; Appendix I). | – |
| Dataset evaluation and selection rationale | Met | Ten criteria scored from 0 to 2, with must-have gates deciding before the scores; the Open University Learning Analytics Dataset selected on condition that its files confirm three facts (the result values separate pass from fail, each module has enough runs for testing, and a student's identifier stays the same across runs), which the structural check then tested (Sections 4.1 and 4.2, Table 4.1; Appendix II). | – |
| Acquisition, provenance, licence, citation and reproducibility | Met | Published version with its DOI, the CC BY 4.0 licence, checksums of every file and a two-command rebuild in the Data Collection Package (Section 5, Table 5.1; Appendix III). | – |
| Structural verification, updated traceability and data gaps | Met | Seven tables checked, three differences between documentation and files recorded, and the coverage of each question rated, with the contact action of the prescriptive question marked as not covered, because the dataset records no contact (Sections 6, 7.1 and 7.2, Tables 6.1 and 7.1). | – |
| Ethics, representativeness, privacy and limitations | Met | A minimum group size of five for any reported figure, sensitive attributes used only to audit fairness, the 2013–2014 United Kingdom scope, and the claims the data cannot support (Section 8). | – |
| Verified and critical use of generative AI | Met | Four AI roles and two critic rounds, in which ten of twelve and all ten critiques were accepted and the rest partly accepted, each checked against the official dataset source (Section 9, Table 9.1; Appendix VI). | – |

### 3. Milestone 3: data understanding and preparation

The Milestone 3 brief grades ten criteria, from the link with earlier milestones to the AI Decision Log, and asks for a reproducible preparation pipeline. Table A.7 assesses each criterion; the main text runs to about 27 pages in English and 33 in Vietnamese, against the recommended 8–12.

**Table A.7. Self-assessment of Milestone 3 against its grading criteria**

| Criterion | Rating | Evidence in the Milestone 3 report | Limitation |
| :---- | :---- | :---- | :---- |
| Link with Milestones 1–2, scope consistency and Change Log | Mostly met | An entry check of six conditions carried over from Milestones 1–2, all passed, and five new recorded changes (Sections 1.1 and 1.2, Table 1.1; Appendix IV). | The test set kept all 13 runs of 2014 instead of the 9 runs with a matching module and start month in 2013 that the plan named; the change was not entered in the Change Log until Milestone 5. |
| Dataset understanding: population, unit, keys, target, time and semantics | Met | The enrolment as unit of analysis, keys checked across tables, the dataset's final-result field as the outcome, time counted from the course start, and six sensitive attributes named (Sections 2.1–2.3, Table 2.1). | – |
| Data profiling and data quality assessment with evidence | Met | All 10.9 million rows profiled on the brief's ten aspects, and nineteen quality issues logged, three of them high severity (Sections 3.1–3.5, Table 3.1; Appendix I). | – |
| Question–data fit and decisions on data gaps or synthetic data | Met | Three questions rated amber and one red, each with a decision, and synthetic data used only for unit tests (Sections 4.1 and 4.2, Tables 4.1 and 4.2). | – |
| Data Preparation Decision Matrix and rationale | Met | Twelve preparation needs, each with its decision, rationale and the validation check that proves it (Section 5, Table 5.1). | – |
| Reproducible preparation pipeline and data lineage | Met | Eight pipeline stages run by one command, a rerun identical byte for byte, and an 88-variable dictionary with lineage (Sections 6.1, 6.2 and 7.2, Table 7.2; Appendices II and III). | – |
| Leakage control, split strategy and predictive readiness | Met | Training on the nine course runs of 2013, testing on the thirteen of 2014, folds that leave one run out, and students enrolled in both years flagged (Section 6.3, Table 6.1). | – |
| Prepared data validation and analytics or model readiness | Met | Twenty-two validation checks passed, an independent recomputation of the six derived features on all 55,604 feature rows (one per enrolment and list date) with no difference, and a readiness matrix for the four analytics levels (Sections 7.1, 7.3 and 8, Tables 7.1 and 8.1). | – |
| Ethics, representativeness, sensitive attributes and limitations | Met | Sensitive attributes kept for audit only; the limits compared with a published fairness study of the same dataset and checked against the 2025 Vietnamese personal data protection law (Section 9). | – |
| Verified, critical use of generative AI and AI Decision Log | Met | Thirteen entries in the AI Decision Log; an AI critic of the preparation plan made twelve critiques (nine accepted, three partly accepted), and an AI leakage audit made eight findings, all reproduced and fixed (Section 10, Table 10.1; Appendix V). | – |

### 4. Milestone 4: modeling and evaluation proposal

The Milestone 4 brief grades Level 1, the proposal of methods and their evaluation, on seven criteria; Level 2, a prototype with results, is optional and not needed for the full 100 points. Table A.8 assesses the seven criteria; the brief sets no page range, and the main text runs to about 22 pages in English and 28 in Vietnamese.

**Table A.8. Self-assessment of Milestone 4 against its grading criteria**

| Criterion | Rating | Evidence in the Milestone 4 report | Limitation |
| :---- | :---- | :---- | :---- |
| Traceability from question to technical task | Met | An entry check of five conditions carried over from Milestone 3, one modeling brief for each question, and a traceability matrix from goal to decision (Sections 1.1, 1.2, 2 and 8, Tables 1.1, 1.2, 2.1 and 8.1). | – |
| Candidate solution families and baseline | Met | A baseline for every question and two candidate families for each modeling question, with no machine learning where descriptive statistics answer the question (Sections 3.1–3.4, Table 3.1). | – |
| Selection rationale | Met | Eight criteria covering, among others, question, data, assumptions, interpretability, complexity and actionability, with a sample-size check for the predictive model (Section 3.1; Appendix I). | – |
| Evaluation design | Met | A primary metric that measures the share of non-completing students a list finds when the list is as long as the number of students the support office can contact, success thresholds fixed before any test, folds that leave one run out, and a bootstrap interval with a paired test (Sections 4.1–4.4, Tables 4.1 and 4.2; Appendices II–IV). | – |
| Leakage, risk, ethics and fairness | Met | A fairness criterion tested formally on three student groups fixed in advance, sixteen risks with their controls, and the Vietnamese rules on high-risk AI (Section 5, Table 5.1; Appendix V). | – |
| Transparency and critical use of generative AI | Met | Twenty-four AI critiques, each with our decision and its evidence (Section 6, Table 6.1; Appendix VI). | – |
| Presentation and consistency | Mostly met | Terms, identifiers and versions are the same across tables and sections. | The main text runs to about 22 pages in English; the brief sets no page range, but this is longer than the 6–10 or 8–12 pages that the briefs of Milestones 1–3 recommend. |

### 5. Milestone 5: final integration and project report

The Milestone 5 brief grades the final report on eleven criteria, from the coherence of problem, goal and questions to presentation and references, and recommends a main text of 15–25 pages. Table A.9 assesses each criterion; the main text runs to about 25 pages in English and 32 in Vietnamese.

**Table A.9. Self-assessment of Milestone 5 against its grading criteria**

| Criterion | Rating | Evidence in the Milestone 5 report | Limitation |
| :---- | :---- | :---- | :---- |
| Coherence of problem, goal and analytical questions | Met | Business context, SMART Goal, indicators and the final four questions, with every change since Milestone 1 traced in a revision log and none dropped (Sections 1–3, Tables 2.1, 3.1 and 3.2). | – |
| Traceability from requirements to data | Met | Data requirements, the selection among seven candidates, the dataset version and the fit and status of each question (Sections 4 and 5, Tables 4.1, 4.2, 5.1 and 5.2). | – |
| Evidence of data understanding and preparation | Met | Nineteen quality issues with their decisions, twenty-two passed validation checks and an 88-variable dictionary (Sections 6 and 7, Tables 6.1, 6.2 and 7.1). | – |
| Modeling and analysis strategy, Level 1 | Met | Task, baseline, two candidate methods and the rationale for each question (Section 8, Table 8.1; Appendix VIII). | – |
| Evaluation design | Met | Metrics, success thresholds, folds that leave one run out and a single final test (Section 9, Table 9.1). | – |
| Experimental evidence, if any | Mostly met | The Level 2 prototype run for the predictive and prescriptive questions: models developed on the 9 runs of 2013 with folds that leave one run out, frozen with a hash of every model and tested once on the 13 runs of 2014; gate S1 met, with 41.5% of later non-completers on lists of 5 per 20 students against 40.3% for the early-sign rule; calibration and error analysis; the verdict against Level 1; and package steps that rerun every result, checked byte for byte (Section 10, Table 10.1; Appendix XIV, Table A.37). | The Milestone 4 plan named no tuning measure; our Milestone 4 draft package, an earlier implementation of the same test, tuned on recall at capacity, and log loss was chosen after that draft's 2014 test result was known. The report states when the choice was made and gives the draft's result beside it. Gate S1 is met under both measures, so only the calibration result depends on the choice. |
| Findings and educational decision support | Met | Of the 28,061 enrolments still registered on day 14 after the course start, 45.3% did not complete the course (95% interval 44.7–45.8%), five early signs that hold in both years, with students who missed a task showing a non-completion rate about 40 percentage points higher than students who missed none, the ranked lists of the single 2014 test with a reason for each name, and the decisions each finding supports, each answer stated at the level of evidence it reaches (Section 11, Table 11.3; Appendices XII–XIV, Figures A.2 and A.3). Day 14 defines the population of the completion indicator; the contact lists are drawn up on days 13 and 27. | – |
| Limitations and research integrity | Met | Data, model, generalisation and causal limits stated, keeping apart what was tested and showed no clear difference from what the data cannot test (Section 12, Table 12.1). | – |
| Traceability Matrix and report integration | Mostly met | A complete matrix with gaps marked, and a narrative written anew rather than joined from earlier reports (Section 11.1, Tables 11.1 and 11.2; Appendix XI). | The brief shows the matrix as one table of eleven columns; the report splits it over two tables for readability, so it departs from the form the brief shows. |
| Transparency of generative AI and human ownership | Met | AI roles, the verification rule and the reflection in the main text, with the full AI Decision Log in an appendix as the brief allows (Section 13; Appendix XVI). | – |
| Presentation and references | Mostly met | Numbered tables and figures with intervals, an APA reference list, and English and Vietnamese versions with the same structure. | The Vietnamese main text runs to about 32 pages, seven over the recommended maximum of 25. |
