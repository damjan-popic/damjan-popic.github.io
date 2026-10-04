# Damjan Popič — osebna spletna stran / personal website

Samostojna dvojezična spletna stran. / A standalone bilingual personal website.

**Repository:** `damjan-popic/damjan-popic.github.io`  
**Website:** https://damjan-popic.github.io/  
**Slovenian:** `/sl/` · **English:** `/en/`

This repository contains only the personal website. The Playbook is a separate
project, linked from the relevant content pages, not a hosting dependency.

## Urejanje brez nameščanja / editing without installing anything

Na objavljeni strani kliknite **Uredi to stran**, spremenite besedilo v GitHubu
in kliknite **Commit changes**. Za običajno urejanje ni treba nameščati Pythona
ali uporabljati terminala. Slovensko in angleško različico urejate ločeno.

On a published page, click **Edit this page**, edit the Markdown in GitHub,
and click **Commit changes**. Commit to `main`, or merge your proposed change.
The **Publish personal website** workflow checks and publishes the update.
There is no local installation needed for everyday editing.

The Edit link does not grant visitors write access. GitHub still enforces
repository permissions. If a build fails, the previous successful deployment
remains published.

## Kje je kaj / content map

| Page | Slovenian source | English source |
| --- | --- | --- |
| Home | `content/sl/index.md` | `content/en/index.md` |
| Bio | `content/sl/o-meni.md` | `content/en/about.md` |
| Research | `content/sl/raziskovanje.md` | `content/en/research.md` |
| Projects | `content/sl/projekti.md` | `content/en/projects.md` |
| Teaching | `content/sl/poucevanje/index.md` | `content/en/teaching/index.md` |
| AGRFT | `content/sl/poucevanje/agrft.md` | `content/en/teaching/agrft.md` |
| Digital Linguistics | `content/sl/poucevanje/digitalno-jezikoslovje.md` | `content/en/teaching/digital-linguistics.md` |
| Students | `content/sl/za-studente.md` | `content/en/students.md` |
| Contact | `content/sl/kontakt.md` | `content/en/contact.md` |

The block between the first two `---` lines sets the page title, description and
section. Keep `key` unchanged: it pairs the translations. Write normal text
below the second `---` line. Use `##` for headings; the title supplies the H1.

Example:

```markdown
## 1. srečanje — Uvod

Kratek opis srečanja in navodila.

[Predstavitev](/assets/files/agrft-uvod.pdf)
```

## Gradiva / course materials

In GitHub, upload files into `assets/files/` using **Add file → Upload files**.
Link to them as in the example. The builder adjusts `/assets/` links for each
page. Upload the file before adding the link, or commit them together:
missing files fail validation. Filenames without spaces are simplest.

The website is public. Never upload grades, student lists, submitted assignments,
passwords, private correspondence, or readings you are not permitted to share.

## Nova stran / a new page

Copy a nearby Markdown file in each language. Give both copies the same new
`key`, and their own title and text. Link to them using relative Markdown links,
e.g. `[New course](new-course.md)`. Both translations are required; the switcher
then points to the corresponding page. For a new main-menu entry, add its key
and translated label in both language sections of `site.yml`.

## Lokalni predogled / local preview

Python 3.10 or newer:

```bash
python -m venv .venv
# Linux / macOS / WSL:
source .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory _site
```

Open http://localhost:8000/ . After an edit, rebuild and refresh.

```bash
python -m unittest discover -s . -p 'test_*.py'
```

The tests check translations, links, downloadable files, anchors, safe output
handling, standalone canonical addresses, and editing links. `_site/` is generated;
edit `content/`, not generated HTML.

## Nastavitve / settings

`site.yml` holds the public URL, repository, branch, source folder and interface
labels. `templates/page.html` is the shared template; `assets/style.css` is the
stylesheet. Content uses ordinary Markdown. There is no CMS, database, tracking,
external-font dependency or login requirement for readers.

Institutional sources are listed in `SOURCES.md`. The page copy is an initial
draft: check it before treating it as formal course regulations or a final CV.

## Objava in preverjanje / publication and checks

Changes committed to `main` trigger `.github/workflows/pages.yml`. It runs the
local tests, builds the website and deploys it to GitHub Pages. After deployment,
`scripts/check_live.py` checks the public HTML pages, language labels, canonical
addresses, editing links and stylesheet. It also verifies the deployed commit.

The publishing source in **Settings → Pages** must remain **GitHub Actions**.
The website is independent of the Playbook repository. Do not edit the old
`personal-site/` files there; use this repository's `content/` directory.

## GitHub documentation

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
