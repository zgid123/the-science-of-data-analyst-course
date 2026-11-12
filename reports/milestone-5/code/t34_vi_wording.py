"""T34: three wording decisions of the team (2026-11-13), applied to Milestones 1–5 and the Vietnamese deck.

1. Title page header: keep only the university and the faculty.
   VI "TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN, ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH" → "TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN";
   EN "UNIVERSITY OF SCIENCE, VIETNAM NATIONAL UNIVERSITY HO CHI MINH CITY" → "UNIVERSITY OF SCIENCE";
   deck title slide "University of Science, VNU-HCM · …" → "University of Science · …" (and its Vietnamese string).
2. Team voice in Vietnamese: "nhóm chúng em" / "chúng em" → "nhóm" ("Nhóm" where the original began with a capital,
   i.e. at the start of a sentence or cell); quoted speech of other people uses "chúng tôi" and is not touched.
3. The support office is "Phòng Đào tạo": "phòng hỗ trợ sinh viên" (any case, also wrapped over a line) → "Phòng Đào tạo".

Usage: venv/bin/python reports/milestone-5/code/t34_vi_wording.py [--write]
Without --write it prints the counts per file and the new "nhóm …" contexts to read before writing. Idempotent.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VI_FILES = sorted(p for m in range(1, 6) for p in (ROOT / f"reports/milestone-{m}/report").glob("*.vi.md"))
DECK_VI = ROOT / "slides_milestone5_30_vi.py"
TITLE_EN = [ROOT / f"reports/milestone-{m}/report/00-0-title-page.md" for m in range(1, 6)]
DECK_EN = [ROOT / "build_slides_milestone5_30.py", ROOT / "slides_milestone5_full/part1.py"]

WS = r"[ \t]*\n?[ \t]*"                                   # a space, possibly wrapped onto the next line
TEAM = [(re.compile(rf"\bNhóm{WS}chúng{WS}em\b"), "Nhóm"), (re.compile(rf"\bnhóm{WS}chúng{WS}em\b"), "nhóm"),
        (re.compile(rf"\bChúng{WS}em\b"), "Nhóm"), (re.compile(rf"\bchúng{WS}em\b"), "nhóm")]
OFFICE = [(re.compile(rf"\b[Pp]hòng{WS}hỗ{WS}trợ{WS}sinh{WS}viên\b"), "Phòng Đào tạo")]
HEADER = [(re.compile(r"TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN, ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH"),
           "TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN"),
          (re.compile(r"UNIVERSITY OF SCIENCE, VIETNAM NATIONAL UNIVERSITY HO CHI MINH CITY"), "UNIVERSITY OF SCIENCE")]
DECK_FIX = [(re.compile(r"Nhóm là nhóm N04 và xin trình bày"), "Nhóm N04 xin trình bày")]   # after TEAM: no doubled "nhóm"
DECK_LINE = [(re.compile(r"University of Science, VNU-HCM · November 2026"), "University of Science · November 2026"),
             (re.compile(r"Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM · Tháng 11 năm 2026"),
              "Trường Đại học Khoa học Tự nhiên · Tháng 11 năm 2026")]


def apply(text, rules):
    n = 0
    for rx, rep in rules:
        text, k = rx.subn(rep, text)
        n += k
    return text, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    totals, contexts = Counter(), Counter()
    jobs = [(f, HEADER + TEAM + OFFICE) for f in VI_FILES] + [(DECK_VI, TEAM + OFFICE + DECK_LINE + DECK_FIX)] \
        + [(f, HEADER) for f in TITLE_EN] + [(f, DECK_LINE) for f in DECK_EN]
    for f, rules in jobs:
        old = f.read_text(encoding="utf-8")
        new = old
        counts = {}
        for name, group in (("header", HEADER), ("team", TEAM), ("office", OFFICE), ("deck line", DECK_LINE),
                            ("deck fix", DECK_FIX)):
            if any(r in rules for r in group):
                new, counts[name] = apply(new, group)
        if new != old:
            for name, k in counts.items():
                totals[name] += k
            if TEAM[0] in rules:                           # the words that now follow "nhóm", to read for sense
                for m in re.finditer(r"\b[Nn]hóm\s+(\w+)", new):
                    contexts[m.group(1)] += 1
                for m in re.finditer(r"\b[Nn]hóm\s+(\w+)", old):
                    contexts[m.group(1)] -= 1
            print(f"{f.relative_to(ROOT)}: " + ", ".join(f"{k} {v}" for k, v in counts.items() if v))
            if args.write:
                f.write_text(new, encoding="utf-8")
    print("TOTAL", dict(totals))
    print("new words after 'nhóm':", [(w, c) for w, c in contexts.most_common() if c > 0][:40])
    if args.write:
        print("written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
