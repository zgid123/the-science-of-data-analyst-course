### 1.1.2. Evaluation Metrics

Because every presentation is either bona fide or an attack, PAD performance is measured by two complementary error rates. The attack presentation classification error rate (APCER) is the "proportion of attack presentations using the same PAI species incorrectly classified as bona fide presentations in a specific scenario" [6]. The bona fide presentation classification error rate (BPCER) is the "proportion of bona fide presentations incorrectly classified as presentation attacks in a specific scenario" [6]. APCER captures the security side of a PAD subsystem, and BPCER captures its convenience side.

APCER is computed separately for each PAI species $S$, and the system is judged by its weakest point. The overall APCER is the maximum APCER across all evaluated attack types, measured at a given decision threshold $\tau$ [13]:

$$\mathrm{APCER}_S(\tau) = \frac{\text{attack presentations of species } S \text{ classified as bona fide}}{\text{attack presentations of species } S}, \qquad \mathrm{APCER}(\tau) = \max_S \mathrm{APCER}_S(\tau)$$

$$\mathrm{BPCER}(\tau) = \frac{\text{bona fide presentations classified as attacks}}{\text{bona fide presentations}}$$

Lowering the threshold trades one error for the other, so studies that follow ISO/IEC 30107-3 also report the detection equal error rate (D-EER), the error rate at the operating point where APCER equals BPCER [11]. Peer-reviewed PAD studies from 2025 evaluate their models with APCER and BPCER in this way [14].

A third metric looks beyond the PAD subsystem to the complete biometric system. The impostor attack presentation match rate (IAPMR) is the "proportion of impostor attack presentations that are successful; that is, in which the biometric reference for the targeted identity is matched" [2]. Recent ISO-aligned research uses the newer name impostor attack presentation accept rate (IAPAR) for this quantity [8], and the FIDO Alliance measures resistance to spoof and deepfake attacks with it [4]. The metric shows how serious a weak PAD subsystem can be: a study of faces printed on T-shirts reported an IAPAR of about 99% at the selected operating points [8].

Competitions and benchmark papers often add the average classification error rate (ACER), the average of APCER and BPCER [10]. Averaging the two rates has been deprecated in ISO/IEC 30107-3, and ACER is reported mainly for comparison with competitions that use it [6]. The ChaLearn face anti-spoofing challenge at the 2019 Conference on Computer Vision and Pattern Recognition (CVPR) cited the ISO/IEC 30107-3 metrics and defined its ACER as the mean of APCER and a bona fide error rate [15]. Face PAD papers in 2026 still report APCER, BPCER and ACER on the OULU-NPU benchmark [16]. Table 1.2 summarises the four metrics.

**Table 1.2. PAD evaluation metrics**

| Metric | Measures | Computed over | Status in ISO/IEC 30107-3 | Source |
| :---- | :---- | :---- | :---- | :---- |
| APCER | Attacks accepted as bona fide | Each PAI species; maximum reported | Normative | [6], [13] |
| BPCER | Bona fide presentations rejected as attacks | All bona fide presentations | Normative | [6] |
| IAPMR (IAPAR) | Impostor attacks that reach a match | Complete biometric system | Normative; newer name IAPAR | [2], [8] |
| ACER | Average of APCER and BPCER | Both error rates | Deprecated | [10], [6] |

As a result, an ISO-aligned evaluation reports APCER, taken as the maximum over the evaluated species, and BPCER at a stated threshold, complemented by the D-EER [11].
