---
layout: page
permalink: /repositories/
title: Code
description: Software I've written and helped develop for molecular simulation, materials, and chemical complexity.
nav: true
nav_order: 4
---

{% assign catalogue = site.data.repositories %}
{% assign project_count = 0 %}
{% for group in catalogue.groups %}
{% assign project_count = project_count | plus: group.projects.size %}
{% endfor %}

<div class="code-catalogue" id="code-catalogue">
  <section class="code-intro" aria-labelledby="code-intro-title">
    <p class="code-eyebrow">Code from my research</p>
    <h2 id="code-intro-title">From a molecular question to a working calculation</h2>
    <p class="code-lead">A lot of my research involves writing software: building a polymer, following a proton through DNA, or working out how a complex molecule could be assembled. Here are the tools I've written and the collaborative projects I've helped develop along the way.</p>
    <p>I've grouped them by the problems they tackle, with the most substantial work first in each section. Alongside research packages, you'll find code from individual papers, everyday simulation helpers, and a few experiments. Each entry links to the source, with documentation and papers where available.</p>
    <div class="code-intro-links">
      <a class="code-github-link" href="https://github.com/{{ catalogue.github_user }}"><i class="fa-brands fa-github" aria-hidden="true"></i> Explore my GitHub <span aria-hidden="true">↗</span></a>
      <span>{{ project_count }} repositories · {{ catalogue.groups.size }} themes</span>
    </div>
  </section>

  <nav class="code-starts" aria-label="Suggested starting points">
    <a href="#materials"><span class="code-eyebrow">Build & measure</span><strong>From monomers to materials</strong><span>Polymer simulations, amorphous structures, and material properties <span aria-hidden="true">→</span></span></a>
    <a href="#quantum"><span class="code-eyebrow">Simulate & understand</span><strong>Beyond classical nuclei</strong><span>Reaction pathways, tunnelling, and quantum molecular dynamics <span aria-hidden="true">→</span></span></a>
    <a href="#assembly"><span class="code-eyebrow">Count & discover</span><strong>The structure of complexity</strong><span>Assembly pathways, reusable fragments, and biochemical networks <span aria-hidden="true">→</span></span></a>
  </nav>

  <div class="code-explore" id="explore-code">
    <h2>Explore the collection</h2>
    <nav class="code-topics" aria-label="Repository themes">
      {% for group in catalogue.groups %}
        <a href="#{{ group.id }}">{{ group.title | escape }} <span>{{ group.projects.size }}</span></a>
      {% endfor %}
    </nav>
    <div class="code-search" hidden>
      <label for="code-search-input">Find a repository</label>
      <div class="code-search-field">
        <input id="code-search-input" type="search" placeholder="Try DNA, OpenMM, Julia, or a project name…" aria-describedby="code-search-status" autocomplete="off">
        <button type="button" id="code-search-clear">Clear</button>
      </div>
      <p id="code-search-status" class="code-search-status" role="status" aria-live="polite" aria-atomic="true">Showing all {{ project_count }} repositories.</p>
    </div>
  </div>

  <div class="code-groups">
    {% for group in catalogue.groups %}
      <section class="code-group" id="{{ group.id }}" aria-labelledby="{{ group.id }}-title">
        <header class="code-group-header">
          <p class="code-eyebrow">{{ forloop.index | prepend: '0' }} / {{ group.question | escape }}</p>
          <h2 id="{{ group.id }}-title">{{ group.title | escape }} <span class="code-group-count">{{ group.projects.size }}</span></h2>
          <p>{{ group.description | escape }}</p>
        </header>
        <div class="code-projects">
          {% for project in group.projects %}
            {% assign project_id = project.repo | slugify %}
            <article class="code-project" aria-labelledby="{{ project_id }}" data-search="{{ group.title | escape }} {{ project.repo | escape }} {{ project.name | escape }} {{ project.summary | escape }} {{ project.language | escape }} {{ project.kind | escape }} {{ project.tags | join: ' ' | escape }}">
              <p class="code-project-kind">{{ project.kind | escape }} <span aria-hidden="true">·</span> {{ project.language | escape }}</p>
              <h3 id="{{ project_id }}"><a href="https://github.com/{{ project.repo }}">{{ project.name | escape }} <span aria-hidden="true">↗</span></a></h3>
              <p class="code-repo-name">{{ project.repo | escape }}</p>
              <p class="code-project-summary">{{ project.summary | escape }}</p>
              <ul class="code-tags" aria-label="Topics">
                {% for tag in project.tags %}<li>{{ tag | escape }}</li>{% endfor %}
              </ul>
              <div class="code-project-links">
                <a href="https://github.com/{{ project.repo }}" aria-label="View {{ project.name | escape }} on GitHub">GitHub <span aria-hidden="true">↗</span></a>
                {% if project.docs %}<a href="{{ project.docs }}" aria-label="Documentation for {{ project.name | escape }}">Docs <span aria-hidden="true">↗</span></a>{% endif %}
                {% if project.paper %}<a href="{{ project.paper }}" aria-label="Paper for {{ project.name | escape }}">Paper <span aria-hidden="true">↗</span></a>{% endif %}
              </div>
            </article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}
    <p class="code-empty" hidden>No repositories match your search. Try a broader topic, or use Clear to see the full collection.</p>
  </div>

  <div class="code-footer">
    <h2>The science behind the software</h2>
    <p>My <a href="{{ '/projects/' | relative_url }}">research pages</a> explain the questions behind much of this code, and the <a href="{{ '/publications/' | relative_url }}">papers</a> give the full details. If you'd like to use a package, start with its README for installation, examples, and citation guidance.</p>
    <p class="code-review-note">Last reviewed {{ catalogue.reviewed }}. I've included original work and substantial collaborations, and labelled templates and experiments so you know what to expect.</p>
  </div>
</div>

<script src="{{ '/assets/js/repositories.js' | relative_url }}" defer></script>
