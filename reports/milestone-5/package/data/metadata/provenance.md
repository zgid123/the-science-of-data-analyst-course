# Data source, provenance and licence

The analysis uses the Open University Learning Analytics Dataset (OULAD), version 1 of the figshare deposit cited by
its data descriptor. The package does not redistribute the data: `run_all.sh` (step 00, `src/link_raw.py`)
downloads the archive from the pinned URL below, checks its SHA-256, extracts the seven tables unchanged into
`data/raw/` and checks every table against its pinned SHA-256 before any other step reads it. The tables are then
made read-only; every later step only reads them.

## Source

| Item | Value |
| :---- | :---- |
| Dataset | Open University Learning Analytics Dataset (OULAD) |
| Provider / authors | Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal; Knowledge Media Institute, The Open University (UK) |
| Data descriptor | Kuzilek, J., Hlosta, M. and Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. https://doi.org/10.1038/sdata.2017.171 |
| Copy used | figshare deposit, DOI https://doi.org/10.6084/m9.figshare.5081998.v1 (version 1), file 8606371, direct link https://ndownloader.figshare.com/files/8606371 |
| Other distributions | UCI Machine Learning Repository, DOI https://doi.org/10.24432/C5KK69 (same tables; missing values written "?" instead of empty); provider page https://research.stem.open.ac.uk/ouanalyse/dataset/ |
| Access date of the pinned copy | 6 November 2026 (UTC+7) |
| Licence | Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ |
| Citation | Cite the data descriptor above; BibTeX entries for the descriptor and the figshare deposit are in `citation.bib` |
| Privacy | The provider anonymised the data before publication: student identifiers are randomised, and age and deprivation are given as bands. The package adds no other data and attempts no re-identification. |

## Pinned files

The archive and each table must match these values (also in `raw_pins.csv`, which `src/link_raw.py` reads); the
check of the latest run is written to `raw_check.csv`.

| File | Bytes | Data rows | SHA-256 |
| :---- | ----: | ----: | :---- |
| anonymisedData.zip | 46,750,706 | – | `90dda45037939953f979072fa70a809ebe07e90ec783c408762af7698a3825ec` |
| courses.csv | 526 | 22 | `4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75` |
| assessments.csv | 8,200 | 206 | `8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1` |
| vle.csv | 260,126 | 6,364 | `d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9` |
| studentInfo.csv | 3,461,652 | 32,593 | `7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6` |
| studentRegistration.csv | 1,109,984 | 32,593 | `0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170` |
| studentAssessment.csv | 5,690,310 | 173,912 | `fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e` |
| studentVle.csv | 453,836,331 | 10,655,280 | `52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0` |

Manual alternative: download the archive from https://doi.org/10.6084/m9.figshare.5081998.v1, unzip the seven CSV
files into `data/raw/` and compare their SHA-256 with the table above; `run_all.sh` then uses them without
downloading.

## From raw to results

| Stage | Version | Where |
| :---- | :---- | :---- |
| Raw data | OULAD, figshare version 1 (hashes above) | `data/raw/` (downloaded) |
| Prepared data | OULAD-N04-prepared-1.0: eight analytic-ready views | `data/processed/` (rebuilt); published hashes and row counts in `version_manifest_published.json`; manifest of the latest rebuild in `version_manifest.json`; comparison in `rebuild_check_prepared.csv` |
| Results | AQ1 and AQ2 on the 9 module runs of 2013 | `results/` (rebuilt); reference checksums in `results/checksums.csv`; comparison in `rebuild_check_results.csv` |

The preparation steps and their order are in `transformation_log.md`, the origin of every prepared variable in
`lineage.md`, the variables of the prepared views in `data_dictionary.md`, and every change to the questions, KPIs
and populations in `change_log.md`.
