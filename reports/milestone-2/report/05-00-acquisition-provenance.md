# 5. Data Acquisition and Provenance

**Principle.** The brief requires the raw data to stay exactly as published and the collection to be repeatable by
anyone [1]. The selected dataset was therefore collected by a script that downloads the published files, checks them
and stores them unchanged, and that records everything needed to obtain them again. Two kinds of evidence make the copy
checkable. A checksum is a short fingerprint computed from a file's exact bytes; if a single byte changes, the
checksum changes. We recorded two of them for every file: SHA-256 (Secure Hash Algorithm, 256-bit), the
standard used for verification, and MD5 (Message Digest 5), the checksum that the provider itself publishes. The files
are stored as comma-separated values (CSV), plain-text tables that any tool can read. Table 5.1 is the brief's
acquisition plan for OULAD.

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

**Which copy, and why.** OULAD is published in three places: the provider's own server, whose link was broken
when the data were collected [2]; a figshare deposit with a DOI and a version number, which the data descriptor cites
[3]; and the UCI repository [12]. We collected and cite the figshare deposit, and a row-by-row comparison found
the UCI copy identical apart from how missing values are written (Appendix III).

**Reproducible in two commands.** Anyone with the Data Collection Package can re-create our copy with two
commands. The first, `src/collect.py`, downloads the archive, checks its size and checksum and extracts the seven
tables. The second, `src/verify_structure.py`, runs the structural checks of Section 6. The package also holds the
manifest of checksums, the data dictionary copied from the descriptor, the source and license sheet, the citation and
the collection log. The raw files stay as published: nothing is cleaned, filtered or converted. Appendix III shows the
package's layout and its source, license and manifest tables.
