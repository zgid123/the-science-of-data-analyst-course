# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T08:28+07:00 | L1 | https://doi.org/10.1145/2382577.2382579 | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-06T08:28+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1145/2382577.2382579 | 302 | text/plain; charset=utf-8 | 0 | – | 0 | error | curl: (47) Maximum (50) redirects followed |
| 2026-11-06T08:28+07:00 | L4 | https://api.crossref.org/works/10.1145/2382577.2382579 | 200 | application/json | 8 | json-metadata | 288 | metadata | bibliographic record |
| 2026-11-06T08:28+07:00 | L4 | https://api.openalex.org/works/doi:10.1145/2382577.2382579 | 200 | application/json | 13 | json-metadata | 304 | metadata | bibliographic record |
| 2026-11-06T08:28+07:00 | L1 | https://www.cs.umb.edu/~ding/history/470_670_fall_2011/papers/cs670_Tran_PreferredPaper_LeakingInDataMining.pdf | 200 | application/pdf | 847 | pdfkit | 7597 | readable | – |
