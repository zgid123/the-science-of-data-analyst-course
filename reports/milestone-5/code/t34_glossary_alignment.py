"""T34 follow-up: align ten Milestone 2–4 Vietnamese lines with glossary terms that Milestone 5 settled after those
reports were built (the parity check flags each replaced form as an error).

- "dấu hiệu học nhiều module (cùng lúc)" → "dấu hiệu học đồng thời nhiều module" (several-modules sign);
- "kỳ mở không có cặp" → "kỳ mở không có kỳ tương ứng năm 2013" (unpaired run);
- "sinh viên học lại" as the repeat students of the 2014 test → "sinh viên đã có mặt năm 2013";
  as the general idea of retaking a module, reworded without the reserved term.

Usage: venv/bin/python reports/milestone-5/code/t34_glossary_alignment.py   (each edit must match exactly once)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EDITS = [
 ("reports/milestone-2/report/06-00-structural-verification.vi.md",
  "một sinh viên học lại cùng một module", "một sinh viên đăng ký lại cùng một module"),
 ("reports/milestone-3/report/04-01-fit-ratings.vi.md",
  "dấu hiệu học nhiều module cùng lúc", "dấu hiệu học đồng thời nhiều module"),
 ("reports/milestone-3/report/06-03-split-leakage.vi.md",
  "cũng có sinh viên học lại", "cũng có sinh viên đã từng học module đó"),
 ("reports/milestone-3/report/12-02-pipeline-package.vi.md",
  "cũng sẽ có sinh viên học lại", "cũng sẽ có sinh viên đã từng học module đó"),
 ("reports/milestone-4/report/04-02-validation-strategy.vi.md",
  "cho 4 kỳ mở không có cặp", "cho 4 kỳ mở không có kỳ tương ứng năm 2013"),
 ("reports/milestone-4/report/06-00-genai-usage.vi.md",
  "nhu cầu hỗ trợ hay không, sinh viên học lại", "nhu cầu hỗ trợ hay không, sinh viên đã có mặt năm 2013"),
 ("reports/milestone-4/report/10-03-validation-protocol.vi.md",
  "các kỳ mở không có cặp (4 kỳ mở)", "các kỳ mở không có kỳ tương ứng năm 2013 (4 kỳ mở)"),
 ("reports/milestone-4/report/10-03-validation-protocol.vi.md",
  "9 kỳ mở có cặp / 4 kỳ mở không có cặp", "9 kỳ mở có cặp / 4 kỳ mở không có kỳ tương ứng năm 2013"),
 ("reports/milestone-4/report/10-05-risk-register.vi.md",
  "xét riêng kỳ mở có cặp và kỳ mở không có cặp", "xét riêng kỳ mở có cặp và kỳ mở không có kỳ tương ứng năm 2013"),
 ("reports/milestone-4/report/10-06-ai-critiques.vi.md",
  "Ngày rút khỏi module không xác định và sinh viên học lại", "Ngày rút khỏi module không xác định và sinh viên đã có mặt năm 2013"),
]

bad = 0
for rel, old, new in EDITS:
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    if t.count(new) and not t.count(old):
        print(f"already  {rel}")
        continue
    if t.count(old) != 1:
        print(f"FAIL     {rel}: '{old}' found {t.count(old)} times"); bad += 1; continue
    p.write_text(t.replace(old, new), encoding="utf-8")
    print(f"edited   {rel}")
sys.exit(1 if bad else 0)
