# Claude Context Profile Manager

Script to manage Claude Code context profiles stored as JSON files.

## Overview

This script processes JSON configuration files in the `configs/` directory and imports them as profiles using the `cctx` CLI tool. Each profile is created by deep merging the specific config file with `default.json` (if it exists).

## Features

- **Deep merge**: Combines `default.json` with each profile config, allowing shared base settings
- **Safe context handling**: Automatically unsets the active context before deleting it, then restores it after processing
- **Error tolerance**: Continues processing remaining profiles if one fails
- **Progress feedback**: Logs each processed profile and context changes

## Requirements

- [`cctx`](https://github.com/nwiizo/cctx) CLI tool installed and available in PATH
- [`uv`](https://docs.astral.sh/uv) (for running the script)

## Usage

```bash
uv run script.py
```

## Configuration Structure

Place JSON files in the `configs/` directory:

```text
configs/
├── default.json    # Base configuration (optional)
├── glm.json        # Profile "glm"
└── other.json      # Profile "other"
```

Each JSON file is merged with `default.json` (if exists) and imported as a profile named after the filename (without extension).

## Example

**configs/default.json:**

```json
{
  "hooks": {
    "pre-model-response": "echo 'Running hook...'"
  },
  "model": "claude-opus-4-5-20251101"
}
```

**configs/glm.json:**

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "ANTHROPIC_MODEL": "glm-4.7"
  }
}
```

Result: The "glm" profile will have both the hooks and model from `default.json`, plus the env variables from `glm.json`.

## Available Commands

| Command     | Description                  |
| ----------- | ---------------------------- |
| `make lint` | Run linters and formatters   |
| `make run`  | Run the script               |
