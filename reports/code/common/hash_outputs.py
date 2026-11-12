"""Determinism check of the development folds: hash the five output files before and after a full rerun.

    python common/hash_outputs.py before     writes logs/determinism_before.sha256
    python common/hash_outputs.py after      writes logs/determinism_after.sha256, compares both, exits 1 on a difference

`aq-3/results/dev_fold_design.csv` is left out because it stores the seconds each fold took.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib  # noqa: E402

FILES = ["aq-3/results/dev_folds.csv", "aq-3/results/dev_tuning.csv", "aq-3/results/dev_pooled.csv",
         "aq-3/extracted-datasets/aq3_dev_oof_scores_d27.csv", "aq-3/extracted-datasets/aq3_dev_oof_scores_d13.csv"]
tag = sys.argv[1]
assert tag in ("before", "after")
text = "".join(f"{lib.sha256(lib.CODE_ROOT / f)}  {f}\n" for f in FILES)
out = lib.CODE_ROOT / "logs" / f"determinism_{tag}.sha256"
out.write_text(text)
print(f"```\n{text}```\nwritten to logs/{out.name}")
if tag == "after":
    before = (lib.CODE_ROOT / "logs" / "determinism_before.sha256").read_text()
    same = sum(a == b for a, b in zip(before.splitlines(), text.splitlines()))
    print(f"\nfiles byte-identical after the rerun of the development folds: {same} of {len(FILES)}")
    print("RESULT:", "PASS" if before == text else "FAIL")
    sys.exit(0 if before == text else 1)
