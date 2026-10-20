"""Assemble the reviewed AGRFT edition using verified existing blocks and additions."""
from pathlib import Path
import base64, hashlib, json, lzma, re, subprocess, zipfile, os

ROOT = Path.cwd()
WORK = ROOT / '.agrft-publish'
sha = lambda data: hashlib.sha256(data).hexdigest()
encoded = ''.join((WORK / f'part{i}.txt').read_text(encoding='utf-8').strip() for i in range(6))
assert sha(encoded.encode()) == '774f60167125f43dcde9397b4ad9ffd9cf5b2fe3490b3b0d66629c0c4dcd7e98', 'Transport checksum failed'
recipe = json.loads(lzma.decompress(base64.b64decode(encoded)))

def normalise(text):
    text = text.replace('https://damjan-popic.github.io/assets/images/agrft/v2/', '/assets/images/agrft/v1/')
    text = text.replace('https://damjan-popic.github.io/assets/images/agrft/v1/', '/assets/images/agrft/v1/')
    text = text.replace('/assets/images/agrft/v2/', '/assets/images/agrft/v1/')
    text = text.replace('schematics/', '/assets/images/agrft/v1/')
    return text

bases = []
for refpath in (
    '3b72bdd10e90bd226223454ba075ebec31aaedc3:assets/files/AGRFT_English_ucno_gradivo_v2.0.md',
    '3b72bdd10e90bd226223454ba075ebec31aaedc3:content/en/teaching/agrft.md',
    'b48ab3170988f8d28421ba1b4579f8d4454473bd:content/en/teaching/agrft.md',
):
    result = subprocess.run(['git', 'show', refpath], capture_output=True, check=False)
    if result.returncode == 0:
        bases.append(normalise(result.stdout.decode('utf-8')))
if os.environ.get('AGRFT_LOCAL_BASE'):
    bases.append(normalise(Path(os.environ['AGRFT_LOCAL_BASE']).read_text(encoding='utf-8')))
assert bases, 'No verified source available'
parts = []
for number, op in enumerate(recipe['ops']):
    if isinstance(op, str):
        parts.append(op)
        continue
    found = None
    for base in bases:
        for match in re.finditer(re.escape(op['p']), base):
            candidate = base[match.start():match.start() + op['n']]
            if sha(candidate.encode('utf-8')) == op['h']:
                found = candidate
                break
        if found is not None:
            break
    if found is None:
        raise ValueError(f'No exact source match for block {number}: {op["p"]!r}, length {op["n"]}')
    parts.append(found)
source = ''.join(parts)
assert sha(source.encode('utf-8')) == recipe['sha256'] == '8be4af956f553f2539a60d26f3ee27320756a7351e5081f52be98fb8fa76876e'
assert '**Edition:** 1.2 · 20 October 2026' in source
exercise_text = source[source.index('## 18. Exercises'):source.index('### Answers and model responses')]
identifiers = re.findall(r'^#### ([A-Z]\d+)\.', exercise_text, re.M)
assert len(identifiers) == len(set(identifiers)) == 152
for i in range(1, 13):
    assert source.count(f'#### P{i:02d}.') == 2
assert source.index('### Pronunciation:') < source.index('## 3. How computers')

def save(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding='utf-8', newline='\n')

