"""Check whether the 28,119 "active at day 14" denominator still contains
late registrations (date_registration > 14) and rows with no registration date.

Usage (from the repository root):
    python3 check-result/check_day14_denominator.py [path/to/studentRegistration.csv]
"""
import csv
import sys

DEFAULT = "datasets/oulad/studentRegistration.csv"
DAY = 14


def num(s):
    s = s.strip()
    return None if s in ("", "?") else float(s)


def main(path):
    with open(path, newline="") as fh:
        rows = [(num(r["date_registration"]), num(r["date_unregistration"]))
                for r in csv.DictReader(fh)]

    def count(cond):
        return sum(1 for reg, unreg in rows if cond(reg, unreg))

    kept = lambda reg, unreg: unreg is None or unreg > DAY
    out = [
        ("Total rows", count(lambda r, u: True)),
        ("date_unregistration <= 0", count(lambda r, u: u is not None and u <= 0)),
        (f"date_unregistration in 1..{DAY}", count(lambda r, u: u is not None and 0 < u <= DAY)),
        (f"date_unregistration empty or > {DAY}", count(kept)),
        (f"  of which date_registration > {DAY}", count(lambda r, u: kept(r, u) and r is not None and r > DAY)),
        ("  of which date_registration missing", count(lambda r, u: kept(r, u) and r is None)),
        (f"All rows with date_registration > {DAY}", count(lambda r, u: r is not None and r > DAY)),
        ("All rows with date_registration missing", count(lambda r, u: r is None)),
        ("  missing registration, unregistered <= 0", count(lambda r, u: r is None and u is not None and u <= 0)),
        (f"  missing registration, unregistered in 1..{DAY}", count(lambda r, u: r is None and u is not None and 0 < u <= DAY)),
    ]
    print(f"File: {path}")
    for label, n in out:
        print(f"{label:<52}{n:>8,}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT)
