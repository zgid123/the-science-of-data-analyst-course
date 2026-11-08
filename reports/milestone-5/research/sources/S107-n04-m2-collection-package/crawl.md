---
id: S107
url: reports/milestone-2/package/README.md
requested: reports/milestone-2/package/README.md reports/milestone-2/package/metadata/data_dictionary.md reports/milestone-2/package/metadata/source.md reports/milestone-2/package/metadata/structure_report.md
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 4 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T05
part: 1
raw: raw.txt (12 KB)
conversion: verbatim copy of 4 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-2/package/README.md @ 19d35a4 =====
# Data Collection Package – Milestone 2 (team N04)

The raw data, metadata and scripts that let anyone re-create the team's copy of the Open University Learning
Analytics Dataset (OULAD) exactly, and check its structure (brief section 15, deliverable C).

```
package/
  README.md
  data/raw/          the published files, unchanged (created by src/collect.py; not committed)
  metadata/          source and license sheet, citation, data dictionary, checksum manifest, logs, structure report
  src/               collect.py (download, verify, extract), verify_structure.py (Task 6 checks)
```

## Re-create the raw data

Run from this folder, with Python 3.12 or later (`python -m pip install -r requirements.txt` first):

```bash
python src/collect.py            # download, verify SHA-256, extract to data/raw
python src/verify_structure.py   # structural checks -> metadata/structure_report.md
```

`collect.py` downloads `anonymisedData.zip` from the figshare deposit cited by the data descriptor
(DOI 10.6084/m9.figshare.5081998.v1, file 8606371), checks its size (46,750,706 bytes) and SHA-256, and extracts the
seven CSV tables unchanged; each table must match its pinned SHA-256 (`metadata/raw_manifest.csv`).
Manual alternative: download the zip from https://doi.org/10.6084/m9.figshare.5081998.v1, unzip it into `data/raw/`
and compare the SHA-256 values with `metadata/raw_manifest.csv`.

## Metadata

| File | Content |
| :---- | :---- |
| `metadata/source.md` | title, provider, official URLs and DOI, version, access date, license (CC BY 4.0), acquisition method, citation |
| `metadata/citation.bib` | citations of the data descriptor and the figshare deposit |
| `metadata/data_dictionary.md` | column definitions copied from the data descriptor |
| `metadata/raw_manifest.csv` | bytes, SHA-256, MD5 and data rows of the archive and each table |
| `metadata/collection_log.txt` | timestamped log of the last collection run |
| `metadata/structure_report.md`, `structure_results.json` | Task 6 results: rows, columns, keys, types, missing values, time fields, differences from the dictionary, selection conditions |

Nothing in this package cleans, filters, imputes or transforms the data; that work belongs to Milestone 3.
License: CC BY 4.0; cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171.

===== reports/milestone-2/package/metadata/data_dictionary.md @ 19d35a4 =====
# OULAD data dictionary (as documented)

Column definitions copied from the data descriptor: Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University
Learning Analytics dataset. Scientific Data, 4, 170171, section "Data Records". Every day value is counted from the
start of the module presentation (day 0). `src/verify_structure.py` compares this list with the headers of the files
in `data/raw/` and reports every difference in `metadata/structure_report.md`.

