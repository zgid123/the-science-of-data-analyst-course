"""Draw a seeded random sample of cited sentences and trace each one to its evidence (fact spot-check).

Usage: spot_check.py --base TASK [--n 10] [--seed 20261003] [--write]

For each sampled sentence (body files only, sentences that carry [n] or [Sxxx]) the chain is followed as far as
a script can: [n] → reference map → Sxxx → claims of that source linked to the sentence's file → their quote
anchors → whether each anchor occurs verbatim in crawl.md. The table is printed, or written with --write to
research/spot-check.md (never overwritten: a new run is appended). The "Result" column is left for the human or
agent judgement: does the anchored evidence state what the sentence says? Exit code 1 when an anchor is missing.
"""

import argparse
import random
import re
import sys
from datetime import date

from common import (QUOTE, base_dir, body_files, body_paragraphs, load_claims, load_register, norm, read_crawl,
                    report_dir, source_folder)

CITE = re.compile(r"\[((?:\d+|S\d{3})(?:\s*[,;–-]\s*(?:\d+|S\d{3}))*)\]")


def sentences(base):
    out = []
    for f in body_files(report_dir(base)):
        for n, para in body_paragraphs(f):
            for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", para):
                if CITE.search(s) and len(s) > 40:
                    out.append((f.name, n, s.strip()))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--seed", type=int, default=int(date.today().strftime("%Y%m%d")))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    base = base_dir(args.base)
    reg, refmap = load_register(base)
    claims = load_claims(base)
    pool = sentences(base)
    sample = random.Random(args.seed).sample(pool, min(args.n, len(pool)))
    rows, missing = [], 0
    for i, (fname, line, sent) in enumerate(sample, 1):
        cites = [c for m in CITE.finditer(sent) for c in re.split(r"\s*[,;]\s*", m.group(1))]
        sids = [refmap.get(int(c)) if c.isdigit() else c for c in cites]
        chain, evid = [], []
        for c, sid in zip(cites, sids):
            chain.append(f"[{c}] → {sid or '?'}")
            if not sid or sid not in reg:
                continue
            folder = source_folder(base, sid, reg[sid]["slug"])
            body = norm(read_crawl(folder)[1]) if (folder / "crawl.md").exists() else ""
            for cl in claims:
                if cl["source"] == sid and fname in cl["files"]:
                    for q in QUOTE.findall(cl["anchor"])[:1]:
                        found = norm(q) in body
                        missing += not found
                        evid.append(f"{cl['id']} \"{q[:60]}\" {'(found)' if found else '(NOT FOUND)'}")
        rows.append(f"| {i} | {fname} | {line} | {sent[:140].replace('|', '/')} | {'; '.join(chain)} | "
                    f"{'; '.join(evid[:3]) or 'no claim linked to this file'} | to verify |")
    table = (f"\n## Spot-check run {date.today()} (seed {args.seed}, {len(sample)} of {len(pool)} cited sentences)\n\n"
             "| # | File | Line | Sentence | Citation → source | Claim and quote anchor | Result |\n"
             "| :---- | :---- | :---- | :---- | :---- | :---- | :---- |\n" + "\n".join(rows) + "\n")
    if args.write:
        path = base / "research" / "spot-check.md"
        head = "" if path.exists() else "# Fact Spot-Check\n\nEach run traces sampled sentences to verbatim evidence.\n"
        with path.open("a", encoding="utf-8") as f:
            f.write(head + table)
        print(f"appended {len(rows)} rows to {path.name}")
    else:
        print(table)
    print(f"{len(rows)} sentences sampled; {missing} quote anchors not found")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
