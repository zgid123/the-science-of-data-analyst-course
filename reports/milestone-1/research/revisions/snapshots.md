# Saved states of the Milestone 1 report

Each saved state is a git commit and a path, not a copied folder. Every file below was checked byte for byte
against commit `255c158` before its folder was removed (log: `logs/R_layout_2026-11-08.log`).

Restore a whole state into a scratch folder:

```bash
git archive 255c158 <path> | tar -x -C /tmp/state     # or: git show 255c158:<path>/<file>
```

| Label | Path at commit 255c158 | Files | First committed | What it is |
| :---- | :---- | :---- | :---- | :---- |
| full-draft | `reports/milestone-1/research/revision/full-draft` | 22 | `decc925` (2026-11-07) | The full draft of the main text before blocks were moved to the appendices. |
| condensed-2026-11-07 | `reports/milestone-1/research/revision/condensed-2026-11-07` | 62 | `decc925` (2026-11-07) | The report as it stood before the full-draft revision (the condensed version), kept for page and word comparison in `01-appendix-decisions.md`. |
