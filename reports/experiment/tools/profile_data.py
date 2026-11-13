"""Fast first look at tabular files: shape, types, nulls, distinct counts, examples, candidate keys.

Usage:
    python profile_data.py data/*.csv                     # Markdown to stdout
    python profile_data.py big.csv --nrows 200000 -o notes/profile.md
    python profile_data.py table.parquet --max-cols 80

A profile shows fitness for use; it is not an analysis. Use it to decide what to inspect next:
column meanings still need the data dictionary and real records. With --nrows, counts describe
the first N rows only, which may not be representative of the full file.

The separator (comma, semicolon, tab or pipe) is read from the header line. Without pandas, delimited text files are profiled with the standard library (types are inferred from the text);
Parquet needs pandas with pyarrow, or pandas with polars; Excel needs pandas with openpyxl (`python setup_env.py`).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    pd = None


def delimiter(path: Path) -> str:
    """Separator of a delimited text file, read from its header line: comma, semicolon, tab or pipe."""
    with open(path, newline="", encoding="utf-8-sig") as fh:
        head = fh.readline()
    return max(",;\t|", key=head.count) if any(c in head for c in ",;\t|") else ","


def read_table(path: Path, nrows: int | None) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        try:
            df = pd.read_parquet(path)
        except ImportError:                                         # no pyarrow or fastparquet: read with polars if present
            try:
                import polars as pl
            except ImportError:
                raise ImportError("reading Parquet needs pyarrow or polars: run `python setup_env.py`") from None
            frame = pl.read_parquet(path, n_rows=nrows)
            return pd.DataFrame(frame.to_dict(as_series=False))   # column by column: needs no pyarrow
        return df.head(nrows) if nrows else df
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, nrows=nrows)
    return pd.read_csv(path, sep=delimiter(path), nrows=nrows, low_memory=False)


def _fmt(value) -> str:
    text = str(value).replace("|", "\\|").replace("\n", " ")
    return text if len(text) <= 40 else text[:37] + "..."


def column_summary(s: pd.Series) -> dict:
    if s.dtype == object:                                           # a cell holding only spaces is a missing value
        s = s.where(~s.astype(str).str.fullmatch(r"\s*"), other=None)
    n = len(s)
    nulls = int(s.isna().sum())
    non_null = s.dropna()
    distinct = int(non_null.nunique())
    info = {
        "column": s.name,
        "dtype": str(s.dtype),
        "null %": f"{nulls / n:.1%}" if n else "—",
        "distinct": f"{distinct:,}",
        "summary": "",
    }
    if non_null.empty:
        info["summary"] = "all null"
    elif pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s):
        q = non_null.quantile([0, 0.5, 1])
        zeros = (non_null == 0).mean()
        info["summary"] = f"min {q.iloc[0]:,.4g} · median {q.iloc[1]:,.4g} · max {q.iloc[2]:,.4g}" + (f" · zeros {zeros:.0%}" if zeros >= 0.05 else "")
    else:
        top = non_null.astype(str).value_counts().head(3)
        info["summary"] = ", ".join(f"{_fmt(k)} ({v / len(non_null):.0%})" for k, v in top.items())
        if distinct > 3 and non_null.astype(str).str.match(r"^\d{4}-\d{2}-\d{2}").mean() > 0.9:
            info["summary"] += f" · range {_fmt(non_null.min())} → {_fmt(non_null.max())}"
    return info


def candidate_keys(df: pd.DataFrame, limit: int = 5) -> list[str]:
    """Single columns, then pairs, then triples that are unique and non-null in the rows read."""
    from itertools import combinations

    n = len(df)
    singles = [c for c in df.columns if df[c].notna().all() and df[c].nunique() == n]
    if singles:
        return [f"`{c}`" for c in singles[:limit]]
    cols = [c for c in df.columns if df[c].notna().all() and 1 < df[c].nunique() < n]
    for size, max_cols in ((2, 25), (3, 12)):
        found = []
        for combo in combinations(cols[:max_cols], size):
            if not df.duplicated(list(combo)).any():
                found.append(" + ".join(f"`{c}`" for c in combo))
                if len(found) >= limit:
                    return found
        if found:
            return found
    return []


def profile_stdlib(path: Path, nrows: int | None, max_cols: int) -> str:
    """The same profile for CSV/TSV with the standard library only."""
    import csv
    import statistics
    from collections import Counter
    from itertools import islice

    if path.suffix.lower() not in {".csv", ".tsv", ".tab", ".txt"}:
        raise RuntimeError("this file type needs pandas (run setup_env.py)")
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.reader(fh, delimiter=delimiter(path))
        header = next(reader)
        rows = list(islice(reader, nrows)) if nrows else list(reader)
    n = len(rows)
    width = len(header)
    cols = [[r[i] if i < len(r) else "" for r in rows] for i in range(width)]
    missing = {"", "na", "n/a", "nan", "null", "none", "?"}

    def numeric(values):
        out = []
        for v in values:
            try:
                out.append(float(v))
            except ValueError:
                return None
        return out

    dup = n - len({tuple(r) for r in rows})
    keys = [f"`{header[i]}`" for i in range(width) if all(v.strip().lower() not in missing for v in cols[i]) and len(set(cols[i])) == n][:5]
    scope = f"first {n:,} rows (sampled with --nrows)" if nrows and n >= nrows else f"{n:,} rows"
    lines = [f"## {path.name}", "", f"- Rows read: {scope}; columns: {width} (profiled without pandas)",
             f"- Exact duplicate rows: {dup:,}" + (" — check whether these are true duplicates or legitimate repeats" if dup else ""),
             f"- Candidate keys (unique, non-null here): {', '.join(keys) if keys else 'none found among single columns'}", "",
             "| Column | Type | Null % | Distinct | Values |", "| --- | --- | --- | --- | --- |"]
    for name, values in list(zip(header, cols))[:max_cols]:
        present = [v for v in values if v.strip().lower() not in missing]
        nums = numeric(present) if present else None
        if not present:
            kind, summary = "empty", "all null"
        elif nums is not None:
            kind = "integer" if all(x == int(x) for x in nums) else "float"
            zeros = sum(1 for x in nums if x == 0) / len(nums)
            summary = f"min {min(nums):,.4g} · median {statistics.median(nums):,.4g} · max {max(nums):,.4g}" + (f" · zeros {zeros:.0%}" if zeros >= 0.05 else "")
        else:
            kind = "text"
            summary = ", ".join(f"{_fmt(k)} ({v / len(present):.0%})" for k, v in Counter(present).most_common(3))
        lines.append(f"| `{_fmt(name)}` | {kind} | {(n - len(present)) / n:.1%} | {len(set(present)):,} | {summary} |" if n else f"| `{_fmt(name)}` | {kind} | — | 0 | |")
    if width > max_cols:
        lines.append(f"\n_{width - max_cols} more columns not shown (raise --max-cols)._")
    lines.append("")
    return "\n".join(lines)


def profile(path: Path, nrows: int | None, max_cols: int) -> str:
    if pd is None:
        return profile_stdlib(path, nrows, max_cols)
    df = read_table(path, nrows)
    lines = [f"## {path.name}", ""]
    scope = f"first {len(df):,} rows (sampled with --nrows)" if nrows and len(df) >= nrows else f"{len(df):,} rows"
    lines.append(f"- Rows read: {scope}; columns: {df.shape[1]}")
    dup = int(df.duplicated().sum())
    lines.append(f"- Exact duplicate rows: {dup:,}" + (" — check whether these are true duplicates or legitimate repeats" if dup else ""))
    keys = candidate_keys(df)
    lines.append(f"- Candidate keys (unique, non-null here): {', '.join(keys) if keys else 'none found among single columns or pairs'}")
    lines.append("")
    lines.append("| Column | Type | Null % | Distinct | Values |")
    lines.append("| --- | --- | --- | --- | --- |")
    for col in df.columns[:max_cols]:
        info = column_summary(df[col])
        lines.append(f"| `{_fmt(info['column'])}` | {info['dtype']} | {info['null %']} | {info['distinct']} | {info['summary']} |")
    if df.shape[1] > max_cols:
        lines.append(f"\n_{df.shape[1] - max_cols} more columns not shown (raise --max-cols)._")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=Path, help="CSV, TSV, Parquet or Excel files")
    parser.add_argument("--nrows", type=int, default=None, help="read only the first N rows of each file")
    parser.add_argument("--max-cols", type=int, default=60, help="maximum columns to list per file")
    parser.add_argument("-o", "--output", type=Path, help="write Markdown here instead of stdout")
    args = parser.parse_args(argv)

    sections = ["# Data profile", ""]
    failed = False
    for path in args.paths:
        try:
            sections.append(profile(path, args.nrows, args.max_cols))
        except Exception as exc:  # report and continue with other files
            failed = True
            sections.append(f"## {path.name}\n\nCould not read: {exc}\n")
    text = "\n".join(sections)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(f"Wrote {args.output}")
    else:
        sys.stdout.write(text)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
