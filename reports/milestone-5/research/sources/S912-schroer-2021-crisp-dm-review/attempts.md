# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-08T23:26+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S1877050921002416 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-08T23:26+07:00 | L2 | https://www.sciencedirect.com/science/article/pii/S1877050921002416/pdf | 403 | text/html; charset=utf-8 | 1181 | – | 0 | error | HTTP 403 |
| 2026-11-08T23:26+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1016/j.procs.2021.01.199 | 403 | text/html; charset=utf-8 | 812 | – | 0 | error | HTTP 403 |
| 2026-11-08T23:26+07:00 | L4 | https://api.crossref.org/works/10.1016/j.procs.2021.01.199 | 200 | application/json | 15 | json-metadata | 44 | metadata | bibliographic record |
| 2026-11-08T23:26+07:00 | L4 | https://api.openalex.org/works/doi:10.1016/j.procs.2021.01.199 | 200 | application/json | 15 | json-metadata | 196 | metadata | bibliographic record |
| 2026-11-08T23:26+07:00 | L1 | https://www.sciencedirect.com/science/article/pii/S1877050921002416/pdf | 403 | text/html; charset=utf-8 | 1181 | – | 0 | error | HTTP 403 |
| 2026-11-08T23:26+07:00 | L1 | https://www.sciencedirect.com/science/article/pii/S1877050921002416 | 403 | text/html; charset=utf-8 | 1181 | – | 0 | error | HTTP 403 |
