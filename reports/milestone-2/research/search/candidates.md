# Candidate Datasets (T06, brief Task 3)

Written on 2026-11-06 from the official pages and papers saved under `research/sources/`. Every fact is followed by its
claim ID (in `part3-claims.md`) and source ID (in `sources.md`); "not stated" means the pages read do not state it.
No dataset was downloaded. Gates are those of `requirements/data-requirements.md` section 5 (revised): G1 outcome
with pass, fail and withdrawal and a dated withdrawal; G2a dated assessed tasks (due dates) and dated submissions;
G2b dated learning-platform activity at day or week level; G3 at least three runs of the same courses ordered in
time with a later run for testing; G4 open licence, official documentation and verifiable provenance; G5 anonymised
or pseudonymised data with a persistent student identifier across tables and runs. Two nice-to-have checks are added
for each candidate: assessed tasks due in weeks 1–4, and enrolment start and end dates.

Search keywords were built from the requirements (AQ1–AQ3): student completion, dropout, withdrawal, LMS/VLE
interaction, assessment submission, clickstream, higher education, learning analytics, MOOC dropout. The queries and
the rejected hits are in `search-log-brief.md` and in `../search-log.md` (rows marked T06).

## Summary of gate results

| Candidate | G1 | G2a | G2b | G3 | G4 | G5 | Tasks due weeks 1–4 | Enrolment start/end dates |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | Met | Met | Met | Met (per module to confirm) | Met | Partly | Not stated (check in data) | Yes (relative days) |
| B. UCI 697 Dropout and Academic Success | Not met | Not met | Not met | Unclear | Met | Partly | No | Not stated |
| C. UCI 320 Student Performance | Not met | Not met | Not met | Not met | Met | Unclear | No | No |
| D. UCI 856 Higher Education Students Performance Evaluation | Not met | Not met | Not met | Not met | Met | Unclear | No | No |
| E. XuetangX MOOC dropout (MOOCData, incl. KDD Cup 2015) | Not met | Not met | Met | Unclear | Not met | Partly | Not stated | Course dates only |
| F. HarvardX Person-Course AY2013 | Not met | Not met | Not met | Not met | Partly | Partly | No | First and last event dates only |
| G. xAPI-Edu-Data (Students' Academic Performance) | Not met | Not met | Not met | Not met | Unclear | Unclear | No | No |

Only OULAD passes every must-have gate on the documented evidence; the others fail at least G1.

## A. Open University Learning Analytics Dataset (OULAD)

| Field | Fact |
| :---- | :---- |
| Provider / authors | Kuzilek, Hlosta and Zdrahal, Knowledge Media Institute, The Open University (UK); provider page by OU Analyse (C3-001, S300; C3-006, S002) |
| Official URL / DOI | https://research.stem.open.ac.uk/ouanalyse/dataset/ (S300); paper doi:10.1038/sdata.2017.171 (S002); UCI record doi:10.24432/C5KK69 (C3-018, S003) |
| License / terms | CC-BY 4.0 (C3-002, S300; C3-018, S003) |
| Version / release date | "Latest version" offered without a version number (C3-004, S300); UCI record donated 20 December 2015 (C3-018, S003) |
| Population and context | Distance-learning university, teaching delivered through the VLE (C3-006, S002); seven modules, 2013 and 2014 (C3-005, S002); modules chosen partly for a significant number of failing students (C3-015, S002) |
| Unit of analysis | Student–module–presentation, with a final result per enrolment (C3-007, S002) |
| Outcome / target | final_result per enrolment; unregistered students have the value Withdrawal (C3-008, S002). The full list of result values is not stated in the pages read |
| Within-semester timing | Assessment cut-off day (C3-009) and submission day (C3-010); daily VLE clicks per student and material (C3-011); all dates in days from presentation start (C3-012); all S002. A typical presentation lasts nine months (C3-017, S002) |
| Number of runs | 22 module-presentations (C3-005, S002), coded by year and start month (B February, J October), B and J to be analysed separately (C3-061, S002). Presentations per module: not stated in the text read (Table 1 is an image) |
| Size | 32,593 students; 10,655,280 daily click rows (C3-005, S002); 206 assessments (C3-065, S002) |
| File formats | CSV tables linked by identifiers (C3-003, S300) |
| Documentation | Data descriptor with table and column definitions (S002); provider page (S300) |
| Anonymisation | Anonymised (C3-001, S300); identifiers randomised and dates relative (C3-012, S002); k-anonymity k = 5 (C3-013, S002) |
| Sensitive attributes | IMD band, disability, among others (C3-014, S002) |
| Citation | Kuzilek, Hlosta & Zdrahal (2017), Scientific Data 4:170171 (S002) |
| Known limits | Unsubmitted assessments leave no row; final-exam results usually missing (C3-016, S002) |

Gates:
- G1 Met: final_result with Withdrawal per enrolment and a dated unregistration (C3-008, C3-063). Pass and fail values to be confirmed in the local data, since the pages read do not list them.
- G2a Met: assessment cut-off days and submission days, counted from the presentation start (C3-009, C3-010, C3-012).
- G2b Met: daily click counts per student (C3-011).
- G3 Met at dataset level: 22 presentations over 2013–2014 ordered by code (C3-005, C3-061); whether each module has three or more runs is not stated in the text read and must be checked in the data.
- G4 Met: CC-BY 4.0, provider page, peer-reviewed descriptor, DOI (C3-002, C3-018, S002).
- G5 Partly: anonymised, k = 5 (C3-013); id_student links all student tables (C3-062); the record of earlier attempts (C3-064) implies the same student across presentations, but persistence of the identifier across runs is not stated explicitly.
- Tasks due in weeks 1–4: not stated; the cut-off days exist (C3-009) and must be checked in the data.
- Enrolment start/end dates: yes, registration and unregistration days relative to the start (C3-063).

## B. Predict Students' Dropout and Academic Success (UCI id 697)

| Field | Fact |
| :---- | :---- |
| Provider / authors | Realinho, Vieira Martins, Machado and Baptista, Polytechnic Institute of Portalegre, Portugal (C3-024, S301; S302) |
| Official URL / DOI | https://archive.ics.uci.edu/dataset/697 ; doi:10.24432/C5MC89 (C3-024, S301); descriptor doi:10.3390/data7110146 (S302) |
| License / terms | CC BY 4.0 (C3-024, S301) |
| Version / release date | Donated 12 December 2021 (S301); version number not stated |
| Population and context | One higher education institution, students of several undergraduate degrees (C3-019, S301), enrolled 2008/2009–2018/2019 (C3-026, S302) |
| Unit of analysis | One student (C3-022, S301) |
| Outcome / target | Dropout, enrolled or graduate at the end of the normal degree duration of 3–4 years (C3-021, S301; C3-028, S302); 32% dropouts (C3-029, S302). No course-level pass, fail or withdrawal |
| Within-semester timing | None: semester-level aggregates of curricular units at the end of semesters 1 and 2 (C3-020, S301; C3-030, S302) |
| Number of runs | Eleven entry cohorts (C3-026, S302); a cohort field is not documented in the text read |
| Size | 4,424 records (C3-060, S301; C3-027, S302) |
| File formats | One UTF-8 CSV, 520.7 KB (C3-023, S301; C3-027, S302) |
| Documentation | UCI variable table and peer-reviewed data descriptor (S301, S302) |
| Anonymisation | Anonymised under GDPR, validated by the institution's DPO (C3-031, S302); preprocessed for anomalies and missing values (C3-025, S301) |
| Sensitive attributes | Nationality, marital status, parents' qualifications, socio-economic factors (S301 comprehension; C3-020) |
| Citation | Realinho et al. (2021) [Dataset], UCI, doi:10.24432/C5MC89 (C3-024, S301) |

Gates: G1 Not met (degree-level three-class label, no withdrawal date; C3-021, C3-028). G2a Not met and G2b Not met (aggregates only; C3-030). G3 Unclear (cohorts 2008/09–2018/19 exist, C3-026, but no documented cohort field to order them). G4 Met (C3-024, S302). G5 Partly (anonymised, C3-031; single table, no identifier across tables or runs). Tasks due in weeks 1–4: no. Enrolment start/end dates: not stated.

## C. Student Performance (UCI id 320)

| Field | Fact |
| :---- | :---- |
| Provider / authors | P. Cortez (introductory paper with A. M. G. Silva, 2008) (C3-037, S303) |
| Official URL / DOI | https://archive.ics.uci.edu/dataset/320 ; doi:10.24432/C5TG7T (C3-037, S303) |
| License / terms | CC BY 4.0 (C3-037, S303) |
| Version / release date | Donated 26 November 2014 (S303); version not stated |
| Population and context | Secondary education, two Portuguese schools; school reports and questionnaires (C3-032, S303); collection years not stated |
| Unit of analysis | One student in one subject (Mathematics or Portuguese) (C3-033, S303) |
| Outcome / target | Final grade G3 from 0 to 20; no withdrawal category (C3-034, S303) |
| Within-semester timing | Three period grades only, no dates (C3-035, S303) |
| Number of runs | One school year implied; not stated |
| Size | 649 instances listed (C3-059, S303) |
| File formats | One 20 KB zip with two tables (C3-038, C3-033, S303) |
| Documentation | Variable list on the UCI page (S303) |
| Anonymisation | Not stated |
| Sensitive attributes | Alcohol consumption, health, family status (C3-036, S303) |
| Citation | Cortez (2008) [Dataset], UCI, doi:10.24432/C5TG7T (C3-037, S303) |

Gates: G1 Not met (grade only; C3-034). G2a Not met, G2b Not met (C3-035). G3 Not met (no runs documented). G4 Met (C3-037). G5 Unclear (no anonymisation statement; no student identifier listed). Tasks due in weeks 1–4: no. Enrolment dates: no. Population is secondary school, outside the project's higher-education scope.

## D. Higher Education Students Performance Evaluation (UCI id 856)

| Field | Fact |
| :---- | :---- |
| Provider / authors | N. Yilmaz and B. Şekeroğlu (C3-043, S304); institution not named on the page (accommodation question refers to Cyprus, S304) |
| Official URL / DOI | https://archive.ics.uci.edu/dataset/856 ; doi:10.24432/C51G82 (C3-043, S304) |
| License / terms | CC BY 4.0 (C3-043, S304) |
| Version / release date | Donated 14 August 2023 (S304); version not stated |
| Population and context | Engineering and educational sciences students, collected in 2019 (C3-039, S304) |
| Unit of analysis | One student's questionnaire with a course ID (S304) |
| Outcome / target | Letter grade from Fail to AA; no withdrawal (C3-041, S304) |
| Within-semester timing | None (questionnaire; C3-040, S304) |
| Number of runs | One collection in 2019 (C3-039) |
| Size | 145 instances (C3-058, S304) |
| File formats | One 10.8 KB CSV (C3-043, S304) |
| Documentation | Question list on the UCI page (S304) |
| Anonymisation | Not stated |
| Sensitive attributes | Income, partner, parental status (C3-042, S304) |
| Citation | Yilmaz & Şekeroğlu (2019) [Dataset], UCI, doi:10.24432/C51G82 (C3-043, S304) |

Gates: G1 Not met (C3-041). G2a Not met, G2b Not met (C3-040). G3 Not met (single 2019 collection, C3-039). G4 Met (C3-043). G5 Unclear (no anonymisation statement). Tasks due in weeks 1–4: no. Enrolment dates: no.

## E. XuetangX MOOC dropout data (MOOCData, Tsinghua University; includes KDD Cup 2015)

| Field | Fact |
| :---- | :---- |
| Provider / authors | Tsinghua University MOOCData site; data of Feng, Tang, Liu et al., AAAI 2019 (C3-044, S305; C3-051, S306) |
| Official URL / DOI | http://moocdata.cn/data/user-activity (S305); paper doi:10.1609/aaai.v33i01.3301517 (S306) |
| License / terms | Not stated on the provider page (S305) |
| Version / release date | Not stated |
| Population and context | Users of XuetangX, one of the largest Chinese MOOC platforms (C3-051, S306); activity August 2015 – August 2017 (C3-045, S305) |
| Unit of analysis | User–course enrolment (C3-046, S305) |
| Outcome / target | Binary dropout / non-dropout label; no pass or fail (C3-047, S305); dropout definition not stated in the text read |
| Within-semester timing | Timestamped actions per enrolment and session (C3-046, S305); course start and end dates (C3-048, S305) |
| Number of runs | Two years of logs (C3-045); repeated runs of the same course not stated |
| Size | Dropout prediction set 299 MB; tracking logs about 1.6 GB; KDD Cup 2015 data 158 MB (S305) |
| File formats | JSON tracking logs; CSV prediction files (S305) |
| Documentation | Column list on the provider page; paper abstract only (full text blocked) (S305, S306) |
| Anonymisation | Not stated |
| Sensitive attributes | Gender, birth year, education level (C3-049, S305) |
| Citation | Feng et al. (2019), AAAI 33, 517–524 (S306) |
| Related | The page also redistributes the full KDD Cup 2015 data (C3-050, S305); the KDD Cup site itself was reported offline in the search results (search-log row 6) |

Gates: G1 Not met (binary dropout, no pass/fail, no withdrawal date; C3-047). G2a Not met (no assessment due dates documented). G2b Met (timestamped actions; C3-046). G3 Unclear (two years of logs, C3-045, but runs of the same course not documented). G4 Not met (no licence or terms stated; S305). G5 Partly (user ID shared by logs, profiles and enrolments, C3-046, C3-049; anonymisation not stated). Tasks due in weeks 1–4: not stated. Enrolment dates: course start and end only (C3-048).

## F. HarvardX Person-Course Academic Year 2013 De-Identified dataset

| Field | Fact |
| :---- | :---- |
| Provider / authors | HarvardX, deposited in Harvard Dataverse (S307) |
| Official URL / DOI | doi:10.7910/DVN/26147 (S307) |
| License / terms | No named licence; Dataverse Community Norms, no re-identification (C3-055, S307) |
| Version / release date | Version 3.0 created 12 November 2019, with MD5 checksum (C3-054, S307) |
| Population and context | HarvardX courses on edX, Fall 2012 – Summer 2013 (C3-052, S307) |
| Unit of analysis | One individual's activity in one course, aggregated (C3-053, S307) |
| Outcome / target | Certified flag and grade (variable list, S307); no fail or withdrawal category |
| Within-semester timing | First and last event dates and aggregate counts only (C3-056, S307) |
| Number of runs | One academic year (C3-052) |
| Size | 338,223 records per the DDI statistics (S307 comprehension; not a stated sentence) |
| File formats | Tab-separated file plus PDF documentation (S307) |
| Documentation | Variable and de-identification documentation PDFs (C3-057, S307) |
| Anonymisation | De-identified; process documented (C3-052, C3-057, S307) |
| Sensitive attributes | Country, education level, year of birth, gender (S307 variable list) |
| Citation | HarvardX (2014), Harvard Dataverse, V11, doi:10.7910/DVN/26147 (S307) |

Gates: G1 Not met (certification only). G2a Not met. G2b Not met (aggregates; C3-053, C3-056). G3 Not met (one year; C3-052). G4 Partly (DOI and documentation, but no open licence; C3-055). G5 Partly (de-identified user ID across courses, C3-052; linkage to other data forbidden, C3-055). Tasks due in weeks 1–4: no. Enrolment dates: first and last event dates only (C3-056).

## G. Students' Academic Performance Dataset (xAPI-Edu-Data)

| Field | Fact |
| :---- | :---- |
| Provider / authors | Amrieh, Hamtini and Aljarah, The University of Jordan (C3-070, S309) |
| Official URL / DOI | https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data, listed by co-author I. Aljarah (S309); the group's own page refused connections (S308, error); no DOI found |
| License / terms | CC BY-SA 4.0 on the Kaggle listing (C3-070, S309) |
| Version / release date | Listing date 8 November 2016 (C3-067, S309); version not stated |
| Population and context | Users of the Kalboard 360 learning management system (C3-066, S309); students from several countries, 179 from Kuwait and 172 from Jordan (C3-068, S309); education level not stated in the text read |
| Unit of analysis | One student record (C3-067, S309) |
| Outcome / target | Grade band Low (0–69), Middle (70–89), High (90–100); no withdrawal (C3-069, S309) |
| Within-semester timing | Not stated in the text read; no dated records documented |
| Number of runs | Two semesters, 245 and 235 records (C3-068, S309) |
| Size | 480 records, 16 attributes (C3-067, S309) |
| File formats | One CSV (S309 listing) |
| Documentation | Attribute list in the Kaggle description; two papers by the authors (2015, 2016) not read (S309) |
| Anonymisation | Not stated |
| Sensitive attributes | Nationality and origin (C3-068, S309) |
| Citation | Amrieh, Hamtini & Aljarah (2016), International Journal of Database Theory and Application (S309) |

Gates: G1 Not met (grade band only; C3-069). G2a Not met, G2b Not met (no dated records documented). G3 Not met (two semesters; C3-068). G4 Unclear (CC BY-SA 4.0 stated, C3-070, but provenance rests on a Kaggle listing; the provider page could not be reached). G5 Unclear (no anonymisation statement). Tasks due in weeks 1–4: no. Enrolment dates: no.

## Overall reading

OULAD is the only candidate that documents a course-level outcome with withdrawal and its date, dated assessments and
submissions, daily platform activity, more than three runs ordered in time, an open licence and anonymised, linked
identifiers. Its open points are the per-module count of runs, the list of final_result values, the share of tasks due
in weeks 1–4 and the persistence of the student identifier across presentations: all four can be checked in the local
copy (`datasets/oulad/`) during structural verification. The XuetangX data are the strongest alternative for dated
activity (G2b) but lack a licence and a pass/fail outcome; the four UCI-style tables (697, 320, 856, xAPI-Edu-Data)
are single-snapshot tables without dates and fail G1 and G2.
