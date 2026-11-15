---
layout: page
title: Research
permalink: /projects/
description: Understanding molecules, from the materials we make to the chemistry of life.
nav: true
nav_order: 3
display_categories: [projects]
---

<div class="research-page" markdown="1">

I use molecular simulation, quantum physics, and machine learning to connect the behaviour of atoms to larger questions:
how can we design more sustainable polymers, what makes biological chemistry distinctive, and when do quantum effects
change a reaction?

My current focus at the University of Birmingham is **polymer properties and biodegradability**. This builds on my work
on chemical complexity and the origins of biochemistry at Arizona State University, and quantum biology at Surrey.
Developing useful research software and reliable datasets runs through all three.

<div class="research-links">
  <a href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">→</span></a>
  <a href="{{ '/repositories/' | relative_url }}">Research code <span aria-hidden="true">→</span></a>
  <a href="{{ '/cv/' | relative_url }}">Academic background <span aria-hidden="true">→</span></a>
</div>

<h2 id="projects" class="research-heading">Explore the research</h2>

<div class="projects">
  {% assign sorted_projects = site.projects | where: "category", "projects" | sort: "importance" %}
  <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>

</div>
