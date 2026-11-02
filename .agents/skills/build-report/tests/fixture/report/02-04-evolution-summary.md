## 2.4. Summary of the Technical Evolution

The three eras form one line of development, in which each era inherited the open problem of the one before. Table 2.10 summarises them by period, approach, representative methods, generalisation and threat focus.

**Table 2.10. The three eras of face PAD**

| Aspect | Era 1: hand-crafted cues | Era 2: deep classifiers with auxiliary supervision | Era 3: generalisation and injection |
| :---- | :---- | :---- | :---- |
| Dominant period | About 2005–2017; deep methods from 2014 [30], [49] | About 2018–2020 [45], [57] | About 2020–2026 [44], [66], [67] |
| Approach | Hand-crafted texture, quality, motion and blink features with traditional classifiers [45], [30] | Deep networks supervised with depth and rPPG; CDC and architecture search [45], [57] | Domain generalisation; vision-language pretrained ViT [44], [42], [66] |
| Representative methods | Optical Flow Lines (2005), eye blink (2007), LBP (2011), colour texture (2016) [30], [51], [37] | Auxiliary supervision (2018), CDCN++ (2020) [45], [57] | MADDG (2019), SSDG (2020), FLIP (2023) [44], [42], [66] |
| Typical datasets | NUAA, CASIA-FASD, Replay-Attack, MSU-MFSD; 15–50 subjects [35], [54] | OULU-NPU, SiW, SiW-M, CASIA-SURF, CeFA; up to 1,607 subjects [43], [45], [56], [58], [59] | O/C/I/M leave-one-out protocol across four datasets [44], [42] |
| Generalisation | Cross-dataset HTER near 50% for motion, LBP and LBP-TOP; 30.3–37.7% for colour texture [45] | Below 5% ACER within datasets, above 20% HTER across them for most models [35]; 12.7–23.6% ACER on unseen attacks [57], [56] | Average O/C/I/M HTER from 23.09% (2019) to 3.01% (2023) [44], [66] |
| Threat focus | Print and replay at the sensor [35] | Wider presentation attacks, including 3D masks; 13 attack types in SiW-M [56] | Digital injection and deepfakes in remote identity verification [67], [10] |

Two lines of progress run through the table. Generalisation improved steadily, from detectors that failed outside their own dataset to models whose average error on unseen datasets is about 3% [66]. At the same time, the threat moved beyond the camera, so that PAD now works alongside injection attack detection [68]. Part 3 follows the parallel track of standards, certification and law that turned these technical results into requirements, and Part 4 examines a foundation model designed for the unified defence of faces against both presentation and digital attacks.
