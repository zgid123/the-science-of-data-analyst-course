---
id: S300
url: https://research.stem.open.ac.uk/ouanalyse/dataset/
requested: https://research.stem.open.ac.uk/ouanalyse/dataset/
fetched: 2026-11-06T01:02+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T06
part: 3
raw: none
conversion: html-text of https://research.stem.open.ac.uk/ouanalyse/dataset/ (unreadable, 216 words)
---
No readable copy was found. Attempts:
- L1 https://research.stem.open.ac.uk/ouanalyse/dataset/: unreadable (exploded layout (67% of lines have ≤2 characters))
- L3 https://web.archive.org/web/2id_/https://research.stem.open.ac.uk/ouanalyse/dataset/: error (HTTP 429)

<!-- fetch 2: https://research.stem.open.ac.uk/ouanalyse/dataset/ | WebFetch (L5) | 2026-11-06T01:03+07:00 | partial -->
tool: WebFetch
fetch_prompt: "Return verbatim, word for word, all text of this page: the dataset description, the list of files/tables, license, citation, download links, version/date, and any statements about anonymisation. Keep the wording exact. Also return the page title."

**Page title:** Open University Learning Analytics dataset – OU Analyse

**Dataset description** (quoted in segments):
- "We introduce the anonymised Open University Learning Analytics Dataset (OULAD)."
- "It contains data about courses, students and their interactions with Virtual Learning Environment (VLE)"
- "for seven selected courses (called modules)."
- "Presentations of courses start in February and October – they are marked by "B" and "J" respectively."
- "The dataset consists of tables connected using unique identifiers. All tables are stored in the csv format."

**Other items on the page:**
- **Download link:** http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip
- **Dataset page link:** https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/
- **Testimonials:** The page lists two hackathons that used the dataset: a Learning Analytics & Open Data Hackathon 3.0 at the University of British Columbia, and the LAK18 Hackathon in Sydney.

**Not on this page:** The page does not include a file/table list, license, citation, version/date, or anonymisation statements beyond the word "anonymised" in the description. These may be on the linked OULAD page, but I haven't checked it.

<!-- fetch 3: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ | fetch.py html-text | 2026-11-06T01:03+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/: unreadable (exploded layout (36% of lines have ≤2 characters))
- L3 https://web.archive.org/web/2id_/https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/: error (HTTP 404)

<!-- fetch 4: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ | WebFetch (L5) | 2026-11-06T01:03+07:00 | partial -->
tool: WebFetch
fetch_prompt: "Return verbatim, word for word, the passages of this page about: the dataset description, the license, the citation, download / version / MD5 checksum, the list of tables/files and their columns (especially final_result values, date fields, studentVle, assessments, studentRegistration date_unregistration), and anonymisation. Keep the wording exact, as running text with the original sentences. Also return the page title."

I can't reproduce the full passages verbatim because each quote from the source is limited to 125 characters. Below are short exact quotes where they matter, with paraphrases for the rest.

**Page title:** "Open University Learning Analytics dataset – OU Analyse"

**Dataset description**
The page introduces the anonymised OULAD. It states that the dataset "contains data about courses, students and their interactions with Virtual Learning Environment (VLE)". Presentations start in February ("B") or October ("J"), and the tables are linked by unique identifiers and stored as CSV files.

**Download, version and checksum**
The page says "You can download the latest version of the OULAD here:" and links to a download. It advises checking the zip file's integrity against an MD5 checksum, which is provided on a separate page.

**License**
The page says "This dataset is released under CC-BY 4.0 license."

**Citation**
The page asks users to cite Kuzilek J., Hlosta M., Zdrahal Z., "Open University Learning Analytics dataset", *Scientific Data* 4:170171 (2017), with a DOI of 10.1038/sdata.2017.171.

**Tables and columns (paraphrased)**
- **courses.csv:** Lists modules and their presentations, with `code_module`, `code_presentation` and `length` (in days). The page notes that B and J presentations may differ, so analysing them separately is good practice. CCC, EEE and GGG lack a matching B/J counterpart.
- **assessments.csv:** Lists assessments per presentation: `code_module`, `code_presentation`, `id_assessment`, `assessment_type` (TMA, CMA or Exam), `date` and `weight`. The date counts days from the presentation start, which is day 0. Exams are usually weighted 100%, and other assessments sum to 100%. The page states that if the exam date is missing, it falls at the end of the last presentation week.
- **vle.csv:** Describes VLE materials with `id_site`, `code_module`, `code_presentation`, `activity_type`, `week_from` and `week_to`.
- **studentInfo.csv:** Holds demographics and results: gender, region, highest education, IMD band, age band, previous attempts, studied credits, disability, and `final_result`. The page does not list the possible `final_result` values, except to say that unregistered students have "Withdrawal" as their value.
- **studentRegistration.csv:** Records `date_registration` and `date_unregistration`, both measured in days relative to the presentation start. Negative registration values mean registration before the start. Students who completed the course have an empty unregistration date.
- **studentAssessment.csv:** Contains `id_assessment`, `id_student`, `date_submitted` (days since start), `is_banked` and `score`. Scores run from 0 to 100, and a score below 40 counts as a fail. No record exists for assessments not submitted.
- **studentVle.csv:** The page says it "contains information about each student's interactions with the materials in the VLE." It includes `date` (days since start) and `sum_click` (daily interaction count).

**Anonymisation**
The page describes the dataset as anonymised, and that is the only statement about anonymisation it makes.
