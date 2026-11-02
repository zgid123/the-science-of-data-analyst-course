### 1.3.3. Deep Classifiers and Auxiliary Supervision

The texture and liveness cues of Sections 1.3.1 and 1.3.2 were designed by hand. Deep learning replaced the design of features with learning from data, and the simplest deep approach treats PAD as a binary classification problem, labelling live faces 0 and spoofing faces 1 and training a convolutional neural network (CNN) with a binary cross-entropy loss [35]. This binary signal tells the network whether a sample is an attack, but not why.

Auxiliary supervision supplies the why. Pseudo-depth labels, reflection maps, binary mask labels and 3D point cloud maps are the typical pixel-wise auxiliary supervision signals [35]. Each one asks the network to predict a pixel-wise map, not only a class label. For pseudo-depth, the ground truth for real faces is estimated with a 3D face model fitting algorithm, while it is set to zero for planar presentation attacks [30]. In this way the 3D geometric cue becomes a training target, and the network learns that a live face has depth while a print or a screen is flat. Section 2.2 traces this idea through its landmark papers.

Two further families extend the deep toolbox. Generative methods model the intrinsic spoofing patterns through relaxed pixel-wise reconstruction constraints [35]. Transformers bring a different architecture: one line feeds spatio-temporal rPPG maps to a Vision Transformer (ViT) to capture periodic heartbeat features [35], so physiological cues also enter deep models. In addition, George and Marcel of the Idiap Research Institute used transfer learning from a pretrained ViT for zero-shot anti-spoofing at the 2021 International Joint Conference on Biometrics, and they outperformed earlier methods on the HQ-WMCA and SiW-M protocols with unseen attacks [41]. Table 1.9 lists the supervision signals.

**Table 1.9. Supervision signals of deep PAD classifiers**

| Supervision | Target the network predicts |
| :---- | :---- |
| Binary [35] | Live or spoof label |
| Pseudo-depth [35], [30] | Depth map from 3D face fitting; zero for planar attacks |
| Reflection map [35] | Pixel-wise reflection |
| Binary mask [35] | Pixel-wise live or spoof label |
| 3D point cloud [35] | Point cloud of the face |
| Reconstruction (generative) [35] | Spoof pattern via relaxed reconstruction |
| rPPG map with ViT [35] | Periodic heartbeat features |
