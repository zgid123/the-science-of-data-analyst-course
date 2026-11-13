"""Put one appendix move back against the current state, for the put-back test of docs/appendix-move-brief.md
(rule 4): a move that saved no page on its own is kept only if putting it back costs a page in either language.

The main-text sections of the move return to their text at the baseline commit (git HEAD of 2026-11-13, before the
moves), with later appendix-table renumbering re-applied, and the blocks the move added to the appendices are cut out
again. Run code/move_cycle.sh afterwards to measure. To undo a put-back, restore the snapshot taken first:

Usage: venv/bin/python reports/milestone-3/code/putback.py snapshot DIR       # copy report/ and research/appendix/
       venv/bin/python reports/milestone-3/code/putback.py apply M1|M6|M7     # put the move back
       venv/bin/python reports/milestone-3/code/putback.py restore DIR        # return to the snapshot
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent.parent
BASE = "HEAD"

# Per move: main-text files restored from the baseline; (file, first line of the added block, text that follows it
# or None for the end of the file) cut from the appendices; renumbering (old, new) re-applied after the restore.
MOVES = {
    "M1": {
        "restore": ["01-01-baseline-aqs", "01-02-dataset-entry-gate"],
        "cut": [("research/appendix/detail-04.md", "**Baseline in full.**", "**Changes from Milestone 2 in full.**"),
                ("research/appendix/detail-02.md", "**Raw files and checksums in full.**", "**Flagged records"),
                ("research/appendix/detail-01.md", "**Entry gate in full.**", "**Profiling findings in full.**"),
                ("report/12-04-traceability-change-log.vi.md", "**Chi tiết về phiên bản cơ sở.**",
                 "**Chi tiết về các thay đổi từ Milestone 2.**"),
                ("report/12-02-pipeline-package.vi.md", "**Chi tiết về các tệp gốc và mã kiểm tra.**",
                 "**Các bản ghi được gắn cờ"),
                ("report/12-01-profiling-details.vi.md", "**Chi tiết về điều kiện đầu vào.**",
                 "**Chi tiết về kết quả khảo sát dữ liệu.**")],
        "renumber": [],
    },
    "M6": {
        "restore": ["07-03-residual-risks"],
        "cut": [("research/appendix/detail-06.md", "**Residual risks in full.**", None),
                ("report/12-06-validation-ledger.vi.md", "**Chi tiết về các rủi ro còn lại.**", None)],
        "renumber": [],
    },
    "M7": {
        "restore": ["08-02-readiness-matrix"],
        "cut": [("research/appendix/detail-06.md", "**Why a ranking is needed.**", "**Before-and-after checks explained.**"),
                ("report/12-06-validation-ledger.vi.md", "**Lý do cần xếp hạng.**",
                 "**Giải thích các phép kiểm tra trước và sau chuẩn bị.**")],
        "renumber": [("A.19", "A.20")],
    },
}


def baseline(rel):
    return subprocess.run(["git", "show", f"{BASE}:reports/milestone-3/{rel}"], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout


def apply(move):
    spec = MOVES[move]
    for stem in spec["restore"]:
        for suffix in (".md", ".vi.md"):
            rel = f"report/{stem}{suffix}"
            text = baseline(rel)
            for old, new in spec["renumber"]:
                text = text.replace(old, new)
            (ROOT / rel).write_text(text)
            print("restored", rel)
    for rel, start, end in spec["cut"]:
        path = ROOT / rel
        text = path.read_text()
        i = text.index(start)
        j = text.index(end, i) if end else len(text)
        text = text[:i] + text[j:] if end else text[:i].rstrip() + "\n"
        path.write_text(text)
        print("cut", rel, "from", start)


def main():
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "snapshot":
        dst = Path(arg)
        shutil.copytree(ROOT / "report", dst / "report", dirs_exist_ok=True)
        shutil.copytree(ROOT / "research" / "appendix", dst / "appendix", dirs_exist_ok=True)
    elif cmd == "restore":
        src = Path(arg)
        shutil.copytree(src / "report", ROOT / "report", dirs_exist_ok=True)
        shutil.copytree(src / "appendix", ROOT / "research" / "appendix", dirs_exist_ok=True)
    elif cmd == "apply":
        apply(arg)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
