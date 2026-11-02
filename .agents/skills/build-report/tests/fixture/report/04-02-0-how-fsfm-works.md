## 4.2. How FSFM Works

FSFM works in two stages: a long pretraining stage that learns from real faces, and a short adaptation stage that turns the result into detectors [102]. Figure 4.1 shows the whole process in three steps.

![Figure 4.1. FSFM in three steps: hide parts of a real face, learn with two signals, reuse the encoder for detection](assets/figures/task2-4-1-fsfm-at-a-glance.png){width=100%}

In the first step, a real face is split into small square patches, and about three quarters of them are hidden according to the facial regions a face parser finds [102]. In the second step, a neural network called the encoder sees only the visible patches and learns from two signals at once: it must rebuild the hidden pixels, and its view of the partly hidden face must agree with what a second, teacher network sees in the complete face [102]. The authors call the three properties this develops the 3C: consistency within each facial region, coherency between regions, and correspondence between local details and the whole face [102].

In the third step, everything except the encoder is set aside. The encoder, a standard ViT, receives a small task-specific head and is fine-tuned briefly for each detection task [102]. The authors test this single backbone on 10 public datasets [102].

Sections 4.2.1 to 4.2.4 follow these steps: why the model learns from real faces only, how the masking is designed, how the two learning signals work, and how one backbone becomes three detectors.
