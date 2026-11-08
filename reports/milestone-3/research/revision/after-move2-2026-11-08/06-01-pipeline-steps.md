## 6.1. Pipeline Steps and Package Structure

**Steps.** The ten steps are functions of one script, `src/prepare_data.py`, run in order; Appendix II (Table A.7)
gives each step with its function and its result. They check the raw tables against their checksums, select the
populations of Section 4.1, correct the 3,516 "10-20" band labels, sum the 10,655,280 click rows into 1,808,119
enrolment-day records, flag the uncertain records, leave out the 98,745 clicks after withdrawal, integrate 286,898
enrolment-task rows, build the features at both cut-offs and write six views and two model-ready matrices with their
documentation.

**Stages.** The preparation script is one of eight stages that a single command, `bash src/run_all.sh`, runs in order,
from linking and checking the raw files to the validation of Section 7 and the two notebooks that show the work
(Appendix II, Table A.8). Each stage writes its console output, its command, its time in
Coordinated Universal Time (UTC) and its exit status to a log file, and the run stops at the first failed stage. The
whole run takes about 15 seconds. Run twice from the raw files, it wrote byte-identical outputs in all eight data files,
and every join kept exactly its input rows.

**Package structure.** The package follows the layout that the brief recommends [1]: `data/raw/` holds the immutable
raw tables; `data/interim/` the intermediate results that the pipeline can recreate; `data/processed/` the
analytic-ready views; `data/metadata/` the dictionary, lineage, quality logs and validation results; `notebooks/` the
notebooks for data understanding and preparation; and `src/` the scripts. Appendix II describes the stages, the
transformation log and every prepared file.
