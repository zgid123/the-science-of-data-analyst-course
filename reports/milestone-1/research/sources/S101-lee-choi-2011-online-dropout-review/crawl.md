---
id: S101
url: https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y
requested: 10.1007/s11423-010-9177-y
fetched: 2026-11-05T20:57+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T04
part: 1
raw: raw.json (12 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y (metadata, 63 words)
---
source: OpenAlex
title: A review of online course dropout research: implications for practice and future research
authors: Youngju Lee; Jaeho Choi
institutions: University of Virginia
venue: Educational Technology Research and Development
publication date: 2010-11-24
volume: 59
issue: 5
pages: 593–618
doi: https://doi.org/10.1007/s11423-010-9177-y
cited_by_count (OpenAlex): 771
type: article
location: https://doi.org/10.1007/s11423-010-9177-y (open access: False)
location: https://link.springer.com/content/pdf/10.1007/s11423-010-9177-y.pdf (open access: False)

<!-- fetch 2: https://www.researchgate.net/profile/Youngju_Lee/publication/227246914_A_review_of_online_course_dropout_research_Implications_for_practice_and_future_research/links/0f317530de159c4d98000000/A-review-of-online-course-dropout-research-Implications-for-practice-and-future-research.pdf | fetch.py none | 2026-11-05T20:57+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://www.researchgate.net/profile/Youngju_Lee/publication/227246914_A_review_of_online_course_dropout_research_Implications_for_practice_and_future_research/links/0f317530de159c4d98000000/A-review-of-online-course-dropout-research-Implications-for-practice-and-future-research.pdf: error (HTTP 403)
- L3 https://web.archive.org/web/2id_/https://www.researchgate.net/profile/Youngju_Lee/publication/227246914_A_review_of_online_course_dropout_research_Implications_for_practice_and_future_research/links/0f317530de159c4d98000000/A-review-of-online-course-dropout-research-Implications-for-practice-and-future-research.pdf: error (HTTP 404)

<!-- fetch 3: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11423-010-9177-y?fields=title,abstract,year,venue,authors,citationCount | fetch.py json-metadata | 2026-11-05T20:57+07:00 | metadata -->
source: Semantic Scholar
title: A review of online course dropout research: implications for practice and future research
authors: YoungJun Lee; Jaeho Choi
year: 2011
venue: 
citationCount (Semantic Scholar): 755
externalIds: 
openAccessPdf: 

<!-- fetch 4: https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y?select=abstract_inverted_index | fetch.py json-metadata | 2026-11-05T20:59+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://api.openalex.org/works/doi:10.1007/s11423-010-9177-y?select=abstract_inverted_index: unreadable (few letters or digits (0% alphanumeric, 0% letters))
