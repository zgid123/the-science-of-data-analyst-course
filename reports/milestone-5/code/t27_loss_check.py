"""T27 loss check: prove that shortening Appendices XII and XIII and editing Sections 11.2 and 11.3 lost no number.

For each English file changed by T27, the version at the git commit given (default HEAD, the state before T27) is split
into sentences (prose) and table rows. Every old sentence that no longer occurs verbatim in the new file is listed with
each number it contains and where that number now stands in the new file: in a table (named by its caption number) or
in the prose (quoted with its sentence). A number found nowhere in the new file is marked LOST; the run exits 1 if any
number is lost. Old table rows are checked the same way, cell by cell. Numbers are compared as written (12,700; 45.3%;
−1.9), so a number re-expressed in other words (for example 20.2 to 15.2 as "by five points") is reported as LOST
and must be explained in the classification of the log.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t27_loss_check.py [--rev HEAD]
"""
import re
import subprocess
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
ROOT = TASK.parents[1]
FILES = ["11-02-aq1-findings.md", "11-03-aq2-findings.md", "16-12-aq1-results.md", "16-13-aq2-results.md"]
NUM = re.compile(r"[−-]?\d[\d,]*(?:\.\d+)?%?")
CAPTION = re.compile(r"^\*\*Table (A?\.?\d+(?:\.\d+)?)\.")


def blocks(text: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Prose sentences, and table rows with the caption of their table."""
    sentences, rows, cap = [], [], ""
    paras = re.split(r"\n\s*\n", text)
    for p in paras:
        p = p.strip()
        m = CAPTION.match(p)
        if m:
            cap = "Table " + m.group(1)
            continue
        if p.startswith("|"):
            rows += [(cap, r) for r in p.splitlines() if not r.startswith("| :")]
            continue
        if p.startswith("!["):
            rows.append((re.match(r"!\[(\w+ \d+\.\d+)", p).group(1), p))  # a figure caption counts as a place where a number stands
            continue
        if p.startswith("#"):
            continue
        flat = " ".join(p.split())
        sentences += [s for s in re.split(r"(?<=[.;:])\s+(?=[A-Z(])", flat) if s]
    return sentences, rows


def numbers(s: str) -> list[str]:
    out = []
    s = re.sub(r"\bA\.\d+", "", s)  # table references: renumbered by t27_renumber_tables.py, checked by check_structure
    for n in NUM.findall(s):
        n = n.rstrip(",.")
        if re.fullmatch(r"(19|20)\d\d[BJ]?", n) or re.fullmatch(r"\d", n):
            continue  # years and single digits (counts like "4 of 4", list numbers) are not checked
        out.append(n)
    return out


def where(n: str, sentences: list[str], rows: list[tuple[str, str]]) -> str:
    pat = re.compile(r"(?<![\d.,])" + re.escape(n) + r"(?![\d])")
    tabs = sorted({cap for cap, r in rows if pat.search(r)})
    if tabs:
        return ", ".join(tabs)
    for s in sentences:
        if pat.search(s):
            return f'prose: "{s[:110]}…"'
    return "LOST"


def main() -> int:
    rev = sys.argv[sys.argv.index("--rev") + 1] if "--rev" in sys.argv else "HEAD"
    lost_total = removed_total = 0
    for f in FILES:
        rel = f"reports/milestone-5/report/{f}"
        old = subprocess.run(["git", "show", f"{rev}:{rel}"], cwd=ROOT, capture_output=True, text=True,
                             check=True).stdout
        new = (TASK / "report" / f).read_text(encoding="utf-8")
        o_s, o_r = blocks(old)
        n_s, n_r = blocks(new)
        new_flat = " ".join(new.split())
        gone = [s for s in o_s if s not in new_flat]
        gone_rows = [(c, r) for c, r in o_r if r not in new]
        print(f"===== {f}: {len(o_s)} old sentences, {len(gone)} changed or removed; "
              f"{len(o_r)} old table rows, {len(gone_rows)} changed")
        for s in gone:
            removed_total += 1
            print(f"- OLD: {s}")
            for n in numbers(s):
                w = where(n, n_s, n_r)
                lost_total += w == "LOST"
                print(f"    {n:>14}  ->  {w}")
        for c, r in gone_rows:
            print(f"- OLD ROW ({c}): {r}")
            for n in numbers(r):
                w = where(n, n_s, n_r)
                lost_total += w == "LOST"
                print(f"    {n:>14}  ->  {w}")
    print(f"SUMMARY: {removed_total} sentences changed or removed; {lost_total} numbers not found in the new files")
    return 1 if lost_total else 0


if __name__ == "__main__":
    sys.exit(main())
