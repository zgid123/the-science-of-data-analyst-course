# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-05T20:57+07:00 | L1 | https://link.springer.com/10.1007/s11423-010-9177-y | 200 | text/html | 2 | html-text | 35 | unreadable | almost no text (35 words) |
| 2026-11-05T20:57+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1007/s11423-010-9177-y | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-05T20:57+07:00 | L4 | https://api.crossref.org/works/10.1007/s11423-010-9177-y | 200 | application/json | 15 | json-metadata | 49 | metadata | bibliographic record |
| 2026-11-05T20:57+07:00 | L4 | https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y | 200 | application/json | 12 | json-metadata | 63 | metadata | bibliographic record |
| 2026-11-05T20:57+07:00 | L1 | https://www.researchgate.net/profile/Youngju_Lee/publication/227246914_A_review_of_online_course_dropout_research_Implications_for_practice_and_future_research/links/0f317530de159c4d98000000/A-review-of-online-course-dropout-research-Implications-for-practice-and-future-research.pdf | 403 | text/html; charset=utf-8 | 19 | – | 0 | error | HTTP 403 |
| 2026-11-05T20:57+07:00 | L3 | https://web.archive.org/web/2id_/https://www.researchgate.net/profile/Youngju_Lee/publication/227246914_A_review_of_online_course_dropout_research_Implications_for_practice_and_future_research/links/0f317530de159c4d98000000/A-review-of-online-course-dropout-research-Implications-for-practice-and-future-research.pdf | 404 | text/html | 5 | – | 0 | error | HTTP 404 |
| 2026-11-05T20:57+07:00 | L1 | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11423-010-9177-y?fields=title,abstract,year,venue,authors,citationCount | 200 | application/json | 0 | json-metadata | 28 | metadata | bibliographic record |
| 2026-11-05T20:59+07:00 | L1 | https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y?select=abstract_inverted_index | 200 | application/json | 0 | json-metadata | 0 | unreadable | few letters or digits (0% alphanumeric, 0% letters) |
