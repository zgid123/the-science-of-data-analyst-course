## 6.1. Pipeline Steps and Package Structure

The ten steps the brief recommends, from loading and validating the raw files to persisting the prepared data with
its dictionary, transformation log and validation summary [1], are functions of `src/prepare_data.py` run in
order (Appendix II, Table A.7). They check the raw tables against their checksums, select the populations, sum the
10,655,280 click rows into 1,808,119 enrolment-day records, leave out the 98,745 clicks after withdrawal, integrate
286,898 enrolment-task rows, build the features and write six views and two model-ready matrices. The package follows
the brief's layout of `data/raw/`, `data/interim/`, `data/processed/`, `data/metadata/`, `notebooks/` and `src/`
[1], and `bash src/run_all.sh` runs all eight scripted stages in about 15 seconds; two runs from the raw files wrote
byte-identical outputs, and every join kept exactly its input rows.
