# 4. Flagship Method: FSFM

Parts 2 and 3 converged on one requirement: a detector that keeps working on data and attacks it has never seen, and that protects faces against both physical presentation attacks and digital forgeries. FSFM, short for Face Security Foundation Model, is an openly released method built for exactly that requirement and presented at CVPR 2025 [102].

Its central idea is easy to state. Instead of learning from labelled examples of attacks, FSFM first learns what a real face looks like, from millions of unlabelled real faces, and only then adapts that knowledge into detectors for deepfakes, presentation attacks and AI-generated faces [102].

Section 4.1 explains why this method was chosen and which problem it addresses. Section 4.2 shows how it works, step by step and with figures. Section 4.3 explains how the method is judged, that is, which tests and measures decide whether it works. Section 4.4 closes with its limitations and the questions that remain open before it could be used in production.
