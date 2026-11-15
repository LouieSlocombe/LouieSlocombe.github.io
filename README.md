# LouieSlocombe.github.io

Source for [louieslocombe.github.io](https://louieslocombe.github.io), my personal academic website — publications, projects, and news.

Built with [Jekyll](https://jekyllrb.com/) on the [al-folio](https://github.com/alshedivat/al-folio) theme, deployed via GitHub Pages/Actions.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

The site is then served at `http://localhost:4000`.

Deploy through `.github/workflows/deploy.yml`, which builds the source with Jekyll, purges unused CSS, and publishes to GitHub Pages. Generated files in `_site/` should not be edited or committed.

Site builds need Ruby, Node.js, and ImageMagick. Python dependencies in `requirements.txt` are only for `bin/update_scholar_citations.py` and its scheduled workflow.

## Structure

- `_pages/` — static pages (about, CV, projects, publications, …)
- `_news/` — homepage announcements
- `_projects/` — project pages
- `_bibliography/` — publication list (`papers.bib`)
- `_data/` — CV and citation data
- `assets/` — images, CSS, and other static assets

Keep this repository focused on the academic site. Theme demonstration pages, sample media, superseded CV and repository-card templates, and upstream theme release workflows have been removed. Retain dated research, publications, and news as part of the academic record. The homepage's selected-publications section is disabled until papers are explicitly marked `selected={true}` in the bibliography.

Unused blog archives, Distill posts, RSS feeds, embedded notebooks, tabs, comments, and newsletter integrations have also been removed, together with their build dependencies. Research cards use Bootstrap's grid without Masonry. Citation counts come from `_data/citations.yml`; the old build-time Google Scholar scraper has been removed.

## Updating the research pages

The homepage biography is in `_pages/about.md`: front matter supplies the introduction, prominent links, and portrait; the Markdown contains current research, the expanded background, and community work. `_layouts/about.liquid` arranges these with news and profile links, and `_sass/_about.scss` scopes the responsive styles. The homepage shows the three most recent announcements and links to the complete news page.

The research overview at `/projects/` displays six themes from `_projects/`, ordered by `importance`. It leads with current polymer research and links to accessible accounts of the methods and collaborations behind it. Keep existing project URLs and section anchors stable.

`_layouts/research.liquid` wraps the individual pages; `_includes/projects.liquid` renders the overview cards, and `_sass/_research.scss` scopes their styles. Each theme includes `research_context` and useful `img_alt` text alongside the usual card metadata. Citations reuse `_bibliography/papers.bib`; distinguish published results, accepted work, preprints, and ongoing projects in the prose.

Illustrations are conceptual schematics. Editable VectorCraft files and their regeneration script live in `_figure_sources/research/`; the website uses SVG exports in `assets/img/research/`. See the source directory's README for editing instructions. Only name and link public research repositories; describe work in private repositories at the level of broad research themes.

## Updating the CV

- `assets/json/resume.json` holds the profile, appointments, education, skills, funding, teaching, service, presentations, and awards. Use `YYYY-MM` for appointment dates, `YYYY` for education dates, and an empty `endDate` for a current role.
- `_data/cv_sections.yml` controls the CV section titles, navigation, and order. `_layouts/cv.liquid` and `_includes/cv/` render the CV; `_sass/_cv.scss` contains the responsive and print styles.
- `_bibliography/papers.bib` supplies both the CV and publications page. Set `cv_group` to `published`, `conference`, or `preprint`; retain acceptance and review statuses in `note`.
- The teaching page reuses the teaching entries in `resume.json` so the two pages stay in sync.
- The CV is presented as web content only. Do not add a downloadable CV PDF or PDF download links.

## Updating the code catalogue

The `/repositories/` page is built from `_data/repositories.yml`. Each group has a stable anchor `id`, a title, introductory copy, and a `projects` list. Each project has a GitHub `owner/repo`, display name, kind, language, short summary, and topic tags; optional `docs` and `paper` fields add related links. List each repository once and label collaborative work, templates, and experiments explicitly. Check the README and source before describing functionality, especially for repositories that still contain starter code.

**Selection rule: do not include forks or very small contributions.** This is a curated portfolio of original work and substantial collaborations, not a complete GitHub inventory. Exclude personal and group forks, copied upstream utilities, and projects where Louie's involvement is limited to small fixes, packaging, or publishing. A repository appearing in GitHub's ownership or contribution history does not establish a substantial role. Keep the deliberately excluded repositories listed in the comments at the top of `_data/repositories.yml` out of future refreshes unless Louie explicitly changes this preference.

**Ordering rule: highest impact and most substantial contributions first within each category.** The order of each `projects` list is the display order, including during search. Maintain a rough editorial balance of scientific significance, Louie's original development and research role, usefulness to other work, and project maturity. For paper companions, consider the accompanying research and the value of its reproducibility materials. Put broadly useful, substantial projects ahead of narrow helpers, examples, scaffolds, and profile repositories. This is a qualitative judgement, not a measured impact score; do not automatically replace it with alphabetical, newest-first, star-count, or commit-count ordering.

`_pages/repositories.md` renders all entries as static HTML, with optional browser-side search in `assets/js/repositories.js`. Styling lives in `_sass/_repositories.scss` and follows the site's light and dark themes. Update the review month after checking the catalogue against GitHub.

## Licence

Site content is mine; the underlying theme is [al-folio](https://github.com/alshedivat/al-folio), MIT licensed (see [LICENSE](LICENSE)).