| Table | Column (documented) | Definition (descriptor) |
| :---- | :---- | :---- |
| courses | code_module | code name of the module, which serves as the identifier |
| courses | code_presentation | code name of the presentation |
| courses | length | the length of the module-presentation in days from module start date to module end date |
| assessments | code_module | module identification code, to which the assessment belongs |
| assessments | code_presentation | presentation identification code, to which the assessment belongs |
| assessments | id_assessment | assessment identification number |
| assessments | assessment_type | type of assessment: Tutor Marked Assessment (TMA), Computer Marked Assessment (CMA), Final Exam (Exam) |
| assessments | date | information about the cut-off day of the assessment |
| assessments | weight | weight of the assessment; exams 100%, the sum of all other assessments also 100% |
| vle | id_site | identification number of the material |
| vle | code_module | identification code for the module |
| vle | code_presentation | identification code of the presentation |
| vle | activity_type | role associated with the module material |
| vle | week_from | week from which the material is planned to be used |
| vle | week_to | week until which the material is planned to be used |
| studentInfo | code_module | module identification code on which the student is registered |
| studentInfo | code_presentation | presentation identification code during which the student is registered on the module |
| studentInfo | id_student | unique student identification number |
| studentInfo | gender | student's gender |
| studentInfo | region | geographic region where the student lived while taking the module-presentation |
| studentInfo | highest_education | highest student education level on entry to the module presentation |
| studentInfo | imd_band | IMD band of the place where the student lived during the module-presentation |
| studentInfo | age_band | band of student's age |
| studentInfo | num_of_prev_attempts | number of times the student has attempted this module |
| studentInfo | studied_credits | total number of credits for the modules the student is currently studying |
| studentInfo | disability | whether the student has declared a disability |
| studentInfo | final_result | student's final result in the module-presentation |
| studentRegistration | code_module | module identification code |
| studentRegistration | code_presentation | presentation identification code |
| studentRegistration | id_student | unique student identification number |
| studentRegistration | date_registration | day of the student's registration for the module presentation |
| studentRegistration | date_unregistration | day of unregistration; empty for students who completed; Withdrawal as final_result for those who unregistered |
| studentAssessment | id_assessment | assessment identification number |
| studentAssessment | id_student | unique student identification number |
| studentAssessment | date_submitted | day of assessment submission |
| studentAssessment | is_banked | flag: the result was transferred from a previous presentation |
| studentAssessment | score | score from 0 to 100; below 40 is interpreted as Fail |
| studentVle | code_module | module identification code |
| studentVle | code_presentation | presentation identification code |
| studentVle | id_student | unique student identification number |
| studentVle | id_site | VLE material identification number |
| studentVle | date | day of the student's interaction with the material |
| studentVle | sum_click | number of times the student interacted with the material |

===== reports/milestone-2/package/metadata/source.md @ 19d35a4 =====
# Source, license and citation

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (official title) |
| Provider / authors | Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal; Knowledge Media Institute, The Open University (UK) |
| Official pages | Provider page: https://research.stem.open.ac.uk/ouanalyse/dataset/ ; data descriptor: https://doi.org/10.1038/sdata.2017.171 |
| Copy collected | figshare deposit cited by the data descriptor, DOI https://doi.org/10.6084/m9.figshare.5081998.v1 (version 1), file https://ndownloader.figshare.com/files/8606371 |
| Other distributions | UCI Machine Learning Repository, DOI https://doi.org/10.24432/C5KK69 (same data; missing values written "?" instead of empty); the provider page's own link http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip returned HTTP 404 on 2026-11-05 |
| Access date | 6 November 2026 (UTC+7; 2026-11-05 18:24 UTC in `metadata/collection_log.txt`) |
| Version | figshare version 1 (the provider page offers "the latest version" without a number) |
| License | Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ |
| Acquisition method | Direct download of one zip archive, verified against pinned SHA-256 values, extracted unchanged (`src/collect.py`) |
| Integrity evidence | `metadata/raw_manifest.csv` (bytes, SHA-256, MD5, data rows per file); `metadata/collection_log.txt` |
| Citation | Kuzilek, Hlosta and Zdrahal (2017), *Scientific Data*, 4, Article 170171, https://doi.org/10.1038/sdata.2017.171 (full entry in citation.bib) |

===== reports/milestone-2/package/metadata/structure_report.md @ 19d35a4 =====
# Initial structural verification (Task 6)

Generated 2026-11-05T18:33:01Z by `src/verify_structure.py` from `data/raw/` (files read as text, nothing changed).

| File | Rows | Columns | Key(s) | Duplicate keys | Exact duplicate rows | Time fields (min–max day) | Headers not in the dictionary | Dictionary columns not in file |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses.csv | 22 | 3 | code_module, code_presentation | 0 | 0 | module_presentation_length 234–269 | module_presentation_length | length |
| assessments.csv | 206 | 6 | id_assessment | 0 | 0 | date 12–261 | – | – |
| vle.csv | 6,364 | 6 | id_site | 0 | 0 | week_from 0–29; week_to 0–29 | – | – |
| studentInfo.csv | 32,593 | 12 | code_module, code_presentation, id_student | 0 | 0 | – | – | – |
| studentRegistration.csv | 32,593 | 5 | code_module, code_presentation, id_student | 0 | 0 | date_registration -322–167; date_unregistration -365–444 | – | – |
| studentAssessment.csv | 173,912 | 5 | id_assessment, id_student | 0 | 0 | date_submitted -11–608 | – | – |
| studentVle.csv | 10,655,280 | 6 | none documented | – | 787,170 | date -25–269 | – | – |

## Missing values (empty cells, by column)

