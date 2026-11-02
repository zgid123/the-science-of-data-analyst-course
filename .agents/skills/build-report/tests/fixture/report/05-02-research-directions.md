## 5.2. Open Problems and Research Directions

Five problems remain open in PAD, and each defines a research direction with a measurable target:

(1) **Generalisation under matched, independent protocols.** Cross-dataset error remains the limit of every technique family: most deep models stay above 20% HTER across datasets [35], and FSFM-FAS moves from 4.2% to 37.3% ACER when training and test datasets differ [105]. Published comparisons also depend on training data, since FLIP and FSFM both add CelebA-Spoof on the O/C/I/M protocol [66], [102]. Results reported under matched training data and independent single-source protocols, as in the Idiap evaluations [105], [110], give the field comparable evidence of progress.

(2) **Unified detection of physical and digital attacks.** Face security research now joins PAD with forgery detection: a joint benchmark found that both tasks improve through joint training [70], a unified detector covers physical and digital attacks with a joint dataset [71], and FSFM transfers one backbone to FAS, DfD and diffusion-forgery detection [102]. The direction is a single detector evaluated on both attack families at once.

(3) **Injection attack detection and its standardisation.** NIST's benchmark left injection attacks outside its scope [31], and FSFM treats attacks as image content without the route that bypasses the camera [102]. The standards answer is taking shape: CEN/TS 18099 specifies injection attack detection [22], the international standard ISO/IEC 25456 is in development with attack levels expected (as of July 2026) [21], iBeta launched injection attack detection testing on 4 June 2026 [88], and FIDO certification requires documented protection against injection [79]. Detectors evaluated against these test methods connect research to certification.

(4) **Foundation models as PAD backbones.** A 2026 benchmark evaluates 15 vision foundation models for domain-generalisable FAS [111], and the Idiap evaluation finds that FSFM-FAS does not provide better PAD features than generic large-scale pretraining [105]. Placing face-security models such as FSFM in such benchmarks, beside general-purpose models, shows which pretraining serves PAD best.

(5) **Demographic and certification evidence.** The FIDO programme tests across skin tone, age and gender [78], NIST's first-order check found no consistent elevation of BPCER for any demographic group [31], and the FSFM authors themselves flag possible bias in VGGFace2 [102]. Demographic evaluation of research models, together with certification at a defined level such as ISO 30107 Level 2 [98], is the evidence that carries a method from publication into a regulated deployment.

Taken together, these directions share one principle: each claim of progress is backed by an independent, reproducible measurement, under conditions that match the threat a deployed system faces.
