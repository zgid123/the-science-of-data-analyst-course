### 2.1.3. Early Datasets and Their Limits

The methods of Sections 2.1.1 and 2.1.2 were developed on a small set of public datasets, which Table 2.3 lists. NUAA, introduced by Tan, Li, Liu and Jiang at the 2010 European Conference on Computer Vision (ECCV) [52], holds 5,105 live and 7,509 spoof images of 15 subjects with flat and wrapped print attacks [35]. Print-Attack (2011) holds 200 printed-photo attack videos and 200 real-access videos of 50 clients [47]. CASIA-FASD, published by Zhang et al. of the Chinese Academy of Sciences at the 2012 International Conference on Biometrics [53], holds 150 live and 450 spoof videos of 50 subjects in 7 scenarios and 3 image qualities, with flat, wrapped and cut prints and tablet replays [35]. Replay-Attack (2012) is described by its database page as 1,300 video clips of photo and video attack attempts to 50 clients under different lighting conditions, and by the survey table as 200 live and 1,000 spoof videos [54], [35]; it was recorded with a laptop webcam at 320 by 240 pixels and attacked with an iPhone 3GS, a first-generation iPad and printed photographs [54]. MSU-MFSD, dated 2014 in the deep-learning survey cited in Section 1.3 [35] and described in IEEE Transactions on Information Forensics and Security in 2015 [55], holds 70 live and 210 spoof videos of 35 subjects captured with a laptop and an Android phone [35], [55].

**Table 2.3. Public face PAD datasets of Era 1**

| Dataset | Year | Subjects | Size (live / spoof) | Attacks | Capture |
| :---- | :---- | :---- | :---- | :---- | :---- |
| NUAA [52], [35] | 2010 | 15 | 5,105 / 7,509 images | Print: flat, wrapped | – |
| Print-Attack [47] | 2011 | 50 | 200 / 200 videos | Print: fixed or hand-held | – |
| CASIA-FASD [53], [35] | 2012 | 50 | 150 / 450 videos | Print: flat, wrapped, cut; tablet replay | 7 scenarios, 3 image qualities |
| Replay-Attack [54], [35] | 2012 | 50 | 200 / 1,000 videos | Print; phone and tablet replay | Laptop webcam, 320 by 240 pixels |
| MSU-MFSD [35], [55] | 2014 (paper 2015) | 35 | 70 / 210 videos | Print; phone and tablet replay | Laptop and Android phone |

These datasets share three properties: 15 to 50 subjects, one or two capture devices, and print and replay attacks only. A method could therefore fit one dataset closely, and the cross-dataset tests exposed this. Trained on one of CASIA-FASD and Replay-Attack and tested on the other, the motion baseline scored 50.2% and 47.9% HTER, LBP 55.9% and 57.6%, and LBP-TOP 49.7% and 60.6%, all close to 50% [45]. The colour-texture method performed best among them, at 30.3% and 37.7% [45], yet within its own paper its HTER rose from 2.9% on Replay-Attack to as much as 47.5% when trained on Replay-Attack and tested on CASIA-FASD [50]. The Oulu authors themselves noted that "the generalization capabilities of these methods have been questionable" [50].

**Table 2.4. Cross-dataset HTER of Era-1 baselines (CASIA-FASD and Replay-Attack)**

| Method | Train CASIA-FASD, test Replay-Attack | Train Replay-Attack, test CASIA-FASD |
| :---- | :---- | :---- |
| Motion | 50.2% | 47.9% |
| LBP | 55.9% | 57.6% |
| LBP-TOP | 49.7% | 60.6% |
| Colour texture | 30.3% | 37.7% |

Source: [45].

The verdict on the era followed from these numbers. Hand-crafted methods became unreliable because of their limited representation capacity, and once large-scale datasets appeared, deep learning came to dominate the field [35]. The first end-to-end deep method had already argued that LBP and LBP-TOP "are still unable to capture the most discriminative cues between genuine and fake faces" [49], and Section 2.2 follows the deep classifiers that took over.
