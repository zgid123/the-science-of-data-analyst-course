### 1.3.5. Summary of the Taxonomies

The system-level axes of Section 1.2 and the technique families of Sections 1.3.1 to 1.3.3 describe the same methods from two directions. The system view asks where the evidence comes from and what the user does; the technique view asks which cue the detector exploits [30]. Table 1.11 joins the two views and adds the generalisation behaviour from Section 1.3.4, and Figure 1.2 draws the same structure as a tree.

**Table 1.11. Technique families placed on the system-level axes**

| Technique family | Evidence source | User role | Input | Typical strength | Generalisation limit |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Texture and frequency [30] | Software on RGB images [26] | Passive [10] | Single image [30] | Micro-texture, colour and moiré differences of print and screen [30] | Colour texture scores 28.09–63.59% HTER on unseen datasets [42] |
| Motion and physiological [30] | Software on video [30] | Passive (blink, rPPG) or active (challenge-response) [35], [26] | Video [35] | rPPG detects photos and high-quality 3D masks [30] | Imitated by video replay; long observation time [35], [40] |
| 3D geometric [30] | Hardware depth sensors [26], or software via pseudo-depth supervision [30] | Passive [27], [29] | Depth map or image [26], [30] | Separates flat attacks from faces with depth [30] | Dedicated hardware is expensive and not broadly available [26] |
| Deep classifiers with binary or auxiliary supervision [35] | Software [35] | Passive [10] | Image or video [35] | Below 5% ACER within one dataset [35] | Above 20% HTER across datasets for most deep models [35] |

![Figure 1.2. Taxonomy of PAD](assets/figures/task2-1-2-pad-taxonomy.png){width=100%}

Two conclusions follow from the table. First, every family, whatever its system-level position, is limited less by what it detects within a known dataset than by how it transfers to new data, attacks and devices [35], [42]. Second, the history of the field in Part 2 can be read as a sequence of answers to this generalisation problem, from hand-crafted cues through auxiliary supervision to domain generalisation and, finally, to the foundation model of Part 4.
