## 4.3. How the Method Is Judged

A detector can be wrong in two ways: it can let an attack through, or it can reject a genuine user. Every measure used for FSFM combines these two errors, and every test is designed so that the detector meets data it has never seen, because that is the situation a deployed system faces.

Three measures appear in the evaluations, all introduced in Part 1:

(1) **AUC** summarises how well a detector ranks attacks above genuine faces across all possible decision thresholds; 1.0 means a perfect separation and 0.5 means guessing, so higher is better [42]. For deepfakes, it is reported per video and per frame [102].
(2) **HTER** is the average of FAR and FRR, the rates of accepted attacks and rejected genuine users at one threshold, so lower is better [35].
(3) **ACER** is the average of APCER and BPCER, the rates of accepted attacks and rejected genuine presentations, so lower is better as well [10].

The tests decide what these numbers mean. Table 4.1 lists the four protocols used for FSFM, and Figure 4.5 contrasts the two ways of testing FAS.

**Table 4.1. The protocols that judge FSFM**

| Task | Trains on | Tests on | Measure | What it reveals |
| :---- | :---- | :---- | :---- | :---- |
| DfD | FF++ at compression level c23 [102] | CelebDF-v2, DFDC, DFDC preview, WildDeepfake [102] | AUC per video and per frame [102] | Transfer to deepfake collections never seen in training |
| FAS, leave-one-out | Three of OULU-NPU, CASIA-FASD, Idiap Replay-Attack, MSU-MFSD, plus CelebA-Spoof [102] | The fourth dataset; average of the four rounds over 5 runs [102] | HTER and AUC [102] | Transfer to new capture conditions, with varied training data |
| AI-generated faces | The DeepFake part of FF++ [102] | The DiFF benchmark: faces from 13 diffusion models [102] | AUC [102] | Transfer to a generation technique never seen in training |
| FAS, independent | One of the four datasets [105] | Each other dataset: 12 pairs; also within each dataset [105] | ACER [105] | Transfer from a single source, measured by a group other than the authors |

![Figure 4.5. Two ways to test FAS on unseen data: leave-one-out and single-source cross-dataset testing](assets/figures/task2-4-5-evaluation-protocols.png){width=100%}

Three rules follow for reading any reported result. First, a result is meaningful only together with its protocol: training on three datasets plus CelebA-Spoof is an easier condition than training on one, as Figure 4.5 shows. Second, two methods are comparable only under the same data condition; FSFM and the vision-language method FLIP, for example, both add CelebA-Spoof to the leave-one-out protocol and both average five runs, so their results can be set side by side [66], [102]. Third, an independent test outweighs a self-reported one, because it removes the authors' choices of data and settings from the result [105].

Section 4.4 applies these rules to FSFM's own results.
