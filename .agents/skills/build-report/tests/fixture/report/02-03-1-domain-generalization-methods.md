### 2.3.1. Domain Generalisation Methods

The first domain generalisation method for face PAD reframed the problem behind the cross-dataset failures of Sections 2.1.3 and 2.2. Shao, Lan, Li and Yuen of Hong Kong Baptist University observed at CVPR 2019 that "existing face anti-spoofing methods capture the differentiation cues that are dataset biased" [44]. Their Multi-Adversarial Discriminative Deep Domain Generalization (MADDG) method learns a feature space shared by several source datasets through adversarial learning "under a dual-force triplet-mining constraint", with auxiliary depth supervision [44]. It also introduced the evaluation that Section 1.3.4 describes, in which one dataset is held out as an unseen target that "cannot be accessed in the training process" [44]. MADDG reported HTERs of 17.69%, 24.5%, 22.19% and 27.98% on the four tasks [44]; its PyTorch code is public, and the paper has 423 citations in OpenAlex as of 2 October 2026 [44].

SSDG, by Jia, Zhang, Shan and Chen of the Institute of Computing Technology of the Chinese Academy of Sciences, refined the idea at CVPR 2020 by treating real and fake faces asymmetrically [42]. Real faces from all domains are made indistinguishable and compact, so that "the feature distribution of the real faces is compact while that of the fake ones is dispersed among domains but compact within each domain" [42]. Its variant SSDG-R reached HTERs between 7.38% and 15.61%, with public code and 316 citations in OpenAlex as of 2 October 2026 [42].

Pretrained transformers brought the next step. FLIP, by Srivatsan, Naseer and Nandakumar of the Mohamed bin Zayed University of Artificial Intelligence, was presented at the 2023 IEEE International Conference on Computer Vision (ICCV) [66]. It initialises a ViT with CLIP vision-language weights and aligns image features with natural-language descriptions of the classes, adding a multimodal contrastive objective [66]. In zero-shot testing its FLIP-MCL variant reached HTERs between 0.54% and 4.95%, averaged over five runs, with an average of 3.01% [66]. Its code is public, and the paper has 74 citations in OpenAlex as of 2 October 2026 [66]. Table 2.8 shows the progression across the series.

**Table 2.8. HTER (%) on the O/C/I/M leave-one-out protocol, by year**

| Method | Year and venue | O&C&I→M | O&M&I→C | O&C&M→I | I&C&M→O | Average |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MADDG [44] | CVPR 2019 | 17.69 | 24.50 | 22.19 | 27.98 | 23.09 (computed) |
| SSDG-R [66], [42] | CVPR 2020 | 7.38 | 10.44 | 11.71 | 15.61 | 11.28 |
| SSAN-R [66] | CVPR 2022 | 6.67 | 10.00 | 8.88 | 13.72 | 9.80 |
| ViT [66] | ECCV 2022 | 1.58 | 5.70 | 9.25 | 7.47 | 6.00 |
| FLIP-MCL [66] | ICCV 2023 | 4.95 | 0.54 | 4.25 | 2.31 | 3.01 |

The MADDG average is the mean of its four reported values; the other averages are those printed in the FLIP comparison table [66].

Within four years, the average error on unseen datasets fell from about 23% to about 3%. As a result, the open problem of the field moved from dataset bias in texture towards attack routes that no camera-side detector observes, which Section 2.3.2 describes.
