# Research Agent Brief

Every research subagent reads this brief before its task card. It fixes the rules and the file formats that the gate scripts check. Paths are relative to the project root; `R=.agents/skills/research-report/scripts`.

## 1. The Core Rule: Record Every Crawl on Disk

What is learned from the web counts once it is written to `reports/milestone-5/research/`. Save each step **immediately**, before the next tool call:

1. After each search: `$R/trail.py log-search --base reports/milestone-5 --task <ID> --query "…" --kept "<url> → S101; …" --dropped "<url> (reason); …"` (row number and date are filled in).
2. Register a new source: `$R/trail.py register --base reports/milestone-5 --id S101 --slug <slug> --source "<short description>" --url <url> --item <outline item or new> --type primary`.
3. Fetch it with `fetch.py` (section 2). It writes `sources/<ID>-<slug>/crawl.md`, `raw.*` and `attempts.md`, and sets the register status.
4. `$R/trail.py comprehension --base reports/milestone-5 --id S101` creates `comprehension.md` with the six headings; read `crawl.md` (`grep -n`, `sed -n` on long files) and fill each heading.
5. Add each claim with `$R/trail.py claim --base reports/milestone-5 --part <N> --source S101 --claim "<claim in my words>" --anchor '"<quote copied from crawl.md>"' --files <report file>`; it assigns the next claim ID and writes the row once the anchor is found verbatim in `crawl.md`.
6. For the APA entry: `$R/fetch.py meta …` (when the crawl still lacks a bibliographic record), then `$R/trail.py apa --base reports/milestone-5 --id S101 --write`; check the draft against the source page.
7. Then move to the next query or source.

Claims cite saved sources only: a page counts as a source once its crawl.md is on disk.

## 2. Fetching: Readable Text, Retries and Fallbacks

```bash
./venv/bin/python $R/fetch.py get --base reports/milestone-5 --id S101 --slug short-name --task T05 --part 1 <URL | DOI | arXiv:ID>
```

`fetch.py` downloads with retries (backoff on 429/5xx, a second user agent on 403), converts PDF, HTML and JSON to readable text, scores readability, and walks the fallback ladder until one copy is readable: **L1** the URL → **L2** other copies of the same work (arXiv HTML/PDF, open-access copies listed by OpenAlex and Semantic Scholar) → **L3** the Wayback Machine → **L4** a metadata record (Crossref, OpenAlex). Give a DOI or arXiv ID whenever one exists: it unlocks L2 and L4. Exit codes and what to do next:

| Exit | Status written | Next step |
| :---- | :---- | :---- |
| 0 | `ok` → register `fetched` | Read crawl.md and write comprehension.md |
| 3 | `partial` (short text, lost ligatures, or metadata only) | Use what is there; quote only text that is present; note the gap in Open questions |
| 4 | `blocked` / `error` | **L5:** try `WebFetch` on the best URL with a verbatim prompt and append its output as a fetch block; for a PDF that no converter reads, use `Read` with page ranges and append the text you read; otherwise search for another source that states the same facts (`fetch.py find "<title>"` or `WebSearch`), log it in `search-log.md` as "replacement for S101", and give it a new ID. Keep the failed folder: it documents the gap |

Further commands: `fetch.py meta` (bibliographic record only: authors, venue, pages, DOI, citation counts for the APA entry and "citation traction"), `fetch.py find "<title>"` (other versions and DOIs), `fetch.py get … --append` (a second page of the same source becomes `<!-- fetch 2: … -->` in the same crawl.md). crawl.md text stays exactly as converted; every later page or fetch is appended as its own block.

When `WebFetch` is used, ask for verbatim text: *"Return verbatim, word for word, the passages about X, Y, Z with the surrounding sentence; keep the wording exact and keep every citation marker such as [93], with the reference-list entries they point to. Also return title, authors, venue, year, DOI."* Save its output unedited to a scratch file, then append it with `fetch.py webfetch --base <task> --id <ID> --url <url> --prompt "<the exact prompt>" --text-file <file> [--status ok|partial]`: the block gets its number, tool, prompt and time, and the crawl and register statuses are raised in step.

