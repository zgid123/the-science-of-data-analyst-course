"""Put ../tools on the import path: start every script in code/ with `import _tools`."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
