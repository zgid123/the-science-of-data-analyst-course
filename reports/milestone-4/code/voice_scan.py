"""List every place a report refers to its own team, in English and Vietnamese, for the first-person switch.

Usage: venv/bin/python reports/milestone-4/code/voice_scan.py [milestone numbers]   (default 1 2 3 4)
Prints counts per milestone and language, then each hit with file:line and context.
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
EN = re.compile(r"\b(the team|team's|we|our|us|ours|ourselves)\b", re.I)
VI = re.compile(r"(nhóm tác giả|các tác giả|chúng em|chúng tôi|(?:^|[.;:]\s+|\*\*\s*)Nhóm(?= [a-zđàáảãạăâêôơưéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵ]))")
ms = sys.argv[1:] or ["1", "2", "3", "4"]
for m in ms:
    rep = ROOT / f"reports/milestone-{m}/report"
    for lang, rx, files in [("EN", EN, [f for f in sorted(rep.glob("*.md")) if not f.name.endswith(".vi.md")]),
                            ("VI", rx_vi := VI, sorted(rep.glob("*.vi.md")))]:
        hits = []
        for f in files:
            for i, line in enumerate(f.read_text().splitlines(), 1):
                for mt in rx.finditer(line):
                    a, b = max(0, mt.start() - 50), mt.end() + 50
                    hits.append(f"  {f.name}:{i}: …{line[a:b]}…")
        print(f"M{m} {lang}: {len(hits)} hits")
        if "-v" in sys.argv[0:0] or True:
            print("\n".join(hits))
