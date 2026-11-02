### 1.2.2. Passive and Active PAD

The second axis concerns what the user is asked to do. Passive PAD analyses the captured sample itself: single-image passive models look for artefacts or anomalies in the input [10]. Passive models offer an excellent user experience with minimal user friction [10], and the NIST FATE Part 10 benchmark evaluates exactly this passive class [31]. Their reliance on one captured image also defines their limit, since single-image models are generally ineffective against digital replay attacks [10].

Active PAD, also called challenge-response, presents a challenge to the user, such as completing a predefined task, or exposes the user to a stimulus in order to record a voluntary or involuntary response [26]. Typical responses include eye movements and speaking predefined words [26]. Challenge-response methods are effective against many presentation attacks, and they usually require more time and cooperation from the user, which is not always possible or desirable [26]. The axis therefore trades convenience against the strength of the liveness evidence.

A third class lets the device issue the challenge without asking the user to act. The AWS threat model advocates a proactive approach that uses the capabilities of the sensors for active sensing and imaging [10]. Face Flashing, a 2018 method, randomly flashes well-designed pictures on the screen and analyses the light reflected from the face [32]. It exploits the speed of light reflection, facial texture and the uneven 3D shape of a real face, and reports an overall accuracy of 98.8% [32]. Such light challenges combine the passive user experience with an active stimulus, and Table 1.6 places them between the two ends of the axis.

**Table 1.6. Passive, active and hybrid PAD**

| Class | User action | Evidence | Strength | Limitation |
| :---- | :---- | :---- | :---- | :---- |
| Passive | None | Artefacts in a single image or short clip [10] | Minimal friction [10] | Weak against digital replay [10] |
| Active (challenge-response) | Completes a task, e.g. eye movements or spoken words [26] | Voluntary or involuntary response [26] | Effective against many presentation attacks [26] | More time and cooperation [26] |
| Hybrid (device challenge) | None; the screen issues the stimulus [32] | Reflected light, texture, 3D shape [32] | Active evidence with a passive experience; 98.8% accuracy reported by its authors [32] | – |
