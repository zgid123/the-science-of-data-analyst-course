"""Check draft report sections while they are written with source IDs [S101] (writing-task gate).

Usage:
    check_drafts.py --base TASK [--files F ...] [--part N] [--words MIN-MAX]

ERROR  [Sxxx] not in research/sources.md, not usable (fetched/partial), or not used by any claim;
       a numeric [n] citation in a draft (numbers are assigned by finalize_refs.py);
       meta commentary about the report or the writing process (the phrases in [checks] meta_phrases of plan.toml,
       or the defaults below), which the reader must never see.
WARN   body paragraph without any citation (part and section introductions, signposts and closing syntheses may
       be legitimate: review each); a file whose word count is outside --words (default from plan.toml
       [checks] words, else 150-700; section intro files, whose name ends in -0- or -00-, are exempt from the
       lower bound); one "Surname et al." (or "Surname và cộng sự") naming works of different years in a file:
       when the works come from different research groups, each first author carries initials ("Liu S.-Q. et
       al. (2016)", "Liu Y. et al. (2018)"), so every cited work keeps its identity (reference.md section 6.2);
       a citation of the authors' own material, a source fetched with `fetch.py local` (a repository, the group's
       draft or documents), which stays in the trail as evidence while the text cites published works only;
       a priority claim ("the first", "novel", "for the first time") stated as the report's own, which reads as
       grounded only with the search that supports it or when attributed to the work that makes it.
Headings, image lines, captions, display math, code, tables and front matter (00-*) are ignored by the paragraph
checks; the author check reads every line outside code, tables included. Exit code 1 on any ERROR.
"""

import argparse
import re
import sys
from pathlib import Path

from common import (USABLE, base_dir, body_files, body_paragraphs, load_claims, load_plan, load_register,
                    report_dir, source_folder)

S_CITE = re.compile(r"\[(S\d{3}(?:\s*[,;]\s*S\d{3})*)\](?!\()")
N_CITE = re.compile(r"(?<!\])\[(\d+(?:\s*[,;–-]\s*\d+)*)\](?!\(|:)")
META = ["this doc", "this report will", "requester", "lecture", "slide", "we will", "in this task",
        "source notes", "reference.md", "the outline", "as instructed", "writing rule", "the reader will",
        "planned run", "pending result", "will be benchmarked"]


AUTHOR = re.compile(r"\b([A-ZÀ-Ý][\w'’-]+)((?:\s+[A-Z]\.(?:-[A-Z]\.)?)*),?\s+(?:et al\.|và cộng sự)")
YEAR = re.compile(r"\b(?:19|20)\d{2}\b")


PRIORITY = re.compile(r"\b(?:(?:the )?first (?:fully \w+ )?(?:approach|method|framework|system|work|study|benchmark|paper|attempt|technique|model|tool|solution|dataset)|first to (?:propose|introduce|show|apply|use|develop|present|demonstrate|combine|automate)|for the first time|novel)\b", re.I)
ATTRIBUTED = re.compile(r"\b(claim|present|describe|call|state|write|report|argue|position|to (?:our|their) "
                        r"knowledge|author|according)", re.I)


def local_sources(base: Path, reg: dict) -> set[str]:
    """Source IDs fetched with `fetch.py local` (tool: local in the crawl header): the authors' own material."""
    out = set()
    for sid, row in reg.items():
        crawl = source_folder(base, sid, row["slug"]) / "crawl.md"
        if crawl.exists() and re.search(r"^tool:\s*local\b", crawl.read_text(encoding="utf-8")[:2000], re.M):
            out.add(sid)
    return out


def author_years(path: Path) -> dict[str, set[str]]:
    """Years named right after each 'Surname et al.' without initials, over every line outside code."""
    found, code = {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            code = not code
        if code:
            continue
        for m in AUTHOR.finditer(line):
            if m.group(2).strip():
                continue                                   # initials already tell the work apart
            window = re.split(r"[\[|;]", line[m.end():m.end() + 40])[0]
            found.setdefault(m.group(1), set()).update(YEAR.findall(window))
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--part", type=int)
    ap.add_argument("--words", help="MIN-MAX words per file")
    args = ap.parse_args()
    base = base_dir(args.base)
    plan = load_plan(base).get("checks", {})
    meta = [m.lower() for m in plan.get("meta_phrases", META)]
    lo, hi = map(int, (args.words or plan.get("words", "150-700")).split("-"))
    report = report_dir(base)
    files = [Path(f).resolve() for f in args.files] if args.files else [
        p for p in body_files(report) if args.part is None or p.name.startswith(f"{args.part:02d}-")]
    reg, _ = load_register(base)
    claimed = {c["source"] for c in load_claims(base)}
    local = local_sources(base, reg)
    errors, warns = [], []
    for f in files:
        words = 0
        for n, text in body_paragraphs(f):
            words += len(re.findall(r"\w+", text))
            ids = [s for m in S_CITE.finditer(text) for s in re.split(r"\s*[,;]\s*", m.group(1))]
            for m in N_CITE.finditer(text):
                if 0 not in [int(x) for x in re.findall(r"\d+", m.group(1))]:
                    errors.append(f"{f.name}:{n}: numeric citation [{m.group(1)}] in a draft (use [Sxxx])")
            for s in ids:
                if s not in reg:
                    errors.append(f"{f.name}:{n}: [{s}] not in sources.md")
                elif reg[s]["status"] not in USABLE:
                    errors.append(f"{f.name}:{n}: [{s}] has status '{reg[s]['status']}'")
                elif s not in claimed:
                    errors.append(f"{f.name}:{n}: [{s}] is not used by any claim")
            low = re.sub(r'"[^"]{8,}?"|“[^”]{8,}?”', " ", text).lower()
            for phrase in meta:
                if re.search(rf"\b{re.escape(phrase)}", low):
                    errors.append(f"{f.name}:{n}: meta commentary '{phrase}': …{low[max(0, low.find(phrase) - 40):low.find(phrase) + 50]}…")
            for s in sorted(set(ids) & local):
                warns.append(f"{f.name}:{n}: [{s}] is the authors' own material (fetch.py local): keep it in the trail, "
                             f"name files or commits in the text where useful and cite published works only "
                             f"(reference.md section 6.2)")
            for sent in re.split(r"(?<=[.!?])\s+", re.sub(r'"[^"]*"|“[^”]*”', " ", text)):
                m = PRIORITY.search(sent)
                if m and not ATTRIBUTED.search(sent):
                    warns.append(f"{f.name}:{n}: priority claim '{m.group(0)}' as the report's own: attribute it to the "
                                 f"work that makes it, or give the search that supports it: {sent.strip()[:80]}…")
            if not ids and not text.lstrip().startswith("|"):
                warns.append(f"{f.name}:{n}: paragraph without a citation: {text[:70]}…")
        for name, years in author_years(f).items():
            if len(years) > 1:
                ys = sorted(years)
                warns.append(f"{f.name}: '{name} et al.' names works of {', '.join(ys)}; when they come from different "
                             f"research groups, give each first author with initials ('{name} A. et al. ({ys[0]})', "
                             f"'{name} B. et al. ({ys[-1]})'); one group across years reads as written")
        intro = bool(re.match(r"^\d{2}-(0|00)-|^\d{2}-\d{2}-0-", f.name))
        if words > hi or (words < lo and not intro):
            warns.append(f"{f.name}: {words} words (expected {lo}-{hi}{', intro: no minimum' if intro else ''})")
    for e in errors:
        print("ERROR " + e)
    for w in warns:
        print("WARN  " + w)
    print(f"\nChecked {len(files)} files (draft mode): {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
