# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:09+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S1560429226002350 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:09+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1007/s40593-021-00285-9 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:09+07:00 | L4 | https://api.crossref.org/works/10.1007/s40593-021-00285-9 | 200 | application/json | 47 | json-metadata | 39 | metadata | bibliographic record |
| 2026-11-06T23:09+07:00 | L4 | https://api.openalex.org/works/doi:10.1007/s40593-021-00285-9 | 200 | application/json | 21 | json-metadata | 284 | metadata | bibliographic record |
| 2026-11-06T23:12+07:00 | L1 | https://link.springer.com/content/pdf/10.1007/s40593-021-00285-9.pdf | 200 | text/html | 2 | html-text | 35 | unreadable | almost no text (35 words) |
| 2026-11-06T23:13+07:00 | L5 | https://osf.io (author preprint AlgorithmicBiasInEducation_rsb3.7.pdf, signed OSF storage URL, fetched 2026-11-06T08:30+07:00) | – | WebFetch | – | – | 20064 | ok | appended |
