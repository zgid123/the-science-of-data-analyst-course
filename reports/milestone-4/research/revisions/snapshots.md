# Saved states of the Milestone 4 report

Each saved state is a git commit and a path, not a copied folder. Every file below was checked byte for byte
against commit `255c158` before its folder was removed (log: `logs/R_layout_2026-11-08.log`).

Restore a whole state into a scratch folder:

```bash
git archive 255c158 <path> | tar -x -C /tmp/state     # or: git show 255c158:<path>/<file>
```

| Label | Path at commit 255c158 | Files | First committed | What it is |
| :---- | :---- | :---- | :---- | :---- |
| condensed-2026-11-08 | `reports/milestone-4/research/revision/condensed-2026-11-08` | 70 | `c6d4f44` (2026-11-08) | The report as it stood before the full-draft revision (the condensed version), kept for page and word comparison in `01-appendix-decisions.md`. |
| full-draft-2026-11-08 | `reports/milestone-4/research/revision/full-draft-2026-11-08` | 52 | `c6d4f44` (2026-11-08) | The full draft of the main text before blocks were moved to the appendices. |
