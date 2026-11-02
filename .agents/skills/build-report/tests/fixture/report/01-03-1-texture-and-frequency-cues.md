### 1.3.1. Texture and Frequency Cues

Texture methods start from the observation that a print or a screen is a different surface from skin. They analyse the micro-texture of the surface presented to the camera, using static or dynamic texture cues [30]. Määttä, Hadid and Pietikäinen of the University of Oulu established this line at the 2011 International Joint Conference on Biometrics, applying three uniform local binary pattern (LBP) operators to a normalised face image of 64 by 64 pixels to detect spoofs from a single image [30], [36]. The paper has 385 citations in Crossref as of 2 October 2026 [36].

Colour added a decisive dimension. Hand-crafted descriptors are extracted from several colour spaces, namely RGB, HSV and YCbCr, to capture spoofing patterns [35]. Boulkenafet, Komulainen and Hadid showed that an LBP-based method reached state-of-the-art performance only by changing the colour space it used [30]. Their colour-texture paper appeared in IEEE Transactions on Information Forensics and Security in August 2016 and has 486 citations in Crossref as of 2 October 2026 [37].

Image quality forms a related branch, because a recaptured face carries distortions that a live face does not. The image distortion analysis of Wen, Han and Jain combines a specular reflection feature, a blurriness feature, a chromatic moment feature and a colour diversity feature, 121 dimensions in total, and classifies them with support vector machines [30]. The paper appeared in IEEE Transactions on Information Forensics and Security in April 2015 and has 764 citations in Crossref as of 2 October 2026 [38]. Frequency-domain methods complete the family: they analyse the Fourier spectra of noise residuals to capture the noise that a spoofing attack introduces, such as the moiré pattern of a recaptured screen [30]. Table 1.7 summarises the representative texture and frequency methods.

**Table 1.7. Representative texture and frequency methods**

| Method | Venue and year | Cue exploited | Crossref citations (2 October 2026) |
| :---- | :---- | :---- | :---- |
| Määttä et al., LBP micro-texture | International Joint Conference on Biometrics, 2011 [36] | Micro-texture of a single face image [30] | 385 [36] |
| Wen et al., image distortion analysis | IEEE Transactions on Information Forensics and Security, 2015 [38] | Specular reflection, blur, chromatic moment, colour diversity [30] | 764 [38] |
| Boulkenafet et al., colour texture | IEEE Transactions on Information Forensics and Security, 2016 [37] | LBP texture in RGB, HSV and YCbCr [30], [35] | 486 [37] |
| Frequency-domain analysis | Survey category [30] | Fourier spectra of noise residuals, moiré [30] | – |

These methods need only one image and no user action, and as a result they fit the passive, software-based corner of the system taxonomy in Section 1.2.
