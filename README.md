# reqgen

`reqgen` is a command-line tool that scans a Python project and generates a
`requirements.txt` file listing all third-party packages it imports. I have
had issues at work with documenting my package and wanted to make an easier
way for me to get all the required packages of python projects with multiple 
nested subfolders. This script works if you point it at a python package or
a directory.

## Usage

Install the tool:

```bash
uv add "git+https://github.com/ddho22/dsc190-final.git"
```

**Single file:**

```bash
uv run reqgen script.py
```

**Directory (flat or nested):**

```bash
uv run reqgen my_project/
```

`reqgen` recursively finds all `.py` files in subdirectories.

**Custom output path:**

```bash
uv run reqgen my_project/ -o deps.txt
```

The tool writes one package name per line to the output file
(default: `requirements.txt`) and prints a summary to stdout.
