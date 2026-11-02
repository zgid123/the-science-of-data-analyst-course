"""Convert draft citations [Sxxx] into numbered references [n] and write the reference list (finishing stage).

Usage: finalize_refs.py --base TASK [--dry-run] [--renumber]

--renumber: after edits to a finished report (a restated fact cited earlier than before, a citation added or
removed), first map every numbered citation [n], [n, m] or [n–m] back to its source ID through the reference map
in sources.md, then number again in order of first citation. Unused references drop out of the list.

1. Backs up every report file to build/.cache/<task>_draft_backup/ (drafts with [Sxxx] stay recoverable).
2. Numbers the cited sources in order of first citation over the body files (sorted; front matter and the
   reference list excluded).
3. Rewrites every [Sxxx] (also lists such as [S101, S102]) as [n].
4. Writes the reference list file (the report file whose name contains "references") in APA 7 from the
   "APA 7 entry" column of research/sources.md, with the heading and intro of plan.toml [references] if given.
5. Writes the "## Reference map" table (n → Source ID) into sources.md, which check_trail.py --all verifies.
Refuses to run when a cited source has no APA entry or when the report holds no [Sxxx] citation.
"""

import argparse
import re
import shutil
import sys

from common import ROOT, base_dir, body_files, load_plan, load_register, references_file, report_dir

CITE = re.compile(r"\[(S\d{3}(?:\s*[,;]\s*S\d{3})*)\](?!\()")
INTRO = ("The references are formatted in APA style (American Psychological Association, 7th edition) and numbered "
         "for in-text citation in the form [n], in order of first citation.")


N_CITE = re.compile(r"\[(\d+(?:\s*[,;–-]\s*\d+)*)\](?!\()")


def to_source_ids(base, report) -> int:
    """Rewrite numbered citations as [Sxxx] through the reference map; returns the number of files changed."""
    sources = (base / "research" / "sources.md").read_text(encoding="utf-8")
    if "## Reference map" not in sources:
        sys.exit("no reference map in sources.md: run finalize_refs.py once without --renumber")
    rows = re.findall(r"^\| (\d+) \| (S\d{3}) \|", sources.split("## Reference map", 1)[1], re.M)
    sid = {int(n): s for n, s in rows}

    def expand(group: str) -> list[int]:
        nums = []
        for part in re.split(r"\s*[,;]\s*", group):
            if re.search(r"[–-]", part):
                a, b = (int(x) for x in re.split(r"\s*[–-]\s*", part))
                nums += list(range(a, b + 1))
            else:
                nums.append(int(part))
        return nums

    def sub(m):
        nums = expand(m.group(1))
        if any(n not in sid for n in nums):
            sys.exit(f"citation [{m.group(1)}] is not in the reference map")
        return "[" + ", ".join(sid[n] for n in nums) + "]"

    changed = 0
    for p in body_files(report):
        text = p.read_text(encoding="utf-8")
        new = N_CITE.sub(sub, text)
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--renumber", action="store_true", help="map [n] back to [Sxxx] first, then number again")
    args = ap.parse_args()
    base = base_dir(args.base)
    report = report_dir(base)
    refs_path = references_file(report)
    if refs_path is None:
        sys.exit("no reference list file (a report file whose name contains 'references')")
    if args.renumber and not args.dry_run:
        print(f"renumber: {to_source_ids(base, report)} files mapped back to source IDs")
    order = []
    for p in body_files(report):
        for m in CITE.finditer(p.read_text(encoding="utf-8")):
            for s in re.split(r"\s*[,;]\s*", m.group(1)):
                if s not in order:
                    order.append(s)
    if not order:
        sys.exit("no [Sxxx] citations found; nothing to convert")
    reg, _ = load_register(base)
    missing = [s for s in order if not reg.get(s, {}).get("apa")]
    if missing:
        sys.exit(f"cited sources without an APA entry in sources.md: {missing}")
    number = {s: i + 1 for i, s in enumerate(order)}
    print(f"{len(order)} cited sources numbered by first citation")
    if args.dry_run:
        return 0

    backup = ROOT / "build" / ".cache" / f"{base.name}_draft_backup"
    backup.mkdir(parents=True, exist_ok=True)
    for p in sorted(report.glob("*.md")):
        shutil.copy2(p, backup / p.name)
    for p in body_files(report):
        text = p.read_text(encoding="utf-8")
        new = CITE.sub(lambda m: "[" + ", ".join(str(number[s]) for s in re.split(r"\s*[,;]\s*", m.group(1))) + "]",
                       text)
        if new != text:
            p.write_text(new, encoding="utf-8")

    cfg = load_plan(base).get("references", {})
    lines = [cfg.get("heading", "# References"), "", cfg.get("intro", INTRO), ""]
    for s in order:
        lines += [f"[{number[s]}] {reg[s]['apa']}", ""]
    refs_path.write_text("\n".join(lines), encoding="utf-8")

    sources = base / "research" / "sources.md"
    src = re.sub(r"\n## Reference map\n.*", "\n", sources.read_text(encoding="utf-8"), flags=re.S).rstrip("\n") + "\n"
    src += (f"\n## Reference map\n\nNumbered references of `report/{refs_path.name}` and their source IDs "
            "(written by finalize_refs.py).\n\n| n | Source ID |\n| :---- | :---- |\n")
    src += "".join(f"| {number[s]} | {s} |\n" for s in order)
    sources.write_text(src, encoding="utf-8")
    print(f"converted {len(body_files(report))} body files; wrote {refs_path.name} and the reference map; "
          f"backup in {backup.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
