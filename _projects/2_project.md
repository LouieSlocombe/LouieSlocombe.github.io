---
layout: research
title: Molecular complexity & assembly theory
description: What can a molecule’s construction tell us about the processes that made it?
img: assets/img/research/assembly.svg
img_alt: A sequence of three joins builds ABCABC by reusing ABC, illustrating assembly from reusable parts.
importance: 4
category: projects
research_context: Theory, algorithms, & life detection
related_publications: true
---

A molecule’s structure contains clues about the chemistry that produced it. Assembly theory approaches this by asking
how many steps are needed to build an object from elementary parts, allowing previously built fragments to be reused.

I work on the practical side of this question: algorithms for finding construction pathways, software for comparing
molecules, and connections between the calculations and experimental measurements. Much of this work is a collaboration
with the Emergence of Life group at Arizona State University.

{% include figure.liquid path="assets/img/research/assembly.svg" alt=page.img_alt caption="A simple string example: join A and B, add C, then reuse ABC to make ABCABC. Reusing an intermediate gives a three-join construction. Molecular calculations use bonds and chemical graphs instead of letters." %}

<h2 id="what-the-index-measures-and-why-it-can-be-measured-at-all">Counting construction steps</h2>

The **assembly index** is the fewest joining steps needed under a specified set of rules. It describes a possible minimal
construction, rather than reconstructing the exact reactions that happened in the past. The **copy number** describes
how many copies of that object occur in a sample.

Our perspective on measuring molecular complexity discusses how structural calculations and measurements such as mass
spectrometry, infrared spectroscopy, and nuclear magnetic resonance can help investigate molecular assembly
{% cite slocombe2024measuring %}.

<h2 id="computing-it-is-the-bottleneck">Making the calculations practical</h2>

Finding the shortest construction becomes difficult as molecules get larger. I work on search algorithms and useful
approximations that let us compare more structures. Our 2026 **Assembly Spaces** preprint develops formal definitions
and fast methods for bounding assembly indices; it remains under review {% cite siebert2026assembly %}.

A bound is useful even when the exact answer is out of reach: it tells us a range in which that answer must lie.
Keeping track of what is exact and what is an estimate is essential when comparing molecules.

## AssemblyTheoryTools

**AssemblyTheoryTools** provides a common Python interface to assembly calculators for molecules, strings, and graphs.
It also helps visualise how fragments combine and compare structures that share building blocks. I lead the associated
methods manuscript, which is under review {% cite slocombe2026assemblytheorytools %}.

Recent collaborative software includes **ParallelAssemblyCpp** for parallel searches and **assemblycfg** for fast bounds
and reusable-fragment pathways. The [assembly code catalogue]({{ '/repositories/' | relative_url }}#assembly) links to these projects.

<h2 id="measuring-it-on-spectra-instead-of-structures">Connecting structure and measurement</h2>

For an unfamiliar sample, we may have a spectrum before we know every molecular structure. I am interested in how
spectral features can be related to assembly measures, and how those estimates compare with calculations on known
molecular graphs. Such comparisons help establish what a measurement captures and where an approximation breaks down.

<span id="the-threshold"></span>

<h2 id="beyond-molecules">Looking for unfamiliar life</h2>

Assembly theory proposes that complex objects found in high abundance can provide evidence of processes that repeatedly
select particular construction pathways. Applying this idea to life detection requires checking it against biological
and non-biological chemistry, as well as the limits of the measurement.

I contribute to work exploring chemical selection in planetary atmospheres {% cite janin2025searching %}. Our 2026
**Habitable Worlds Observatory white paper** proposes how assembly measures could inform exoplanet observations
{% cite walker2026searching %}. This is a developing approach to evaluating biosignatures, rather than a reported detection of life.

<h2 id="chemical-space-to-test-against">Chemical data to test the ideas</h2>

Our **CBR-db** resource provides curated biochemical compounds and reactions for exploring chemical space
{% cite slocombe2026cbrdb %}. It supports comparisons between molecular structure, reaction networks, and complexity.

<span id="related-threads"></span>
Related work on [biochemical origins and proteins]({{ '/projects/biochemical_origins.html' | relative_url }}) asks how molecular
handedness and elemental composition connect to the organisation of life {% cite malloy2025emergence benites2026deeptime %}.

## Software

Find [AssemblyTheoryTools](https://github.com/ELIFE-ASU/assemblytheorytools),
[ParallelAssemblyCpp](https://github.com/ELIFE-ASU/parallelassemblycpp), and
[assemblycfg](https://github.com/ELIFE-ASU/assemblycfg) in the public repositories, with documentation and examples for the available methods.
