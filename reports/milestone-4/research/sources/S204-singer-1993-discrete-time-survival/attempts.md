# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:07+07:00 | L1 | https://doi.org/10.3102/10769986018002155 | 302 | text/html;charset=utf-8 | 0 | – | 0 | error | curl: (7) Failed to connect to journals.sagepub.com port 443 after 2 ms: Couldn't connect to server |
| 2026-11-06T23:07+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.3102/10769986018002155 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:07+07:00 | L4 | https://api.crossref.org/works/10.3102/10769986018002155 | 200 | application/json | 7 | json-metadata | 206 | metadata | bibliographic record |
| 2026-11-06T23:07+07:00 | L4 | https://api.openalex.org/works/doi:10.3102/10769986018002155 | 200 | application/json | 16 | json-metadata | 225 | metadata | bibliographic record |
