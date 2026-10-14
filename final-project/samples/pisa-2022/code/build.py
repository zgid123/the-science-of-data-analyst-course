from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"_shared"))
from build_remaining import build
build('pisa-2022')
