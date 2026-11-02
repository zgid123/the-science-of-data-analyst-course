# Research Trail

Everything learned from the web for the report is saved here at the moment it is found. The report in `../report/` is written only from these files.

| File | Layer | Content |
| :---- | :---- | :---- |
| `search-log.md` | 1. Search | Every search query, with the results kept and dropped |
| `sources/Sxxx-slug/crawl.md` | 2. Crawl | The source as readable text under a metadata header; `raw.*` holds the original file and `attempts.md` every fetch attempt |
| `sources/Sxxx-slug/comprehension.md` | 3. Comprehension | Summary, key facts with quote anchors, use in the report, comparison with the outline, reliability, open questions |
| `sources.md` | Register | One row per source ID with its status and APA 7 entry; the reference map after finishing |
| `partN-claims.md` | Claims | One row per claim, pointing to a source ID and a verbatim quote anchor in its `crawl.md` |
| `partN-synthesis.md` | Part comprehension | Claim IDs per planned report file, outline, conflicts, gaps |
| `AGENT_BRIEF.md` | Rules | What every research subagent reads first |
| `spot-check.md`, `style-review.md` | Finishing | Fact spot-check and style read-through logs |

Chain from a report sentence to its evidence:
`[n] → reference entry n → sources.md Sxxx → partN-claims.md → comprehension.md → crawl.md quote (→ raw.*)`

Outline: `{{outline}}`. Source ID blocks: {{blocks}}.
