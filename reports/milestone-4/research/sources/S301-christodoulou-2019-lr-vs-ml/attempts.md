# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:05+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S0895435618310813 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:05+07:00 | L2 | https://kuleuven.limo.libis.be/discovery/search?query=any,contains,LIRIAS2368520&tab=LIRIAS&search_scope=lirias_profile&vid=32KUL_KUL:Lirias&offset=0 | 200 | text/html | 4 | html-text | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters) |
| 2026-11-06T23:05+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1016/j.jclinepi.2019.02.004 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:05+07:00 | L4 | https://api.crossref.org/works/10.1016/j.jclinepi.2019.02.004 | 200 | application/json | 40 | json-metadata | 58 | metadata | bibliographic record |
| 2026-11-06T23:05+07:00 | L4 | https://api.openalex.org/works/doi:10.1016/j.jclinepi.2019.02.004 | 200 | application/json | 32 | json-metadata | 161 | metadata | few function words (3.7%): scrambled or non-text |
| 2026-11-06T23:05+07:00 | L1 | https://pubmed.ncbi.nlm.nih.gov/30763612/ | 203 | text/html | 5 | html-text | 24 | blocked | blocking page (cookies must be enabled) |
| 2026-11-06T23:06+07:00 | L1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.jclinepi.2019.02.004&resultType=core&format=xml | 200 | application/xml | 10 | html-text | 491 | readable | – |
