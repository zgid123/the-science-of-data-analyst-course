### 2.2.2. Central Difference Convolution

Two years after auxiliary supervision, Yu, Zhao and colleagues of the University of Oulu, Mininglamp Academy of Sciences, Aibee and Northwestern Polytechnical University changed the building block of the network itself. Their CDCN was posted on 9 March 2020 and accepted at CVPR 2020 [57]. It addressed two weaknesses: stacked vanilla convolutions are "weak in describing detailed fine-grained information and easily being ineffective when the environment varies (e.g., different illumination)", and long input sequences are hard to deploy where a quick response is needed [57]. CDC therefore works on single frames and aggregates both intensity and gradient information [57].

The operator adds a gradient term to ordinary convolution. For an output position $p_0$, neighbourhood $\mathcal{R}$, weights $w$ and input $x$ [57]:

$$y(p_0) = \theta \sum_{p_n \in \mathcal{R}} w(p_n)\,\big(x(p_0 + p_n) - x(p_0)\big) + (1 - \theta) \sum_{p_n \in \mathcal{R}} w(p_n)\,x(p_0 + p_n)$$

The hyperparameter $\theta \in [0, 1]$ trades off gradient-level and intensity-level information, and $\theta = 0$ reduces the operator to vanilla convolution [57]. In the ablation on OULU-NPU Protocol 1, $\theta = 0.7$ gave the best ACER of 1.0%, against 3.8% for vanilla convolution [57]. CDCN keeps the depth supervision of Section 2.2.1, predicting a 32 by 32 facial depth map with a mean-square-error loss and a contrastive depth loss [57]. CDCN++ goes one step further: neural architecture search (NAS) over a CDC-specific search space, the first NAS approach for face anti-spoofing, finds the backbone, which is combined with a multiscale attention fusion module [57].

The results in Table 2.6 show the gain. CDCN++ reached ACERs of 0.2%, 1.3%, 1.8% and 5.0% on the four OULU-NPU protocols and 1.90% or lower on SiW [57]. Across datasets, it cut the HTER from CASIA-FASD to Replay-Attack to 6.5%, against 27.6% for auxiliary supervision, while the reverse direction stayed at 29.8% [57]. On the unseen attacks of SiW-M it averaged 12.7% ACER, a 24% improvement on the previous state of the art [57].

**Table 2.6. Reported results of CDCN++ (Yu et al., 2020)**

| Benchmark | Protocol | Result |
| :---- | :---- | :---- |
| OULU-NPU | Protocols 1 / 2 / 3 / 4 | ACER 0.2% / 1.3% / 1.8% / 5.0% [57] |
| SiW | Protocols 1 / 2 / 3 | ACER 0.12% / 0.04% / 1.90% [57] |
| CASIA-FASD and Replay-Attack | Cross-testing, both directions | HTER 6.5% and 29.8% [57] |
| SiW-M | Leave-one-attack-out | Average ACER 12.7%, EER 11.9% [57] |

The method also proved itself in open competition. In the ChaLearn Face Anti-spoofing Attack Detection Challenge at CVPR 2020, organised by ChaLearn with CASIA, the Oulu team BOBO led by Zitong Yu placed 1st in the multi-modal track with an ACER of 1.02% and 2nd in the single-modal (RGB) track with 4.84%, behind VisionLabs [60], [62]. The paper has 592 citations in Crossref as of 2 October 2026 [57]. Its official repository publishes the training script, the data loaders and the model definitions under a modified MIT licence for research use, and it contains no pretrained checkpoint files (checked on 2 October 2026) [62]. OULU-NPU, the dataset that the repository's data loaders target, is itself available only under a signed end user licence agreement (EULA) [63].
