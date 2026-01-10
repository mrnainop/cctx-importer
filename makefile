lint:
	uvx ruff format
	uvx ruff check --fix
	uvx ty check

import-from-configs:
	uv run script.py cctx

import-from-ccs:
	uv run script.py ccs
