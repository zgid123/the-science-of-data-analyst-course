# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:10+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S1096751620300014 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T23:10+07:00 | L2 | https://aura.abdn.ac.uk/items/e66a001f-97b7-4518-8291-1e3bd345bebd | 200 | text/html | 407 | html-text | 222 | partial | short text (222 words) |
| 2026-11-06T23:10+07:00 | L2 | https://figshare.com/articles/journal_contribution/The_scalable_implementation_of_predictive_learning_analytics_at_a_distance_learning_university_Insights_from_a_longitudinal_case_study/23779401 | 202 | text/html | 1 | html-text | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters); exploded layout (100% of lines have ≤2 characters) |
| 2026-11-06T23:10+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1016/j.iheduc.2020.100725 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T23:10+07:00 | L4 | https://api.crossref.org/works/10.1016/j.iheduc.2020.100725 | 200 | application/json | 22 | json-metadata | 58 | metadata | bibliographic record |
| 2026-11-06T23:10+07:00 | L4 | https://api.openalex.org/works/doi:10.1016/j.iheduc.2020.100725 | 200 | application/json | 19 | json-metadata | 125 | metadata | bibliographic record |
| 2026-11-06T23:10+07:00 | L1 | https://aura.abdn.ac.uk/server/api/core/bitstreams/612ed1d9-645d-4fe2-9f73-bd9ae2b0b890/content | 200 | application/pdf | 791 | pdfkit | 11315 | readable | – |