## 3. Source IDs and Statuses

- Seeds S001–S0nn from the outline are in `sources.md` with status `to-fetch`: keep their ID and slug when you fetch them, and change the status.
- New sources take the next free ID in your part's block (Part 1 S100–S199, Part 2 S200–S299, Part 3 S300–S399, Part 4 S400–S499, Part 5 S500–S599, Part 6 S600–S699, Part 7 S700–S799, Part 8 S800–S899, Part 9 S900–S999, Part 10 S1000–S1099, Part 11 S1100–S1199, Part 12 S1200–S1299, Part 13 S1300–S1399, Part 14 S1400–S1499). Check `sources.md` first, so each source is registered once; mark true duplicates `duplicate` with "duplicate of Sxxx".
- `sources.md` rows have 8 columns (`| S101 | slug | Short description | URL | outline item or "new" | primary or secondary | fetched | APA 7 entry |`); `trail.py register` writes and updates them.
- Status: `fetched` (ok), `partial` (some content missing), `blocked` (paywall, robots, JavaScript only), `error`. Blocked or error sources keep their folder and files as a record of the gap; **claims cite `fetched` and `partial` sources**.

## 4. File Formats (checked by `check_trail.py`)

`comprehension.md` has exactly these six `## ` headings, each with content:

```
# S101 – <short title>
## Summary in my own words      3–6 sentences
## Key facts                    - <fact> – "<verbatim quote from crawl.md, at least 8 characters>"
## Used in                      planned report files
## Against reference.md     confirms / extends / contradicts, citing the exact outline passage
## Reliability                  primary or secondary; author or institution; venue; citation traction (with "as of" date)
## Open questions               what still needs another source, or "None"
```

A work that the source itself cites appears in Key facts by first author with initials, year and venue, with its own source ID when `sources.md` holds it: `- Liu Y., Jourabloo & Liu X. (CVPR 2018; S206) fuse depth and rPPG – "…"`. Read the registered work's own crawl for the facts the report will state about it.

Every `"…"` quote in Key facts is checked verbatim against `crawl.md` (whitespace collapsed, curly quotes straightened): copy and paste each quote exactly as it stands.

`part<N>-claims.md` rows (6 columns, no `|` inside cells; write `\|` if a quote holds one):

```
| C1-001 | <claim in my words> | "<verbatim quote anchor ≥ 8 characters>" | S101 | primary | 01-01-2-file.md |
```

Claim IDs run on per part. Read the file first and continue from the last number.

`part<N>-synthesis.md`: one `## <report file name>` entry per file of your card with **Claims** (IDs in the order the text should use them), **Outline** (3–6 bullets, the paragraph plan), **Conflicts with the outline** (each one, or "None") and **Gaps** (or "None").

## 5. Research Rules

- Prefer primary sources: the standard or its catalogue, the paper (arXiv HTML, open-access PDF), the official government or institution site. Fall back to secondary sources (encyclopedias, news, vendor blogs) when the primary sources are unreachable, and label them `secondary` with the reason.
- A new source meets the outline's selection criteria if it states them (known authors or institutions, citation traction, reputable venue).
- Record point-in-time figures (counts, adoption numbers, citation counts) with their "as of" date.
- Compare every fact with the outline. Every contradiction goes into "Against …" and into the synthesis under "Conflicts with the outline" for the human to decide.
- Stay within the card's questions; note side findings under Open questions.
- Budget: about 6–12 sources per task. Depth on the key sources beats breadth.

## 6. Before Returning

1. Run `./venv/bin/python $R/check_trail.py --base reports/milestone-5 --task <task ID>` and fix every ERROR.
2. Return **at most 5 lines**: sources fetched, partial, blocked and new; claims added; the gate result; conflicts with the outline (count and one-line gist); unanswered questions. Keep page content on disk, where the evidence lives.
