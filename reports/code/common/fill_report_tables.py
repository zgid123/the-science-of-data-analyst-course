"""Write the tables of the four reports into `aq-*/README.md` from the result tables.

A report marks the place of a table with a pair of HTML comments, which a Markdown viewer does not show:

    <!-- table: AQ2 Table 3 -->
    <!-- /table -->

This script puts the title and the rows built by `common/report_tables.py` between the two comments, replacing
whatever stood there. The prose of a report is written by hand; its tables are never typed.

    python common/fill_report_tables.py     (run through common/run_step.py: logs/fill_report_tables.md)
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report_tables as rt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
missing = 0
for aq, fn in rt.ALL.items():
    path = ROOT / aq / "README.md"
    text = path.read_text()
    filled = 0
    for title, lines in fn().items():
        key = title.split(".")[0]                                  # "AQ2 Table 3"
        shown = title.split(" ", 1)[1]                             # "Table 3. ..."
        block = f"<!-- table: {key} -->\n**{shown}**\n\n" + "\n".join(lines) + "\n<!-- /table -->"
        pattern = re.compile(rf"<!-- table: {re.escape(key)} -->.*?<!-- /table -->", re.S)
        if not pattern.search(text):
            print(f"- {aq}/README.md: no place marked for '{key}'")
            missing += 1
            continue
        text = pattern.sub(lambda _m: block, text, count=1)
        filled += 1
    path.write_text(text)
    print(f"- {aq}/README.md: {filled} tables written from the result tables")
print("\nRESULT:", "PASS" if not missing else f"FAIL ({missing} tables have no place in a report)")
sys.exit(1 if missing else 0)
