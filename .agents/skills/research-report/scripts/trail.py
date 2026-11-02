"""Write research-trail entries exactly: search-log rows, register rows, claims, comprehension skeletons, APA entries.

Usage (all with --base TASK):
  trail.py log-search   --task T05 --query "…" --kept "url → S101; …" --dropped "url (reason); …"
  trail.py register     --id S101 [--slug s] [--source "…"] [--url u] [--item 3|new] [--type primary|secondary]
                        [--status fetched|partial|blocked|error|to-fetch|duplicate] [--apa "…"]
  trail.py claim        --part 1 --source S101 --claim "…" --anchor '"verbatim quote"' [--type primary] [--files f.md]
  trail.py comprehension --id S101                 create comprehension.md with the six headings, title from crawl.md
  trail.py apa          --id S101 [--write]        APA 7 entry drafted from the metadata in crawl.md (fetch.py meta)
  trail.py link         --claims C1-001,C2-040 --files 05-01-key-findings.md [--remove]   add (or remove) a report file

Each command does the bookkeeping a person would otherwise type: the next row number and today's date, the next
claim ID of the part, escaped pipes, the register's 8 columns. `claim` writes only when the source is usable and
every quote anchor occurs verbatim in its crawl.md; `register` adds a row or updates the named fields of an
existing one. Exit code 1 when an entry is refused.

Every command holds an exclusive lock on research/.trail.lock while it reads and rewrites the shared files
(search-log.md, sources.md, partN-claims.md), so research agents working on different parts can run at the same time.
"""

from __future__ import annotations

import argparse
import fcntl
import re
import sys
from datetime import date
from pathlib import Path

from common import (QUOTE, TEMPLATES, USABLE, base_dir, load_claims, load_plan, load_register, norm, read_crawl,
                    source_folder, split_cells, table_rows)

COLUMNS = ["id", "slug", "source", "url", "item", "type", "status", "apa"]


def cell(text: str) -> str:
    return (text or "–").replace("\n", " ").replace("|", "\\|")


