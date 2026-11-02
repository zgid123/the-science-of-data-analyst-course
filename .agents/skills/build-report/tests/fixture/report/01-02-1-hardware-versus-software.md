### 1.2.1. Hardware-Based and Software-Based PAD

Hardware-based PAD adds sensors that measure properties a print, a screen or a mask cannot easily reproduce. Dedicated hardware approaches use near-infrared (NIR) cameras, thermal sensors, light field cameras, multispectral sensors and 3D cameras [26]. These sensors read physical evidence directly, for example temperature from thermal cameras and the 3D volume of an artefact from 3D acquisition sensors [26]. In addition, human skin shows characteristic remission properties at multispectral short-wave infrared (SWIR) wavelengths, independent of a subject's age, gender or skin type [6], which gives spectral sensors a physical signature of living skin.

Two widely deployed consumer systems show hardware PAD in practice. Apple's Face ID projects and analyses thousands of invisible dots to build a depth map of the face and also captures an infrared image of it [27]. To counter digital and physical spoofs, its TrueDepth camera randomises the sequence of 2D and depth captures and projects a device-specific random pattern [28]. Microsoft's Windows Hello face authentication uses a camera configured for NIR imaging [29], and Microsoft states that infrared imaging prevents the most accessible attacks because infrared does not display in photographs or on liquid-crystal displays [29]. Hardware approaches tend to reach high detection rates, yet they remain less common because the required hardware is expensive and not broadly available [26].

Software-based PAD works on the data a standard camera already produces. It upgrades the countermeasures of existing systems without new hardware and authenticates in real time without extra user interaction [26], and it decides between bona fide presentations and attacks by algorithm, irrespective of the capture device [25]. A dedicated line of research covers face PAD that requires only the red, green and blue (RGB) cameras of generic consumer devices, built up over two decades [30]. Software methods divide into static analysis of single frames and dynamic analysis of temporal information [26]. This class is also the one that government benchmarking addresses: the Face Analysis Technology Evaluation (FATE) Part 10 of NIST evaluates passive, purely software-based face PAD algorithms operating on conventional 2D imagery [31]. The main limitation of software PAD is generalisation, because performance usually drops significantly when models are tested across databases [26].

The axis describes the source of the evidence rather than mutually exclusive products. Face ID combines its dedicated sensors with anti-spoofing neural networks against masks and other spoofs [27], so a deployed system often draws on both ends of the axis. Table 1.5 compares the two sources of evidence.

**Table 1.5. Hardware-based and software-based PAD**

| Aspect | Hardware-based PAD | Software-based PAD |
| :---- | :---- | :---- |
| Evidence | Physical measurements: depth, temperature, NIR and spectral response [26], [6] | Image and video content from the existing camera [26], [30] |
| Deployment cost | Expensive, dedicated sensors not broadly available [26] | No new hardware; upgrades existing systems [26] |
| User interaction | None beyond the capture itself [27], [29] | None; real time [26] |
| Main limitation | Availability and cost [26] | Generalisation across databases [26] |
| Deployed or evaluated example | Face ID, Windows Hello [27], [29] | NIST FATE Part 10 [31] |
