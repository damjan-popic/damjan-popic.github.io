#!/usr/bin/env python3
"""Apply a hash-verified AGRFT manuscript revision on the preparation branch."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PARTS = Path(__file__).resolve().parent / 'parts'
BASE = '0f46347dd0a6b27108d989dc7b39f6b8de5dc5836b4014147ade9f00449ffd03'
ASSEMBLED = 'a44d45266da2737380289e70fef1c82642d8692b8a1efb780b26b892ecdfd88b'
TARGET = 'e4fd1a82a147b1a07d4962a26e6e679f74e5a86e27bc432b053a71dcec121756'
STANDALONE = 'b8575fb1a1c90edd2aa5e1f40af9fa96ba58bdbc5e5fa219a930ef3b7e3fcb6e'
EXPECTED = {
 '01.json':'0714f0520d50523dcd1c4808cfcbb471894b3661c80b92c2171e28ef2a3afecf',
 '02-01.txt':'fc0ba0c27b9c046359215e00b8bf017e1424aac876c3e3c77616d7557fd5b65d',
 '02-02.txt':'3ad4a89768579f29b7e8157a73d9203413fa805c35fce046b97c25700dd20553',
 '02-03.txt':'caa2b444291df420b32e9def2ff6e24501f9b4e15f22b44b47b6df8379a7ee56',
 '02-04.txt':'cd3ad469a89634d34c450a0cbfe987a746cbb79818a6e2af00df48151c9ff621',
 '02-05.txt':'cf096f54555c81175bfc6eaa233e94e0ddd4fd15d967d4f1fe7e3ed0d2acfd3b',
 '03.json':'a2744e88952a087df4abbcc99dd15213ea99c8a736276c1b4fa9a2c44e275b09',
 '04.json':'4a2846f6390c39ce054c418d725126142572cdb07b23022f32756ef1535a60c0',
 '05.json':'caec2d62b3d1e196ba4824650c17aba8c827d483c7ade61c86f7a747f7034e4a',
 '06.json':'8d20b522962c95e6577be0638f86a499c63f04baa54a4c940526a9ba9cd63366',
 '07.json':'fa3b8c62bd7c9af39da7e9c693d6f44e66174858b2a112c12b36bf786accbd33',
 '08.json':'9ff3178d699f07ec01afaee5a9ae23983530068af5cd3dd09d01655c47f81817',
 '09.json':'62ccfb91ecf70d0611abcd714b134738f80f816a998927c4b7be4e8ebf153840',
 '10.json':'bc1fce7b7dcb46abd91703eea3402f170182b411e64788a4ebab7ef958e86400',
}
def sha(data):
    return hashlib.sha256(data).hexdigest()

for name, expected in EXPECTED.items():
    payload = (PARTS / name).read_bytes()
    if name.endswith('.json'):
        payload = json.dumps(json.loads(payload), ensure_ascii=False, separators=(',', ':')).encode()
    actual = sha(payload)
    print(name, actual, 'OK' if actual == expected else 'MISMATCH', flush=True)
    if actual != expected:
        raise ValueError(f'Patch transmission differs: {name}')

path = ROOT / 'content/en/teaching/agrft.md'
original = path.read_bytes()
assert sha(original) == BASE, 'Source changed; do not overwrite concurrent edits.'
ops = json.loads((PARTS / '01.json').read_text())
intro = ''.join((PARTS / f'02-{n:02}.txt').read_text() for n in range(1, 6))
ops.append([41, 42, intro])
for n in range(3, 11):
    ops.extend(json.loads((PARTS / f'{n:02}.json').read_text()))
lines = original.decode().splitlines(True)
for start, end, replacement in reversed(ops):
    lines[start:end] = replacement.splitlines(True)
source = ''.join(lines)
assert sha(source.encode()) == ASSEMBLED, 'Assembled manuscript checksum mismatch.'
# An absolute URL distinguishes a downloadable Markdown asset from a content page.
source = source.replace('](/assets/files/AGRFT_English_ucno_gradivo_v1.2.md)', '](https://damjan-popic.github.io/assets/files/AGRFT_English_ucno_gradivo_v1.2.md)')
assert sha(source.encode()) == TARGET, 'Final manuscript checksum mismatch.'
exercises = source.split('## 18. Exercises', 1)[1].split('### Answers and model responses', 1)[0]
ids = re.findall(r'^#### ([A-Z]\d{2})[.\s]', exercises, re.M)
assert len(ids) == len(set(ids)) == 152
answers = source.split('### Answers and model responses', 1)[1]
for n in range(1, 13):
    assert len(re.findall(rf'^#### P{n:02}\.', answers, re.M)) == 1
assert source.index('### Pronunciation:') < source.index('## 3. How computers')
path.write_text(source, encoding='utf-8')

raw = 'https://raw.githubusercontent.com/damjan-popic/damjan-popic.github.io/agrft-v1.2/assets/images/agrft/v1/'
body = source.split('---', 2)[2].lstrip('\n')
standalone = '# English for Film and Television\n\n' + body
standalone = standalone.replace('](/assets/images/agrft/v1/', '](' + raw)
standalone = standalone.replace('](/assets/files/', '](https://damjan-popic.github.io/assets/files/')
assert sha(standalone.encode()) == STANDALONE
files = ROOT / 'assets/files'
name = 'AGRFT_English_ucno_gradivo_v1.2'
(files / (name + '.md')).write_text(standalone, encoding='utf-8')
images = sorted((ROOT / 'assets/images/agrft/v1').glob('*.svg'))
assert len(images) == 18
with zipfile.ZipFile(files / (name + '.zip'), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
    out.writestr(name + '.md', standalone.replace(raw, 'schematics/'))
    for image in images:
        out.write(image, 'schematics/' + image.name)
with zipfile.ZipFile(files / (name + '.zip')) as package:
    assert len(package.namelist()) == 19
    assert package.testzip() is None
    for image in images:
        assert package.read('schematics/' + image.name) == image.read_bytes()

slpath = ROOT / 'content/sl/poucevanje/agrft.md'
sl = slpath.read_text()
sl = sl.replace('različica 1.0', 'različica 1.2').replace('Različica 1.0', 'Različica 1.2')
sl = sl.replace('agrft-v1.0/', 'agrft-v1.2/').replace('_v1.0.', '_v1.2.')
sl = sl.replace('105 individualnih', '152 individualnih')
sl = sl.replace('Prva štiri poglavja sistematično', 'Poglavja 3–6 sistematično')
sl = sl.replace('Začnemo z opremo: odpremo računalnik,', 'Po uvodnih poglavjih o številih, merskih enotah in angleščini preidemo k opremi: odpremo računalnik,')
needle = '\nUvodne razlage povežejo'
assert needle in sl
sl = sl.replace(needle, '\nDrugo poglavje poleg pogostih slovničnih težav obravnava izgovorjavo: glasovna nasprotja, besedni in stavčni naglas, šibke oblike ter jasnost števil in navodil. Dodani so izgovorni slovarček z 22 strokovnimi izrazi in povezavami do zvočnih zgledov, 12 izvirnih jezikovnih zavozlank ter 12 individualnih vaj z rešitvami.\n\nUvodne razlage povežejo', 1)
slpath.write_text(sl, encoding='utf-8')

docs = ROOT / 'docs'
docs.mkdir(exist_ok=True)
(docs / 'AGRFT_CHANGELOG.md').write_text('''# English for Film and Television — editions

## 1.2 — 20 October 2026

The complete edition integrates the previously prepared 1.1 manuscript and a new pronunciation section in Chapter 2. It adds contrastive guidance for Slovene and other learners, 22 specialist-word entries with dictionary audio links, 12 original articulation drills, and individual exercises P01–P12 with explained answers. Earlier exercise identifiers are retained. There are now 152 individual exercises and 18 unchanged SVG schematics.

The language foundations, gentler technical openings, analogue equipment vocabulary, camera history and Great Seal case prepared for 1.1 are included. The website and downloadable Markdown are complete versions, not supplements. The offline package includes all diagrams; linked dictionary audio remains online.

The archive branch agrft-v1.2 identifies this edition. For an immutable citation, use the release commit in the URL. Subsequent substantive changes belong to a new numbered edition.

## 1.1 — 15 October 2026

Prepared manuscript with numbers and measurements, English–Slovene contrasts, common grammar issues, analogue equipment and historical examples. This manuscript was supplied as files but was not published on the website at that time; its content is incorporated into 1.2.

## 1.0 — 8 October 2026

First official technical edition: computers, sound, video, cameras and professional English; 105 exercises and 18 diagrams. The edition remains preserved at commit b48ab3170988f8d28421ba1b4579f8d4454473bd and on agrft-v1.0. Its files have not been overwritten by this release.
''', encoding='utf-8')
print('Verified source:', TARGET, 'Standalone:', STANDALONE, flush=True)
print('152 individual exercises; 18 unchanged SVGs; ZIP validated.', flush=True)
# Preparation-only transport files are not part of the published materials.
shutil.rmtree(PARTS.parent)
(ROOT / '.github/workflows/agrft-release-preparation.yml').unlink()
