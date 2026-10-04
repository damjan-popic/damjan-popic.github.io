#!/usr/bin/env python3
"""Check anonymous Pages delivery, including ordinary cached browser requests.

This complements check_live.py's content checks. It makes only public GETs,
prints selected response headers, and never sends a GitHub token to the site.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import socket
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = "https://damjan-popic.github.io/"
USER_AGENT = "Mozilla/5.0 (compatible; personal-site-delivery-check/1.0)"
PATHS = ("", "sl/", "en/", "sl/index.html", "en/index.html", "en/teaching/agrft/")
HEADERS = ("date", "server", "cache-control", "age", "x-cache", "x-served-by", "x-github-request-id")


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        if tag == "html":
            self.lang = dict(attrs).get("lang")
        if tag == "h1":
            self.headings += 1


def probe(item: tuple[str, bool], stamp: str) -> dict:
    path, fresh = item
    url = BASE + path + ("?delivery_check=" + stamp if fresh else "")
    result = {"url": url, "mode": "fresh" if fresh else "ordinary"}
    try:
        request = Request(url, headers={"User-Agent": USER_AGENT})
        try:
            response = urlopen(request, timeout=15)
        except HTTPError as error:
            response = error
        with response:
            result["status"] = response.code
            result["final_url"] = response.geturl()
            result["headers"] = {key: response.headers.get(key) for key in HEADERS if response.headers.get(key)}
            document = Document()
            document.feed(response.read().decode("utf-8", errors="replace"))
        expected_lang = "en" if path.startswith("en/") else "sl"
        result["lang"] = document.lang
        result["ok"] = result["status"] == 200 and document.lang == expected_lang and document.headings == 1 and result["final_url"] == url
    except (OSError, URLError, ValueError) as error:
        result.update(ok=False, error=str(error))
    return result


def main(strict: bool, attempts: int) -> int:
    print("Delivery check UTC:", datetime.now(timezone.utc).isoformat(), flush=True)
    try:
        addresses = sorted({entry[4][0] for entry in socket.getaddrinfo("damjan-popic.github.io", 443, type=socket.SOCK_STREAM)})
        print("Public DNS addresses:", json.dumps(addresses), flush=True)
    except OSError as error:
        print("DNS resolution failed:", error, flush=True)
    pending = [(path, fresh) for path in PATHS for fresh in (False, True)]
    for attempt in range(attempts):
        stamp = str(time.time_ns())
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda item: probe(item, stamp), pending))
        for result in results:
            print(json.dumps(result, ensure_ascii=False), flush=True)
        pending = [item for item, result in zip(pending, results) if not result["ok"]]
        if not pending:
            print("PASS: ordinary and fresh anonymous requests served the correct pages.", flush=True)
            return 0
        if attempt + 1 < attempts:
            time.sleep(15)
    print(f"Delivery failures: {len(pending)}. See the exact URLs and response headers above.", flush=True)
    return 1 if strict else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Fail when a public URL is not served correctly")
    parser.add_argument("--attempts", type=int, choices=range(1, 5), default=1)
    args = parser.parse_args()
    raise SystemExit(main(args.strict, args.attempts))
