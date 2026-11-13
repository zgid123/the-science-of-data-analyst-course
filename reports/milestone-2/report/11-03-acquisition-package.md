## Appendix III – Acquisition Plan and Data Collection Package

The Data Collection Package re-creates our copy of OULAD exactly. Its layout is shown below; the raw files are produced by the collection script and are not edited.

```text
package/
  README.md
  data/
    raw/           published files, unchanged
    metadata/      source.md, citation.bib, data_dictionary.md, raw_manifest.csv,
                   collection_log.txt, structure_report.md, structure_results.json
  src/             collect.py (download, verify, extract), verify_structure.py (Section 6)
```

Table A.3 is the source and license sheet of the package.

**Table A.3. Source, license and citation**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (official title) |
| Provider / authors | Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal; Knowledge Media Institute, The Open University (UK) |
| Official pages | Provider page: https://research.stem.open.ac.uk/ouanalyse/dataset/ ; data descriptor: https://doi.org/10.1038/sdata.2017.171 |
| Copy collected | figshare deposit cited by the data descriptor, DOI https://doi.org/10.6084/m9.figshare.5081998.v1 (version 1), file https://ndownloader.figshare.com/files/8606371 |
| Other distributions | UCI Machine Learning Repository, DOI https://doi.org/10.24432/C5KK69 (same data; missing values written "?" instead of empty); the provider page's own link http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip returned HTTP 404 on 2026-11-05 |
| Access date | 6 November 2026 (UTC+7; 2026-11-05 18:24 UTC in `data/metadata/collection_log.txt`) |
| Version | figshare version 1 (the provider page offers "the latest version" without a number) |
| License | Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ |
| Acquisition method | Direct download of one zip archive, verified against pinned SHA-256 values, extracted unchanged (`src/collect.py`) |
| Integrity evidence | `data/metadata/raw_manifest.csv` (bytes, SHA-256, MD5, data rows per file); `data/metadata/collection_log.txt` |
| Citation | Kuzilek, Hlosta and Zdrahal (2017), *Scientific Data*, 4, Article 170171, https://doi.org/10.1038/sdata.2017.171 (full entry in citation.bib) |

Table A.4 lists the size, checksums and data rows of every collected file; each table matched its pinned SHA-256.

**Table A.4. Raw file manifest**

| File | Bytes | SHA-256 | MD5 | Data rows | Check |
| :---- | :---- | :---- | :---- | :---- | :---- |
| anonymisedData.zip | 46,750,706 | 90dda45037939953f979072fa70a809ebe07e90ec783c408762af7698a3825ec | 7412686fd77cf0e0ee1e8c3e9b354308 |  | MATCH |
| courses.csv | 526 | 4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75 | 4c3df8a42a98a0d26b22f507007c31a8 | 22 | MATCH |
| assessments.csv | 8,200 | 8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1 | 6126f9d435767bcc70134b46f21c2a90 | 206 | MATCH |
| vle.csv | 260,126 | d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9 | 0e7ef38c483daca42900ca426b66f8da | 6,364 | MATCH |
| studentInfo.csv | 3,461,652 | 7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6 | ead11d001fe8b7aed1469daa643a812c | 32,593 | MATCH |
| studentRegistration.csv | 1,109,984 | 0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170 | ef06e3d5784dc7dffe06ef911c5b190c | 32,593 | MATCH |
| studentAssessment.csv | 5,690,310 | fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e | 9ceb38acaeb26fbc15c98b563290c1db | 173,912 | MATCH |
| studentVle.csv | 453,836,331 | 52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0 | b8aae6f4ffd1523319aeb56d66b17f72 | 10,655,280 | MATCH |

OULAD is published in three places, so we had to decide which copy to collect and cite. The provider page links an archive on the Open University's own server [2] and asks users to check it against an MD5 checksum [2]; that link returned an HTTP 404 error, meaning that the file was not found, when the data were collected. The data descriptor, the peer-reviewed article that documents the dataset, cites a deposit on figshare [3], which carries a DOI and a version number; this is the copy we collected. The UCI repository holds a third copy under its own DOI [12]. To make sure the copies agree, we compared the UCI copy with the collected files. All seven tables hold the same rows. The only difference is that UCI writes a missing value as "?" where figshare leaves the cell empty, in five tables (Table A.5). The analysis therefore reads empty cells as missing values and cites the figshare deposit and the descriptor.

Table A.5 compares the UCI copy of OULAD with the collected figshare files, table by table.

**Table A.5. Comparison of the UCI copy with the collected files**

| Table | Figshare bytes | UCI bytes | Same SHA-256 | Line endings (figshare / UCI) | Rows (figshare / UCI) | Same rows |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| assessments.csv | 8200 | 8211 | False | CRLF / CRLF | 206 / 206 | only missing values written '?' in UCI, empty in figshare (11 rows) |
| courses.csv | 526 | 526 | True | CRLF / CRLF | 22 / 22 | True |
| studentAssessment.csv | 5690310 | 5690483 | False | CRLF / CRLF | 173912 / 173912 | only missing values written '?' in UCI, empty in figshare (173 rows) |
| studentInfo.csv | 3461652 | 3462763 | False | CRLF / CRLF | 32593 / 32593 | only missing values written '?' in UCI, empty in figshare (1111 rows) |
| studentRegistration.csv | 1109984 | 1132550 | False | CRLF / CRLF | 32593 / 32593 | only missing values written '?' in UCI, empty in figshare (22560 rows) |
| studentVle.csv | 453836331 | 453836331 | True | CRLF / CRLF | 10655280 / 10655280 | True |
| vle.csv | 260126 | 270612 | False | CRLF / CRLF | 6364 / 6364 | only missing values written '?' in UCI, empty in figshare (5243 rows) |
