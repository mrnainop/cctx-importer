install:
	uv sync --all-groups --all-extras

lint:
	uv run ruff format
	uv run ruff check --fix
	uv run ty check

import-from-configs:
	uv run cctx-importer cctx

import-from-ccs:
	uv run cctx-importer ccs
