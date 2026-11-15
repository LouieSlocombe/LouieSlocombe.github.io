---
layout: research
title: Sustainable polymers
description: How can we connect a polymer’s chemistry to its useful properties and its fate after use?
img: assets/img/research/polymers.svg
img_alt: A polymer chain, a collection of packed chains, and smaller fragments, linking molecular structure to material behaviour and breakdown.
importance: 1
category: projects
research_context: Current focus · Birmingham
---

Polymers are long molecules made from repeating units. Their chemistry and the way their chains pack together influence
how a material stretches, softens, and interacts with water. I am interested in how we can use that molecular picture
to design materials with useful properties and better options at the end of their life.

At Birmingham, I am developing **databases, machine-learning methods, and molecular simulations** to study polymer
properties and biodegradability. This is ongoing research: the aim is to connect evidence from experiments with models
that can help guide which materials to investigate next.

{% include figure.liquid path="assets/img/research/polymers.svg" alt=page.img_alt caption="Three connected questions: what is the chain made of, how do chains behave together, and how can they break down? This is a schematic, not a prediction of biodegradability." %}

## Learning from the evidence

Useful predictions need useful data. Published measurements are spread across articles, tables, and figures, often
with different experimental conditions. I build tools to bring those records together while retaining the information
needed to interpret them.

My recent work includes **PaperMinerToolkit**, developed with the Scanlon Materials Theory Group, for collecting papers
and extracting structured information using text and vision models. **figrecover** recovers numerical data from plotted
curves. These tools help with data collection; checking the extracted values, units, and experimental context remains
part of the research.

## Following chains in a simulation

I develop **openmmpolymer** to build, pack, and simulate polymer melts and blends. It connects a description of a repeating
unit to calculations of structure, mechanical behaviour, and the glass transition, where a material changes between
glassy and more mobile behaviour.

Alongside this, I am exploring how molecular structure, water access, and reaction pathways influence polymer breakdown,
including routes relevant to chemical recycling. Biodegradation and chemical recycling involve different processes;
understanding both helps us ask more precise questions about a material’s fate.

## Connecting models to experiments

A simulation follows a model over a limited time, and a machine-learning prediction depends on the examples it has
seen. I therefore work on checking sampling, comparing calculations with measurements, and assessing where predictions
are reliable. My wider [simulation-methods work]({{ '/projects/molecular_simulation.html' | relative_url }}) supports this effort.

The public tools are [openmmpolymer](https://github.com/LouieSlocombe/openmmpolymer),
[PaperMinerToolkit](https://github.com/SMTG-Bham/PaperMinerToolkit), and
[figrecover](https://github.com/SMTG-Bham/figrecover). The
[code catalogue]({{ '/repositories/' | relative_url }}#materials) gives more detail on their scope.
