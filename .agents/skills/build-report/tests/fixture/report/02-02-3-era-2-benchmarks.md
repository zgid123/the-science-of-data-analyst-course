### 2.2.3. Benchmarks and Challenges

The methods of Sections 2.2.1 and 2.2.2 were measured on a new generation of datasets, larger in subjects and broader in attacks and sensors. Table 2.7 summarises them together with their access terms, which make them research resources rather than open downloads.

**Table 2.7. Face PAD benchmarks of Era 2**

| Dataset | Year and group | Subjects and videos | Modalities and attacks | Access |
| :---- | :---- | :---- | :---- | :---- |
| OULU-NPU | 2017, University of Oulu (Section 1.3.4) | 55 subjects, 4,950 videos [43] | RGB; print and replay [43] | EULA signed by a permanent staff member; no public e-mail domains [63] |
| SiW | 2018, Michigan State University [45] | 165 subjects, 4,620 videos [45] | RGB; print and replay [45] | Release agreement signed by a supervisor; internal research only [64] |
| SiW-M | 2019, Michigan State University [56] | 493 live subjects; 660 live and 968 spoof videos [56] | RGB; 13 attack types, including 3D masks [56] | – |
| CASIA-SURF | 2019, Chinese Academy of Sciences [58] | 1,000 subjects, 21,000 videos [58] | RGB, depth and infrared (IR); six print-cut attacks [58] | Signed agreement and contest rules [65] |
| CASIA-SURF CeFA | 2020, Chinese Academy of Sciences [59] | 1,607 subjects, 23,538 videos; three ethnicities [59] | RGB, depth and IR; 2D and 3D attacks [59] | Signed licensing agreement; commercial licence separate [65] |

Each dataset added a new axis of difficulty. CASIA-SURF, recorded with an Intel RealSense SR300 camera, was the largest dataset in subjects and videos at its release [58]. SiW-M introduced a leave-one-out protocol in which a model trains on 12 attack types and is tested on the held-out type [56], so it measures performance on unseen attacks directly. CeFA was the first face PAD dataset with explicit ethnic labels, covering African, East Asian and Central Asian subjects with 500 subjects per ethnicity in its 2D subset, while its 3D mask subsets add 99 and 8 subjects [59].

Two ChaLearn challenges turned these datasets into public contests. The 2019 challenge used CASIA-SURF; more than 300 academic and industrial institutions took part, 13 teams reached the final stage [61], and VisionLabs won with a true positive rate of 99.8739% at a false positive rate of $10^{-4}$ [61]. The 2020 challenge used CeFA to address ethnic bias, with a single-modal (RGB) track and a multi-modal (RGB, depth and IR) track [60]. Its Protocol 4 trains on one ethnicity with replay attacks and tests on the two other ethnicities with print attacks [60]. In total, 340 teams joined the development stage, 11 and 8 teams submitted code in the single-modal and multi-modal tracks respectively, and the organisers re-ran all results [60]. The best entries reduced the ACER from 36.62% to 2.72% in the single-modal track and from 32.02% to 1.02% in the multi-modal track [60].

These benchmarks made the problem of Era 3 measurable. Protocols that cross attacks, ethnicities and sensors became the standard test of generalisation [60], [61].
