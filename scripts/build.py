#!/usr/bin/env python3
"""Build self-contained Sogeti HTML artifacts from template sources.

Usage:
    python3 scripts/build.py                 # build every file in references/templates/_src
    python3 scripts/build.py path/to/src.html

A source file links the shared assets normally:

    <link rel="stylesheet" href="../../../assets/sogeti.css">
    <script src="../../../assets/sogeti.js" defer></script>
    <img src="../../../assets/logos/sogeti-logo-color.png" ...>

The build inlines the CSS (including embedded fonts), JS and local images.
The output is a single portable .html file with no network dependencies.
"""
from __future__ import annotations

import base64
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "references" / "templates" / "_src"
OUT_DIR = ROOT / "references" / "templates"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def css_bundle() -> str:
    fonts = read(ROOT / "assets" / "fonts.css")
    css = read(ROOT / "assets" / "sogeti.css")
    css = re.sub(r'@import\s+url\(["\']?fonts\.css["\']?\)\s*;', "", css)
    return fonts + "\n" + css


INCLUDE_RE = re.compile(r"<!--\s*@include\s+([^\s]+)\s*-->")


def expand_includes(html: str, base: Path, seen: set[Path] | None = None) -> str:
    """Expand <!-- @include relative/path.html --> recursively.

    Paths inside partials are written relative to the including template,
    so the whole source directory behaves like one document.
    """
    seen = seen or set()

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        path = (base / name).resolve()
        if path in seen:
            return f"<!-- include cycle: {name} -->"
        if not path.is_file():
            print(f"  ! missing include: {name}")
            return match.group(0)
        seen.add(path)
        return expand_includes(read(path), base, seen)

    return INCLUDE_RE.sub(repl, html)


def inline_assets(html: str, src_path: Path) -> str:
    css = css_bundle()
    js = read(ROOT / "assets" / "sogeti.js")

    # Inline the design-system stylesheet link.
    html = re.sub(
        r'<link[^>]+href=["\'][^"\']*sogeti\.css["\'][^>]*>',
        lambda _m: "<style>\n" + css + "\n</style>",
        html,
        flags=re.I,
    )
    # Inline the helper script.
    html = re.sub(
        r'<script[^>]+src=["\'][^"\']*sogeti\.js["\'][^>]*>\s*</script>',
        lambda _m: "<script>\n" + js + "\n</script>",
        html,
        flags=re.I,
    )

    def data_uri(raw: Path) -> str:
        mime = mimetypes.guess_type(raw.name)[0] or "application/octet-stream"
        payload = base64.b64encode(raw.read_bytes()).decode("ascii")
        return f"data:{mime};base64,{payload}"

    # Inline local images referenced by <img src="...">
    def repl_img(match: re.Match[str]) -> str:
        whole, url = match.group(0), match.group(1)
        if url.startswith(("data:", "http://", "https://", "//")):
            return whole
        raw = (src_path.parent / url).resolve()
        if not raw.is_file():
            print(f"  ! missing image: {url}")
            return whole
        return whole.replace(url, data_uri(raw))

    html = re.sub(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>', repl_img, html, flags=re.I)

    # Inline local SVG illustrations referenced by <img> (already covered) and CSS url()s.
    def repl_css_url(match: re.Match[str]) -> str:
        url = match.group(1)
        if url.startswith(("data:", "http://", "https://", "//")):
            return match.group(0)
        raw = (src_path.parent / url).resolve()
        if raw.is_file():
            return f'url("{data_uri(raw)}")'
        return match.group(0)

    html = re.sub(r'url\(["\']?(?!data:|https?:|//)([^"\')]+)["\']?\)', repl_css_url, html)
    return html


def check_external(html: str) -> list[str]:
    hits: list[str] = []
    for pat, label in [
        (r'<(?:script|link|img|iframe)[^>]+(?:src|href)=["\'](https?:)?//', "remote asset"),
        (r"@import\s+url\(https?", "remote @import"),
    ]:
        if re.search(pat, html, flags=re.I):
            hits.append(label)
    return hits


def build_one(src: Path) -> Path:
    html = expand_includes(read(src), src.parent)
    out = inline_assets(html, src)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / (src.stem + ".html")
    dest.write_text(out, encoding="utf-8")
    ext = check_external(out)
    print(f"  built {dest.relative_to(ROOT)}  ({len(out)/1024:.1f} KB)" + (f"  WARN: {ext}" if ext else ""))
    return dest


def main() -> int:
    targets = [Path(p).resolve() for p in sys.argv[1:]] or sorted(SRC_DIR.glob("*.html"))
    if not targets:
        print(f"No sources found in {SRC_DIR}")
        return 1
    for src in targets:
        if not src.is_file():
            print(f"  ! not a file: {src}")
            continue
        build_one(src)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
