## 1.2. Dataset, Version and Entry Gate

The brief admits a team to Milestone 3 only when its Data Collection Package from Milestone 2 is complete: the
Milestone 1 baseline in force, an updated traceability matrix, raw files kept unchanged, a data dictionary,
collection evidence and the Controlled Change Log [1]. All six inputs are complete; Appendix I (Table A.1) states the
content and status of each.

The raw data are the seven comma-separated values (CSV) tables of OULAD, figshare version 1, with the digital object
identifier (DOI) 10.6084/m9.figshare.5081998.v1. A checksum is a fingerprint of a file's exact content: the Secure
Hash Algorithm 256 (SHA-256) gives a different value if a single byte changes. Each raw table matches the SHA-256 value
pinned in Milestone 2, and the eight files of the Milestone 1 proposal from which the baseline was copied are also
unchanged. In the Prepared Data Package, the raw tables are hard links to those collected files, set to read-only and
checked against their checksums at every run, so they cannot change unnoticed; this meets the brief's rule that raw
data stay immutable and every change produces a new file [1].

The dataset holds 22 module runs of seven Open University (OU) modules from 2013 and 2014, with 32,593 student
records [2]; each record is an enrolment, one student in one run, and the enrolments belong to 28,785 distinct
students (Section 2.1). The brief warns that a team should not continue to cleaning and modelling when the dataset
supports only a very small part of the proposal [1]. OULAD supports AQ1 to AQ3 in part and the ranking part of AQ4,
with a real outcome for every enrolment, assessment dates and daily activity records; only the contact part of AQ4
lacks data, and it is deferred to the pilot (Section 4.1). The entry gate therefore holds, and preparation is
justified.
