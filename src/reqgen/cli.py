import argparse
import sys
from pathlib import Path

from reqgen.parser import extract_imports, to_package_name


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        if target.suffix != ".py":
            print(f"Error: {target} is not a Python file.", file=sys.stderr)
            sys.exit(1)
        return [target]
    if target.is_dir():
        return list(target.rglob("*.py"))
    print(f"Error: {target} does not exist.", file=sys.stderr)
    sys.exit(1)


def generate_requirements(files: list[Path]) -> list[str]:
    all_imports: set[str] = set()
    for f in files:
        all_imports |= extract_imports(f)
    return sorted(to_package_name(name) for name in all_imports)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="reqgen",
        description="Generate a requirements.txt from a Python file or directory.",
    )
    parser.add_argument(
        "target",
        type=Path,
        help="A .py file or directory containing .py files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("requirements.txt"),
        help="Output file path (default: requirements.txt).",
    )
    args = parser.parse_args()

    files = collect_files(args.target)
    if not files:
        print("No Python files found.", file=sys.stderr)
        sys.exit(1)

    packages = generate_requirements(files)
    args.output.write_text("\n".join(packages) + "\n" if packages else "")
    print(f"Wrote {len(packages)} package(s) to {args.output}")
    for pkg in packages:
        print(f"  {pkg}")
