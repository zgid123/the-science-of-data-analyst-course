# Data Collection Package – Milestone 2 (team N04)

The raw data, metadata and scripts that let anyone re-create the team's copy of the Open University Learning
Analytics Dataset (OULAD) exactly, and check its structure (brief section 15, deliverable C).

```
package/
  README.md
  requirements.txt
  data/
    raw/             the published files, unchanged (created by src/collect.py; not committed)
    metadata/        source and license sheet, citation, data dictionary, checksum manifest, logs, structure report
  src/               collect.py (download, verify, extract), verify_structure.py (Task 6 checks)
```

## Re-create the raw data

Run from this folder, with Python 3.12 or later (`python -m pip install -r requirements.txt` first):

```bash
python src/collect.py            # download, verify SHA-256, extract to data/raw
python src/verify_structure.py   # structural checks -> data/metadata/structure_report.md
```

`collect.py` downloads `anonymisedData.zip` from the figshare deposit cited by the data descriptor
(DOI 10.6084/m9.figshare.5081998.v1, file 8606371), checks its size (46,750,706 bytes) and SHA-256, and extracts the
seven CSV tables unchanged; each table must match its pinned SHA-256 (`data/metadata/raw_manifest.csv`).
Manual alternative: download the zip from https://doi.org/10.6084/m9.figshare.5081998.v1, unzip it into `data/raw/`
and compare the SHA-256 values with `data/metadata/raw_manifest.csv`.

## Metadata

| File | Content |
| :---- | :---- |
| `data/metadata/source.md` | title, provider, official URLs and DOI, version, access date, license (CC BY 4.0), acquisition method, citation |
| `data/metadata/citation.bib` | citations of the data descriptor and the figshare deposit |
| `data/metadata/data_dictionary.md` | column definitions copied from the data descriptor |
| `data/metadata/raw_manifest.csv` | bytes, SHA-256, MD5 and data rows of the archive and each table |
| `data/metadata/collection_log.txt` | timestamped log of the last collection run |
| `data/metadata/structure_report.md`, `structure_results.json` | Task 6 results: rows, columns, keys, types, missing values, time fields, differences from the dictionary, selection conditions |

Nothing in this package cleans, filters, imputes or transforms the data; that work belongs to Milestone 3.
License: CC BY 4.0; cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171.
