---
layout: research
title: Molecular simulation & quantum dynamics
description: How do we follow reactions accurately while keeping their surroundings in the picture?
img: assets/img/research/simulation.svg
img_alt: A small reactive region highlighted inside a larger molecular environment, alongside a path between two molecular arrangements.
importance: 2
category: projects
research_context: Methods & research software
---

A chemical reaction may involve only a few atoms, but the water, protein, or material around them can change its outcome.
I develop computational methods and software to connect these scales: the detailed physics of a reaction and the motion
of its surroundings.

This work supports my studies of [DNA]({{ '/projects/1_project.html' | relative_url }}) and
[polymers]({{ '/projects/sustainable_polymers.html' | relative_url }}), while producing tools that can be used in other molecular systems.

{% include figure.liquid path="assets/img/research/simulation.svg" alt=page.img_alt caption="A detailed model of a small reacting region can be coupled to a larger environment. Reaction-path calculations then connect the initial and final arrangements. Schematic only." %}

## A detailed reaction inside a larger system

Quantum mechanics describes electrons rearranging as bonds change. Applying that level of detail to an entire protein
or a large material can be expensive. **QM/MM** combines a quantum-mechanical calculation for the region of interest
with a simpler molecular-mechanics model for its environment.

My **openmmqmmm** package connects ORCA and OpenMM for these calculations. It is derived from the ASH modelling program
and also provides routes to use machine-learning models for atomic interactions. **reactiontools** helps find and
analyse the paths between molecular arrangements, including the energy barriers that make some reactions slow.

## When nuclei behave quantum mechanically

Hydrogen nuclei are light enough that a classical picture of moving particles can miss important behaviour. They can
tunnel through an energy barrier, and changing hydrogen to its heavier isotope, deuterium, can change a reaction rate.
Those differences provide ways to investigate the mechanism.

I develop **HEOM.jl** to follow quantum motion while accounting for interaction with an environment.
**openmmnqe** brings methods for quantum nuclei into OpenMM, while **nqetools** supports setup and analysis around i-PI
calculations. Each offers a different balance of physical detail and computational cost.

## Making larger calculations useful

I also work on machine-learning models of atomic forces, efficient calculations, and the preparation needed before a
simulation can begin. **py-chargemol** analyses electron density to assign atomic charges and related quantities;
**vanderfast** calculates dispersion interactions, the weak attractions that matter when molecules pack together.

Speed is useful when it lets us study more configurations or longer times. I am equally interested in checking that
the model, numerical settings, and sampled structures support the conclusions drawn from a calculation.

Browse the public [reaction and quantum-dynamics tools]({{ '/repositories/' | relative_url }}#quantum) and
[materials tools]({{ '/repositories/' | relative_url }}#materials) for source code and documentation.
