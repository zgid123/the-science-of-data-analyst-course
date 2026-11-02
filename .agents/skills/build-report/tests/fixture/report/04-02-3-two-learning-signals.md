### 4.2.3. Two Learning Signals

The encoder improves through two signals that work together, and each covers a weakness of the other [102].

The first signal is reconstruction. A small decoder takes the encoder's output and predicts the pixels of every hidden patch, and the error of that prediction is the first loss; a second, smaller loss checks the fully covered region on its own [102]. This is the design of a masked autoencoder (MAE), here guided by the face-aware masking of Section 4.2.2 [102]. It teaches fine local detail and how neighbouring regions fit together.

The second signal is matching. A teacher network looks at the same face without any masking, and the encoder's summary of the partly hidden face must point in the same direction as the teacher's summary of the full face [102]. The teacher is not trained directly; it slowly follows the encoder as a running average of its weights, which keeps its targets stable [102]. This signal teaches the link between local parts and the face as a whole.

The training objective adds the three parts with fixed weights [102]:

$$L = L_1 + 0.007 \cdot L_2 + 0.1 \cdot L_3$$

Here $L_1$ is the reconstruction error over all hidden patches, $L_2$ the reconstruction error of the fully covered region, and $L_3$ the disagreement between the encoder and the teacher; the authors chose both weights by experiment [102]. One training step therefore reads as follows:

```text
for each batch of real face images:
    regions  = face_parser(image)                      # eyes, nose, mouth, ...
    visible, hidden, covered = crfr_p_mask(image, regions, ratio=0.75)
    features = encoder(visible)                        # the encoder sees about 25% of the face
    L1 = rebuild_error(decoder(features), hidden)      # all hidden patches
    L2 = rebuild_error(decoder(features), covered)     # the fully covered region
    L3 = disagreement(features, teacher(image))        # the teacher sees the full face
    update encoder and decoder to reduce L1 + 0.007*L2 + 0.1*L3
    teacher = running_average(teacher, encoder)        # the teacher follows slowly
```

Figure 4.3, reproduced from the paper, shows what the two signals achieve. Given faces with 75% of their patches hidden, the model trained with both signals rebuilds faces with finer texture within regions and more consistent relations between regions than models trained with reconstruction alone [102].

![Figure 4.3. Faces rebuilt from 75% hidden patches: (a) MAE with random masking, (b) with CRFR-P masking, (c) FSFM. Reproduced from Wang et al. [102]](assets/figures/task2-4-3-paper-reconstructions.png){width=80%}
