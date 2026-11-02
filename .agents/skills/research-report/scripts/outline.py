"""Read the concise input outline (for example taskN/reference.md) that a research report is planned from.

Usage:
    outline.py OUTLINE                 section tree: number, title, line range, words, anchors (URLs, DOIs, arXiv)
    outline.py OUTLINE --seeds         proposed seed rows for research/sources.md from the outline's reference list
    outline.py OUTLINE --section 3b.2  print one section (its line range), for a task card's LOAD step

The outline is free-form markdown: headings (bold or plain, escaped numbers such as "2\\." allowed), bullets, and
usually a reference list under a heading that contains "Reference": a numbered list ("1. Author…" or "[1] Author…") or a table
whose rows start with an item ID ("| R1 | Citation | [link](url) | Status |"). Line ranges let a task load only
its slice with `sed -n 'A,Bp'`, which keeps the working context small.
"""

import argparse
import re
import sys
from pathlib import Path

from common import ROOT

HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
URL = re.compile(r"https?://[^\s)>\]\"']+")
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>;,]+)")
ARXIV = re.compile(r"arXiv[:\s]*(\d{4}\.\d{4,5})", re.I)


def clean(title):
    title = re.sub(r"\*\*|__|\\", "", title).strip()
    return re.sub(r"\s+", " ", title)


def sections(lines):
    heads = []
    for i, line in enumerate(lines, 1):
        m = HEAD.match(line)
        if m:
            heads.append((i, len(m.group(1)), clean(m.group(2))))
    out = []
    for k, (start, level, title) in enumerate(heads):
        end = next((s - 1 for s, lv, _ in heads[k + 1:] if lv <= level), len(lines))
        body = "\n".join(lines[start:end])
        num = re.match(r"^((?:\d+[a-z]?)(?:\.\d+)*)\.?\s", title)
        out.append(dict(start=start, end=end, level=level, title=title, number=num.group(1) if num else "",
                        words=len(re.findall(r"\w+", body)), urls=URL.findall(body),
                        dois=sorted(set(d.rstrip(".") for d in DOI.findall(body))), arxiv=sorted(set(ARXIV.findall(body)))))
    return out


def references(lines, secs):
    ref = next((s for s in secs if re.search(r"reference", s["title"], re.I)), None)
    if not ref:
        return []
    items, cur = [], None
    for line in lines[ref["start"]:ref["end"]]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
        if cells and re.fullmatch(r"[A-Za-z]{0,3}\d+", cells[0]):   # a table row: | R1 | citation | link | status |
            cur = None
            links = URL.findall(" ".join(cells[2:]))           # the citation cell, then the link cells' URLs
            items.append(dict(item=cells[0], text=" ".join([cells[1]] + [u.rstrip(")") for u in links])))
            continue
        m = re.match(r"^\s*(\d+)\\?\.\s+(.*)", line) or re.match(r"^\s*\\?\[(\d+)\\?\]\s+(.*)", line)  # "1. …" or "[1] …"
        if m:
            cur = dict(item=m.group(1), text=m.group(2))
            items.append(cur)
        elif cur and line.strip() and not HEAD.match(line):
            cur["text"] += " " + line.strip()
    for it in items:
        t = re.sub(r"\\", "", it["text"])
        it["urls"] = [u.rstrip(".;,") for u in URL.findall(t)]
        it["doi"] = next(iter(DOI.findall(t)), "").rstrip(".")
        it["arxiv"] = next(iter(ARXIV.findall(t)), "")
        it["short"] = re.split(r"\.\s+(?:HTML|PDF|Reported|https?)", re.sub(r"\*", "", t))[0][:160]
    return items


def slug(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    stop = {"the", "a", "an", "of", "and", "for", "in", "on", "to", "with", "via", "by"}
    return "-".join([w for w in words if w not in stop][:5]) or "source"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outline")
    ap.add_argument("--seeds", action="store_true")
    ap.add_argument("--section")
    args = ap.parse_args()
    path = Path(args.outline)
    path = path if path.is_absolute() else ROOT / path
    lines = path.read_text(encoding="utf-8").splitlines()
    secs = sections(lines)

    if args.section:
        sec = next((s for s in secs if s["number"] == args.section or s["title"].startswith(args.section)), None)
        if not sec:
            sys.exit(f"no section {args.section}")
        print(f"# lines {sec['start']}-{sec['end']} of {path.name}\n")
        print("\n".join(lines[sec["start"] - 1:sec["end"]]))
        return 0
    if args.seeds:
        items = references(lines, secs)
        print("| ID | Folder slug | Source | URL | Outline item | Primary/secondary | Status | APA 7 entry |")
        print("| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |")
        for k, it in enumerate(items, 1):
            url = (f"https://arxiv.org/abs/{it['arxiv']}" if it["arxiv"] else
                   f"https://doi.org/{it['doi']}" if it["doi"] else (it["urls"] or ["–"])[0])
            print(f"| S{k:03d} | {slug(it['short'])} | {it['short'].replace('|', '/')} | {url} | {it['item']} | "
                  f"primary | to-fetch | – |")
        print(f"\n{len(items)} reference items; check each row (duplicates such as 'already listed as 1' are merged)",
              file=sys.stderr)
        return 0
    print(f"{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}: {len(lines)} lines, {len(secs)} sections")
    for s in secs:
        anchors = len(s["urls"]) + len(s["dois"]) + len(s["arxiv"])
        print(f"{'  ' * (s['level'] - 1)}{s['title'][:80]}  [lines {s['start']}-{s['end']}, {s['words']} words"
              + (f", {anchors} anchors" if anchors else "") + "]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
