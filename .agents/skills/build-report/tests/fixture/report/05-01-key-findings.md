## 5.1. Main Conclusions

Five conclusions follow from the evidence on PAD, its evolution, its policy track and its newest methods.

(1) **Known attacks are detected well; unseen conditions are not.** In NIST's evaluation, several developers kept both APCER and BPCER at or below 0.01 for print and replay attacks and for protective and silicone masks, while some attack types stayed high-error for every algorithm and no algorithm caught all of them [31], [91]. Deep models reach below 5% ACER within one dataset and above 20% HTER across datasets [35], and an independent test of a 2025 foundation model measured 4.2% ACER within datasets against 37.3% across them [105]. Accuracy on a known dataset is therefore weak evidence of robustness in the field.

(2) **Reported progress depends on the test conditions.** The average HTER on unseen datasets of the O/C/I/M protocol fell from 23.09% in 2019 to 3.01% in 2023 [44], [66]. These numbers rest on specific training data: FLIP and FSFM both add CelebA-Spoof to the protocol [66], [102], and FSFM's average HTER rises from 4.81% to 8.88% without it [102]. Results become comparable only when training data and protocol match.

(3) **The threat has moved beyond the sensor.** Presentation attacks are generally manual and low-scale, whereas injection attacks scale far more easily [21]; ENISA reports video injection as "the most promising attack method, according to market players" [67], and the two now form the two main threat categories of remote face verification [10]. A PAD gate therefore secures the camera, and a separate injection detector secures the data stream.

(4) **Trust is established by independent testing.** The field's evidence of assurance comes from institutions rather than from method papers: 273 confirmation letters from an accredited laboratory [20], a government benchmark of 82 algorithms from 45 developers [31], and a banking regulation that requires certified PAD at ISO 30107 Level 2 or an equivalent level [98]. At national scale, more than 173 million individual customer records had been biometrically matched in Vietnam by 11 September 2026 [101], and the central bank links the programme to a fall of more than 59% in fraud cases [100].

(5) **Openness turns claims into testable evidence.** FSFM released its code and weights in December 2024 [106], and independent researchers evaluated it under their own protocol in 2026 [105], [110]. By contrast, CDCN's repository contains no pretrained checkpoint [62], so its results can be reproduced only by retraining. Released weights shorten the path from a published result to an independent measurement. Table 5.1 sets the five conclusions beside their evidence and implications.

**Table 5.1. Main conclusions, their evidence and their implications**

| Conclusion | Evidence | Implication |
| :---- | :---- | :---- |
| Known attacks are detected well; unseen conditions are not | APCER and BPCER ≤ 0.01 for print, replay and masks by several developers, no algorithm catching all attack types [31], [91]; 4.2% against 37.3% ACER within and across datasets [105] | Ask for cross-dataset and unseen-attack results, not in-dataset accuracy |
| Reported progress depends on the test conditions | 23.09% to 3.01% average O/C/I/M HTER, 2019–2023 [44], [66]; 4.81% to 8.88% HTER without CelebA-Spoof [102] | Compare methods only under matched training data and protocols |
| The threat has moved beyond the sensor | Injection scales far more easily than presentation attacks [21]; video injection named the most promising method [67] | Pair PAD with injection attack detection in remote verification |
| Trust is established by independent testing | 273 confirmation letters [20]; 82 algorithms benchmarked [31]; certified Level 2 PAD in law [98] | Treat certification levels and benchmark results as the basis of procurement |
| Openness turns claims into testable evidence | Released FSFM weights evaluated independently [106], [105]; no CDCN checkpoint [62] | Prefer methods with released weights for evaluation and comparison |
