---
layout: research
title: Proton transfer in DNA
description: Can the motion of a single proton change how DNA is copied?
img: assets/img/research/dna.svg
img_alt: A proton moving between two DNA bases, changing their hydrogen-bonding arrangement.
importance: 5
category: projects
research_context: Quantum biology · Surrey & collaborators
related_publications: true
---

DNA is copied by matching its molecular letters, or bases, with their partners. A small rearrangement of hydrogen atoms
can change those pairing rules. I study whether **proton transfer**, including quantum tunnelling, can help create such
changes and whether they last long enough to matter during replication.

With my collaborators, I combine quantum calculations with simulations of water and enzymes. The central question is
not only whether an unusual base pair can form, but what happens to it as the cell handles the DNA.

{% include figure.liquid path="assets/img/research/dna.svg" alt=page.img_alt caption="Moving a proton can change a base’s hydrogen-bonding pattern. The resulting form is called a tautomer. The drawing illustrates the idea, rather than a complete DNA base pair." %}

## Mapping the energy landscape

A **tautomer** is a form of a molecule with a different arrangement of hydrogen atoms and bonds. Our calculations map
routes between ordinary DNA base pairs and their tautomers, and the energy barriers along the way. The adenine–thymine
and guanine–cytosine pairs behave differently, so an explanation for one cannot simply be applied to the other
{% cite slocombe2021quantum %}.

<h2 id="tunnelling-dominates-and-decoherence-does-not-kill-it">When quantum motion matters</h2>

Quantum tunnelling allows a proton to cross a barrier that a classical particle would have to climb over. In our model
of guanine–cytosine, tunnelling strongly increases proton transfer even when the base pair exchanges energy with its
surroundings {% cite slocombe2022open %}.

A calculated tautomer population is only one part of a possible mutation mechanism. Its biological significance depends
on the lifetime of that state and on the enzymes that separate and copy the strands.

<h2 id="strand-separation-traps-the-tautomer">What happens as the strands separate?</h2>

DNA must unzip before it can be copied. We found that stretching the hydrogen bonds changes the reaction landscape:
it can slow the formation of a tautomer while also making an existing one harder to reverse
{% cite slocombe2022protontransfer %}. Related work on adenine–thymine shows why the separating strands need to be
considered alongside the closed double helix {% cite king2023tautomerisation %}.

## The enzymes change the answer

The proteins handling DNA are active participants in this chemistry. Our simulations of the PcrA helicase, an enzyme
that separates the strands, show that its local environment can strongly suppress guanine–cytosine tautomer formation
{% cite winokan2023multiscale %}.

In a different setting, the DNA-copying enzyme polymerase can help a guanine–thymine mismatch access a different pairing
arrangement through proton transfer {% cite slocombe2023tunnelling %}. Comparing these cases helps us understand why the
same chemical process may have different consequences in different parts of the replication machinery.

## Beyond the canonical bases

More recent collaborative work examines **O6-methylguanine**, a chemically modified base. Methylation disrupts its
hydrogen bonding, while nearby water can provide another route for proton transfer {% cite de2025proton %}.

We have also investigated **hachimoji DNA**, a synthetic genetic system with additional letters, to ask how changing the
base chemistry affects proton-transfer pathways {% cite warman2023proton %}. Together, these studies test how far ideas
from ordinary DNA extend to modified and synthetic systems.

## Methods

I develop [simulation tools]({{ '/projects/molecular_simulation.html' | relative_url }}) that connect reaction paths,
quantum nuclear motion, and the surrounding molecular environment. Public inputs and analysis for several studies are
listed under [code behind the papers]({{ '/repositories/' | relative_url }}#paper-code).

## Related threads

Quantum effects do not play the same role in every biological system. Our **ASIC1 ion-channel preprint** investigates
why this membrane protein favours particular ions. Its calculations find extremely short coherence lifetimes and
support a classical explanation of selectivity; the manuscript remains under review {% cite vallee2025beyond %}.
Our broader review discusses the range of questions studied in quantum biology {% cite kim2021quantum %}.
