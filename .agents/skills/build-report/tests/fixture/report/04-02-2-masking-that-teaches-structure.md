### 4.2.2. Masking That Teaches Facial Structure

What the network learns depends on what is hidden, because it learns to infer the hidden parts from the visible ones. FSFM therefore designs its masking around the structure of a face. A face parser first divides each face into regions: eyebrows, eyes, mouth, nose, hair, skin, background and the boundary of the face [102]. Figure 4.2 compares three ways of hiding 75% of the face.

![Figure 4.2. Three masking strategies on a schematic face (redrawn from the description in [102])](assets/figures/task2-4-2-masking-strategies.png){width=100%}

Plain random masking ignores the face, so it often hides small but informative regions such as the eyes completely [102]. Masking the same share of every region, called proportional masking, keeps every region partly visible; this, however, creates a shortcut, since a region can be filled in from its own leftover patches without any understanding of the rest of the face [102].

FSFM's strategy, Covering a Random Facial Region followed by Proportional masking (CRFR-P), combines the strengths of both [102]. It hides one randomly chosen region completely, such as the nose or the mouth, and then hides an equal share of every other region until 75% of the face is covered [102]. The fully covered region can only be rebuilt from the surrounding face, which teaches how regions relate to each other; the evenly masked rest still demands fine detail within each region [102]. The authors describe this as "a nontrivial and meaningful MIM task", where masked image modelling (MIM) is the name for this hide-and-rebuild exercise [102].

As a result, the network learns where the eyes must sit given the nose, what skin texture continues beyond an edge, and how the parts of one face belong together, which is the knowledge that forgeries and spoofs tend to violate.
