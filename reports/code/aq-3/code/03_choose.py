"""AQ3 step 3 – model choice on the development folds (Appendix III step 4; PROTOCOL.md P11).

Rule fixed in Level 1: the primary approach M1 (penalised logistic regression, primary predictors) stays unless a
challenger gains at least 0.03 pooled normalised recall at day 27, k = 5 per 20, AND gains in at least 7 of 9 folds.

Writes results/model_choice.csv and results/dev_m1_vs_rule_by_fold.csv.
"""

import polars as pl

from aq3_models import CHALLENGERS, CONFIGS, RESULTS, lib

m = pl.read_csv(RESULTS / "dev_folds.csv").filter((pl.col("cutoff") == lib.MAIN_CUTOFF) & (pl.col("per20") == lib.MAIN_PER20))
wide_tp = m.pivot(on="ranking", index=["run", "max_attainable"], values="non_completers_on_list").sort("run")
wide_nr = m.pivot(on="ranking", index="run", values="normalised_recall").sort("run")
pool = {c: wide_tp[c].sum() / wide_tp["max_attainable"].sum() for c in ["B2_rule", *CONFIGS]}

lib.banner("AQ3 model choice (development folds, day 27, 5 per 20)")
print("**Normalised recall per validation run**\n\n" + lib.md_table(wide_nr))
rows, qualifiers = [], []
for c in CONFIGS:
    gain = pool[c] - pool["M1"]
    folds_gain = int((wide_nr[c] > wide_nr["M1"]).sum())
    extra = int(wide_tp[c].sum() - wide_tp["M1"].sum())
    ok = c in CHALLENGERS and gain >= 0.03 and folds_gain >= 7
    if ok:
        qualifiers.append((round(gain, 9), -CHALLENGERS.index(c), c))
    rows.append({"config": c, "label": CONFIGS[c]["label"], "pooled_normalised_recall": pool[c], "gain_vs_M1": gain,
                 "extra_non_completers_listed_vs_M1": extra, "folds_with_gain_vs_M1": folds_gain,
                 "meets_margin_0.03": gain >= 0.03, "meets_7_of_9_folds": folds_gain >= 7})
chosen = max(qualifiers)[2] if qualifiers else "M1"
out = pl.DataFrame(rows).with_columns((pl.col("config") == chosen).alias("chosen"))
print("\n**Choice table**\n\n" + lib.md_table(out.drop("label"), digits=4))
reason = ("a challenger met both conditions" if qualifiers else
          "no challenger gains 0.03 pooled normalised recall and 7 of 9 folds, so the primary approach of Level 1 stays")
print(f"\n**Chosen configuration: {chosen}** – {CONFIGS[chosen]['label']}. Reason: {reason}.")
out = out.with_columns(pl.lit(reason).alias("reason"))
lib.save_csv(out, RESULTS / "model_choice.csv")

cmp = wide_nr.select("run", "B2_rule", "M1", "B3").with_columns((pl.col("M1") - pl.col("B2_rule")).alias("M1_minus_rule"))
print("\n**Development only: M1 against the rule and the background-only model, per fold**\n\n" + lib.md_table(cmp))
print(f"\npooled: rule {pool['B2_rule']:.4f}, background-only {pool['B3']:.4f}, M1 {pool['M1']:.4f}; M1 above the rule in "
      f"{int((cmp['M1_minus_rule'] > 0).sum())} of 9 folds. These fold values serve the choice only.")
lib.save_csv(cmp, RESULTS / "dev_m1_vs_rule_by_fold.csv")
