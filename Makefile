.PHONY: help start run install restart fix

PYTHON = ./venv/bin/python

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
	@$(PYTHON) -m pip install -r requirements.txt
	@echo "Running app..."
	@$(PYTHON) -m Project.main

# run:
# 	@$(PYTHON) -m Project.main

run:
	@$(PYTHON) -m uvicorn Project.main:app --reload --port 8000

run-prod:
	@$(PYTHON) -m uvicorn Project.main:app --workers 4 --port 8000

install:
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install -r requirements.txt

restart:
	@echo "Recreating virtual environment..."
	@rm -rf venv
	@python3 -m venv venv
	@$(PYTHON) -m pip install -r requirements.txt

fix:
	@ruff check . --fix
	@ruff format .