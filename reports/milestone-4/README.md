# Milestone 4 report (team N04)

From modeling to evaluation: modeling strategy, method selection and evaluation design for OULAD, Level 1 of
`milestones/04/milestone-4.md` (Level 2 not run; Part 7 points to the prototype protocol in Appendix III).

- `reference.md`, `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md`: outline, plan and ledger (research-report skill).
- `research/`: frozen Milestone 3 baseline, design decisions, sources, claims, AI review prompts and outputs, Vietnamese
  review logs.
- `report/`: English sections and Vietnamese twins (figures drawn by `figures/milestone_4/`); `build/`:
  `N04_Milestone4_EN.docx`, `N04_Milestone4_VI.docx`.
- `code/`: task scripts; `results/`: design facts; `logs/`: run, check and build logs (UTC time, command, output, exit
  status).

## Commands (from the repository root)

```bash
venv/bin/python reports/milestone-4/code/freeze_baseline.py     # entry gate: Milestone 3 baseline copy and checks
venv/bin/python reports/milestone-4/code/design_facts.py        # counts from the prepared views (no model fitted)
venv/bin/python reports/milestone-4/code/threshold_reasons.py   # arithmetic behind the fixed thresholds
bash reports/milestone-4/code/run_logged.sh NAME CMD ...        # run one command and keep its log in logs/NAME.log
venv/bin/python reports/milestone-4/code/renumber_tables.py --map "A.1=A.5,4.5=4.2" [--write]  # renumber table captions and references, EN and VI
bash reports/milestone-4/code/check_pairs.sh                    # parity check of changed VI twins, then mark them translated
bash reports/milestone-4/code/move_measure.sh TAG               # appendix move: build EN+VI, pessimistic pages (logs/TAG_*)
make pages TASK=milestone-4 BUDGET=12                           # page budget, optimistic and pessimistic layout
make all TASK=milestone-4                                       # checks, EN and VI Word build, post-checks, tests
```
