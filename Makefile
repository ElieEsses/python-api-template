.PHONY: run test lint format fix check

run:
	uv run uvicorn Project.main:app --reload

test:
	uv run pytest -v

coverage:
	uv run coverage run -m pytest
	uv run coverage report -m

fix:
	uv run ruff check . --fix
	uv run ruff format .

ci:
	uv run ruff check .
	uv run pytest

clean:
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	find . -type d -name '__pycache__' -exec rm -rf {} +