| File | Column | Missing |
| :---- | :---- | :---- |
| assessments.csv | date | 11 |
| vle.csv | week_from | 5,243 |
| vle.csv | week_to | 5,243 |
| studentInfo.csv | imd_band | 1,111 |
| studentRegistration.csv | date_registration | 45 |
| studentRegistration.csv | date_unregistration | 22,521 |
| studentAssessment.csv | score | 173 |

## Inferred types

- courses.csv: code_module (text), code_presentation (text), module_presentation_length (integer)
- assessments.csv: code_module (text), code_presentation (text), id_assessment (integer), assessment_type (text), date (integer), weight (decimal)
- vle.csv: id_site (integer), code_module (text), code_presentation (text), activity_type (text), week_from (integer), week_to (integer)
- studentInfo.csv: code_module (text), code_presentation (text), id_student (integer), gender (text), region (text), highest_education (text), imd_band (text), age_band (text), num_of_prev_attempts (integer), studied_credits (integer), disability (text), final_result (text)
- studentRegistration.csv: code_module (text), code_presentation (text), id_student (integer), date_registration (integer), date_unregistration (integer)
- studentAssessment.csv: id_assessment (integer), id_student (integer), date_submitted (integer), is_banked (integer), score (integer)
- studentVle.csv: code_module (text), code_presentation (text), id_student (integer), id_site (integer), date (integer), sum_click (integer)

## Selection conditions and denominators

```json
{
 "final_result_values": {
  "Pass": 12361,
  "Withdrawn": 10156,
  "Fail": 7052,
  "Distinction": 3024
 },
 "withdrawn_with_date": 10063,
 "withdrawn_without_date": 93,
 "date_but_not_withdrawn": 9,
 "studentInfo_registration_match": true,
 "runs_per_module": {
  "AAA-J": [
   "2013J",
   "2014J"
  ],
  "BBB-B": [
   "2013B",
   "2014B"
  ],
  "BBB-J": [
   "2013J",
   "2014J"
  ],
  "CCC-B": [
   "2014B"
  ],
  "CCC-J": [
   "2014J"
  ],
  "DDD-B": [
   "2013B",
   "2014B"
  ],
  "DDD-J": [
   "2013J",
   "2014J"
  ],
  "EEE-B": [
   "2014B"
  ],
  "EEE-J": [
   "2013J",
   "2014J"
  ],
  "FFF-B": [
   "2013B",
   "2014B"
  ],
  "FFF-J": [
   "2013J",
   "2014J"
  ],
  "GGG-B": [
   "2014B"
  ],
  "GGG-J": [
   "2013J",
   "2014J"
  ]
 },
 "runs_per_module_all": {
  "AAA": [
   "2013J",
   "2014J"
  ],
  "BBB": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "CCC": [
   "2014B",
   "2014J"
  ],
  "DDD": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "EEE": [
   "2013J",
   "2014B",
   "2014J"
  ],
  "FFF": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "GGG": [
   "2013J",
   "2014B",
   "2014J"
  ]
 },
 "students_total": 28785,
 "students_in_more_than_one_run": 3538,
 "same_module_repeats": 1309,
 "repeats_with_higher_attempt_counter": 1309,
 "first_task_due_day": {
  "AAA-2013J": 19,
  "AAA-2014J": 19,
  "BBB-2013B": 19,
  "BBB-2013J": 19,
  "BBB-2014B": 12,
  "BBB-2014J": 19,
  "CCC-2014B": 18,
  "CCC-2014J": 18,
  "DDD-2013B": 23,
  "DDD-2013J": 25,
  "DDD-2014B": 25,
  "DDD-2014J": 20,
  "EEE-2013J": 33,
  "EEE-2014B": 33,
  "EEE-2014J": 33,
  "FFF-2013B": 19,
  "FFF-2013J": 19,
  "FFF-2014B": 24,
  "FFF-2014J": 24,
  "GGG-2013J": 61,
  "GGG-2014B": 61,
  "GGG-2014J": 61
 },
 "runs_with_task_due_by_day_13": 1,
 "runs_with_task_due_by_day_27": 16,
 "exams_without_cutoff_day": 11,
 "unregistered_on_or_before_day_0": 3097,
 "registered_after_day_14": 58,
 "registration_day_missing": 45,
 "still_registered_at_day_14": 28119,
 "assessment_rows_without_parent": 0,
 "submissions_without_enrolment": 0,
 "click_rows_without_enrolment": 0,
 "click_rows_without_site": 0
}
```
