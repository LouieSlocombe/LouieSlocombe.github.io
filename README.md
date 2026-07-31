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

## License

Site content is mine; the underlying theme is [al-folio](https://github.com/alshedivat/al-folio), MIT licensed (see [LICENSE](LICENSE)).
