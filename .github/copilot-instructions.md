# Copilot Instructions

## Workspace & Project Context

- **Repository root**: `C:\Users\afour\Documents\thèse\website\afm215.github.io` (GitHub Pages personal academic website built on the Academic Pages v0.9.x / Minimal Mistakes Jekyll template).
- **Source materials for site content** (from `../instructions.md`):
  - Resume / CV: `C:\Users\afour\Documents\thèse\CV2027`
  - Thesis manuscript & associated paper: `C:\Users\afour\Documents\thèse\ThesisManuscript\thesis_ressources`
- **Local toolchains**:
  - **Python**: Use and update the `uv` virtual environment at `C:\Users\afour\Documents\code_projects\demographic\.venv`.
  - **Node.js**: Managed via `nvm`.
- **Template policy** (from `AGENTS.md`): All customizations belong in this personal repository (`afm215.github.io`). Never create pull requests back to `academicpages/academicpages.github.io`.
- **Strict local-folder confinement**: When configuring or running preview servers, MCP servers, or build/dependency artifacts (e.g., `vendor/bundle`, `_site`, `.jekyll-cache`, `.playwright-mcp`), work exclusively within the local workspace folder (`C:\Users\afour\Documents\thèse\website`) and never read or write user-global config directories.

## Build, Serve, and Asset Commands

Run all commands below from `afm215.github.io/`:

- **Install Ruby dependencies locally**:
  ```bash
  bundle config set --local path 'vendor/bundle'
  bundle install
  ```
- **Serve locally with live reload** (serves at `http://localhost:4000`; restart required after editing `_config.yml`):
  ```bash
  bundle exec jekyll serve -l -H localhost
  ```
- **Production build & front-matter validation** (matches CI in `.github/workflows/jekyll-build.yml`):
  ```bash
  JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
  ```
- **Docker / DevContainer preview** (uses `_config_docker.yml` to override `url: ""`):
  ```bash
  docker compose up
  ```
- **Rebuild minified JavaScript bundle**:
  ```bash
  npm install
  npm run build:js   # or `npm run watch:js`
  ```
- **Python content & asset generators** (run using `C:\Users\afour\Documents\code_projects\demographic\.venv\Scripts\python.exe`):
  - From `afm215.github.io/markdown_generator/` (must be run from this directory because outputs write to `../_publications/` and `../_talks/`):
    ```bash
    python publications.py publications.tsv
    python pubsFromBib.py
    python talks.py talks.tsv
    ```
  - From `afm215.github.io/`:
    ```bash
    python talkmap.py                # Geocodes `location` in `_talks/*.md` into `talkmap/`
    python scripts/make-og-image.py  # Generates `images/og-image.png` from `images/favicon-512x512.png`
    ```

## High-Level Architecture

- **Configuration & Navigation**:
  - `_config.yml` defines site metadata (`url`, `repository`, `site_theme`), the left-sidebar author profile (`author`), `publication_category` definitions, and default front-matter scopes.
  - `_data/navigation.yml` controls the top masthead links. Removing an entry hides it from the header without disabling the underlying page.
- **Collections & Single-Source Content Flow**:
  - Content items live in `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`, and `_posts/`.
  - A single Markdown file's YAML front matter drives multiple views across the site:
    1. Individual item pages rendered via `_layouts/single.html` or `_layouts/talk.html`.
    2. Collection index pages in `_pages/` (`publications.html`, `talks.html`, `teaching.html`, `portfolio.html`) using `_includes/archive-single.html` or `_includes/archive-single-talk.html`.
    3. Dynamic sections in `_pages/cv.md` rendered via `_includes/archive-single-cv.html` and `_includes/archive-single-talk-cv.html`.
- **Styling & Theme System**:
  - `assets/css/main.scss` imports SCSS partials from `_sass/`, loading both `theme/<site_theme>_light` and `theme/<site_theme>_dark`.
  - Dark mode is toggled client-side (`assets/js/_main.js`) by setting `data-theme="dark"` on the `<html>` element and persisting the choice in `localStorage`.

## Key Conventions

- **JavaScript bundling is manual**: `_includes/scripts.html` only loads `assets/js/main.min.js`, and `_config.yml` excludes `assets/js/_main.js` and `assets/js/plugins` from the Jekyll build. Any edits to `assets/js/_main.js`, `assets/js/theme.js`, or `assets/js/plugins/jquery.greedy-navigation.js` require running `npm run build:js` and committing the updated `assets/js/main.min.js`.
- **Publication `category` filtering**: `_pages/publications.html` iterates over the keys defined under `publication_category` in `_config.yml` (`books`, `manuscripts`, `conferences` by default) and skips any item in `_publications/` whose `category` front-matter value does not match one of those keys.
- **Static downloadable files vs. images**: Place downloadable PDFs, slides, and `.bib` files in `files/` and reference them in publication/talk front matter via `paperurl`, `slidesurl`, and `bibtexurl`. Place site images and social preview teasers in `images/`.
- **URL construction**: Templates prepend `{{ base_path }}` (resolved in `_includes/base_path` from `site.url` + `site.baseurl`) to internal links and image paths. Keep internal permalinks root-relative (e.g., `/publication/YYYY-MM-DD-slug`).
- **MathJax, Mermaid, and Plotly in Markdown**:
  - Kramdown (`GFM` input) is used for Markdown parsing.
  - **MathJax v4**: In Markdown bodies, write math as `$$...$$` (inline when inside a sentence, display when on its own paragraph). Kramdown shields `$$...$$` from Markdown parsing and emits `\(...\)` / `\[...\]` for MathJax. Avoid single `$...$`: although `_includes/footer/custom.html` enables it in MathJax, kramdown parses its contents first, so `_` in subscripts (e.g. `\text{C}_{ge}$ and $\text{C}_{all}`) becomes `<em>` and breaks the formula. Inside YAML `citation` strings, use `\(...\)`.
  - **Mermaid v11 & Plotly v3.6.0**: Lazy-loaded from CDN by `assets/js/_main.js` only when ```` ```mermaid ```` or ```` ```plotly ```` blocks are present on the page. Plotly code blocks must contain strictly valid JSON (all keys double-quoted) and automatically inherit `plotlyLightLayout` / `plotlyDarkLayout` from `assets/js/theme.js`.
- **YAML escaping in generators**: When generating collection Markdown files (`markdown_generator/`), escape `&`, `"`, and `'` as `&amp;`, `&quot;`, and `&apos;` inside single-quoted YAML fields (`excerpt`, `venue`, `citation`) so Jekyll front-matter parsing does not fail.
