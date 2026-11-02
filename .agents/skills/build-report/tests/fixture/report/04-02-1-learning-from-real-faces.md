### 4.2.1. Learning from Real Faces Only

FSFM's pretraining never sees an attack. It learns from VGGFace2, a public collection of about 3.3 million images of real faces, which are detected, cropped and resized to 224 by 224 pixels before use [102]. No image carries a label, so no one has to annotate which faces are genuine, forged or spoofed [102].

This style of training is called self-supervised learning: the data provide their own exercise. Hiding part of a face and asking the network to complete it is such an exercise, much as a person who has seen thousands of faces can guess what lies behind a hand covering a mouth. A network that solves this task well has to learn how real skin, eyes and mouths look and how they fit together, which is the knowledge a detector needs to notice that something does not fit [102].

The amount of real-face data matters. When the authors pretrain on larger collections of real faces, the resulting deepfake detectors become more accurate on unseen data [102]. Pretraining is also the costly part: the default model trains for 400 passes over the data on 4 high-end NVIDIA RTX A6000 graphics cards [102]. Once this is done, however, the same pretrained encoder serves every task, so its cost is paid only once.
