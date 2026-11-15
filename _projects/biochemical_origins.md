---
layout: research
title: Biochemical origins & proteins
description: What patterns connect life’s reaction networks, molecular building blocks, and proteins?
img: assets/img/research/biochemistry.svg
img_alt: A branching reaction network beside an amino-acid chain folding into a compact shape.
importance: 3
category: projects
research_context: Collaborative research · Arizona State
related_publications: true
---

Life uses a small part of the chemistry that is possible. With collaborators in Sara Walker’s group at Arizona State
University, I study patterns in that chemistry: which molecules participate in metabolism, how their reactions connect,
and what constraints appear across very different organisms.

My contribution combines chemical data curation, molecular modelling, and software for exploring large collections of
molecules and proteins.

{% include figure.liquid path="assets/img/research/biochemistry.svg" alt=page.img_alt caption="From networks of chemical reactions to the building blocks and shapes of proteins. The network and folded chain are illustrations, not a particular pathway or predicted structure." %}

## A database for biochemical reactions

Before comparing reaction networks, we need chemical records that a computer can interpret consistently. I led the
**CBR-db** paper, published in 2026, with collaborators who helped build a curated resource of biochemical compounds and
reactions {% cite slocombe2026cbrdb %}.

CBR-db brings together information from KEGG and the ATLAS of Biochemistry, repairs problematic molecular and reaction
representations, and adds properties for analysis. This provides a foundation for studying metabolism, possible routes
to early biochemistry, and [molecular complexity]({{ '/projects/2_project.html' | relative_url }}).

## Why does biological chemistry have a handedness?

Some molecules come in mirror-image forms, like left and right hands. This property is called **chirality**, and it
matters because biological molecules can interact differently with each form.

In a collaboration on the emergence of chirality from metabolism, we investigate how expanding reaction networks can
favour particular patterns of chiral molecules. The study connects molecular handedness to the organisation of
metabolism, offering hypotheses about how chemical selection developed during life’s origins. The paper is accepted
at _Nature Communications_ {% cite malloy2025emergence %}.

## What stays consistent across proteins?

A **proteome** is an organism’s collection of proteins. Our 2026 preprint compares their elemental composition across
cellular and viral life. Despite enormous differences in sequences and proteome sizes, we find a surprisingly narrow
range of elemental compositions {% cite benites2026deeptime %}.

We also examine reconstructed ancestral proteomes and simplified amino-acid alphabets to explore where this pattern
may come from. Predicted protein structures help us investigate how changes in the available building blocks could
affect folding. This work remains a preprint under review.

For these kinds of studies, I develop workflows around ESMFold, a model that predicts protein structure from an
amino-acid sequence, including preparation for molecular simulation and execution on different computing accelerators.
These are computational predictions, whose confidence and assumptions need to be assessed.

## Data and software

The public [CBR-db repository](https://github.com/ELIFE-ASU/CBRdb) provides the biochemical resource. My
[protein tools and examples]({{ '/repositories/' | relative_url }}#proteins-data) support structure prediction and preparation.
