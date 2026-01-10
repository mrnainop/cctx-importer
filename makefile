run:
	uv run script.py

lint:
	uvx ruff format
	uvx ruff check --fix
	uvx ty check
