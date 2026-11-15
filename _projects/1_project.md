---
layout: page
title: Proton transfer in DNA
description: how moving a proton can change the way DNA is copied
img: assets/img/proton_transfer_dna.svg
importance: 1
category: projects
related_publications: true
---

A proton moving across a hydrogen bond can change the way a DNA base pairs. The resulting **tautomer**, a form with
a different arrangement of hydrogen atoms, may pair with the wrong partner when DNA is copied. In 1963, Löwdin proposed
that quantum tunnelling could drive this process and cause spontaneous point mutations. A persistent objection was
that the tautomer would disappear in the warm, fluctuating environment of a cell before a polymerase could read it.

I study what happens to these protons during replication. With my collaborators, I combine electronic-structure
calculations, quantum dynamics, and models of the surrounding water and enzymes to follow both the formation of a
tautomer and its chances of surviving. The timing matters as much as the energy barrier.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/proton_transfer_dna.svg" title="Double proton transfer in the G–C base pair" alt="Asymmetric double-well potential connecting the canonical G–C minimum to the higher-lying tautomeric G*–C* minimum, with a tunnelling pathway through the barrier" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Double proton transfer converts the canonical guanine–cytosine pair into the mutagenic tautomer G*–C* across an
    asymmetric double-well potential. At biological temperatures, the tunnelling contribution to the transfer rate is
    several orders of magnitude larger than that of classical over-the-barrier hopping.
</div>

## Mapping the energy landscape

We began by mapping the reaction surface between the usual amino-keto base pairs and their imino-enol tautomers,
using density functional theory and machine-learning nudged elastic band methods {% cite slocombe2021quantum %}.
The two base pairs behave quite differently. In A–T, the reverse barrier is so small that A*–T* quickly returns to its
usual form. G–C has a much larger thermal population of its tautomer, G*–C*, making it a candidate for further study
as the DNA passes through the replication machinery.

## Tunnelling dominates, and decoherence does not kill it

To follow the proton over time, we couple the base-pair potential to an open quantum systems master equation. This
includes energy exchange with the surroundings and the loss of quantum coherence. Even in that environment,
tunnelling contributes several orders of magnitude more to proton transfer than classical hopping over the barrier
{% cite slocombe2022open %}.

The usual and tautomeric forms exchange so quickly that the pair reaches thermal equilibrium well before the relevant
biological processes occur. The calculated probability of finding it in the tautomeric form is **1.73 × 10⁻⁴**,
orders of magnitude above the observed rate of spontaneous point mutations. That leaves a crucial step to understand:
how many of those tautomers survive long enough for a polymerase to read them?

## Strand separation traps the tautomer

During replication, the two DNA strands separate. We found that double proton transfer follows a sequential,
step-like mechanism, with a barrier that rises quasi-linearly as the bases move apart
{% cite slocombe2022protontransfer %}. This slows the formation of new tautomers, but it also makes existing ones
much more stable. A tautomer present when the strands begin to unzip can therefore become trapped.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/proton_transfer_strand_separation.svg" title="Effect of strand separation on the proton transfer landscape" alt="Potential energy curves for the closed duplex and for separating strands, showing a higher barrier and a stabilised tautomer minimum as the strands unzip" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    As the hydrogen bonds stretch during strand separation, the transfer barrier grows and the reaction asymmetry falls,
    stabilising the tautomer rather than destroying it.
</div>

Molecular dynamics lets us estimate how long that survival window needs to be. Across 210 simulations and 1,442
separation events, the strands part at roughly 1.2 Å ps⁻¹. A tautomer needs to survive for about **1.7 ps** to be carried
through, compared with the roughly 100 ps assumed in earlier work.

This also changes the picture for A–T. Although A*–T* is unstable in the closed duplex, it becomes more stable as the
strands unzip and the hydrogen bonds stretch. Strand separation could therefore allow a proton-transfer route to A–T
point mutations that would be missed by considering the closed pair alone {% cite king2023tautomerisation %}.

## The enzymes change the answer

The proteins handling DNA have a strong influence on this process. In QM/MM simulations of the bacterial PcrA helicase,
the protein raises the forward barrier from 0.60 ± 0.04 eV in aqueous DNA to 1.24 ± 0.07 eV in the helicase site.
It also raises the reaction asymmetry from 0.54 ± 0.08 eV to 1.68 ± 0.10 eV. Together, these changes reduce the
tautomeric equilibrium constant by roughly eighteen orders of magnitude {% cite winokan2023multiscale %}.
Asparagine N624 plays a particularly strong role, suggesting that suppressing spontaneous mutation may be one of its
secondary functions. The calculations also show why individual configurations matter: averaging over an ensemble
can hide features of the reaction profile that affect tunnelling.

In the polymerase active site, we find the opposite effect. A QM/MM model of guanine–thymine wobble misincorporation,
coupled to an open quantum systems master equation, reveals a short-lived configuration that increases the proton
transfer rate roughly **a hundredfold** {% cite slocombe2023tunnelling %}. The predicted error rates agree with
experimentally observed replication error frequencies. A kinetic isotope effect of around ten also offers a way to
test the proposed mechanism experimentally.

These results make the surrounding enzyme central to the explanation. Proton transfer can be fast, but its relevance
to a mutation depends on where it happens and what happens to the base pair next.

## Beyond the canonical bases

We've also used these methods to look at modified bases and synthetic genetic alphabets:

- **Synthetic genetic alphabets.** In hachimoji DNA, which extends the alphabet with the bases Z, P, S, and B, the
  proton transfer barriers for the Z–P and S–B pairs are around 30% lower than for G–C and A–T
  {% cite warman2023proton %}. Proton transfer should therefore be markedly more frequent than in canonical DNA, with
  a corresponding cost in replication fidelity for synthetic biology applications.
- **Epigenetic and damage-induced modifications.** Methylation of guanine at the O6 position disrupts the hydrogen
  bonding of the pair and hinders proton transfer, but explicit water opens a water-assisted hopping channel that
  lowers the barriers again {% cite de2025proton %}. Understanding the effect on mutagenesis therefore requires us
  to include the water molecules that participate in the reaction.

## Methods

Each method answers a different part of the question. Hybrid density functional theory and machine-learning-accelerated
nudged elastic band calculations give us reaction paths and barriers. QM/MM places the base pair inside an enzyme,
while classical molecular dynamics samples strand separation and base-opening angles. Open quantum systems master
equations then describe how the proton moves while exchanging energy and losing coherence to its surroundings.
Combining these calculations lets us connect the molecular energy landscape to the timescales of DNA replication.

## Related threads

The same questions arise elsewhere in biology, sometimes with a different answer. Our work on the acid-sensing ion
channel ASIC1 finds coherence lifetimes below a femtosecond, pointing to a classical explanation for its selectivity
{% cite vallee2025beyond %}. For a broader discussion of where quantum effects matter in biology, see our review
{% cite kim2021quantum %}.
