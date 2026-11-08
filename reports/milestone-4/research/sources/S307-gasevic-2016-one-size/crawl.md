---
id: S307
url: https://api.openalex.org/works/doi:10.1016/j.iheduc.2015.10.002
requested: 10.1016/j.iheduc.2015.10.002
fetched: 2026-11-06T23:08+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T05
part: 3
raw: raw.json (19 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1016/j.iheduc.2015.10.002 (metadata, 95 words)
---
source: OpenAlex
title: Learning analytics should not promote one size fits all: The effects of instructional conditions in predicting academic success
authors: Dragan Gašević; Shane Dawson; Tim Rogers; Danijela Gašević
institutions: University of Edinburgh; University of South Australia
venue: The Internet and Higher Education
publication date: 2015-10-23
volume: 28
issue: None
pages: 68–84
doi: https://doi.org/10.1016/j.iheduc.2015.10.002
cited_by_count (OpenAlex): 726
type: article
location: https://doi.org/10.1016/j.iheduc.2015.10.002 (open access: False)
location: https://www.research.ed.ac.uk/files/21853000/Learn_engag_student_perf_Version21_authors.pdf (open access: True)
location: https://hdl.handle.net/11541.2/112019 (open access: False)

<!-- fetch 2: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.iheduc.2015.10.002&resultType=core&format=xml | fetch.py html-text | 2026-11-06T23:11+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.iheduc.2015.10.002&resultType=core&format=xml: unreadable (almost no text (4 words))
- L3 https://web.archive.org/web/2id_/https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.iheduc.2015.10.002&resultType=core&format=xml: error (HTTP 429)
- L4 https://api.crossref.org/works/10.1016/j.iheduc.2015.10.002&resultType=core&format=xml: error (HTTP 404)

<!-- fetch 3: https://www.research.ed.ac.uk/files/21853000/Learn_engag_student_perf_Version21_authors.pdf | fetch.py none | 2026-11-06T23:11+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://www.research.ed.ac.uk/files/21853000/Learn_engag_student_perf_Version21_authors.pdf: error (HTTP 403)

<!-- fetch 4: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.iheduc.2015.10.002?fields=title,abstract,year,venue,authors | fetch.py none | 2026-11-06T23:12+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.iheduc.2015.10.002?fields=title,abstract,year,venue,authors: error (HTTP 429)
