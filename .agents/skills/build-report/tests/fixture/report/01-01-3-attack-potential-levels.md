### 1.1.3. Attack Potential

The error rates of Section 1.1.2 state how often attacks succeed. A complete evaluation also states how much effort those attacks required, and this effort is expressed as attack potential. The concept comes from the security evaluation of information technology products. The ISO/IEC 19989 series supplements the Common Criteria standard ISO/IEC 15408 and its evaluation methodology ISO/IEC 18045 with extended security functional requirements and matching assurance activities [17]. Its Part 3, ISO/IEC 19989-3, addresses PAD; the British Standards Institution edition was published on 30 September 2020 and is listed as current and under review [17]. In this framing, attackers "attempt to subvert the system security policy by presenting their natural biometric characteristics or artefacts holding copied or faked characteristics" [17], which places PAD evaluation inside an established security methodology.

The Common Criteria are a set of internationally recognised technical standards [18], and they rate the attack potential of each attack by scoring it on five factors: expertise, knowledge of the target of evaluation, window of opportunity, equipment and elapsed time [18]. The summed score maps to an ordered rating that rises from Basic through Moderate and High to Beyond High [18]. Building on this mechanism, a higher rating states that a system resisted attacks requiring more skill, more knowledge, more time and better equipment.

Test laboratories make the concept concrete as test levels, in which higher levels use attack instruments that "reflect increased attacker effort, skill, and resources" [19]. The levels of iBeta Quality Assurance, an accredited laboratory whose confirmation letters Part 3 of this report examines, show how each factor becomes a test parameter. Table 1.3 lists them as retrieved on 2 October 2026.

**Table 1.3. iBeta PAD test levels (as of 2 October 2026)**

| Parameter | Level 1 | Level 2 | Level 3 |
| :---- | :---- | :---- | :---- |
| Time allowed | 8 hours per subject or species | 2–4 days per subject or species | 7 days per species, 4 days per subject |
| Attacker expertise | Not specified | Moderate: at least one other PAD test with the target modality | Significant: at least 16 hours of research on presentation attacks and at least 10 other PAD tests with the modality |
| Equipment | Readily available in a normal home or office | More expensive, such as a 3D printer, resin mask or latex mask | – |
| Cost limit per artefact | $30 | $300 | – |
| Attacks run | 150 attacks alternated with 50 genuine presentations | – | – |
| Attack success allowed | 0% | 1% | 5% |
| Bona fide error cap | 15% | 15% | 10% |

Source: [20].

iBeta also caps the bona fide errors for a pass, the BPCER and the false non-match rate (FNMR), at 15% for Levels 1 and 2 and 10% for Level 3, and it reviews these limits every six months [20]. A system therefore cannot reach a level by rejecting genuine users. The level structure is now spreading beyond presentation attacks: the forthcoming standard ISO/IEC 25456 for injection attack detection is expected to weight the complexity of attacks in levels as well (as of July 2026) [21].
