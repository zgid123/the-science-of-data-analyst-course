"""Prepare the Python environment of an analysis folder and say what is available.

    python setup_env.py                 create .venv here, install requirements.txt, write requirements.lock
    python setup_env.py --check         only report which packages the current interpreter can import

`run_all.sh` uses `.venv/bin/python` when it exists. If the installation fails (no network, no venv module), the
script says so and exits 1: carry on with the standard-library tools, which need no package, state the limit in
NOTES.md, and write analysis code with the standard library (csv, statistics, math). Standard library only.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

PACKAGES = {"pandas": "pandas", "numpy": "numpy", "matplotlib": "matplotlib", "openpyxl": "openpyxl (Excel)", "pyarrow": "pyarrow (Parquet)",
            "sklearn": "scikit-learn", "statsmodels": "statsmodels"}


def available(python: str = sys.executable) -> dict:
    if python == sys.executable:
        return {label: importlib.util.find_spec(module) is not None for module, label in PACKAGES.items()}
    code = "import importlib.util as u, json; print(json.dumps({m: u.find_spec(m) is not None for m in %r}))" % list(PACKAGES)
    import json
    found = json.loads(subprocess.run([python, "-c", code], capture_output=True, text=True, check=True).stdout)
    return {PACKAGES[m]: ok for m, ok in found.items()}


def report(state: dict, python: str) -> None:
    print(f"interpreter: {python}")
    for label, ok in state.items():
        print(f"- {label}: {'available' if ok else 'MISSING'}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create .venv and install the analysis packages, or report what is available.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--requirements", type=Path, default=None)
    args = parser.parse_args(argv)
    if args.check:
        state = available()
        report(state, sys.executable)
        return 0 if all(state.values()) else 1
    requirements = args.requirements or next((p for p in (Path("requirements.txt"), Path("tools/requirements.txt"),
                                                         Path(__file__).resolve().parent / "requirements.txt",
                                                         Path(__file__).resolve().parents[1] / "requirements.txt") if p.exists()), None)
    if requirements is None:
        print("no requirements.txt found")
        return 1
    venv_python = Path(".venv/bin/python")
    try:
        if not venv_python.exists():
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        subprocess.run([str(venv_python), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "-r", str(requirements)], check=True)
        frozen = subprocess.run([str(venv_python), "-m", "pip", "freeze"], capture_output=True, text=True, check=True).stdout
        Path("requirements.lock").write_text(frozen)
    except (subprocess.CalledProcessError, OSError) as exc:
        print(f"environment NOT prepared ({exc}). The standard-library tools still work; record this limit in NOTES.md.")
        return 1
    state = available(str(venv_python))
    report(state, str(venv_python))
    print("requirements.lock written; run_all.sh will use .venv/bin/python")
    return 0 if all(state.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
