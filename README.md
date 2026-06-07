# reqgen

`reqgen` is a command-line tool that scans a Python project and generates a
`requirements.txt` file listing all third-party packages it imports. Point it
at a single `.py` file or an entire directory and it handles the rest.

## Usage

Install the tool:

```bash
uv add "git+https://github.com/ddho22/dsc190-final.git"
```

**Single file:**

```bash
reqgen script.py
```

**Directory (flat or nested):**

```bash
reqgen my_project/
```

`reqgen` recursively finds all `.py` files in subdirectories.

**Custom output path:**

```bash
reqgen my_project/ -o deps.txt
```

The tool writes one package name per line to the output file
(default: `requirements.txt`) and prints a summary to stdout.
