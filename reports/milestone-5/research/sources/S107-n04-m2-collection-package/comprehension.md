# S107 – N04 (2026). Milestone 2 data collection package

## Summary in my own words

The Milestone 2 Data Collection Package lets anyone re-create the team's raw OULAD copy and check its structure. Its README gives two commands: one downloads the figshare archive, checks size and SHA-256 and extracts the seven CSV tables unchanged; the other runs the structural checks. The metadata include the source and licence sheet, the data dictionary copied from the descriptor and a generated structure report with rows, keys, duplicates, missing values, types and the selection conditions. Nothing in the package cleans or transforms the data.

## Key facts

- Purpose – "Nothing in this package cleans, filters, imputes or transforms the data"
- Archive check – "checks its size (46,750,706 bytes) and SHA-256"
- Broken provider link – "returned HTTP 404 on 2026-11-05"
- Licence – "Creative Commons Attribution 4.0 International (CC BY 4.0)"
- Version – "figshare version 1 (the provider page offers"
- Dictionary definition of score – "score from 0 to 100; below 40 is interpreted as Fail"
- Structure report generated – "Generated 2026-11-05T18:33:01Z by `src/verify_structure.py`"
- Empty unregistration day – "empty for students who completed; Withdrawal as final_result for those who unregistered"
- Data descriptor: Kuzilek J., Hlosta & Zdrahal (Scientific Data 2017; S002) – "cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171"

## Used in

04-01-dataset-selection.md (provenance, version, licence, reproducible acquisition), 05-00-dataset-description.md (data dictionary, structure report), and the Final Project Package description (Part 14 appendix).

## Against reference.md

Confirms outline Section 4's "provenance, version and licence of OULAD" and Section 5's tables, keys and sizes; the figures match Milestone 2 Table 6.1. No contradiction.

## Reliability

Primary: the team's own package files at commit 19d35a4 (README, data dictionary, source sheet, generated structure report). The structure report is script output, so its counts are reproducible from the raw files. No citation traction, as of 2026-11-08.

## Open questions

None.
