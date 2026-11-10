"""Term decisions after the Vietnamese reader test, applied to every Milestone 5 twin (*.vi.md).
Prints the count per term and file; run from the repository root: venv/bin/python <this file>."""
import re
from pathlib import Path

R = Path(__file__).resolve().parents[3] / "report"
S = r"\s+"
RULES = [
    ("penalised (first use form)", re.compile(rf"hiệu{S}chỉnh{S}phạt{S}\(penalised{S}logistic{S}regression\)"), "điều chuẩn (penalised)"),
    ("penalised", re.compile(rf"hiệu{S}chỉnh{S}phạt"), "điều chuẩn"),
    ("registered at day d", re.compile(rf"còn{S}hiệu{S}lực"), "chưa rút"),
    ("registered at day d (capital)", re.compile(rf"Còn{S}hiệu{S}lực"), "Chưa rút"),
    ("fit rating", re.compile(rf"([Mm])ức{S}hỗ{S}trợ"), r"\1ức phù hợp của dữ liệu"),
    ("lift", re.compile(rf"[Mm]ức{S}vượt{S}tỷ{S}lệ{S}nền(?:{S}của{S}kỳ{S}mở)?(?:{S}\(lift\))?(?:{S}\(lift\))?"), "lift"),
]
total = {}
for p in sorted(R.glob("*.vi.md")):
    text = p.read_text()
    for name, rx, rep in RULES:
        text, n = rx.subn(rep, text)
        if n:
            total[name] = total.get(name, 0) + n
            print(f"{p.name}: {name} × {n}")
    p.write_text(text)
print("TOTAL", total)
