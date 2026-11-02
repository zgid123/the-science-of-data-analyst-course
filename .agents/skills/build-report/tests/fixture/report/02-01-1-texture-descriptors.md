### 2.1.1. Texture Descriptors

Texture analysis became the main line of Era 1 through a sequence of four steps. In 2011, Määttä et al. of the University of Oulu first proposed to apply multi-scale LBP to face PAD [30], at the International Joint Conference on Biometrics [36]. In 2012 and 2014, de Freitas Pereira et al. extended the idea from single images to video by applying dynamic texture based on LBP, and introduced the LBP from Three Orthogonal Planes (LBP-TOP) feature [30].

The third step moved from texture to image quality. The image distortion analysis of Wen, Han and Jain appeared in IEEE Transactions on Information Forensics and Security in April 2015 [38], and Section 1.3.1 describes its specular reflection, blur and colour features.

The fourth step added colour. On 19 November 2015, Boulkenafet, Komulainen and Hadid posted their colour-texture method, observing that earlier research had "mainly been focused on analyzing the luminance of the face images" [50]. Extracting LBP from the YCbCr colour space improved the results of grey-scale LBP "on CASIA-FA and Replay-Attack databases by 64.5 % and 81.4 %, respectively" [50], and the combined YCbCr and HSV descriptor reached 0.4% equal error rate (EER) and 2.9% HTER on Replay-Attack [50]. The journal version appeared in IEEE Transactions on Information Forensics and Security in August 2016 [37], which marks the peak of hand-crafted texture analysis. Table 2.1 summarises the sequence.

**Table 2.1. Chronology of Era-1 texture and quality methods**

| Year | Method | Group | Venue | Contribution |
| :---- | :---- | :---- | :---- | :---- |
| 2011 | Multi-scale LBP [30] | University of Oulu [30] | International Joint Conference on Biometrics [36] | First application of LBP to face PAD [30] |
| 2012, 2014 | LBP-TOP dynamic texture [30] | de Freitas Pereira et al. [30] | – | Texture extended to video [30] |
| 2015 | Image distortion analysis [38] | Wen, Han and Jain [38] | IEEE Transactions on Information Forensics and Security [38] | Quality cues: reflection, blur, colour [30] |
| 2015, 2016 | Colour texture [50], [37] | Boulkenafet, Komulainen and Hadid [50] | arXiv 2015; IEEE Transactions on Information Forensics and Security 2016 [50], [37] | 0.4% EER and 2.9% HTER on Replay-Attack [50] |

Each step improved the results on the benchmark it targeted, and as a result the colour-texture method became the reference hand-crafted baseline that later deep methods compared against [45].
