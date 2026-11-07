# 5. Data Acquisition and Provenance

The selected dataset was collected by a script that keeps the published files unchanged and records how to obtain
them again, as the brief requires [1]. Sources are named by their digital object identifier (DOI), files
are stored as comma-separated values (CSV), and their integrity is checked with SHA-256 (Secure Hash Algorithm, 256-bit)
 and MD5 (Message Digest 5) checksums. Table 5.1 is the acquisition plan; the full Data Collection Package is
described in Appendix III.

**Table 5.1. Data acquisition plan for OULAD**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (official title) |
| Provider / authors | J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University [3] |
| Official URL / DOI | Provider page [2]; data descriptor doi:10.1038/sdata.2017.171 [3]; files deposited on figshare, doi:10.6084/m9.figshare.5081998.v1 [3] |
| Access date | 6 November 2026 (Vietnam time, UTC+7) |
| Version / release | figshare version 1; the provider page offers the latest version without a number [2] |
| License / terms | CC BY 4.0 [2], [12] |
| Acquisition method | Direct download of one zip archive from the figshare deposit; size and SHA-256 checked against reference values written in the collection script; the seven tables extracted unchanged |
| Raw files | anonymisedData.zip (46,750,706 bytes) containing courses, assessments, vle, studentInfo, studentRegistration, studentAssessment and studentVle (CSV, 453.8 MB for studentVle) |
| Integrity evidence | SHA-256 and MD5 of the archive and of each table in the manifest, the list of files with their checksums; all seven tables matched their pinned SHA-256 |
| Citation | Kuzilek, Hlosta and Zdrahal (2017), *Scientific Data*, 4, 170171 [3] |

OULAD is published in three places, so the provenance of the copy matters. The provider page links an archive on the
Open University's server [2] and asks users to check it against an MD5 checksum [2]; that link returned HTTP 404
when the data were collected. The data descriptor cites the figshare deposit [3], which carries a DOI and a version
number and is the copy collected. The UCI repository holds a third copy under its own DOI [12]. A comparison of the
UCI copy with the collected files found the same rows in all seven tables; the only difference is that UCI writes
missing values as "?" where figshare leaves the cell empty, in five tables (Appendix III). The analysis therefore
reads empty cells as missing and cites the figshare deposit and the descriptor.

The collection is reproducible from two commands. The first, `src/collect.py`, downloads the archive, verifies it
and extracts the tables; the second, `src/verify_structure.py`, runs the structural checks of Section 6. Both scripts, the manifest of checksums, the data
dictionary copied from the descriptor and the collection log form the Data Collection Package; the raw files stay as
published, with nothing cleaned, filtered or converted.
