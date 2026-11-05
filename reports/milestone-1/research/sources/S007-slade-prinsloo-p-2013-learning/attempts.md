# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-02T00:47+07:00 | L1 | https://doi.org/10.1177/0002764213479366 | 302 | text/html;charset=utf-8 | 0 | – | 0 | error | curl: (7) Failed to connect to journals.sagepub.com port 443 after 14 ms: Couldn't connect to server |
| 2026-11-02T00:47+07:00 | L2 | https://figshare.com/articles/report/Learning_analytics_ethical_issues_and_dilemmas/24348508 | 202 | text/html | 1 | html-text | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters); exploded layout (100% of lines have ≤2 characters) |
| 2026-11-02T00:47+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1177/0002764213479366 | 404 | text/html;charset=utf-8 | 6 | – | 0 | error | HTTP 404 |
| 2026-11-02T00:47+07:00 | L4 | https://api.crossref.org/works/10.1177/0002764213479366 | 200 | application/json | 15 | json-metadata | 273 | metadata | bibliographic record |
| 2026-11-02T00:47+07:00 | L4 | https://api.openalex.org/works/doi:10.1177/0002764213479366 | 200 | application/json | 17 | json-metadata | 312 | metadata | bibliographic record |
| 2026-11-02T00:49+07:00 | L1 | https://oro.open.ac.uk/36594/1/SladePrinsloo_ABS_submission.doc | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-02T00:49+07:00 | L3 | https://web.archive.org/web/2id_/https://oro.open.ac.uk/36594/1/SladePrinsloo_ABS_submission.doc | 200 | text/html | 28 | html-text | 42 | unreadable | exploded layout (67% of lines have ≤2 characters) |
| 2026-11-02T00:50+07:00 | L1 | https://openbooks.col.org/learninganalyticsaprimer/assets/pdf/ECE12B6B.pdf | 200 | application/pdf | 149 | pdfkit | 8704 | readable | – |
