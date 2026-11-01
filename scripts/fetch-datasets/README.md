# Fetch the project datasets

`fetch_datasets.py` downloads, extracts, derives and verifies the education datasets into `datasets/` at the
repository root (git-ignored). Sources live in `datasets.toml`; edit that file when a URL or an expected file
changes.

## Analysis focus: OULAD

The final project's deep-dive analysis uses **OULAD** (Open University Learning Analytics Dataset,
`datasets/oulad/`). Running the script without dataset names fetches OULAD only. The other six datasets were
screened during milestone 2 and stay available as reference data: name them, or use `--all`.

| Dataset | Role | Folder | Source | Checks |
|---|---|---|---|---|
| `oulad` | **analysis focus** | `oulad/` | figshare `anonymisedData.zip` (kept as raw evidence) | archive and 7 CSVs match the SHA-256 recorded in milestone 2 |
| `fff` | reference: OULAD subset | `fff/` | derived from OULAD: module FFF, 4 cohorts | exact row counts of all 7 tables |
| `ednet` | reference | `ednet/` | Google Drive: contents + KT1 logs | 4 content tables, ≥ 784,309 KT1 user files |
| `mooccubex` | reference | `mooccubex/` | GitHub repo + XuetangX CDN entities/relations | repo README, 3 entity and 9 relation files |
| `college-scorecard` | reference | `college-scorecard/` | U.S. Dept. of Education, most recent cohorts | institution and field-of-study CSVs |
| `pisa-2022` | reference | `pisa-2022/` | OECD webfs: school/teacher questionnaires, ESCS trend | 2 SPSS files, ESCS CSV, ReadMe |
| `talis-2024` | reference | `talis-2024/` | OECD webfs: principal and teacher questionnaires | 8 CSVs |

## Run

From the repository root:

```bash
venv/bin/python scripts/fetch-datasets/fetch_datasets.py               # OULAD (analysis focus)
venv/bin/python scripts/fetch-datasets/fetch_datasets.py fff pisa-2022 # named reference datasets
venv/bin/python scripts/fetch-datasets/fetch_datasets.py --all         # all seven
venv/bin/python scripts/fetch-datasets/fetch_datasets.py --verify      # check what is on disk
venv/bin/pip install -r scripts/fetch-datasets/requirements.txt        # once, before fetching EdNet (gdown)
```

Options: `--root DIR` writes elsewhere, `--workers N` sets parallel range requests per large file (default 8),
`--force` re-downloads and re-derives.

## Behaviour

- **Resumable and idempotent.** Finished downloads, extractions and derived files are skipped on rerun;
  interrupted downloads continue from their partial files.
- **Fast on throttled hosts.** Files over 20 MB on servers that accept byte ranges download in parallel parts,
  which matters for `webfs.oecd.org` (about 60 KB/s per connection).
- **Raw files preserved.** Archives stay next to their extracted contents; FFF rows are copied line for line
  from the OULAD CSVs.
- **Verified result.** The run ends with an inventory (files, size, PASS/FAIL per dataset, the failing check).
  `datasets/inventory.json` always describes all seven datasets; the exit code is 1 when a selected dataset
  fails a check.
- **Earlier paths keep working.** Code and saved evidence in `final-project/` read
  `final-project/datasets/...`; the script keeps `final-project/datasets` as a symlink to `../datasets`.
- **Portable TLS.** Uses `certifi` when installed, otherwise the system CA bundle, so it also works on
  python.org builds of Python on macOS.
