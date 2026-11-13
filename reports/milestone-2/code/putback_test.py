"""Put-back test for one appendix move of the Milestone 2 report (docs/appendix-move-brief.md, rule 4).

Restores the main-text paragraphs of one move from git HEAD (the state before the moves), in both languages, rebuilds
and measures the pessimistic pages, then restores the current files. The appendix is left as it is, since it does not
count towards the main content.

Usage (from the repository root): venv/bin/python reports/milestone-2/code/putback_test.py MOVE
  MOVE: m1, m4, m7, m8, m9, m10 or m11; logs go to reports/milestone-2/logs/R22_t<MOVE>_putback_*.log
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REP = ROOT / "reports" / "milestone-2" / "report"
P = ROOT / ".claude" / "skills" / "build-report" / "scripts"
PY = str(ROOT / "venv" / "bin" / "python")


def head(name):
    return subprocess.run(["git", "show", f"HEAD:reports/milestone-2/report/{name}"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def span(text, start, end=None):
    """The text from the marker start up to the marker end (or the end of the text)."""
    s = text.index(start)
    return text[s:text.index(end, s)] if end else text[s:]


def swap(name, start, end=None):
    """Replace the span [start, end) of the current file with the same span of the HEAD file."""
    cur = (REP / name).read_text()
    old = span(cur, start, end)
    new = span(head(name), start, end)
    (REP / name).write_text(cur.replace(old, new.rstrip() + "\n\n" if end else new))


def restore_whole(name):
    (REP / name).write_text(head(name))


MOVES = {
    "m1": lambda: (
        swap("01-01-frozen-baseline.md", "**Why the baseline is frozen.**", "**Goal and measures.**"),
        swap("01-01-frozen-baseline.vi.md", "**Lý do chốt phiên bản cơ sở.**", "**Mục tiêu và các chỉ số.**"),
        swap("01-02-scope-change-log.md", "**What this milestone does.**", "None of the"),
        swap("01-02-scope-change-log.vi.md", "**Công việc của Milestone 2.**", "Không điều chỉnh nào làm thay đổi")),
    "m4": lambda: (
        swap("04-02-selection-matrix.md", "**Why not the others.**", "**A modest total, made conditional.**"),
        swap("04-02-selection-matrix.vi.md", "**Lý do loại các ứng viên khác.**",
             "**Tổng điểm vừa phải, quyết định có điều kiện.**")),
    "m7": lambda: (restore_whole("09-00-genai-reflection.md"), restore_whole("09-00-genai-reflection.vi.md")),
    "m8": lambda: (swap("08-00-risks-ethics.md", "**Data issues for the next milestone.**"),
                   swap("08-00-risks-ethics.vi.md", "**Các vấn đề dữ liệu cho Milestone tiếp theo.**")),
    "m9": lambda: (restore_whole("04-01-criteria-gates.md"), restore_whole("04-01-criteria-gates.vi.md")),
    "m10": lambda: (swap("04-02-selection-matrix.md", "**Limits that come with the choice.**"),
                    swap("04-02-selection-matrix.vi.md", "**Giới hạn đi kèm lựa chọn.**")),
    "m11": lambda: None,  # handled below
}


def putback_m11():
    for name, clause, start in (
            ("01-02-scope-change-log.md", " None of them alters the Business Goal, the SMART Goal\nor the decisions.",
             "None of the revisions alters"),
            ("01-02-scope-change-log.vi.md",
             " Không điều chỉnh nào làm thay đổi Business Goal, SMART Goal hoặc các quyết định.",
             "Không điều chỉnh nào làm thay đổi")):
        cur = (REP / name).read_text()
        assert clause in cur, name
        para = span(head(name), start)
        (REP / name).write_text(cur.replace(clause, "").rstrip() + "\n\n" + para)


def main():
    move = sys.argv[1]
    files = sorted(p.name for p in REP.glob("0*.md"))
    saved = {n: (REP / n).read_text() for n in files}
    try:
        putback_m11() if move == "m11" else MOVES[move]()
        changed = [n for n in files if (REP / n).read_text() != saved[n]]
        print("changed:", ", ".join(changed))
        src = [str(REP / n) for n in changed if not n.endswith(".vi.md")]
        subprocess.run([PY, str(P / "translation_status.py"), "--report", str(REP), "--lang", "vi", "--mark", *src],
                       cwd=ROOT, check=True)
        subprocess.run(["bash", "reports/milestone-2/code/measure_move.sh", f"t{move}_putback"], cwd=ROOT, check=True)
    finally:
        for n, t in saved.items():
            (REP / n).write_text(t)
        src = [str(REP / n) for n in files if not n.endswith(".vi.md")]
        subprocess.run([PY, str(P / "translation_status.py"), "--report", str(REP), "--lang", "vi", "--mark", *src],
                       cwd=ROOT, check=True, capture_output=True)


if __name__ == "__main__":
    main()
