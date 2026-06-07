import ast
import sys
from pathlib import Path

# stdlib module names (Python 3.12)
_STDLIB = sys.stdlib_module_names


def extract_imports(path: Path) -> set[str]:
    """Return top-level package names imported by a single .py file."""
    source = path.read_text(encoding="utf-8", errors="ignore")
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError:
        return set()

    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                names.add(node.module.split(".")[0])

    return {n for n in names if n not in _STDLIB and n != "__future__"}


# Common import-name → PyPI package-name mappings
_IMPORT_TO_PACKAGE: dict[str, str] = {
    "cv2": "opencv-python",
    "sklearn": "scikit-learn",
    "PIL": "Pillow",
    "bs4": "beautifulsoup4",
    "yaml": "PyYAML",
    "dotenv": "python-dotenv",
    "dateutil": "python-dateutil",
    "wx": "wxPython",
    "gi": "PyGObject",
    "usaddress": "usaddress",
    "Crypto": "pycryptodome",
    "pkg_resources": "setuptools",
    "attr": "attrs",
    "google": "google-cloud",
    "serial": "pyserial",
    "MySQLdb": "mysqlclient",
    "psycopg2": "psycopg2-binary",
}


def to_package_name(import_name: str) -> str:
    return _IMPORT_TO_PACKAGE.get(import_name, import_name)
