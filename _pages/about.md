---
layout: about
title: About
permalink: /
subtitle: Computational physicist & theoretical chemist
introduction: |
  I study how molecules behave, from the quantum motion of a proton to the properties of a material.
  **My current focus is sustainable polymers:** connecting their chemistry to how they perform and how they break down.

  I’m a **Group Leader Research Fellow** in the Scanlon Materials Theory Group at the **University of Birmingham**,
  working with David Scanlon. I combine molecular simulation, machine learning, and chemical data to investigate
  these questions.
intro_links:
  - title: Explore my current research
    url: /projects/sustainable_polymers.html
    primary: true
  - title: Publications
    url: /publications/
  - title: Research code
    url: /repositories/

profile:
  image: prof_pic.jpg
  image_circular: false
  alt: Louie Slocombe in front of a chalkboard of molecular assembly calculations.
  more_info: >
    <p>Scanlon Materials Theory Group</p>
    <p>School of Chemistry</p>
    <p>University of Birmingham</p>

selected_papers: false # enable after choosing papers with "selected={true}" in the bibliography
social: true

announcements:
  enabled: true
  scrollable: false
  limit: 3
---

<section class="about-focus" aria-labelledby="current-research" markdown="1">

<p class="about-eyebrow">Current research · Birmingham · Since June 2026</p>
<h2 id="current-research">How can we make useful polymers with a better end of life?</h2>

<div class="about-focus-intro" markdown="1">

Polymers are long molecules whose chemistry and arrangement determine how a material behaves. I’m developing ways to
connect that molecular picture to **material properties and biodegradability**, bringing together experimental evidence,
computer simulations, and machine learning. The aim is to help guide the design of more sustainable materials.

{% include figure.liquid path="assets/img/research/polymers.svg" alt="A polymer’s repeat units, many chains packed into a material, and smaller fragments after breakdown." caption="From molecular structure to material behaviour and breakdown: the questions connecting my current work. Schematic only." %}

</div>

<div class="about-approaches" markdown="1">

<div markdown="1">

### Learn from experiments

I develop tools to collect information from papers and recover data from published plots, building datasets that
retain the conditions behind each measurement.

</div>
<div markdown="1">

### Follow molecules in motion

I build and simulate polymer structures to explore how their chains pack, respond to forces, and interact with water.
Reaction calculations help investigate routes to breakdown and chemical recycling.

</div>
<div markdown="1">

### Connect data to predictions

I develop machine-learning methods for polymer properties and biodegradability, with an emphasis on testing predictions
and understanding where a model can be trusted.

</div>
</div>

<div class="about-links">
  <a href="{{ '/projects/sustainable_polymers.html' | relative_url }}">Inside the polymer research <span aria-hidden="true">→</span></a>
  <a href="{{ '/projects/molecular_simulation.html' | relative_url }}">The simulation methods <span aria-hidden="true">→</span></a>
</div>

</section>

<section class="about-background" aria-labelledby="research-background" markdown="1">

## Research background

My research has moved between physics, chemistry, and biology. Across these fields, I use molecular models and data to
ask how small-scale interactions shape larger patterns: an error in DNA copying, the organisation of biochemistry, or
the behaviour of a material.

<div class="about-history">
<div class="about-history-entry" markdown="1">

<p class="about-period">2024–2026<br>Arizona State University</p>
<div markdown="1">

### Exploring the chemistry of life

In Sara Walker’s group at the Beyond Center, I investigated what makes biological chemistry distinctive. I combined
machine learning, chemical complexity, and graph theory to explore molecular construction, biochemical reaction networks,
and protein folding.

I led the **CBR-db** paper, developing a curated biochemical reaction resource with collaborators, and worked on
**AssemblyTheoryTools** and algorithms that examine how complex molecules can be built from reusable parts. Other
collaborations explored the emergence of molecular handedness in metabolism and the striking consistency of elemental
composition across proteins from cellular and viral life. The protein-composition work remains a preprint under review.

Alongside research, I was a Research Lab Manager and Postdoctoral Researcher: I supported the group’s day-to-day work,
trained and mentored researchers, and contributed substantially to a successful **$1.5 million NASA ROSES grant proposal**.

[Biochemical origins and proteins]({{ '/projects/biochemical_origins.html' | relative_url }}) ·
[Molecular complexity and assembly theory]({{ '/projects/2_project.html' | relative_url }})

</div>
</div>
<div class="about-history-entry" markdown="1">

<p class="about-period">2018–2024<br>University of Surrey</p>
<div markdown="1">

### Following quantum effects through DNA

My PhD in Quantum Biology, completed in 2022 with Marco Sacchi and Jim Al-Khalili, asked whether the motion of a proton
could change how accurately DNA is copied. In _Quantum Effects in DNA Replication Fidelity_, I studied proton transfer
and quantum tunnelling, including how the surrounding molecular environment affects these processes.

I continued as a Research Fellow in Theoretical Quantum Biology, connecting quantum calculations with simulations of
DNA, water, and enzymes. Our work showed why the proteins that separate and copy DNA matter to the explanation:
they change the conditions in which unusual base-pair arrangements form and survive.

These questions also took me beyond DNA, into ion-channel transport, DNA damage, and surface chemistry. They continue
to inform the multiscale simulation and quantum-dynamics tools I develop today.

[Proton transfer in DNA]({{ '/projects/1_project.html' | relative_url }}) ·
[Surfaces and energy materials]({{ '/projects/surfaces_materials.html' | relative_url }})

</div>
</div>
<div class="about-history-entry" markdown="1">

<p class="about-period">Earlier work<br>Physics & engineering</p>
<div markdown="1">

### Keeping a connection to experiments

My route into computational research began with a physics degree at Surrey and research at the University of Wollongong
on terahertz spectroscopy, imaging, and detector electronics. I also worked in biomedical research and development on
atmospheric plasma technology for wound care. That experience of building instruments, extracting signals, and testing
models against measurements still shapes how I approach a computational problem.

</div>
</div>
</div>

<div class="about-links">
  <a href="{{ '/projects/' | relative_url }}">Explore all six research themes <span aria-hidden="true">→</span></a>
  <a href="{{ '/cv/' | relative_url }}">Full academic CV <span aria-hidden="true">→</span></a>
</div>

</section>

<section class="about-community" aria-labelledby="teaching--scientific-community" markdown="1">

## Teaching & scientific community

I care about making computational research easier to learn and reproduce. I have managed or supervised **28 scientists**,
taught scientific computing and computational chemistry, and helped develop teaching on generative AI. At Birmingham,
I have led and mentored students applying machine learning to the biodegradability of short polymers through the
Reckitt Challenge.

Bringing researchers together is another part of that work. As co-chair of the 2025 Quantum Biology Gordon Research
Symposium, I raised **$22,000** to support attendance by underrepresented and minority early-career researchers.

[Teaching and mentoring]({{ '/teaching/' | relative_url }}) · [Academic service]({{ '/cv/#service' | relative_url }})

</section>
