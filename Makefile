.PHONY: run test coverage lint format fix check

run:
	uv run uvicorn Project.main:app --reload

test:
	uv run pytest -v

coverage:
	uv run coverage run -m pytest
	uv run coverage report -m

lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff format .
	uv run ruff check . --fix

check:
	uv run ruff check .
	uv run pytest -q

clean:
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	find . -type d -name '__pycache__' -exec rm -rf {} +