def append_row(path: Path, cells: list[str]):
    """Insert a row after the last row of the file's first table (later sections such as the reference map stay below)."""
    lines = path.read_text(encoding="utf-8").rstrip("\n").split("\n")
    start = next(i for i, ln in enumerate(lines) if ln.startswith("|"))
    end = start
    while end + 1 < len(lines) and lines[end + 1].startswith("|"):
        end += 1
    lines.insert(end + 1, "| " + " | ".join(cells) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def log_search(base, a):
    path = base / "research" / "search-log.md"
    nums = [int(r[0]) for r in table_rows(path) if r[0].isdigit()]
    n = max(nums, default=0) + 1
    append_row(path, [str(n), a.task, str(date.today()), cell(a.query), cell(a.kept), cell(a.dropped)])
    print(f"search-log.md: row {n} ({a.task})")
    return 0


def register(base, a):
    path = base / "research" / "sources.md"
    lines = path.read_text(encoding="utf-8").split("\n")
    given = {k: getattr(a, k) for k in COLUMNS if getattr(a, k, None)}
    for i, ln in enumerate(lines):
        cells = split_cells(ln) if ln.startswith("|") else []
        if cells and cells[0] == a.id:
            cells += ["–"] * (8 - len(cells))
            for k, v in given.items():
                cells[COLUMNS.index(k)] = v
            lines[i] = "| " + " | ".join(cell(c) for c in cells[:8]) + " |"
            path.write_text("\n".join(lines), encoding="utf-8")
            print(f"sources.md: {a.id} updated ({', '.join(k for k in given if k != 'id')})")
            return 0
    missing = [k for k in ("slug", "source", "url") if k not in given]
    if missing:
        print(f"ERROR new source {a.id} needs --{' --'.join(missing)}")
        return 1
    row = [given.get(k, d) for k, d in zip(COLUMNS, ["", "", "", "", "new", "primary", "to-fetch", "–"])]
    append_row(path, [cell(c) for c in row])
    print(f"sources.md: {a.id} added ({row[6]})")
    return 0


def claim(base, a):
    reg, _ = load_register(base)
    entry = reg.get(a.source)
    if not entry or entry["status"] not in USABLE:
        print(f"ERROR {a.source}: status '{entry['status'] if entry else 'unknown'}'; claims cite fetched or partial sources")
        return 1
    folder = source_folder(base, a.source, entry["slug"])
    body = norm(read_crawl(folder)[1]) if (folder / "crawl.md").exists() else ""
    anchors = QUOTE.findall(a.anchor)
    if not anchors:
        print('ERROR the anchor needs at least one "…" quote of 8 or more characters')
        return 1
    for q in anchors:
        if norm(q) not in body:
            print(f"ERROR anchor not found verbatim in {folder.name}/crawl.md: \"{q[:70]}\" (copy it from the file)")
            return 1
    path = base / "research" / f"part{a.part}-claims.md"
    nums = [int(c["id"].split("-")[1]) for c in load_claims(base) if c["part"] == a.part]
    cid = f"C{a.part}-{max(nums, default=0) + 1:03d}"
    append_row(path, [cid, cell(a.claim), cell(a.anchor), a.source, a.type, cell(a.files)])
    print(f"part{a.part}-claims.md: {cid} ← {a.source}")
    return 0


def comprehension(base, a):
    reg, _ = load_register(base)
    entry = reg.get(a.id)
    if not entry:
        print(f"ERROR {a.id} is not in sources.md")
        return 1
    folder = source_folder(base, a.id, entry["slug"])
    path = folder / "comprehension.md"
    if path.exists():
        print(f"{path.name} exists; kept")
        return 0
    header, body = read_crawl(folder) if (folder / "crawl.md").exists() else ({}, "")
    title = next((ln.split(":", 1)[1].strip() for ln in body.splitlines()[:40] if ln.startswith("title:")), entry["source"])
    outline = Path(load_plan(base).get("plan", {}).get("outline", "reference.md")).name
    text = (TEMPLATES / "research" / "comprehension.md").read_text(encoding="utf-8")
    text = text.replace("Sxxx – <short title>", f"{a.id} – {title[:90]}").replace("{{outline_name}}", outline)
    path.write_text(text, encoding="utf-8")
    print(f"{folder.name}/comprehension.md created; fill each heading from crawl.md")
    return 0


def metadata(body: str) -> dict:
    """Fields of the Crossref / OpenAlex blocks that fetch.py meta writes (first value wins)."""
    out = {}
    for ln in body.splitlines():
        m = re.match(r"^([a-z][\w \-()]*?): (.*)$", ln.strip())
        if m and m.group(2).strip() and m.group(1) not in out:
            out[m.group(1)] = m.group(2).strip()
    return out


def apa_authors(raw: str) -> str:
    people = [p.strip() for p in raw.split(";") if p.strip()]
    def initials(given):
        return " ".join(f"{g[0]}." for g in re.split(r"[\s.-]+", given) if g)
    names = []
    for p in people:
        if "," in p:
            family, given = [x.strip() for x in p.split(",", 1)]
        else:
            parts = p.split()
            family, given = parts[-1], " ".join(parts[:-1])
        names.append(f"{family}, {initials(given)}".strip(", "))
    if len(names) > 20:
        names = names[:19] + ["…", names[-1]]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + ", & " + names[-1] if names else ""


def apa(base, a):
    reg, _ = load_register(base)
    entry = reg.get(a.id)
    folder = source_folder(base, a.id, entry["slug"]) if entry else None
    if not folder or not (folder / "crawl.md").exists():
        print(f"ERROR {a.id}: no crawl.md (run fetch.py meta first)")
        return 1
    m = metadata(read_crawl(folder)[1])
    year = (m.get("published") or m.get("publication date") or m.get("year") or "n.d.")[:4]
    title = m.get("title", entry["source"]).rstrip(".")
    venue = m.get("container") or m.get("venue") or ""
    vol, iss = m.get("volume", ""), m.get("issue", "")
    pages = m.get("pages", "").replace("-", "–").strip("–")
    doi = (m.get("doi", "") or "").replace("https://doi.org/", "")
    kind = m.get("type", "")
    ref = f"{apa_authors(m.get('authors', ''))} ({year}). "
    if "proceedings" in kind or "conference" in venue.lower() or "proceedings" in venue.lower():
        ref += f"{title}. In *{venue}*" + (f" (pp. {pages})" if pages else "") + "."
    elif venue:
        ref += f"{title}. *{venue}*" + (f", *{vol}*" if vol else "") + (f"({iss})" if iss else "") + (f", {pages}" if pages else "") + "."
    else:
        ref += f"*{title}*."
    ref += f" https://doi.org/{doi}" if doi else (f" {entry['url']}" if entry.get("url", "–") != "–" else "")
    print(ref)
    if a.write:
        a.apa = ref
        for k in ("slug", "source", "url", "item", "type", "status"):
            setattr(a, k, None)
        return register(base, a)
    return 0


def link(base, a):
    ids = {c.strip() for c in (a.claims or "").split(",") if c.strip()}
    found = set()
    for path in sorted((base / "research").glob("part*-claims.md")):
        lines = path.read_text(encoding="utf-8").split("\n")
        changed = False
        for i, ln in enumerate(lines):
            cells = split_cells(ln) if ln.startswith("|") else []
            if cells and cells[0] in ids and len(cells) >= 6:
                files = [f.strip() for f in re.split(r",\s*|;\s*", cells[5]) if f.strip() and f.strip() not in ("–", "-")]
                for f in a.files.split(","):
                    if a.remove:
                        files = [x for x in files if x != f.strip()]
                    elif f.strip() and f.strip() not in files:
                        files.append(f.strip())
                cells[5] = ", ".join(files) or "–"
                lines[i] = "| " + " | ".join(cell(c) for c in cells[:6]) + " |"
                found.add(cells[0])
                changed = True
        if changed:
            path.write_text("\n".join(lines), encoding="utf-8")
    missing = sorted(ids - found)
    print(f"{'unlinked' if a.remove else 'linked'} {len(found)} claim(s) {'from' if a.remove else 'to'} {a.files}"
          + (f"; not found: {', '.join(missing)}" if missing else ""))
    return 1 if missing else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["log-search", "register", "claim", "comprehension", "apa", "link"])
    ap.add_argument("--base", required=True)
    for opt in ("task", "query", "kept", "dropped", "id", "slug", "source", "url", "item", "status", "apa", "claim",
                "anchor", "files", "claims"):
        ap.add_argument(f"--{opt}")
    ap.add_argument("--type", default=None)
    ap.add_argument("--part", type=int)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--remove", action="store_true", help="link: remove the report file from the claims instead")
    a = ap.parse_args()
    base = base_dir(a.base)
    with open(base / "research" / ".trail.lock", "w") as lock:   # one writer at a time across parallel agents
        fcntl.flock(lock, fcntl.LOCK_EX)
        if a.command == "claim":
            a.type = a.type or "primary"
            return claim(base, a)
        return {"log-search": log_search, "register": register, "comprehension": comprehension, "apa": apa,
                "link": link}[a.command](base, a)


if __name__ == "__main__":
    sys.exit(main())
