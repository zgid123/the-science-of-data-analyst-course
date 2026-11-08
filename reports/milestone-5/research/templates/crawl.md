---
id: Sxxx
url: <url actually read>
requested: <url, DOI or arXiv ID asked for>
fetched: <YYYY-MM-DDTHH:MM+TZ>
tool: fetch.py (curl + <converter>; ladder L1-L4)   # or WebFetch, or Read (PDF pages)
fetch_prompt: "none (full text conversion, not a model extract)"   # the exact WebFetch prompt when WebFetch is used
status: ok                # ok | partial | blocked | error
task: <T05, …>            # the research task that fetched it
part: <1-9>
raw: raw.pdf (… KB)       # or "none (<reason>)"
---
<converted or verbatim text below this line, kept exactly as converted>
