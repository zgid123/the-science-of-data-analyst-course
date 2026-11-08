# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:06+07:00 | L1 | https://doi.org/10.1177/0272989X06295361 | 302 | text/html;charset=utf-8 | 0 | – | 0 | error | curl: (7) Failed to connect to journals.sagepub.com port 443 after 102 ms: Couldn't connect to server |
| 2026-11-06T23:06+07:00 | L2 | https://pmc.ncbi.nlm.nih.gov:443/articles/PMC2577036/ | 200 | text/html | 161 | html-text | 6720 | readable | – |
| 2026-11-06T23:12+07:00 | L1 | https://api.crossref.org/works/10.1177/0272989X06295361 | 200 | application/json | 6 | json-metadata | 270 | metadata | bibliographic record |
| 2026-11-06T23:12+07:00 | L1 | https://api.openalex.org/works/doi:10.1177/0272989X06295361 | 200 | application/json | 19 | json-metadata | 323 | metadata | bibliographic record |
| 2026-11-06T23:13+07:00 | L1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/ | 200 | text/html | 161 | html-text | 6720 | readable | – |
| 2026-11-06T23:14+07:00 | L1 | https://api.crossref.org/works/10.1177/0272989X06295361 | 200 | application/json | 6 | json-metadata | 270 | metadata | bibliographic record |
| 2026-11-06T23:14+07:00 | L1 | https://api.openalex.org/works/doi:10.1177/0272989X06295361 | 200 | application/json | 19 | json-metadata | 323 | metadata | bibliographic record |
