#!/usr/bin/env python3
"""Check downloadable course packages and their vector schematics."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, is_zipfile

ROOT = Path(__file__).resolve().parents[1]
SVG = "{http://www.w3.org/2000/svg}"

def check_svg(data, label):
    root = ET.fromstring(data)
    if root.tag != SVG + "svg":
        raise ValueError(f"{label}: expected an SVG document")
    view = [float(value) for value in root.attrib["viewBox"].split()]
    if len(view) != 4 or view[2] <= 0 or view[3] <= 0:
        raise ValueError(f"{label}: invalid viewBox")
    if root.find(SVG + "title") is None or root.find(SVG + "desc") is None:
        raise ValueError(f"{label}: missing explanatory title or description")

def main():
    diagrams = sorted((ROOT / "assets" / "images" / "agrft").rglob("*.svg"))
    for path in diagrams:
        check_svg(path.read_bytes(), path.relative_to(ROOT))
    packages = sorted((ROOT / "assets" / "files").glob("AGRFT_English_ucno_gradivo_*.zip"))
    entries = 0
    for path in packages:
        if not is_zipfile(path):
            raise ValueError(f"{path.name}: invalid ZIP structure")
        with ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                raise ValueError(f"{path.name}: CRC failure in {bad}")
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError(f"{path.name}: duplicate entries")
            texts = [name for name in names if name.endswith(".md")]
            if len(texts) != 1:
                raise ValueError(f"{path.name}: expected one complete Markdown text")
            text = archive.read(texts[0]).decode("utf-8")
            if "[FIGURE:" in text:
                raise ValueError(f"{path.name}: unresolved figure marker")
            referenced = re.findall(r"!\[[^\]]*\]\((schematics/[^)]+\.svg)\)", text)
            bundled = [name for name in names if name.endswith(".svg")]
            if set(referenced) != set(bundled):
                raise ValueError(f"{path.name}: bundled and referenced diagrams differ")
            for name in bundled:
                check_svg(archive.read(name), f"{path.name}/{name}")
            entries += len(names)
    print(f"Checked {len(diagrams)} SVG schematics and {len(packages)} course packages ({entries} entries).")

if __name__ == "__main__":
    main()
