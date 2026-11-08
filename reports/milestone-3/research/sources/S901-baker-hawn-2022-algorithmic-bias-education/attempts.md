# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T08:30+07:00 | L1 | https://linkinghub.elsevier.com/retrieve/pii/S1560429226002350 | 200 | text/html | 2 | html-text | 2 | unreadable | exploded layout (80% of lines have ≤2 characters) |
| 2026-11-06T08:30+07:00 | L3 | https://web.archive.org/web/2id_/https://doi.org/10.1007/s40593-021-00285-9 | 429 | text/html | 0 | – | 0 | error | HTTP 429 |
| 2026-11-06T08:30+07:00 | L4 | https://api.crossref.org/works/10.1007/s40593-021-00285-9 | 200 | application/json | 47 | json-metadata | 39 | metadata | bibliographic record |
| 2026-11-06T08:30+07:00 | L4 | https://api.openalex.org/works/doi:10.1007/s40593-021-00285-9 | 200 | application/json | 21 | json-metadata | 284 | metadata | bibliographic record |
| 2026-11-06T08:30+07:00 | L1 | https://idvyorynw6xy.compat.objectstorage.us-ashburn-1.oraclecloud.com/cos-prod-osf-1-files-ash/e81429030c2b2dc77a772a8ca38d1ad93e95e422724185766fb63734abadd0fc?response-content-disposition=attachment%3B+filename%3D%22AlgorithmicBiasInEducation_rsb3.7.pdf%22%3B+filename%2A%3DUTF-8%27%27AlgorithmicBiasInEducation_rsb3.7.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=8a1e5869d3122814cba7bd4265a84ad444199855%2F20261106%2Fus-ashburn-1%2Fs3%2Faws4_request&X-Amz-Date=20261106T013012Z&X-Amz-Expires=60&X-Amz-SignedHeaders=host&X-Amz-Signature=25b865bff8720736147dc7425e92acc1e0ea13291c3a30977cd4fd5d781e1de7 | 200 | application/octet-stream | 431 | pdfkit | 18456 | readable | – |
