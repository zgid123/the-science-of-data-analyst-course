#!/usr/bin/env python3
"""Follow-up to apply.py: the 01-01 twin's delivery-mode clause used ', và', which the Vietnamese parity check
flags (guide sections 2.7 and 5). Set the clause in parentheses instead; the meaning is unchanged.

Run: venv/bin/python reports/milestone-4/research/revision/english-additions-2026-11-08/fix_twin.py
"""
from pathlib import Path
import sys

TWIN = Path(__file__).resolve().parents[3] / "report" / "01-01-goal-decisions-aqs.vi.md"
OLD = ("theo hình thức học, vốn không khác nhau trong OULAD vì mọi kỳ mở đều là đào tạo từ xa, "
       "và theo năm theo học")
NEW = ("theo hình thức học (vốn không khác nhau trong OULAD vì mọi kỳ mở đều là đào tạo từ xa) "
       "và theo năm theo học")


def main() -> int:
    text = TWIN.read_text(encoding="utf-8")
    assert text.count(OLD) == 1, f"old string occurs {text.count(OLD)} times"
    TWIN.write_text(text.replace(OLD, NEW), encoding="utf-8")
    print(f"{TWIN.name}: delivery-mode clause set in parentheses")
    return 0


if __name__ == "__main__":
    sys.exit(main())
