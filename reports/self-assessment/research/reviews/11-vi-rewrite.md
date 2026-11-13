# Decisions on the round-3 re-test flags

Flags from `10-vi-reader-test.md` (13: clarity 1/2/3 = 1/11/1). "EN+VI" = fixed in the English source and the twin.

| # | Decision | Change |
| :-- | :-- | :-- |
| 1 | Fixed VI | Cliff's delta named first, then what changed by 0.004. |
| 2 | Fixed EN+VI | "the remaining differences are stated as limitations in the reports". |
| 3 | Fixed VI | Actor first: "Nhóm chỉ dùng dữ liệu huấn luyện để quyết định những biến nào cần thêm biến chỉ báo…". |
| 4 | Fixed EN+VI | "all 22 checks of the preparation pipeline". |
| 5 | Fixed EN+VI | "editors other than Microsoft Word, such as Google Docs". |
| 6 (clarity 1) | Fixed EN+VI | Deck named (Milestone 5 presentation deck with appendix slides) and its state said plainly: Vietnamese version not yet final, completed once the slide count is settled. Open user decision (slide count). |
| 7 | Partly fixed EN+VI | "recorded in the Milestone 5 Change Log". Ratings of Milestones 3 and 4 kept: the Milestone 3 report already tests on all 13 runs of 2014 with paired-run flags (Milestone 3 Section 6.3), so its Change Log has no missing entry for its own scope. |
| 8 | Fixed EN+VI | Appendix I explains where length lowers a rating (criteria on presentation or report quality: Milestones 1, 4, 5) and why Milestones 2 and 3 carry it in Table A.2 only; Table A.2 Milestone 2 row also names the downgraded criterion's reason. |
| 9 | Fixed EN+VI | Table A.2 Milestone 4: Level 2 optional, not required for 100 points, specified but not run. |
| 10 | Fixed EN+VI | 70% baseline: an assumption about the scenario university, not a measured figure. |
| 11 | Fixed VI | Parenthesis replaced by a colon and a second sentence. |
| 12 | Fixed EN+VI | "about 22 pages in English, long for a proposal, although the brief sets no page range". |
| 13 | Fixed EN+VI | Day 14 is the indicator's population; the contact lists are drawn up on days 13 and 27. |

Checks: `check_parity.py --lang vi` 0 errors, 1 accepted warning; `check_pairs.py` 0 pairs with differences (the '70%' exception removed, as both languages now carry it); twins marked.
