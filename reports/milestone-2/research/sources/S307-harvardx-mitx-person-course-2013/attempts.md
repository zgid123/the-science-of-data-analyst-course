# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T01:09+07:00 | L1 | https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/26147 | 200 | application/json | 8 | json-metadata | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters) |
| 2026-11-06T01:09+07:00 | L3 | https://web.archive.org/web/2id_/https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/26147 | 500 | text/html | 138 | – | 0 | error | HTTP 500 |
| 2026-11-06T01:09+07:00 | L4 | https://api.crossref.org/works/10.7910/DVN/26147 | 404 | text/plain | 0 | – | 0 | error | HTTP 404 |
| 2026-11-06T01:09+07:00 | L1 | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/26147 | 202 | text/html | 2 | html-text | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters); exploded layout (100% of lines have ≤2 characters) |
| 2026-11-06T01:10+07:00 | L1 | https://dataverse.harvard.edu/api/datasets/export?exporter=ddi&persistentId=doi:10.7910/DVN/26147 | 200 | application/xml | 14 | html-text | 537 | readable | – |
