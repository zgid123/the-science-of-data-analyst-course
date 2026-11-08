# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:14+07:00 | L1 | https://doi.org/10.1509/jmr.16.0163 | 302 | text/html;charset=utf-8 | 0 | – | 0 | error | curl: (7) Failed to connect to journals.sagepub.com port 443 after 3 ms: Couldn't connect to server |
| 2026-11-06T23:14+07:00 | L2 | https://doi.org/10.2139/ssrn.2759170 | 302 | text/html; charset=utf-8 | 0 | – | 0 | error | curl: (7) Failed to connect to papers.ssrn.com port 443 after 96 ms: Couldn't connect to server |
| 2026-11-06T23:14+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1509/jmr.16.0163 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:14+07:00 | L4 | https://api.crossref.org/works/10.1509/jmr.16.0163 | 200 | application/json | 11 | json-metadata | 258 | metadata | bibliographic record |
| 2026-11-06T23:14+07:00 | L4 | https://api.openalex.org/works/doi:10.1509/jmr.16.0163 | 200 | application/json | 15 | json-metadata | 273 | metadata | bibliographic record |
