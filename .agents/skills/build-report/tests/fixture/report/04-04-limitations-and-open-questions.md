## 4.4. Limitations and Open Questions

Applied to FSFM, the rules of Section 4.3 show a method that is promising across tasks and still unproven where security decisions need proof. Six limitations stand out.

(1) **The independent test shows a large generalisation gap.** A benchmark from the Idiap Research Institute, accepted at the 2026 International Joint Conference on Biometrics, tested FSFM's anti-spoofing model under the single-source protocol of Figure 4.5: it averages 4.2% ACER when training and test data come from the same dataset, but 37.3% across the twelve cross-dataset pairs [105]. A second Idiap study reports the same figures [110], and the authors conclude that FSFM's model does not provide better PAD features than generic large-scale pretraining [105].
(2) **Its own best results depend on extra training data.** Under the leave-one-out protocol, FSFM reports an average HTER of 4.81% with CelebA-Spoof added to training and 8.88% without it [102]. Under the same condition, the vision-language method FLIP reports 3.01% [66], so on FAS alone a specialised method does better; FSFM's strength is its breadth across three tasks rather than the best score on one [102].
(3) **It sees images, not the route they arrive by.** FSFM learns from images only, without signals such as audio or physiological cues, as its authors note [102], and it treats attacks as image content without addressing injection attacks that bypass the camera [102], although FIDO certification requires documented protection against injection [79].
(4) **Its training data may carry bias.** The authors flag that VGGFace2 may carry race, ethnicity and age biases [102], and no evaluation across demographic groups has been published as of 3 October 2026, while the FIDO programme tests across skin tone, age and gender [78].
(5) **It is a research release, not a certified product.** Code, weights and demonstration are released under the CC BY-NC 4.0 licence for non-commercial research, and as of 3 October 2026 no FSFM-based product holds an iBeta confirmation letter, a FIDO certification or a NIST FATE PAD result [107], whereas Vietnamese banking regulation requires PAD certified at ISO 30107 Level 2 or an equivalent level [98].
(6) **Reproduction and training carry real costs.** The repository pins Python 3.9.21, PyTorch 1.13.1 with CUDA 11.7 and timm 0.4.5 [106], so a current environment must recreate these versions, and pretraining takes 400 passes over 3.3 million images on four high-end graphics cards [102]. A 2026 benchmark of 15 vision foundation models for anti-spoofing has not yet included FSFM [111].

Table 4.2 sets these limits beside the method's strengths.

**Table 4.2. FSFM's strengths and limitations**

| Aspect | Strength | Limitation |
| :---- | :---- | :---- |
| Learning | Learns from unlabelled real faces only [102] | Training data may carry demographic bias [102] |
| Scope | One backbone for deepfakes, spoofs and AI-generated faces [102] | Images only; no protection of the injection route [102] |
| Accuracy | Strong results under the authors' protocols [102] | Large cross-dataset gap in an independent test [105]; specialised FLIP does better on anti-spoofing [66] |
| Openness | Code, weights and a running demonstration are public [106], [107], [108] | Non-commercial licence; no certification [107] |
| Practicality | One pretraining serves every task [102] | Costly pretraining; pinned software stack [102], [106] |

These limits define the questions a deployment would have to answer. The first is whether FSFM's knowledge of real faces holds up in independent cross-dataset tests once training data are matched. The second is whether a product built on it can reach a certified PAD level such as ISO 30107 Level 2, which Vietnamese law now accepts [98]. The third is how it should be combined with injection attack detection. Until these are answered, FSFM serves best as an open, well-documented example of where face security research is heading, and as a strong starting point for further independent testing.
