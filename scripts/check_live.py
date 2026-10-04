#!/usr/bin/env python3
"""Check deployed pages without third-party packages or privileged credentials."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://damjan-popic.github.io/"
EDIT = "https://github.com/damjan-popic/damjan-popic.github.io/edit/main/content/"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang, self.canonical, self.h1 = None, None, 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "a":
            self.links.append(attrs.get("href", ""))


def fetch(path: str) -> str:
    request = Request(BASE + path, headers={"User-Agent": "personal-site-deployment-check", "Cache-Control": "no-cache"})
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}: {path}")
        return response.read().decode("utf-8")


def retry(operation):
    for attempt in range(6):
        try:
            return operation()
        except (OSError, URLError, ValueError) as error:
            if attempt == 5:
                raise
            print(f"Retry {attempt + 1}/5: {error}", flush=True)
            time.sleep(5)


def check_page(route: str, source: str):
    page = Page()
    page.feed(fetch(route))
    lang = source.split("/", 1)[0]
    canonical = BASE + (route or "sl/")
    if page.lang != lang or page.h1 != 1 or page.canonical != canonical:
        raise ValueError(f"Wrong language, title or canonical address: {route}")
    if EDIT + source not in page.links:
        raise ValueError(f"Wrong editing destination: {route}")
    if any("digital-linguistics-playbook/damjan/" in link for link in page.links):
        raise ValueError(f"Old nested site link: {route}")
    print(f"PASS HTTP 200, language, canonical and edit link: /{route}", flush=True)


def main(expected_commit: str):
    def check_manifest():
        manifest = json.loads(fetch("build.json?deployment=" + expected_commit))
        if manifest.get("source_commit") != expected_commit:
            raise ValueError("Published build does not match the deploying commit")
        if set(manifest.get("languages", [])) != {"sl", "en"}:
            raise ValueError("Published build is missing a language")
        print(f"PASS deployed source commit: {expected_commit}", flush=True)
    retry(check_manifest)
    routes = [("", "sl/index.md")]
    for path in sorted((ROOT / "content").rglob("*.md")):
        source = path.relative_to(ROOT / "content").as_posix()
        route = source[:-3]
        route = route[:-5] if route.endswith("/index") else route + "/"
        routes.append((route, source))
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda item: retry(lambda: check_page(*item)), routes))
    stylesheet = retry(lambda: fetch("assets/style.css"))
    if ".main-nav" not in stylesheet:
        raise ValueError("Published stylesheet is missing")
    print(f"Verified {len(routes)} public pages and the stylesheet.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True)
    main(parser.parse_args().expected_commit)
