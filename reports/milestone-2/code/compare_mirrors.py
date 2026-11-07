"""Compare the OULAD tables of a second distribution (the UCI zip) with the collected figshare tables.

Usage: venv/bin/python reports/milestone-2/code/compare_mirrors.py PATH_TO_UCI_ZIP
For each table: bytes and SHA-256 in both copies, data rows, line-ending style, and whether the parsed rows are
identical after normalising line endings and quoting (so a formatting-only difference is told apart from content).
"""
import csv
import hashlib
import io
import sys
import zipfile
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "package" / "data" / "raw"


def rows(data):
    text = data.decode("utf-8-sig").replace("\r\n", "\n")
    return [tuple(c.strip() for c in r) for r in csv.reader(io.StringIO(text))]


def main(uci):
    z = zipfile.ZipFile(uci)
    print(f"UCI archive: {Path(uci).stat().st_size} bytes, SHA-256 {hashlib.sha256(Path(uci).read_bytes()).hexdigest()}")
    print("| Table | Figshare bytes | UCI bytes | Same SHA-256 | Line endings (figshare / UCI) | Rows (figshare / UCI) | Same parsed rows |")
    print("| :---- | :---- | :---- | :---- | :---- | :---- | :---- |")
    for p in sorted(RAW.glob("*.csv")):
        a = p.read_bytes()
        b = z.read(p.name)
        ea = "CRLF" if b"\r\n" in a[:5000] else "LF"
        eb = "CRLF" if b"\r\n" in b[:5000] else "LF"
        ra, rb = rows(a), rows(b)
        same = ra == rb
        diff = ""
        q_only = len(ra) == len(rb) and all(x == y or all(u == v or (u == "" and v == "?") for u, v in zip(x, y))
                                            for x, y in zip(ra, rb))
        if not same and q_only:
            n = sum(1 for x, y in zip(ra, rb) if x != y)
            same = f"only missing values written '?' in UCI, empty in figshare ({n} rows)"
        elif not same:
            n = sum(1 for x, y in zip(ra, rb) if x != y) + abs(len(ra) - len(rb))
            first = next(((x, y) for x, y in zip(ra, rb) if x != y), None)
            diff = f" ({n} rows differ; first: {first})"
        print(f"| {p.name} | {len(a)} | {len(b)} | {hashlib.sha256(a).digest() == hashlib.sha256(b).digest()} | "
              f"{ea} / {eb} | {len(ra) - 1} / {len(rb) - 1} | {same}{diff} |")
    extra = [n for n in z.namelist() if not n.endswith(".csv")]
    print(f"UCI-only members: {', '.join(extra) or 'none'}")


if __name__ == "__main__":
    main(sys.argv[1])
