### 2.1.2. Motion and Blink-Based Liveness

The liveness line of Era 1 started even earlier than texture analysis. In 2005, Kollreider et al. proposed Optical Flow Lines, a method that detects the motion differences between planar photographs and genuine 3D faces [30]. The cue is geometric: "a translated photograph generates constant motion among all face regions" [30], whereas the parts of a real face move differently. In 2009, Bao et al. also used optical flow to distinguish 3D faces from planar photo attacks [30]. Optical-flow methods proved sensitive to their surroundings, since they "are not robust toward background and illumination changes" [30].

Eye blinking offered a second, physiological cue. Pan, Sun, Wu and Lao presented eye-blink-based anti-spoofing from a generic webcam at the 2007 IEEE International Conference on Computer Vision [51], and the paper has 462 citations in Crossref as of 2 October 2026 [51]. Blinking "normally happens 15 to 30 times per minute" [30], so any camera running at 15 frames per second or more captures two or more frames per blink, and the user needs no instruction [30]. Blink detection is therefore passive by default, and it becomes active only when a system prompts the user to blink, in the sense of Section 1.2.2.

By 2011 these cues had public benchmarks. Anjos and Marcel published the Print-Attack database together with a baseline countermeasure at the 2011 International Joint Conference on Biometrics, where it served the first competition [47]. The operating range of liveness cues became clear in the same period: blink-based methods "can effectively detect printed photo attacks, but not video replay attacks or eye-cut photo attacks" [30]. Table 2.2 summarises the liveness milestones.

**Table 2.2. Chronology of Era-1 motion and blink cues**

| Year | Method | Cue | Operating range |
| :---- | :---- | :---- | :---- |
| 2005 | Kollreider et al., Optical Flow Lines [30] | Motion of a planar photo versus a 3D face [30] | Not robust to background and illumination changes [30] |
| 2007 | Pan et al., eye-blink detection [51] | Spontaneous blinks, 15 to 30 per minute [30] | Detects printed photos; not video replay or eye-cut photos [30] |
| 2009 | Bao et al., optical flow [30] | Planar versus 3D motion [30] | Not robust to background and illumination changes [30] |
| 2011 | Anjos and Marcel, Print-Attack baseline [47] | Benchmark and baseline for print attacks [47] | Print attacks [47] |

Because blink cues do not stop video replay [30], the replay datasets described in Section 2.1.3 shifted attention back towards texture and quality cues.
