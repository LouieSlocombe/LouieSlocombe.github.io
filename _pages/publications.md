---
layout: page
permalink: /publications/
title: Publications
description: Research in quantum biology, molecular simulation, chemical complexity, and machine learning.
nav: true
nav_order: 2
---

Journal articles, conference contributions, preprints, and manuscripts. See my
[Google Scholar profile](https://scholar.google.com/citations?user=JISRQewAAAAJ)
for citation information and my [CV]({{ '/cv/' | relative_url }}) for the wider research record.

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