save('content/en/teaching/agrft.md', source)
body = source.split('---', 2)[2].lstrip()
portable = '# English for Film and Television\n\n' + body
portable = portable.replace('](/assets/images/agrft/v1/', '](https://raw.githubusercontent.com/damjan-popic/damjan-popic.github.io/agrft-v1.2/assets/images/agrft/v1/')
portable = portable.replace('](/assets/files/', '](https://damjan-popic.github.io/assets/files/')
assert sha(portable.encode()) == 'dd33f60a5649c26ee37e82e24f3af55f6329a79c903b600e721fbdf4d25c87ca'
save('assets/files/AGRFT_English_ucno_gradivo_v1.2.md', portable)
offline = portable.replace('https://raw.githubusercontent.com/damjan-popic/damjan-popic.github.io/agrft-v1.2/assets/images/agrft/v1/', 'schematics/')
svgs = sorted((ROOT / 'assets/images/agrft/v1').glob('*.svg'))
assert len(svgs) == 18
image_hashes = {p.name: sha(p.read_bytes()) for p in svgs}
package = ROOT / 'assets/files/AGRFT_English_ucno_gradivo_v1.2.zip'
with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, data in [('AGRFT_English_ucno_gradivo_v1.2.md', offline.encode())] + [('schematics/' + p.name, p.read_bytes()) for p in svgs]:
        info = zipfile.ZipInfo(name, (2026, 10, 20, 12, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, data, compresslevel=9)
with zipfile.ZipFile(package) as archive:
    assert len(archive.namelist()) == 19
    assert archive.testzip() is None
    for name, digest in image_hashes.items():
        assert sha(archive.read('schematics/' + name)) == digest

sl_path = ROOT / 'content/sl/poucevanje/agrft.md'
sl = sl_path.read_text(encoding='utf-8')
sl = sl.replace('1.0', '1.2').replace('**105 individualnih vaj', '**152 individualnih vaj')
sl = sl.replace('Prva štiri poglavja sistematično obravnavajo', 'Tehnična poglavja sistematično obravnavajo')
old = 'Začnemo z opremo: odpremo računalnik, poimenujemo njegove dele v angleščini in razložimo njihovo delovanje.'
new = 'Začnemo s števili, merjenjem in zapisovanjem podatkov ter z najpogostejšimi težavami pri rabi angleščine. Drugo poglavje vključuje tudi izgovarjavo: glasovna nasprotja, naglas, končnice in členitev govora, zlasti kot pomoč slovensko govorečim študentom. Dodani so strokovne besede z izgovornimi zgledi, dvanajst lomilcev jezika in individualne vaje. Nato odpremo računalnik, poimenujemo njegove dele v angleščini in razložimo njihovo delovanje.'
assert old in sl
sl = sl.replace(old, new)
sl = sl.replace('## Datoteka in različice', '## Datoteka in različice\n\nRazličica **1.2 · 20. oktober 2026** vključuje tudi razširitve o številih, slovnici, analogni opremi in zgodovini kamer, pripravljene za različico 1.1. [Predhodna objavljena različica 1.0](https://github.com/damjan-popic/damjan-popic.github.io/blob/agrft-v1.0/assets/files/AGRFT_English_ucno_gradivo_v1.0.md) ostaja ohranjena.')
save('content/sl/poucevanje/agrft.md', sl)
save('docs/AGRFT_CHANGELOG.md', '''# AGRFT — English for Film and Television

## 1.2 — 20 October 2026

- Added a pronunciation section within Chapter 2, Common English mistakes: vowels, /w/ and /v/, /th/ sounds, final consonants, clusters, schwa, word and sentence stress, grammatical endings and numerical read-back.
- Added 24 specialist word-bank entries with dictionary audio links, 12 original tongue twisters and 12 individual exercises P01–P12 with answers or listening criteria.
- Published the previously prepared 1.1 additions together with this release: numbers and measurements, English–Slovene contrasts, common grammatical errors, gentler technical explanations, analogue equipment and historical case studies.
- Preserved all 140 exercises from the prepared 1.1 text; the complete edition contains 152 individual exercises and answers. Preserved all 18 SVG schematics.
- Updated the English course text, Slovene landing page, full Markdown download and offline package.

## 1.1 — prepared manuscript

Numbers, notation, common English errors and expanded technical and historical material were prepared as downloadable files but were not published on the website separately. These additions are included in 1.2.

## 1.0 — 8 October 2026

Published technical-first edition, including 105 individual exercises and 18 schematics. The original archive branch and files remain unchanged.

## Citation

Cite the author, title, year, version number and a link to the precise Git commit or preserved edition. The main course page is the developing reading copy; an edition archive identifies a fixed text.
''')
print(json.dumps({'edition': '1.2', 'exercises': len(identifiers), 'pronunciation_exercises': 12, 'svg_files': len(svgs), 'source_sha256': sha(source.encode()), 'markdown_sha256': sha(portable.encode()), 'zip_sha256': sha(package.read_bytes())}, indent=2))
