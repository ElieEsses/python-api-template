.PHONY: run test coverage lint format fix check init-db

run:
	uv run uvicorn src.app.main:app --reload

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

init-db:
	uv run python -c "from app.db import init_db; init_db()"

clean:
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	find . -type d -name '__pycache__' -exec rm -rf {} +