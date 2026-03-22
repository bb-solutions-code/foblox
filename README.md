# Foblox

**Foundation Blocks for BBScript** — a block package you can import into BBScript-based workflows. Blocks live under subfolders (for example `say/`) with a `.bbpackage` manifest and Python `entrypoint` per block.

## Contents

- **`say`** — Prints its `input` to the console (stdout) and passes the same value through as output.
- **`variable`** — Passes its `value` input through to the block `output` for use in context.
- **`calculate`** — Takes numbers `a` and `b`, applies `operation` (`+`, `-`, `*`, `/`, or `pow`), and outputs the numeric result on `output`.

## Requirements

- **[BBScript](https://github.com/bb-solutions-code/bbscript)** `>=0.2.0` (see `foblox.bbpackage`).

## Running tests

From the repository root, with `bbscript` and `pytest` available on your environment:

```bash
pytest foblox/tests
```

`foblox/tests/conftest.py` prepends the `foblox` directory to `sys.path` so `say.say` imports resolve. `foblox/pytest.ini` also sets `pythonpath = .` when pytest is run with that config file as the active config.

## Installation

Use **[bbpm](https://github.com/bb-solutions-code/bbpm)** (BBScript Package Manager) in your project: `bbpm init` (default) or `bbpm fetch https://github.com/bb-solutions-code/foblox.git` installs this package under `.bbpm/packages/`. Run graphs with `bbpm run` so Foblox blocks load next to built-in [BBScript](https://github.com/bb-solutions-code/bbscript) blocks.

## Related projects

- **[BBScript](https://github.com/bb-solutions-code/bbscript)** — graph runtime and CLI for `.bbs` documents; Foblox blocks run on this engine.
- **[bbpm](https://github.com/bb-solutions-code/bbpm)** — installs and registers Foblox (and other `.bbpackage` repos) in a project.

## Contributing

1. Open a branch for your change.
2. Add or update tests under `tests/` and run pytest as described in **Running tests**.
3. Keep each block in its own folder with a `.bbpackage` manifest and a clear Python `entrypoint`; document behavior in English.
4. Target **[BBScript](https://github.com/bb-solutions-code/bbscript)** `>=0.2.0` and align block I/O with how the runtime resolves `args` and `output`.
