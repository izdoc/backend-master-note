"""Render versioned Markdown articles into an offline static Site."""

import json
import re
import shutil
import subprocess
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
DIST = ROOT / "dist"


def render(markdown: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html5", "--no-highlight", str(markdown)],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def rewrite_links(html: str, source: Path, known_paths: set[str]) -> str:
    current_id = source.relative_to(CONTENT).as_posix().removesuffix(".md")

    def replace(match: re.Match[str]) -> str:
        url = unescape(match.group(1))
        if url.startswith("#"):
            return f'href="#/{current_id}?anchor={url[1:]}"'
        if ":" in url or url.startswith("/"):
            return match.group(0)
        path, _, fragment = url.partition("#")
        if path in ("../../README.md", "../README.md", "README.md"):
            return 'href="#/"'
        resolved = (source.parent / path).resolve()
        try:
            relative = resolved.relative_to(CONTENT.resolve()).as_posix()
        except ValueError:
            return match.group(0)
        if relative.endswith("/README.md"):
            return 'href="#/"'
        if relative not in known_paths:
            return match.group(0)
        route = f"#/{relative.removesuffix('.md')}"
        if fragment:
            route += f"?anchor={fragment}"
        return f'href="{route}"'

    return re.sub(r'href="([^"]+)"', replace, html)


def main() -> None:
    if not shutil.which("pandoc"):
        raise SystemExit("pandoc is required to build the Site")
    catalog = json.loads((CONTENT / "config" / "catalog.json").read_text(encoding="utf-8"))
    known = {page["path"] for category in catalog for page in category["pages"]}

    pages = []
    for category in catalog:
        for page in category["pages"]:
            source = CONTENT / page["path"]
            html = rewrite_links(render(source), source, known)
            plain = re.sub(r"<[^>]+>", " ", html)
            pages.append(
                {
                    "id": page["path"].removesuffix(".md"),
                    "title": page["title"],
                    "category": category["title"],
                    "categoryId": category["category"],
                    "path": page["path"],
                    "html": html,
                    "searchText": unescape(re.sub(r"\s+", " ", plain)).strip(),
                }
            )

    (DIST / "assets").mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "assets/app.js", "assets/styles.css"):
        source = ROOT / "src" / name
        destination = DIST / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    (DIST / "assets" / "content.json").write_text(
        json.dumps({"categories": catalog, "pages": pages}, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Built {len(pages)} articles in {len(catalog)} categories")


if __name__ == "__main__":
    main()
