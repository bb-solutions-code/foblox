# Foblox

**Foundation Blocks for BBScript** — a block package you can import into BBScript-based workflows. Blocks live under subfolders (for example `say/`) with a `.bbpackage` manifest and Python `entrypoint` per block.

## Contents

- **`say`** — Prints its `input` to the console (stdout) and passes the same value through as output.
- **`variable`** — Passes its `value` input through to the block `output` for use in context.
- **`calculate`** — Takes numbers `a` and `b`, applies `operation` (`+`, `-`, `*`, `/`, or `pow`), and outputs the numeric result on `output`.

## Requirements

- **bbscript** `>=0.2.0` (see `foblox.bbpackage`).

## Running tests

From the repository root, with `bbscript` and `pytest` available on your environment:

```bash
pytest foblox/tests
```

`foblox/tests/conftest.py` prepends the `foblox` directory to `sys.path` so `say.say` imports resolve. `foblox/pytest.ini` also sets `pythonpath = .` when pytest is run with that config file as the active config.

## Installation

A BBScript Package Manager (BBPM) will install and register this package in BBScript; that tooling is not part of this repository yet.
