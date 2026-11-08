"""Build and execute the two notebooks of brief section 10.1 from the package's own outputs.

notebooks/02_data_understanding.ipynb walks through Tasks 1–2 (Dataset Understanding Map, profile, Data Quality
Issue Log); notebooks/03_data_preparation.ipynb walks through Tasks 4–8 (decision matrix, transformation log, the
prepared views, split and leakage checks, validation). Each notebook reads the files written by run_all.sh and
re-queries the prepared views with polars, so a reader can retrace the pipeline cell by cell; the pipeline itself
runs in run_all.sh, not in the notebooks. Executed with nbclient; outputs are saved in the notebooks.

Usage (from the package folder): python src/build_notebooks.py   (after run_all.sh steps 00-06)
"""
from __future__ import annotations

import nbformat
from nbclient import NotebookClient

from common import PKG

NB = PKG / "notebooks"
SETUP = """import json, sys
from pathlib import Path
import polars as pl
from IPython.display import Markdown, display
PKG = Path.cwd().parent
sys.path.insert(0, str(PKG / "src"))
META, PROCESSED = PKG / "data" / "metadata", PKG / "data" / "processed"
pl.Config.set_tbl_rows(30); pl.Config.set_tbl_cols(20); pl.Config.set_fmt_str_lengths(80)
show = lambda name: display(Markdown((META / name).read_text()))"""


def nb(cells):
    n = nbformat.v4.new_notebook()
    n.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    n.cells = [nbformat.v4.new_markdown_cell(c) if c.startswith("#") else nbformat.v4.new_code_cell(c)
               for c in cells]            # markdown cells start with a heading, every other cell is code
    return n


UNDERSTANDING = [
    "# 02 – Data understanding and data quality (Tasks 1–2)\n\nOULAD as collected in Milestone 2 (seven CSV tables, "
    "SHA-256 pinned). This notebook reads the outputs of `src/01_understand.py` and `src/02_profile.py`; every number "
    "comes from `data/metadata/understanding.json` or `profile.json`.",
    SETUP,
    "## Raw files are the Milestone 2 files",
    "pl.read_csv(META / 'raw_check.csv')",
    "## Dataset Understanding Map (Task 1)",
    "show('understanding_map.md')",
    "U = json.loads((META / 'understanding.json').read_text())\n"
    "{k: U['population'][k] for k in ['runs', 'enrolments', 'students', 'students_with_several_enrolments', 'run_length_days']}",
    "U['outcome']",
    "U['time']",
    "## Profile (Task 2): the ten aspects of brief section 7",
    "P = json.loads((META / 'profile.json').read_text())\nlist(P)",
    "P['duplicates']['chance_test_two_row_groups']",
    "P['missing']['imd_band_by_region_top3'], P['missing']['imd_band_success_missing_vs_present']",
    "P['outcome']['population_at_cutoff'], P['outcome']['kpi_completion_rate']",
    "P['temporal']['tasks_due_by_cutoff']",
    "P['joins']",
    "## Cross-check with the earlier OULAD exploration",
    "pl.read_csv(META / 'profile_crosscheck.csv')",
    "## Data Quality Issue Log",
    "show('quality_issue_log.md')",
]

PREPARATION = [
    "# 03 – Data preparation, leakage control and validation (Tasks 4–8)\n\nThis notebook reads the outputs of "
    "`src/prepare_data.py`, `src/fit_transforms.py` and `src/validate_prepared.py` and re-queries the prepared views.",
    SETUP,
    "## Preparation Decision Matrix (Task 4)",
    "show('decision_matrix.md')",
    "## Transformation log (Task 5): rows in and out of every step",
    "show('transformation_log.md')",
    "## The prepared views",
    "{p.stem: pl.scan_parquet(p).select(pl.len()).collect().item() for p in sorted(PROCESSED.glob('*.parquet'))}",
    "f27 = pl.read_parquet(PROCESSED / 'features_d27.parquet')\nf27.head(5)",
    "## Split and leakage (Task 6)",
    "f27.group_by('split').agg(pl.len(), pl.col('code_presentation').unique().sort())",
    "f27.filter(pl.col('split') == 'train').select(pl.col('non_completion').mean().alias('training non-completion rate'))",
    "tp = json.loads((META / 'transform_params.json').read_text())\n"
    "tp['fitted_on'], tp['cutoffs']['d27']['nominal_levels']",
    "## Early-sign rule: firing rate per run (no outcome used)",
    "pl.read_csv(META / 'rule_rates.csv').filter(pl.col('cutoff_day') == 27)",
    "## Validation (Task 8)",
    "show('validation_summary.md')",
    "pl.read_csv(META / 'manual_check_d27.csv')",
    "## Data dictionary (excerpt) and lineage",
    "display(Markdown('\\n'.join((META / 'data_dictionary.md').read_text().splitlines()[:30])))",
]


def main():
    NB.mkdir(exist_ok=True)
    for name, cells in (("02_data_understanding", UNDERSTANDING), ("03_data_preparation", PREPARATION)):
        n = nb(cells)
        NotebookClient(n, timeout=600, kernel_name="python3", resources={"metadata": {"path": str(NB)}}).execute()
        errors = [o for c in n.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.output_type == "error"]
        nbformat.write(n, NB / f"{name}.ipynb")
        print(f"{name}.ipynb: {sum(c.cell_type == 'code' for c in n.cells)} code cells executed, {len(errors)} errors")
        if errors:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
