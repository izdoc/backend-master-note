"""Copy the canonical securities wiki into this site's versioned content snapshot."""

import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", type=Path, default=Path("../securities-wiki"))
    args = parser.parse_args()

    wiki = args.wiki.resolve()
    destination = Path(__file__).resolve().parents[1] / "content"
    catalog = wiki / "config" / "catalog.json"
    if not catalog.is_file() or not (wiki / "docs").is_dir():
        parser.error(f"Wiki source not found: {wiki}")

    if destination.exists():
        shutil.rmtree(destination)
    (destination / "config").mkdir(parents=True)
    shutil.copy2(catalog, destination / "config" / "catalog.json")
    shutil.copytree(wiki / "docs", destination / "docs")
    print(f"Synced wiki articles from {wiki}")


if __name__ == "__main__":
    main()
