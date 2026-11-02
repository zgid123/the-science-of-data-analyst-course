### 1.3.2. Motion and Physiological Cues

Where texture methods inspect a surface, liveness methods look for signs of life over time. The most widely used liveness cues are motion, such as head movements and facial expressions, and the micro intensity changes caused by the blood pulse [30]. Dynamic cues explored for PAD include eye blinking, head movement, gaze tracking and remote physiological signals [35].

Motion cues came first. Pan et al. modelled eye blinking with conditional random fields fed by temporally observed images [30], so that a blink appears as a sequence of eye states that a photograph cannot produce. Optical-flow methods detect the differences in motion patterns between planar photographs and genuine three-dimensional faces [30].

The blood pulse offers a cue that even a perfect copy of the face's appearance lacks. Remote photoplethysmography (rPPG) recovers these pulse-driven intensity changes of the skin from an ordinary video [30]. The approach of Li et al., presented at the 2016 International Conference on Pattern Recognition, rests on the fact that "a pulse signal exists in a real living face but not in any mask or print material" [39]. It builds the signal from the lower half of the face, detected as a region of interest in each frame [30]. Liu et al. extended the idea in 2016 by extracting rPPG signals from multiple facial regions instead of the lower half only, and in 2018 by combining learned pseudo-rPPG estimates with 3D geometric cues [30]. As a result, rPPG serves as an intrinsic liveness cue specifically against 3D mask attacks [40], and it detects photo attacks and even high-quality 3D masks [30].

Each cue also has a clear operating range. rPPG does not, in general, detect video replay attacks [30], because head motions and rPPG signals are easily imitated by a replayed video [35]. Physiological cues are usually captured from long interactive videos, which is inconvenient for practical deployment [35]. Earlier rPPG methods against masks required 10 to 12 seconds of observation, and the TSrPPG method, presented at the 2020 Winter Conference on Applications of Computer Vision, reduced the observation time to within one second while keeping its performance [40]. Table 1.8 summarises the motion and physiological cues.

**Table 1.8. Motion and physiological cues**

| Cue | What it detects | Representative work | Operating range |
| :---- | :---- | :---- | :---- |
| Eye blink | Sequence of open and closed eye states [30] | Pan et al., conditional random fields [30] | Video input required [35] |
| Optical flow | Planar motion of a photograph versus 3D facial motion [30] | Survey category [30] | Imitated by video replay [35] |
| rPPG pulse | Pulse present in skin, absent in masks and prints [39] | Li et al. 2016; Liu et al. 2016 and 2018 [39], [30] | Detects photos and 3D masks, not video replay [30]; observation time cut to within one second [40] |
