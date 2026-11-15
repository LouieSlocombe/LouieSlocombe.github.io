---
layout: research
title: Surfaces & energy materials
description: How do atomic interactions control motion on a surface and a material’s response to light?
img: assets/img/research/surfaces.svg
img_alt: A water molecule moving over a honeycomb surface beside incoming light reaching a layered material.
importance: 6
category: projects
research_context: Collaborative research · Surrey & Birmingham
related_publications: true
---

The same computational chemistry used to study a molecule can help explain how a material behaves. My collaborations
in this area connect atomic-scale calculations with experiments and with tools for assessing energy materials.

{% include figure.liquid path="assets/img/research/surfaces.svg" alt=page.img_alt caption="Two applications of atomic-scale modelling: following molecules at an interface and understanding how materials absorb light. Schematic only; no measured trajectories or efficiencies are shown." %}

## Following water one molecule at a time

Graphene and hexagonal boron nitride both form honeycomb sheets, but their chemistry is different. In a 2025
collaboration, we combined experiments tracking molecular motion with electronic-structure calculations to investigate
how individual water molecules move on these surfaces {% cite seiler2025understanding %}.

On the studied nickel-supported boron nitride surface, water moves through coupled rotation and translation; on
graphene, it makes more distinct hops. The supporting material also changes the interaction. This helps explain why
similar-looking surfaces can have different friction and water-transport behaviour.

Related collaborative work examines how alkali-metal atoms adsorb on metal surfaces, connecting the way atoms bind
with the measurements used to study their motion {% cite raghavan2021alkali %}.

## Assessing materials for solar cells

I contribute to **Solphin**, a collaborative Python package for analysing whether a material could be useful as a solar
absorber. It connects electronic-structure calculations with optical absorption and estimates of the theoretical limits
of photovoltaic efficiency {% cite cox2026solphin %}.

These estimates help compare candidate materials; they describe model limits rather than the efficiency of a finished
device. The accompanying 2026 manuscript is a preprint, being prepared for submission to the _Journal of Open Source Software_.

## Building models of disordered materials

Many materials do not have a repeating crystal lattice. Through **AmorphGen**, developed with the Scanlon Materials
Theory Group, I contribute to methods for constructing amorphous structures by random placement, simulated melting
and cooling, or combinations of these approaches.

Generating several plausible structures lets us explore how much a calculated property depends on the particular
atomic arrangement. This complements my work on [molecular simulation]({{ '/projects/molecular_simulation.html' | relative_url }}).

The public projects are [Solphin](https://github.com/SMTG-Bham/solphin) and
[AmorphGen](https://github.com/SMTG-Bham/AmorphGen).
