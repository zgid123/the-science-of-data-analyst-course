"""Arithmetic behind the thresholds fixed in the evaluation design (Sections 4.2–4.4), from training-run counts only.

- calibration-in-the-large bounds of ±0.2 on the log-odds scale: average predicted risk they allow around the
  training base rate at day 27 (5,245 / 11,811 = 44.4%);
- fairness gap of 10 percentage points: standard error of a recall near 0.5 estimated on 100 non-completers;
- eligibility of 400 test enrolments: expected non-completers at the lowest training rate of an eligible group (28%);
- challenger rule "better in at least 7 of 9 folds": probability under no difference (sign test);
- gate wording "beats the rule in at least 9 of 13 runs": probability under no difference.
Usage: venv/bin/python reports/milestone-4/code/threshold_reasons.py
"""
import math
from math import comb

base = 5245 / 11811
logit = math.log(base / (1 - base))
risk = lambda x: 1 / (1 + math.exp(-x))
print(f"base rate day 27 (training): {base:.3f}; intercept -0.2 -> {risk(logit - 0.2):.3f}, +0.2 -> {risk(logit + 0.2):.3f}")
print(f"standard error of a recall near 0.5 on 100 non-completers: {math.sqrt(0.25 / 100):.3f}")
print(f"expected non-completers among 400 enrolments at 28%: {400 * 0.28:.0f}")
print(f"P(at least 7 of 9 folds | no difference) = {sum(comb(9, k) for k in range(7, 10)) / 2**9:.3f}")
print(f"P(at least 9 of 13 runs | no difference) = {sum(comb(13, k) for k in range(9, 14)) / 2**13:.3f}")
