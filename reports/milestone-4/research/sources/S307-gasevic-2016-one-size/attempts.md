# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:08+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S1096751615300038 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:08+07:00 | L2 | https://www.research.ed.ac.uk/files/21853000/Learn_engag_student_perf_Version21_authors.pdf | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-06T23:08+07:00 | L2 | https://hdl.handle.net/20.500.11820/bb8a1388-d48b-495d-a0e7-807b14f491f1 | 500 | text/html;charset=utf-8 | 7 | – | 0 | error | HTTP 500 |
| 2026-11-06T23:08+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1016/j.iheduc.2015.10.002 | 0 | – | 0 | – | 0 | error | curl: (7) Failed to connect to web.archive.org port 443 after 248 ms: Couldn't connect to server |
| 2026-11-06T23:08+07:00 | L4 | https://api.crossref.org/works/10.1016/j.iheduc.2015.10.002 | 200 | application/json | 22 | json-metadata | 56 | metadata | bibliographic record |
| 2026-11-06T23:08+07:00 | L4 | https://api.openalex.org/works/doi:10.1016/j.iheduc.2015.10.002 | 200 | application/json | 19 | json-metadata | 95 | metadata | bibliographic record |
| 2026-11-06T23:11+07:00 | L1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.iheduc.2015.10.002&resultType=core&format=xml | 200 | application/xml | 0 | html-text | 4 | unreadable | almost no text (4 words) |
| 2026-11-06T23:11+07:00 | L3 | https://web.archive.org/web/2id_/https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.iheduc.2015.10.002&resultType=core&format=xml | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:11+07:00 | L4 | https://api.crossref.org/works/10.1016/j.iheduc.2015.10.002&resultType=core&format=xml | 404 | text/plain | 0 | – | 0 | error | HTTP 404 |
| 2026-11-06T23:11+07:00 | L1 | https://www.research.ed.ac.uk/files/21853000/Learn_engag_student_perf_Version21_authors.pdf | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-06T23:12+07:00 | L1 | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.iheduc.2015.10.002?fields=title,abstract,year,venue,authors | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
