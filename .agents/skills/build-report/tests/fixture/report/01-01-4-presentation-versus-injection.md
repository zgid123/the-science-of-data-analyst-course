### 1.1.4. Presentation Attacks and Digital Injection Attacks

The vocabulary and the levels above share one boundary: ISO/IEC 30107-3 covers attacks that "take place at the biometric capture device during presentation" [3]. Remote identity verification, in which a user's own phone or computer captures the face, opens a second route that avoids the sensor altogether [10]. A 2024 paper from Amazon Web Services (AWS) AI Labs, "Principles of Designing Robust Remote Face Anti-Spoofing Systems", formalises this distinction and identifies physical presentation attacks and digital injection attacks as the two main categories of threats to a face anti-spoofing system [10].

In a digital injection attack (DIA), the attacker bypasses the sensor and injects malicious digital content directly into the data stream [10]. The content can be pre-recorded images or videos, or media produced with deepfake technology [10]. The paper divides the injection category into three sub-categories: deepfake attacks, digital adversarial attacks and digital replay attacks [10]. Adversarial attacks assume that the attacker can call the model, with limited or unlimited access, and can therefore craft adversarial samples, including adversarial noise, to pass the system [10]. Part of the PAD literature also uses the term injection attack for imperceptible noise added to the digital image before classification [13], so adversarial noise sits naturally within the injection category.

The AWS threat model extends beyond these two categories with processor override and results modification, and it organises defences by system layer: model performance, model robustness, machine learning pipeline robustness and platform robustness [10]. Its headline recommendation is a proactive anti-spoofing system that uses active sensors [10]. The two categories also differ in scale. Presentation attacks are generally manual and low-scale, whereas injection attacks scale far more easily once an attacker can push manipulated data into a system [21].

Standardisation follows the same boundary. CEN/TS 18099, "Biometric data injection attack detection", a technical specification of the European Committee for Standardization (CEN), was published on 2 December 2024 and is current [22]. It defines biometric data injection attacks and injection attack instruments, describes systems for detecting them and test plans, and leaves presentation attack testing to the ISO/IEC 30107 standards [23]. As of July 2026 it is the only operational formal technical specification for injection attack resilience, and the international standard ISO/IEC 25456 is in development on its basis [21]. Table 1.4 contrasts the two attack routes.

**Table 1.4. Presentation attacks and injection attacks**

| Aspect | Presentation attack | Injection attack (DIA) |
| :---- | :---- | :---- |
| Point of attack | Capture device, during presentation [3] | Data stream after the sensor [10] |
| Instrument | Physical PAI: print, replay screen, mask [10] | Digital content: deepfake, adversarial sample, digital replay [10] |
| Scale | Manual and low-scale [21] | Repeatable and scalable [21] |
| Standard | ISO/IEC 30107 [23] | CEN/TS 18099; ISO/IEC 25456 in development [22], [21] |

PAD and injection attack detection therefore form two related but distinct defences, and Section 1.2 places both within the architecture of a biometric system.
