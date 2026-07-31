---
layout: page
title: proton transfer in DNA
description: nuclear quantum effects, tautomerisation, and the origin of spontaneous point mutations
img: assets/img/proton_transfer_dna.svg
importance: 1
category: projects
related_publications: true
---

The bases of DNA are held together by hydrogen bonds, and a hydrogen bond is really a proton sitting in a double-well
potential. In 1963 Löwdin proposed that such a proton could hop to the opposite base, converting a Watson–Crick pair
into a rare **tautomer** that mispairs during replication — a purely quantum-mechanical route to a spontaneous point
mutation. The idea was attractive but largely dismissed: a warm, wet, noisy cell is a hostile place for delicate quantum
behaviour, and the tautomer was assumed to collapse long before a polymerase could ever read it.

My work asks whether that dismissal holds up once you treat the problem properly — with an accurate electronic structure
description of the base pair, quantum dynamics for the proton, an explicit model of the dissipative cellular
environment, and the enzymes of the replisome actually present.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/proton_transfer_dna.svg" title="Double proton transfer in the G–C base pair" alt="Asymmetric double-well potential connecting the canonical G–C minimum to the higher-lying tautomeric G*–C* minimum, with a tunnelling pathway through the barrier" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Double proton transfer converts the canonical guanine–cytosine pair into the mutagenic tautomer G*–C* across an
    asymmetric double-well potential. At biological temperatures the tunnelling contribution to the transfer rate is
    several orders of magnitude larger than classical over-the-barrier hopping.
</div>

## Mapping the energy landscape

The starting point was a careful map of the reaction surface connecting the canonical amino-keto pairs to their
imino-enol tautomers, built with density functional theory and machine-learning nudged elastic band methods
{% cite slocombe2021quantum %}. A–T and G–C behave very differently. The reverse barrier for A*–T* is so small that the
tautomer simply falls back before it can do anything biologically meaningful, whereas the thermal population of G*–C* is
large enough to be worth taking seriously — and, in principle, large enough to propagate through the replisome.

## Tunnelling dominates, and decoherence does not kill it

Barriers alone do not settle the question; the proton's dynamics do. Coupling the base-pair potential to an open
quantum systems master equation — the proton interacting with a decoherent, dissipative environment — shows that the
quantum tunnelling contribution to proton transfer is several orders of magnitude larger than classical over-the-barrier
hopping {% cite slocombe2022open %}. The consequence is that the canonical and tautomeric forms interconvert on
timescales far shorter than biological ones, so the base pair reaches thermal equilibrium essentially instantly, with a
tautomeric occupation probability of **1.73 × 10⁻⁴**. That is orders of magnitude above the observed rate of
spontaneous point mutations, which turns the interesting question into a different one: not whether tautomers form, but
whether any of them survive long enough to be read by a polymerase.

## Strand separation traps the tautomer

Equilibrium in a closed duplex is only half the story: mutations are fixed when the strands come apart at the
replication fork. The double proton transfer turns out to follow a sequential, step-like mechanism whose barrier rises
quasi-linearly as the strands separate {% cite slocombe2022protontransfer %}. Unzipping therefore does two opposing
things at once — it slows the *formation* of new tautomers while sharply increasing the *stability* of any that already
exist, effectively trapping the population that was there when the fork arrived.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/proton_transfer_strand_separation.svg" title="Effect of strand separation on the proton transfer landscape" alt="Potential energy curves for the closed duplex and for separating strands, showing a higher barrier and a stabilised tautomer minimum as the strands unzip" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    As the hydrogen bonds stretch during strand separation the transfer barrier grows and the reaction asymmetry falls,
    stabilising the tautomer rather than destroying it.
</div>

Molecular dynamics puts a clock on this. Across 210 simulations and 1,442 separation events the strands part at roughly
1.2 Å ps⁻¹, meaning a tautomer needs to survive only about **1.7 ps** to be carried through — two orders of magnitude
less demanding than the ~100 ps that earlier work had assumed.

The A–T pair deserves a second look for the same reason. Although A*–T* is unstable in the closed duplex, its stability
increases as the strands unzip and the hydrogen bonds stretch, which reopens a proton-transfer route to point mutations
in A–T that the equilibrium picture had ruled out {% cite king2023tautomerisation %}.

## The enzymes change the answer

Treating DNA in water is a convenient idealisation; replication happens inside proteins. QM/MM simulations of the
bacterial PcrA helicase show how much that matters {% cite winokan2023multiscale %}. The local protein environment
raises the forward barrier from 0.60 ± 0.04 eV in aqueous DNA to 1.24 ± 0.07 eV in the helicase site, and pushes the
reaction asymmetry from 0.54 ± 0.08 eV to 1.68 ± 0.10 eV — collapsing the tautomeric equilibrium constant by roughly
eighteen orders of magnitude. One residue does much of the work: asparagine N624 appears to serve a secondary function
of suppressing spontaneous mutation. The same study is a caution about methodology, since ensemble-averaging washes out
structure in the reaction profile that matters for the tunnelling regime.

At the other end of the replisome, the polymerase active site pushes in the opposite direction. Modelling
guanine–thymine wobble misincorporation with QM/MM coupled to an open quantum systems master equation reveals a
short-lived "tunnelling-ready" configuration along the wobble pathway that increases the proton transfer rate roughly
**a hundredfold** {% cite slocombe2023tunnelling %}. The predicted rates of genetic error formation agree with
experimentally observed replication error frequencies, and the mechanism carries a kinetic isotope effect of around ten
— large enough to be an experimental handle on it.

Taken together these results replace a yes/no question with a more interesting one. Proton transfer is quantum
mechanical and fast, but whether the resulting tautomer ever reaches a polymerase depends on which enzyme is holding
the base pair at the time — the helicase suppressing it, the polymerase active site enhancing it.

## Beyond the canonical bases

The same machinery applies to genetic systems that are not Watson–Crick DNA:

- **Synthetic genetic alphabets.** In hachimoji DNA, which extends the alphabet with the bases Z, P, S and B, the
  proton transfer barriers for the Z–P and S–B pairs are around 30% lower than for G–C and A–T
  {% cite warman2023proton %}. Proton transfer should therefore be markedly more frequent than in canonical DNA, with
  a corresponding cost in replication fidelity for synthetic biology applications.
- **Epigenetic and damage-induced modifications.** Methylation of guanine at the O6 position disrupts the hydrogen
  bonding of the pair and hinders proton transfer, but explicit water opens a water-assisted hopping channel that
  lowers the barriers again {% cite de2025proton %}. The net effect on mutagenesis is not a simple one, and depends on
  treating the solvent as an active participant rather than a passive dielectric.

## Methods

The work sits at the junction of several approaches, and most of the results come from combining rather than choosing
between them: hybrid density functional theory and machine-learning-accelerated nudged elastic band calculations for
reaction paths and barriers; QM/MM to embed a base pair in an explicit enzyme; classical molecular dynamics for
strand-separation statistics and opening-angle ensembles; and open quantum systems master equations to propagate the
proton in a dissipative, decohering environment. That last ingredient is what distinguishes this work from a purely
static barrier-height picture, and it is where the biologically relevant answers tend to come from.

## Related threads

Proton and nuclear quantum effects run through biology well beyond DNA, and it is just as important to identify where
they *do not* matter. Work on the acid-sensing ion channel ASIC1 finds coherence lifetimes in the sub-femtosecond
range, pointing to classical rather than quantum origins for its selectivity {% cite vallee2025beyond %}. The broader
context for this programme, and an assessment of which quantum-biological claims are on solid ground, is set out in
{% cite kim2021quantum %}.
