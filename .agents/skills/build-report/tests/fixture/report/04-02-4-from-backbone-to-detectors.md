### 4.2.4. From One Backbone to Three Detectors

After pretraining, FSFM keeps only the encoder and adds a small task head for each detection job [102]. The same encoder is fine-tuned three times, once per task, each time on labelled data of that task only [102]:

(1) **DfD.** The detector learns from the manipulated videos of the FaceForensics++ (FF++) collection and is then tested on four deepfake datasets it has never seen: CelebDF-v2, DFDC, DFDC preview and WildDeepfake [102].
(2) **FAS.** The detector learns from three of four public anti-spoofing datasets, with the CelebA-Spoof collection as extra training data, and is tested on the fourth [102].
(3) **AI-generated faces.** The detector learns from the DeepFake part of FF++ only and is tested on faces produced by 13 different diffusion models, the technology behind today's image generators [102].

The released online demonstration goes one step further and combines the tasks in a single four-way detector that labels a face as real, deepfake, diffusion-generated or presentation attack [108].

Heat maps show where such a detector looks when it decides. Figure 4.4, reproduced from the paper, compares a detector built on everyday-photo pretraining, one built on a plain MAE, and FSFM. In the authors' words, "FSFM highlights forgery artifacts and spoofing clues": on deepfakes its attention gathers on the manipulated parts of the face, and on spoofs on the clues of the attack [102].

![Figure 4.4. Where the detectors look: heat maps on (a) deepfakes and (b) spoofs for ImageNet-supervised, MAE and FSFM backbones. Reproduced from Wang et al. [102]](assets/figures/task2-4-4-paper-heat-maps.png){width=100%}

One pretrained backbone thus becomes three specialised detectors. How well they work, and how that is measured, is the subject of Section 4.3.
