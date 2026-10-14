# Source / license / access evidence — 14 October 2026

Official pages inspected through web browsing:

1. OULAD UCI landing page, DOI 10.24432/C5KK69; authors Kuzilek, Hlosta, Zdrahal; CC BY 4.0. Saved `oulad-uci.html`, HTTP 200 via direct retrieval.
2. OU data dictionary: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ . Accessible through web browsing after following the OULAD page link from https://research.stem.open.ac.uk/ouanalyse/dataset/ . Direct HTML fetch from execution environment returned 403; `source_access.json` records that failure. No fabricated local HTML snapshot is supplied.
3. UCI Predict Students' Dropout and Academic Success: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success ; DOI 10.24432/C5MC89; CC BY 4.0. Saved `dropout-uci.html`. Metadata, not raw, inspected for screening.
4. UCI Student Performance: https://archive.ics.uci.edu/dataset/320/student+performance ; DOI 10.24432/C5TG7T; CC BY 4.0. Saved `performance-uci.html`. Metadata, not raw, inspected for screening.

Access limitations observed, not silently repaired:

- OU Download dataset target https://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip returned 404 in the web tool.
- Legacy checksum URL https://analyse.kmi.open.ac.uk/open-dataset/downloadCheckSum redirected to the OU Analyse homepage; it did not provide an MD5 checksum to compare.
- UCI Download target https://archive.ics.uci.edu/static/public/349/open+university+learning+analytics+dataset.zip timed out in the web tool. Direct HTTP HEAD returned 200; response recorded in `uci-download-head.txt`. The binary was not redownloaded. This is endpoint reachability evidence, not proof that its bytes equal the packaged local archive.

Collection reused the pre-existing local `datasets/oulad/anonymisedData.zip` without changes. Original acquisition date and provider version are unknown. Archive/member SHA-256 fingerprints plus CRC establish the exact local version and internal integrity. All seven extracted local CSV files match archive member hashes; see `local_source_checks.json`.

Semantics required by the report were checked against the OU dictionary: relative event/deadline days, banked assessment flag, per-day click counts, and final outcome role. Actual names/labels take precedence in runnable mappings: raw `module_presentation_length` versus dictionary `length`; raw `Withdrawn` versus dictionary prose `Withdrawal`. These discrepancies are documented, not corrected in raw.

No candidate dataset was merged into OULAD; no shared person keys or compatible intervention records were verified. No claim that absent submission records mean lack of effort, that score existed at submission time, or that observational risk identifies an effective intervention.
