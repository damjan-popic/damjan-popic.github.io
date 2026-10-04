# Damjan Popič — osebna spletna stran / personal website

Samostojna dvojezična spletna stran. / A standalone bilingual personal website.

**Repository:** `damjan-popic/damjan-popic.github.io`  
**Address after deployment:** https://damjan-popic.github.io/  
**Slovenian:** `/sl/` · **English:** `/en/`

This repository contains only the personal website. The Playbook is a separate
project, linked from the relevant content pages, not a hosting dependency.

## Prva objava / first publication

The files in this package are ready to publish, but the package itself does not
create the repository or enable Pages.

1. Create a **public** repository named exactly `damjan-popic.github.io` under
   `damjan-popic`. Turn **Add README** on so the `main` branch exists.
2. In **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**.
   No template needs to be selected: this package already includes the workflow.
3. Commit this package's files at the repository root, including the hidden
   `.github/workflows/pages.yml` file. The workflow builds and publishes the site.
4. Check that **Actions → Publish personal website** completes successfully and
   open both language versions before replacing any old links.

The GitHub connection used to upload files must have access to this repository.
Do not rename, delete or repurpose the Playbook repository to publish this site.

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

## Moving from the old address

Keep the old public copy unchanged until the standalone site is confirmed live.
Then remove the three personal-site-specific steps from the Playbook workflow
and replace the old `/damjan/` pages with links or redirects to their matching
new pages. Do not redirect the Playbook homepage or change its Pages settings.
Keep a source backup before removing the old `personal-site/` directory.

## GitHub documentation

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
