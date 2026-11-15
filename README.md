# LouieSlocombe.github.io

Source for [louieslocombe.github.io](https://louieslocombe.github.io), my personal academic website — publications, projects, and news.

Built with [Jekyll](https://jekyllrb.com/) on the [al-folio](https://github.com/alshedivat/al-folio) theme, deployed via GitHub Pages/Actions.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

The site is then served at `http://localhost:4000`.

## Structure

- `_pages/` — static pages (about, CV, projects, publications, …)
- `_news/` — homepage announcements
- `_projects/` — project pages
- `_bibliography/` — publication list (`papers.bib`)
- `_data/` — CV and citation data
- `assets/` — images, CSS, and other static assets

## Updating the CV

- `assets/json/resume.json` holds the profile, appointments, education, skills, funding, teaching, service, presentations and awards. Use `YYYY-MM` for appointment dates, `YYYY` for education dates, and an empty `endDate` for a current role.
- `_data/cv_sections.yml` controls the CV section titles, navigation and order. `_layouts/cv.liquid` and `_includes/cv/` render the CV; `_sass/_cv.scss` contains the responsive and print styles.
- `_bibliography/papers.bib` supplies both the CV and publications page. Set `cv_group` to `published`, `conference` or `preprint`; retain acceptance and review statuses in `note`.
- The teaching page reuses the teaching entries in `resume.json` so the two pages stay in sync.
- The CV is presented as web content only. Do not add a downloadable CV PDF or PDF download links.

## License

Site content is mine; the underlying theme is [al-folio](https://github.com/alshedivat/al-folio), MIT licensed (see [LICENSE](LICENSE)).
