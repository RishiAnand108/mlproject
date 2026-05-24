import os
from pathlib import Path

try:
    import cairosvg
except Exception:
    raise SystemExit("cairosvg is required. Install with 'pip install cairosvg'")


def convert(svg_path: Path, png_path: Path):
    if not svg_path.exists():
        print(f"Missing {svg_path}")
        return
    png_path.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path))
    print(f"Wrote {png_path}")


def main():
    repo_root = Path(__file__).resolve().parents[1]
    docs = repo_root / "docs"
    pairs = [
        (docs / "architecture.svg", docs / "architecture.png"),
        (docs / "sample_plot.svg", docs / "sample_plot.png"),
    ]
    for s, p in pairs:
        convert(s, p)


if __name__ == '__main__':
    main()
