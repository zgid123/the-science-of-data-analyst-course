---
id: S005
url: https://api.openalex.org/works/doi:10.1145/3027385.3027449
requested: 10.1145/3027385.3027449
fetched: 2026-11-02T00:47+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T03
part: 5
raw: raw.json (12 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1145/3027385.3027449 (metadata, 154 words)
---
source: OpenAlex
title: Ouroboros
authors: Martin Hlosta; Zdeněk Zdráhal; Jaroslav Zendulka
institutions: Brno University of Technology; The Open University
venue: International Conference on Learning Analytics and Knowledge (LAK)
publication date: 2017-02-27
volume: None
issue: None
pages: 6–15
doi: https://doi.org/10.1145/3027385.3027449
cited_by_count (OpenAlex): 113
type: conference-paper
location: https://doi.org/10.1145/3027385.3027449 (open access: False)
location: https://oro.open.ac.uk/49731/1/paper.pdf (open access: False)

abstract:
This paper focuses on the problem of identifying students, who are at risk of failing their course. The presented method proposes a solution in the absence of data from previous courses, which are usually used for training machine learning models. This situation typically occurs in new courses. We present the concept of a "self-learner" that builds the machine learning models from the data generated during the current course. The approach utilises information about already submitted assessments, which introduces the problem of imbalanced data for training and testing the classification models.

<!-- fetch 2: https://oro.open.ac.uk/49731/1/paper.pdf | fetch.py none | 2026-11-02T00:49+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://oro.open.ac.uk/49731/1/paper.pdf: error (HTTP 403)
- L3 https://web.archive.org/web/2id_/https://oro.open.ac.uk/49731/1/paper.pdf: error (HTTP 403)

<!-- fetch 3: https://core.ac.uk/download/83955564.pdf | fetch.py none | 2026-11-02T00:50+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://core.ac.uk/download/83955564.pdf: error (HTTP 403)
- L3 https://web.archive.org/web/2id_/https://core.ac.uk/download/83955564.pdf: error (HTTP 404)
