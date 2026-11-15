# Research illustrations

These six conceptual diagrams introduce the research themes. They contain no measured data, molecular coordinates, or quantitative predictions.

The editable originals are the `.vectorcraft` files in this directory. The website uses their SVG exports in `assets/img/research/`.

To regenerate all six with the installed VectorCraft CLI:

```bash
python3 _figure_sources/research/generate.py
```

The script uses VectorCraft's headless command API, runs without plug-ins, and requires Liberation Sans. It overwrites both the native documents and the SVG exports. Edit the script for reproducible changes, or edit a native document in VectorCraft and export its corresponding SVG when working manually.

Keep labels large enough to read on the research cards. The Markdown pages provide figure captions and alternative text. The fixed pale background keeps the same illustration legible in both site themes.
