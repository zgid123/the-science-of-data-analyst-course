"""T15 loss check: find sentences and table rows of the full draft that occur nowhere in the current report.

The full draft (Sections 1–14) is read from git commit a6a8d5a; the current English report is every body file
01-* … 16-* in report/ (main text and appendices, *.vi.md excluded). Both sides are normalised the same way:
Markdown markup removed, whitespace collapsed, and cross-references ("Table 7.1", "Appendix XII", "Section 11.2.2",
"Figure 1.1", "(Milestone 3, Section 4.1)") reduced to placeholders, because the move renumbered them.

A draft unit (a sentence of a paragraph, or one row of a table) counts as matched when its normalised text occurs in
the normalised current corpus. Every unmatched unit is printed with its file, so it can be reviewed by hand.

Usage: venv/bin/python reports/milestone-5/code/t15_loss_check.py [--commit a6a8d5a] [--min-words 4]
"""

import argparse
import re
import subprocess
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
REPO = TASK.parents[1]
REPORT = TASK / "report"
DRAFT_PATH = "reports/milestone-5/report"

ROMAN = r"(?:[IVXL]+)"
REFS = [
    (re.compile(r"\((Milestone \d), Sections? [\d.–]+\)"), r"(\1)"),
    (re.compile(r"\bTables? [A0-9]+\.\d+(?:\s*(?:–|-|and|to)\s*[A0-9]+\.\d+)?"), "Table #"),
    (re.compile(r"\bFigures? \d+\.\d+"), "Figure #"),
    (re.compile(rf"\bAppendix(?:es)? {ROMAN}(?:\s*(?:–|-|and|to)\s*{ROMAN})?\b"), "REF"),
    (re.compile(r"\bSections? \d+(?:\.\d+)*(?:\s*(?:–|-|and|to)\s*\d+(?:\.\d+)*)?"), "REF"),
]
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\[“\"*])")


def git_show(commit, path):
    return subprocess.run(["git", "show", f"{commit}:{path}"], cwd=REPO, check=True, capture_output=True,
                          text=True).stdout


def draft_files(commit):
    out = subprocess.run(["git", "ls-tree", "--name-only", f"{commit}:{DRAFT_PATH}"], cwd=REPO, check=True,
                         capture_output=True, text=True).stdout.split()
    return sorted(f for f in out if re.match(r"^(0[1-9]|1[0-4])-.*\.md$", f) and not f.endswith(".vi.md"))


def norm(text):
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?", r"\1", text)    # figures: keep the caption
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)                    # links
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"^#+\s*(\d+(\.\d+)*\.\s*)?", "", text, flags=re.M)   # headings and their numbers
    for rx, rep in REFS:
        text = rx.sub(rep, text)
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip().lower()


def units(text):
    """Yield (kind, raw) units: table rows and sentences of non-table paragraphs."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?", r"\1", text)    # figure: keep its caption as text
    for block in re.split(r"\n\s*\n", text):
        lines = [ln for ln in block.strip().splitlines() if ln.strip()]
        if not lines:
            continue
        if all(ln.lstrip().startswith("|") for ln in lines):
            for ln in lines:
                if re.fullmatch(r"\s*\|(\s*:?-{2,}:?\s*\|)+\s*", ln):
                    continue
                yield "row", ln.strip()
            continue
        para = " ".join(ln.strip() for ln in lines)
        if para.startswith("#"):
            yield "heading", para
            continue
        for s in SENT_SPLIT.split(para):
            label = re.match(r"^\*\*[^*]+\.\*\*\s+", s)     # run-in label such as "**Coverage.**"
            if label:
                yield "label", label.group(0).strip()
                s = s[label.end():]
            yield "sentence", s


def row_cells(row):
    return [norm(c) for c in row.strip().strip("|").split("|")]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--commit", default="a6a8d5a")
    ap.add_argument("--min-words", type=int, default=4, help="ignore units shorter than this (labels, captions)")
    args = ap.parse_args()

    current = sorted(p for p in REPORT.glob("[01][0-9]-*.md")
                     if not p.name.endswith(".vi.md") and re.match(r"^(0[1-9]|1[0-46])-", p.name))
    corpus_raw = "\n\n".join(p.read_text() for p in current)
    corpus = norm(corpus_raw)
    corpus_cells = set()
    for kind, raw in units(corpus_raw):
        if kind == "row":
            corpus_cells.update(row_cells(raw))

    total = {"sentence": 0, "row": 0, "heading": 0, "label": 0}
    missing = []
    for name in draft_files(args.commit):
        for kind, raw in units(git_show(args.commit, f"{DRAFT_PATH}/{name}")):
            n = norm(raw)
            if len(n.split()) < args.min_words:
                continue
            total[kind] += 1
            if n in corpus:
                continue
            if kind == "row":
                lost = [c for c in row_cells(raw) if c and len(c.split()) >= 2 and c not in corpus_cells
                        and c not in corpus]
                if not lost:
                    continue
                missing.append((name, kind, raw, lost))
            else:
                missing.append((name, kind, raw, None))

    print(f"current report files: {len(current)} ({', '.join(p.name for p in current[:1])} … {current[-1].name})")
    print("draft units checked: " + ", ".join(f"{k} {v}" for k, v in total.items()))
    by_kind = {}
    for _, kind, _, _ in missing:
        by_kind[kind] = by_kind.get(kind, 0) + 1
    print("unmatched: " + str(len(missing)) + " (" + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items())) + ")")
    last = None
    for i, (name, kind, raw, lost) in enumerate(missing, 1):
        if name != last:
            print(f"\n### {name}")
            last = name
        print(f"[{i}] {kind}: {raw}")
        if lost:
            print("     cells not found: " + " || ".join(lost))


if __name__ == "__main__":
    main()
