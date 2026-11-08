## 4.1. Dataset Selection, Provenance and Licence

The requirements and gates of Section 4 decided what the dataset search looked for. The search was therefore led by
the requirements: its keywords came from the requirement matrix (student completion, dropout and withdrawal;
interaction with a learning management system or virtual learning environment; assessment submission; clickstream;
higher education; learning analytics; and dropout from massive open online courses), not from datasets already known
to us.

**How the search worked.** Milestone 2 searched the University of California, Irvine (UCI) Machine Learning
Repository, data repositories that assign a digital object identifier (DOI) such as figshare, Harvard Dataverse and
Zenodo, the pages of research groups that publish datasets, and general web search. Three rules applied to every hit:
the documentation and the licence were read before the data were judged; a dataset found on Kaggle, a blog or another
copy was traced back to the provider that published it; and re-uploads without a known origin were rejected. The
search log holds 16 entries from 11 searches, and seven candidates remained, more than the three the course brief
requires: A, the Open University Learning Analytics Dataset (OULAD); B, the UCI dataset 697 on dropout and academic
success; C, the UCI dataset 320 on student performance; D, the UCI dataset 856 on higher-education students'
performance; E, the XuetangX MOOC dropout data; F, the HarvardX Person-Course 2013 data; and G, the xAPI-Edu-Data set.

**How the candidates were judged.** Each candidate was scored from 0 to 2 on the brief's ten criteria, where 0 means
not met or not stated, 1 partly met or uncertain and 2 well met, for a total out of 20. The six must-have gates came
first: gates decide, scores inform, so a candidate that fails a gate is rejected whatever its total. Table 4.2 is the
Dataset Selection Matrix; three of its columns pair two criteria each, so the table shows all ten scores, the total and
the decision with the gates each rejected candidate fails.

**Table 4.2. Dataset Selection Matrix**

| Candidate | AQ coverage | Population fit | Unit / temporal | Target / timing | Docs / licence | Quality feasibility | Ethics / representativeness | Total (of 20) | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A OULAD | 1 | 1 | 2 / 1 | 1 / 1 | 1 / 2 | 1 | 1 | 12 | Selected, on condition that the files confirm three facts |
| B UCI 697 | 0 | 1 | 0 / 1 | 1 / 0 | 2 / 2 | 2 | 1 | 10 | Rejected: fails G1, G2a, G2b |
| C UCI 320 | 0 | 0 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 6 | Rejected: fails G1, G2a, G2b, G3 |
| D UCI 856 | 0 | 1 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 7 | Rejected: fails G1, G2a, G2b, G3 |
| E XuetangX | 1 | 1 | 1 / 1 | 1 / 1 | 1 / 0 | 1 | 0 | 8 | Rejected: fails G1, G2a, G4 |
| F HarvardX | 0 | 1 | 1 / 0 | 1 / 0 | 2 / 0 | 2 | 1 | 8 | Rejected: fails G1, G2a, G2b, G3, G4 |
| G xAPI-Edu-Data | 0 | 0 | 0 / 0 | 1 / 0 | 0 / 1 | 2 | 0 | 4 | Rejected: fails G1, G2a, G2b, G3; G4 unclear |

**Why OULAD, and why not the others.** OULAD is selected because it is the only candidate whose documentation meets
the timing and licence gates and records a dated withdrawal: a final result for each enrolment, including withdrawal
with the day of unregistration, dated assessments with the day of each submission, and the daily number of clicks of
each student on each page of the learning platform. Every other candidate fails at least the outcome gate (G1).
UCI 697 labels students by their degree after several years and holds only semester totals, so it cannot show when
within a course a student stopped; UCI 320 and UCI 856 describe secondary-school pupils or a single questionnaire, with
grades but no withdrawal and no dated tasks or activity; the XuetangX data record dated activity but have a yes-or-no
dropout label without pass or fail and state no licence; HarvardX records only the first and last activity of each
learner and is not openly licensed; and xAPI-Edu-Data has no dated records and is known only from a Kaggle listing.
OULAD was therefore chosen for its fit with the questions, not for ease of access: five candidates scored higher on
quality feasibility, and UCI 697 and HarvardX also on documentation, but none of them could show when a student stopped taking part.

**A modest total, made conditional.** OULAD's total of 12 out of 20 is modest because the scores count only what the
documentation states, and its documentation leaves several facts open. The selection was therefore made conditional
on the files confirming three facts: that the result values separate pass from fail (G1), that each module has enough
runs for testing (G3), and that a student's identifier stays the same across runs (G5). The structural check of
Milestone 2 confirmed the first and third, and showed the second met for five of the seven modules, the five with three or four runs. AQ3 is therefore tested on all 13 runs of 2014, with the 9 runs that have an earlier run of the same module and start month reported apart from the 4 that have none (Sections 5 and 9.1).

**Limits that come with the choice.** OULAD describes UK distance-learning modules from 2013–2014, and its modules
were selected by the publisher partly because many students failed them, so its failure and withdrawal rates are
likely to exceed those of a typical program. It holds no delivery mode, year of study, attendance, leave or transfer
status, and its authors advise analysing runs that start in February and in October separately. No supplementary
dataset is added, because no candidate holds the missing contact, capacity or attendance data.

**Provenance, version and licence.** Table 4.3 records where our copy of OULAD comes from, which version it is, under
which licence it may be used and how its integrity was checked. The dataset is described in the data descriptor of
Kuzilek, Hlosta and Zdrahal, which reports 22 courses and 32,593 students with their assessment results and daily
summaries of their clicks, released anonymised under a CC-BY 4.0 licence [S002].

**Table 4.3. Provenance, version and licence of OULAD**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (OULAD) |
| Provider and authors | J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University |
| Copy used and version | figshare deposit, doi:10.6084/m9.figshare.5081998.v1, version 1; the provider page offers the latest version without a number |
| Access date | 6 November 2026 (Vietnam time, UTC+7) |
| Licence | Creative Commons Attribution 4.0 (CC BY 4.0): academic use with attribution |
| Raw files | One archive, anonymisedData.zip (46,750,706 bytes), holding seven tables in comma-separated values (CSV) format |
| Integrity | Size and SHA-256 checksum of the archive and of each table pinned at collection; all seven tables matched; Milestone 3 re-confirmed every pinned checksum before preparation |
| Other copies | The UCI repository copy is identical apart from how missing values are written ("?"); the provider page's own download link returned HTTP 404 on 5 November 2026 |

**Reproducible collection and privacy.** The collection procedure re-creates the raw copy with two commands, one that
downloads the archive and checks its size and checksum, and one that verifies the structure of the seven tables;
nothing in it cleans, filters, imputes or transforms the data, so the raw files stay as published. OULAD is anonymised
by its publisher with random identifiers, days counted relative to each run and k-anonymity with k = 5, so that every
combination of identifying attributes is shared by at least five students. We make no attempt at re-identification,
and no record of the data is entered into public AI tools. Section 5 describes the tables of this copy and how far they
fit the requirements.
