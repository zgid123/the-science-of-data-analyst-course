r"""Check the research trail: every source is saved, understood and quoted faithfully.

Usage:
    check_trail.py --base TASK --task T05          # sources whose crawl.md says task: T05 (+ its search-log rows)
    check_trail.py --base TASK --ids S101,S102     # explicit IDs (ranges: S100-S199)
    check_trail.py --base TASK --part 1            # part1-claims.md and the sources it cites
    check_trail.py --base TASK --all               # everything, plus the reference map

ERROR  sources.md row whose folder, crawl.md or comprehension.md is missing (status fetched/partial/blocked/error);
       crawl.md header without id/url/fetched/tool/status/task, or with an id that differs from the folder;
       comprehension.md with a missing or empty template heading (Summary in my own words, Key facts, Used in,
       Against <outline>, Reliability, Open questions);
       a quoted fact in comprehension.md "Key facts" that does not occur verbatim in crawl.md;
       claim whose source ID is unknown, still to-fetch, blocked or in error (orphan claim);
       claim without a quote anchor, or whose anchor does not occur verbatim in the source's crawl.md;
       --task: no search-log.md row for the task;
       --all: reference map entry ([n] → Sxxx) pointing to an unknown or unusable source.
WARN   fetched source with no claim; claim not yet linked to a report file; crawl.md status that disagrees with
       the register (ok ↔ fetched, partial ↔ partial, blocked ↔ blocked, error ↔ error).
Matching is verbatim after collapsing whitespace and straightening typographic quotes; "\|" inside a cell is an
escaped pipe. Exit code 1 on any ERROR.
"""

import argparse
import re
import sys

from common import (QUOTE, SAVED, SOURCE_ID, USABLE, base_dir, load_claims, load_register, norm, read_crawl,
                    source_folder, table_rows)

HEADINGS = ["Summary in my own words", "Key facts", "Used in", "Against", "Reliability", "Open questions"]
HEADER_FIELDS = ["id", "url", "fetched", "tool", "status", "task"]
CRAWL_TO_REGISTER = {"ok": "fetched", "partial": "partial", "blocked": "blocked", "error": "error"}


def comprehension_sections(path):
    parts = re.split(r"^## +(.+?)\s*$", path.read_text(encoding="utf-8"), flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def expand_ids(spec):
    ids = set()
    for item in spec.split(","):
        item = item.strip()
        m = re.fullmatch(r"S(\d{3})-S?(\d{3})", item)
        if m:
            ids |= {f"S{i:03d}" for i in range(int(m.group(1)), int(m.group(2)) + 1)}
        elif item:
            ids.add(item)
    return ids


def check_source(base, sid, entry, errors, warns, crawls):
    folder = source_folder(base, sid, entry["slug"])
    if not folder.is_dir():
        errors.append(f"{sid}: folder {folder.name}/ missing")
        return
    for name in ("crawl.md", "comprehension.md"):
        if not (folder / name).exists():
            errors.append(f"{sid}: {name} missing")
    if not (folder / "crawl.md").exists():
        return
    header, body = read_crawl(folder)
    if header is None:
        errors.append(f"{sid}: crawl.md has no front-matter header")
        return
    for f in HEADER_FIELDS:
        if not header.get(f):
            errors.append(f"{sid}: crawl.md header field '{f}' missing or empty")
    if header.get("id") and header["id"] != sid:
        errors.append(f"{sid}: crawl.md header id is {header['id']}")
    if CRAWL_TO_REGISTER.get(header.get("status", "")) not in (None, entry["status"]):
        warns.append(f"{sid}: crawl.md status '{header['status']}' but register status '{entry['status']}'")
    crawls[sid] = norm(body)
    comp = folder / "comprehension.md"
    if comp.exists():
        secs = comprehension_sections(comp)
        for h in HEADINGS:
            key = next((k for k in secs if k == h or (h == "Against" and k.startswith("Against "))), None)
            if not key or not secs[key]:
                errors.append(f"{sid}: comprehension.md heading '{h if h != 'Against' else 'Against <outline>'}' "
                              "missing or empty")
        for q in QUOTE.findall(secs.get("Key facts", "")):
            if norm(q) not in crawls[sid]:
                errors.append(f"{sid}: comprehension quote not found in crawl.md: \"{q[:70]}\"")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True, help="task folder, e.g. task3")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--task")
    g.add_argument("--ids")
    g.add_argument("--part", type=int)
    g.add_argument("--all", action="store_true")
    args = ap.parse_args()
    base = base_dir(args.base)
    reg, refmap = load_register(base)
    all_claims = load_claims(base)
    errors, warns, crawls = [], [], {}

    saved = {sid: e for sid, e in reg.items() if e["status"] in SAVED}
    if args.all:
        scope = set(saved)
    elif args.ids:
        scope = expand_ids(args.ids)
    elif args.part:
        scope = {c["source"] for c in all_claims if c["part"] == args.part}
    else:
        scope = set()
        for sid, e in saved.items():
            folder = source_folder(base, sid, e["slug"])
            if (folder / "crawl.md").exists() and (read_crawl(folder)[0] or {}).get("task") == args.task:
                scope.add(sid)
        if not any(len(r) > 1 and r[1] == args.task for r in table_rows(base / "research" / "search-log.md")):
            errors.append(f"search-log.md: no row for {args.task}")
        if not scope:
            errors.append(f"no source has 'task: {args.task}' in its crawl.md header")

    for sid in sorted(scope):
        if sid not in reg:
            errors.append(f"{sid}: not in sources.md")
        elif reg[sid]["status"] not in SAVED:
            errors.append(f"{sid}: status '{reg[sid]['status']}' (expected fetched/partial/blocked/error)")
        else:
            check_source(base, sid, reg[sid], errors, warns, crawls)

    claims = [c for c in all_claims if args.all or c["source"] in scope or c["part"] == args.part]
    for c in claims:
        sid = c["source"]
        if not SOURCE_ID.fullmatch(sid) or sid not in reg:
            errors.append(f"{c['id']}: orphan claim, source {sid} not in sources.md")
            continue
        if reg[sid]["status"] not in USABLE:
            errors.append(f"{c['id']}: source {sid} has status '{reg[sid]['status']}', cannot support a claim")
            continue
        if sid not in crawls:
            check_source(base, sid, reg[sid], errors, warns, crawls)
        anchors = QUOTE.findall(c["anchor"])
        if not anchors:
            errors.append(f"{c['id']}: no quote anchor (\"…\", at least 8 characters)")
        for q in anchors:
            if sid in crawls and norm(q) not in crawls[sid]:
                errors.append(f"{c['id']}: anchor not found verbatim in {sid}/crawl.md: \"{q[:70]}\"")
        if not c["files"] or c["files"] in ("–", "-"):
            warns.append(f"{c['id']}: not yet linked to a report file")

    cited = {c["source"] for c in all_claims}
    for sid in sorted(scope):
        if sid in reg and reg[sid]["status"] in USABLE and sid not in cited:
            warns.append(f"{sid}: fetched but no claim uses it")
    if args.all:
        for n, sid in sorted(refmap.items()):
            if sid not in reg or reg[sid]["status"] not in USABLE:
                errors.append(f"reference [{n}] maps to {sid}, which is unknown or not usable")

    for e in errors:
        print("ERROR " + e)
    for w in warns:
        print("WARN  " + w)
    print(f"\nChecked {len(scope)} sources, {len(claims)} claims: {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
