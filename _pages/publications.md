---
layout: page
permalink: /publications/
title: Publications
description: Research in quantum biology, molecular simulation, chemical complexity, and machine learning.
nav: true
nav_order: 2
---

These papers follow my work from quantum effects in DNA to chemical complexity and the origins of biochemistry.
They include journal articles, conference contributions, and work still in progress, with preprints and manuscripts
listed separately below. You can search by title, author, or topic.

For the story behind the papers, visit my [research pages]({{ '/projects/' | relative_url }}).
Citation information is on [Google Scholar](https://scholar.google.com/citations?user=JISRQewAAAAJ),
and my [CV]({{ '/cv/' | relative_url }}) brings together the rest of my academic work.

{% include bib_search.liquid %}

<div class="publications">
  <section class="publication-group">
    <h2>Journal articles &amp; accepted papers</h2>
    {% bibliography --query @*[cv_group=published] %}
  </section>

  <section class="publication-group">
    <h2>Conference contributions</h2>
    {% bibliography --query @*[cv_group=conference] %}
  </section>

  <section class="publication-group">
    <h2>Preprints &amp; manuscripts</h2>
    {% bibliography --query @*[cv_group=preprint] %}
  </section>
</div>
