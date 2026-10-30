# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.26"]
# ///
"""Build hard-layout.pdf: layouts the pdf2md scripts cannot fully handle.

Page 1: title, intro, then a two-column section.
Page 2: a borderless (whitespace-aligned) table and a nested list.
Used by evals/evals.json to test the agent-takeover path in SKILL.md.

Usage: uv run make_hard_layout.py [out.pdf]
"""
import sys

import pymupdf

out = sys.argv[1] if len(sys.argv) > 1 else "hard-layout.pdf"
doc = pymupdf.open()

p = doc.new_page()
p.insert_text((72, 80), "Field Study Report", fontsize=20, fontname="hebo")
p.insert_textbox(pymupdf.Rect(72, 100, 523, 160),
                 "This report summarises a two-week field study of study habits. "
                 "The left column describes the method; the right column lists the main observations.",
                 fontsize=10.5, fontname="helv")
p.insert_text((72, 185), "Method", fontsize=13, fontname="hebo")
p.insert_text((310, 185), "Observations", fontsize=13, fontname="hebo")
left = ("Students kept a daily log of study sessions, recording start time, duration and location. "
        "Logs were collected every evening and checked for gaps. Twelve students took part, "
        "all from the same first-year statistics course. Sessions shorter than ten minutes were "
        "recorded but excluded from totals.")
right = ("Most sessions happened after 8 pm. Library sessions were longer than sessions at home. "
         "Group sessions were rare in the first week and more common before the quiz. "
         "Three students stopped logging after day nine, so their second week is incomplete.")
p.insert_textbox(pymupdf.Rect(72, 195, 285, 420), left, fontsize=10.5, fontname="helv")
p.insert_textbox(pymupdf.Rect(310, 195, 523, 420), right, fontsize=10.5, fontname="helv")

p = doc.new_page()
p.insert_text((72, 80), "Session summary", fontsize=13, fontname="hebo")
rows = [("Location", "Sessions", "Median minutes"), ("Library", "41", "52"),
        ("Home", "96", "31"), ("Cafe", "12", "24"), ("Other", "7", "18")]
y = 110
for i, (a, b, c) in enumerate(rows):
    font = "hebo" if i == 0 else "helv"
    p.insert_text((72, y), a, fontsize=10.5, fontname=font)
    p.insert_text((230, y), b, fontsize=10.5, fontname=font)
    p.insert_text((330, y), c, fontsize=10.5, fontname=font)
    y += 18
p.insert_text((72, 230), "Follow-up actions", fontsize=13, fontname="hebo")
items = [(0, "•", "Repeat the study in week 6"), (1, "◦", "use the same twelve students"),
         (1, "◦", "add a sleep column to the log"), (0, "•", "Share results with the course team"),
         (1, "◦", "short summary, no individual data")]
y = 255
for lvl, glyph, text in items:
    x = 82 + lvl * 20
    p.insert_text((x, y), glyph, fontsize=10.5, fontname="helv")
    p.insert_text((x + 12, y), text, fontsize=10.5, fontname="helv")
    y += 16
p.insert_text((72, y + 14), "All data stays on the course drive.", fontsize=10.5, fontname="helv")
doc.save(out)
print("wrote", out)
