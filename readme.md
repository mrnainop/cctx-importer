# cctx-importer | Claude Context Switcher Importer

Import [CCS](https://github.com/kaitranntt/ccs) profiles into [cctx](https://github.com/nwiizo/cctx).

CCS lets you configure Claude Code with different providers and accounts, but it doesn't modify Claude's default settings. This means you must use the `ccs` command and IDE extensions won't work.

cctx solves this by overwriting Claude's settings file, so you can use the `claude` command directly or IDE extensions.

This tool bridges both: it imports your CCS profiles into cctx so you can switch between them and use them with `claude` or IDE extensions.

## Requirements

- [cctx](https://github.com/nwiizo/cctx)

## Installation

The recommended way is to run directly with [uvx](https://docs.astral.sh/uv/guides/tools/) (no installation needed):

```bash
uvx cctx-importer from-ccs
```

Alternatively, install with pip:

```bash
pip install cctx-importer
```

Or with uv:

```bash
uv tool install cctx-importer
```

## Usage

```bash
# Import profiles from ~/.ccs/*.settings.json
cctx-importer from-ccs

# Import profiles from ~/.cctx-importer/*.json
cctx-importer from-configs
```

Both commands merge each profile with `~/.cctx-importer/default.json` if it exists.

## Options

```bash
# Use a custom directory for default.json
cctx-importer from-ccs --configs-dir /path/to/dir
```
