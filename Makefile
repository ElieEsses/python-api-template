.PHONY: help start run install restart fix

help:
	@echo "start    Create venv, install deps, run app"
	@echo "run      Run app"
	@echo "install  Install dependencies"
	@echo "restart  Recreate venv"
	@echo "fix      Run Ruff fixes and formatting"

start:
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv venv; \
	fi
	@echo "Installing dependencies..."
	@./venv/bin/python -m pip install -r requirements.txt
	@echo "Running app..."
	@./venv/bin/python -m Project.main

run:
	@./venv/bin/python -m Project.main

install:
	@echo "Installing dependencies..."
	@./venv/bin/python -m pip install -r requirements.txt

restart:
	@echo "Recreating virtual environment..."
	@rm -rf venv
	@python3 -m venv venv
	@./venv/bin/python -m pip install -r requirements.txt

fix:
	@ruff check . --fix
	@ruff format .