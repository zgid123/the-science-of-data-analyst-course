# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:08+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S2666389923001599 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:08+07:00 | L2 | http://www.cell.com/article/S2666389923001599/pdf | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-06T23:08+07:00 | L2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/pdf/main.pdf | 200 | text/html | 1 | html-text | 10 | unreadable | almost no text (10 words) |
| 2026-11-06T23:08+07:00 | L2 | https://pmc.ncbi.nlm.nih.gov:443/articles/PMC10499856/ | 200 | text/html | 248 | html-text | 10499 | readable | – |
| 2026-11-06T23:12+07:00 | L1 | https://api.crossref.org/works/10.1016/j.patter.2023.100804 | 200 | application/json | 31 | json-metadata | 40 | metadata | bibliographic record |
| 2026-11-06T23:12+07:00 | L1 | https://api.openalex.org/works/doi:10.1016/j.patter.2023.100804 | 200 | application/json | 19 | json-metadata | 240 | metadata | bibliographic record |
| 2026-11-06T23:13+07:00 | L1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/ | 200 | text/html | 20 | html-text | 25 | blocked | blocking page (captcha) |
| 2026-11-06T23:13+07:00 | L1 | https://pmc.ncbi.nlm.nih.gov:443/articles/PMC10499856/ | 200 | text/html | 20 | html-text | 25 | blocked | blocking page (captcha) |
| 2026-11-06T23:14+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S2666389923001599 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:14+07:00 | L2 | http://www.cell.com/article/S2666389923001599/pdf | 403 | text/html; charset=utf-8 | 5 | – | 0 | error | HTTP 403 |
| 2026-11-06T23:14+07:00 | L2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/pdf/main.pdf | 200 | text/html | 1 | html-text | 10 | unreadable | almost no text (10 words) |
| 2026-11-06T23:14+07:00 | L2 | https://pmc.ncbi.nlm.nih.gov:443/articles/PMC10499856/ | 200 | text/html | 248 | html-text | 10499 | readable | – |
| 2026-11-06T23:14+07:00 | L1 | https://api.crossref.org/works/10.1016/j.patter.2023.100804 | 200 | application/json | 31 | json-metadata | 40 | metadata | bibliographic record |
| 2026-11-06T23:14+07:00 | L1 | https://api.openalex.org/works/doi:10.1016/j.patter.2023.100804 | 200 | application/json | 19 | json-metadata | 240 | metadata | bibliographic record |
