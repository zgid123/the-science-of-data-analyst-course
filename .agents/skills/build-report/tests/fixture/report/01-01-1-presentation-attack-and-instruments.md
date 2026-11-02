### 1.1.1. Presentation Attacks and Attack Instruments

The central term of the vocabulary is the presentation attack. ISO/IEC 30107 defines it as a "presentation to the biometric data capture subsystem with the goal of interfering with the operation of the biometric system" [6]. The same wording appears in ISO/IEC 30107-1:2016 [7], and research published in 2026 still quotes it as the definition in ISO/IEC 30107-3 [8], so the definition has stayed stable across editions. ISO/IEC 30107-1 also states the concept as "the presentation of an artefact or of human characteristics to a biometric capture subsystem in a fashion intended to interfere with system policy", as quoted in the PAD benchmark plan of the National Institute of Standards and Technology (NIST) [9]. Both formulations describe the same event: an artefact or a human characteristic is presented to the sensor in order to defeat the policy of the system.

The counterpart of an attack is the bona fide presentation, the "interaction of the biometric capture subject and the biometric data capture subsystem in the fashion intended by the policy of the biometric system" [6]. Every presentation to the sensor is either a bona fide presentation or an attack presentation [2]. As a result, PAD reduces to a binary decision about each presentation, and its errors fall into exactly two kinds, which Section 1.1.2 measures.

The object of an attack is named separately. A presentation attack instrument (PAI) is a "biometric characteristic or object used in a presentation attack" [6]. It can be a biometric characteristic, possibly a non-living sample, or an artificial object [2]. Instruments are grouped into a PAI species, a "class of presentation attack instruments created using a common production method and based on different biometric characteristics" [6]. A species is therefore defined by how an instrument is made, not by whose characteristic it copies; for example, printed photographs of many different people form one species. This grouping matters in practice, because the error rates of Section 1.1.2 are computed per species.

For faces, the common species are printed images, replays on a screen or tablet, and three-dimensional masks [10]. Recent benchmarks add partial attacks, such as funny eyes, partial eyes, partial mouth and paper glasses, alongside print, replay and mask attacks [11]. Low-cost instruments extend the range further: a face printed on a T-shirt is cheap to make compared with a silicone mask [8]. In-the-wild datasets reflect this breadth, and the WFAS 2023 dataset contains 17 presentation attack types in both two-dimensional and three-dimensional forms [12]. Table 1.1 summarises the face species named in these sources.

**Table 1.1. Face PAI species named in recent sources**

| PAI species | Production method | Source |
| :---- | :---- | :---- |
| Print | Face image printed on a tangible medium such as paper | [10] |
| Physical replay | Face image or video displayed on a screen or tablet | [10] |
| Three-dimensional mask | Mask built from the victim's facial characteristics | [10] |
| Partial attacks | Funny eyes, partial eyes, partial mouth, paper glasses | [11] |
| Printed garment | Face printed on a T-shirt | [8] |
