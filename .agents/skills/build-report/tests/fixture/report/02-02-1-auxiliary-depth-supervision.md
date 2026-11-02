### 2.2.1. Auxiliary Depth and rPPG Supervision

Liu, Jourabloo and Liu began from a diagnosis of binary training. A CNN trained with a softmax loss "might discover arbitrary cues that are able to separate the two classes, such as screen bezel" [45], and it "will only generate a binary decision without explanation or rationale for the decision" [45]. Their answer was to supervise the network with two physical signals that a live face produces and a spoof does not.

The model combines a CNN with a recurrent neural network. The CNN estimates the face depth map under pixel-wise supervision, the recurrent part estimates rPPG signals under sequence-wise supervision, and a non-rigid registration layer uses the estimated dense 3D shape to align the CNN feature maps for the recurrent part [45]. The depth labels follow the idea described in Section 1.3.3: for live faces, fitted 3D face vertices are normalised so that "the vertex closest to the camera (e.g., nose) has a depth of one" [45], while spoof videos receive a plain surface of zero depth [45]. The estimated depth and rPPG are then fused into one live-versus-spoof score, with a constant weight that combines the two outputs [45]. Memory limits restricted the input to 128 by 128 pixels in all experiments [45].

The same paper introduced the Spoof in the Wild (SiW) dataset. It provides 30-frames-per-second videos of 165 subjects, 8 live and 20 spoof videos each, 4,620 videos in total, with live videos at 1,920 by 1,080 pixels [45]. Its four sessions vary the distance to the camera, the head pose within a yaw range of –90° to 90° with facial expressions, and the lighting from a point source moved around the face [45]. Each subject has two print and four replay attacks, the replays shown on Samsung Galaxy S8, iPhone 7, iPad Pro and PC screens [45].

The reported results are summarised in Table 2.5. On OULU-NPU the model reached ACERs between 1.6% and 9.5% across the four protocols, and on SiW between 0.57% and 8.31% [45]. In cross-testing between CASIA-FASD and Replay-Attack it scored 27.6% and 28.4% HTER, compared with 48.5% and 45.5% for a binary CNN and 30.3% and 37.7% for the colour-texture method of Section 2.1.1 [45].

**Table 2.5. Reported results of auxiliary depth and rPPG supervision (Liu et al., 2018)**

| Benchmark | Protocol | ACER or HTER |
| :---- | :---- | :---- |
| OULU-NPU | Protocols 1 / 2 / 3 / 4 | ACER 1.6% / 2.7% / 2.9% / 9.5% [45] |
| SiW | Protocols 1 / 2 / 3 | ACER 3.58% / 0.57% / 8.31% [45] |
| CASIA-FASD and Replay-Attack | Cross-testing, both directions | HTER 27.6% and 28.4%; binary CNN 48.5% and 45.5% [45] |

The paper turned auxiliary supervision into the standard design of the era, and it has 593 citations in Crossref as of 2 October 2026 [45]. Its limit appeared one year later on unseen attack types, where the same model averaged 23.6% ACER on SiW-M [56].
