"""Move the supporting tables of the Milestone 4 full draft back to the appendices and renumber everything.

After the full draft brought every appendix table into the main text, the moves decided against the brief (research/
revision/appendix-decisions.md) take the supporting tables out again. This script, run once on the English sources:
1. removes the moved tables (caption and rows) from the main-text files;
2. rebuilds the appendix files: the template tables now in the main text (Modeling Briefs, Evaluation Design Cards,
   AI Decision Log) leave the appendices, and the remaining appendices and tables are renumbered I–VII and A.1–A.13;
3. renumbers the main-text tables and rewrites every table and appendix reference in all English report files.
The Vietnamese twins are renamed to the new file names; their text is updated in the translation pass.

Usage: venv/bin/python reports/milestone-4/code/restructure_appendices.py
"""
import re
from pathlib import Path

R = Path(__file__).resolve().parent.parent / "report"

# main-text tables that move back to an appendix: draft number -> new appendix number
MOVE = {"3.2": "A.1", "3.3": "A.2", "3.4": "A.3", "4.5": "A.4", "4.6": "A.5", "4.7": "A.6", "4.9": "A.7",
        "4.10": "A.8", "5.2": "A.9", "6.2": "A.10", "6.3": "A.11", "8.2": "A.12", "8.3": "A.13"}
# main-text tables that stay and change number
RENUM = {"4.8": "4.5"}
# old appendix table numbers -> where the table now is
OLD_A = {"A.1": "Table 2.1", "A.2": "Table 2.2", "A.3": "Table 2.3", "A.4": "Table 2.4", "A.5": "Table A.1",
         "A.6": "Table A.2", "A.7": "Table A.3", "A.8": "Table 4.1", "A.9": "Table 4.2", "A.10": "Table 4.3",
         "A.11": "Table 4.4", "A.12": "Table A.4", "A.13": "Table A.5", "A.14": "Table A.6", "A.15": "Table A.7",
         "A.16": "Table A.8", "A.17": "Table A.9", "A.18": "Table 6.1", "A.19": "Table A.10", "A.20": "Table A.11",
         "A.21": "Table A.12", "A.22": "Table A.13"}
# old appendix numerals -> new place
OLD_APP = {"VIII": "Appendix VII", "VII": "Appendix VI", "VI": "Appendix V", "V": "Appendix IV",
           "IV": "Appendix III", "III": "Appendix II", "II": "Appendix I", "I": "Section 2.1"}
# old appendix file -> (new file, new heading)
FILES = {"10-02-candidate-comparison": ("10-01-candidate-comparison", "## Appendix I – Candidate Comparison by Criterion"),
         "10-04-validation-protocol": ("10-03-validation-protocol", "## Appendix III – Validation and Test Protocol"),
         "10-05-fairness-spec": ("10-04-fairness-spec", "## Appendix IV – Error and Fairness Analysis Specification"),
         "10-06-risk-register": ("10-05-risk-register", "## Appendix V – Risk Register"),
         "10-07-ai-decision-log": ("10-06-ai-critiques", "## Appendix VI – Decisions on the AI Critiques and Prompts"),
         "10-08-traceability-full": ("10-07-traceability-full", "## Appendix VII – Full Traceability and Change Log")}


def cut_table(text, number):
    """Remove '**Table n. …**' and its rows (and the blank line after) from text."""
    m = re.search(r"\*\*Table " + re.escape(number) + r"\. [^\n]*\*\*\n\n(\|[^\n]*\n)+\n?", text)
    if not m:
        raise SystemExit(f"table {number} not found")
    return text[:m.start()] + text[m.end():]


def table_block(text, number):
    m = re.search(r"\*\*Table " + re.escape(number) + r"\. [^\n]*\*\*\n\n(\|[^\n]*\n)+", text)
    return m.group(0).rstrip("\n")


