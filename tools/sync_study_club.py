#!/usr/bin/env python3
"""Copy Nadia's Study Club from its revision repository into the phone app.

The revision repository (the folder other Claudes edit) is the source of truth.
This script never writes to it. It copies the pages and wallpapers into
study-club/ and adds the few tags a home-screen web app needs.

Usage:
    python3 tools/sync_study_club.py [SOURCE_FOLDER]

SOURCE_FOLDER defaults to the copy in Nadia's Claude projects folder.
Only index.html, nine-stories.html and bg/ in study-club/ are replaced; the
app's own files (manifest, service worker, icons, app.js) are left alone.
"""
import hashlib
import shutil
import sys
from pathlib import Path

DEFAULT_SOURCE = Path(
    "~/Documents/Claude/Projects/uOttawa/Nadia Study Club - Repository"
).expanduser()
APP = Path(__file__).resolve().parent.parent / "study-club"
MARK = "<!-- study-club-app -->"

HEAD_TAGS = f"""{MARK}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#B9E0F1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Study Club">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<script src="app.js"></script>
"""


def add_app_tags(html: str) -> str:
    if MARK in html:
        return html
    lower = html[:2000].lower()
    if "<head>" in lower:
        i = lower.index("<head>") + len("<head>")
        return html[:i] + "\n" + HEAD_TAGS + html[i:]
    # Claude artifact pages start straight at <title>; give them a proper
    # document start so the browser uses standards mode.
    return "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n" + HEAD_TAGS + html


def main() -> None:
    src = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_SOURCE
    if not (src / "index.html").is_file():
        sys.exit(f"No index.html in {src}")
    APP.mkdir(exist_ok=True)

    for name in ("index.html", "nine-stories.html"):
        f = src / name
        if f.is_file():
            (APP / name).write_text(add_app_tags(f.read_text(encoding="utf-8")), encoding="utf-8")
            print("copied", name)

    if (src / "bg").is_dir():
        if (APP / "bg").exists():
            shutil.rmtree(APP / "bg")
        shutil.copytree(src / "bg", APP / "bg")
        print("copied bg/")

    # Stamp the service worker so phones pick up the new copy.
    digest = hashlib.sha1()
    for p in sorted(APP.rglob("*")):
        if p.is_file() and p.name not in ("sw.js",):
            digest.update(p.read_bytes())
    sw = APP / "sw.js"
    text = sw.read_text(encoding="utf-8").splitlines(keepends=True)
    text[0] = f'const VERSION = "{digest.hexdigest()[:10]}";\n'
    sw.write_text("".join(text), encoding="utf-8")
    print("app version", digest.hexdigest()[:10])


if __name__ == "__main__":
    main()
