## 3.3. Government Benchmarking: NIST FATE PAD

Laboratory letters such as those of Section 3.2 test one product at a time on the vendor's request. A government benchmark adds a different kind of evidence: one test of many algorithms on the same sequestered data, run by an agency with no product to sell. NIST IR 8491, FATE Part 10, by Mei Ngan, Patrick Grother and Austin Hom of the NIST Information Technology Laboratory, provides this evidence for PAD [31]. It was approved on 19 September 2023, runs to 152 pages [31], and was released on 20 September 2023 [90].

The benchmark grew out of NIST's long-running face programme. From 1999 to July 2023, NIST's face recognition and face analysis tests "were collectively known as FRVT" [31], the Face Recognition Vendor Test, which already covered PAD under the name FRVT PAD in its 2022 evaluation plan [9]. On 18 August 2023 NIST split the programme into the Face Recognition Technology Evaluation (FRTE) and FATE [90], and IR 8491 was among the first two publications after the split, intended to inform developers, end users, standards processes and policy makers [91].

The test design follows the methodology of Section 3.1. NIST evaluated 82 prototype algorithms from 45 developers; all 82 implemented impersonation detection, and 27 also implemented evasion detection [31]. Participation was open worldwide and free of charge from 3 January to 28 February 2023, with up to two algorithms per developer, each submitted as a compiled library behind NIST's published C++ interface and run as a black box [31], [90]. The two use cases differ in the attacker's goal: impersonation means trying to look like another specific person, and evasion means trying to avoid looking like oneself [91]. In line with Sections 1.2.1 and 1.2.2, the test covered passive, software-based PAD on pre-collected imagery with physical attacks only [31]. Each algorithm returned a binary decision and a confidence score, NIST computed APCER and BPCER per attack type as defined in ISO/IEC 30107-3, and every failure to process counted as a detected attack [31]. Table 3.4 summarises the design.

**Table 3.4. Test design of NIST FATE Part 10 (IR 8491)**

| Element | Value |
| :---- | :---- |
| Algorithms | 82 prototype algorithms from 45 developers; 27 also tested on evasion [31] |
| Data | About 20,000 attack attempts in 9 attack types and about 21,000 bona fide presentations, plus 747 videos; sequestered at NIST [31] |
| Named attack types | Photo print or replay, zoomed print or replay, protective face mask, flexible silicone mask; the other five reported by number only [31] |
| Imagery | Fixed colour camera; stills from 640 by 480 to 5,184 by 3,456 pixels; compressed video [31] |
| Metrics | APCER and BPCER per attack type (ISO/IEC 30107-3); APCER at BPCER = 0.01 (convenience) and BPCER at APCER = 0.01 (security) [31] |
| Scope | Passive, software-based, physical attacks; offline [31] |

Section 3.3.1 presents what the benchmark found.