def renumber_refs(text, in_appendix=False):
    # placeholders first, so that chains (A.13 -> A.5 -> ...) cannot collide
    text = re.sub(r"Tables? A\.(\d+)", lambda m: m.group(0), text)
    text = re.sub(r"\bA\.(\d+)\b", lambda m: f"@@A{m.group(1)}@@", text)
    text = re.sub(r"Appendix (VIII|VII|VI|V|IV|III|II|I)\b", lambda m: f"@@APP{m.group(1)}@@", text)
    for old, new in MOVE.items():
        text = re.sub(r"Table " + re.escape(old) + r"\b", f"@@MV{new}@@", text)
    for old, new in RENUM.items():
        text = re.sub(r"Table " + re.escape(old) + r"\b", f"@@RN{new}@@", text)
    text = re.sub(r"@@MV(A\.\d+)@@", r"Table \1", text)
    text = re.sub(r"@@RN([\d.]+)@@", r"Table \1", text)

    def old_a(m):
        new = OLD_A[f"A.{m.group(1)}"]
        return new.replace("Table ", "")
    text = re.sub(r"@@A(\d+)@@", old_a, text)
    text = re.sub(r"@@APP(VIII|VII|VI|V|IV|III|II|I)@@", lambda m: OLD_APP[m.group(1)], text)
    return text


def main():
    main_files = sorted(p for p in R.glob("0[1-8]-*.md") if not p.name.endswith(".vi.md"))
    moved = {}
    for p in main_files:
        s = p.read_text()
        for num in MOVE:
            if f"**Table {num}. " in s:
                moved[num] = table_block(s, num)
                s = cut_table(s, num)
        p.write_text(s)
    # appendix files: renumber their own tables from the old numbering, rename, re-head
    old = {f.stem: f.read_text() for f in R.glob("10-0*.md") if not f.name.endswith(".vi.md")}
    for stem, (new_stem, heading) in FILES.items():
        s = old[stem]
        s = heading + s[s.index("\n"):]
        if stem == "10-07-ai-decision-log":
            s = cut_table(s, "A.18")
        (R / f"{new_stem}.md").write_text(s)
    cards = old["10-03-evaluation-cards-full"]
    defs = table_block(cards, "A.12")
    (R / "10-02-metric-definitions.md").write_text(
        "## Appendix II – Metric Definitions\n\nThe Evaluation Design Cards of Section 4.1 use the metrics that "
        "Table A.12 defines, for a run r with n enrolments, the set Y of its non-completers, base rate b = |Y|/n, and "
        "a list L of the k highest scores; Section 4.1 explains the main ones in words.\n\n" + defs + "\n")
    for stem in ("10-01-briefs-full", "10-03-evaluation-cards-full", "10-08-traceability-full"):
        f = R / f"{stem}.md"
        if f.exists() and stem not in [v[0] for v in FILES.values()]:
            f.unlink()
    for stem in ("10-02-candidate-comparison", "10-04-validation-protocol", "10-05-fairness-spec",
                 "10-06-risk-register", "10-07-ai-decision-log"):
        f = R / f"{stem}.md"
        if f.exists() and stem not in [v[0] for v in FILES.values()]:
            f.unlink()
    # Vietnamese twins follow the file names (their text is updated in the translation pass)
    renames = {**{k: v[0] for k, v in FILES.items()}, "10-03-evaluation-cards-full": "10-02-metric-definitions"}
    for old_stem in sorted(renames, reverse=True):
        src = R / f"{old_stem}.vi.md"
        if src.exists():
            src.rename(R / f"{renames[old_stem]}.vi.tmp")
    for f in R.glob("*.vi.tmp"):
        f.rename(f.with_suffix("").with_suffix(".vi.md"))
    for stem in ("10-01-briefs-full", "10-08-traceability-full"):
        f = R / f"{stem}.vi.md"
        if f.exists() and not (R / f"{stem}.md").exists():
            f.unlink()
    # renumber every reference in every English file
    for p in sorted(R.glob("*.md")):
        if p.name.endswith(".vi.md") or p.name.startswith("09-") or p.name.startswith("00-0"):
            continue
        p.write_text(renumber_refs(p.read_text()))
    print("moved:", ", ".join(f"{k}->{v}" for k, v in MOVE.items()))
    print("appendix files:", ", ".join(sorted(f.name for f in R.glob("10-0*.md") if not f.name.endswith(".vi.md"))))


if __name__ == "__main__":
    main()
