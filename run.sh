#!/usr/bin/env bash
set -e

if [ -n "$1" ] && [ "$1" != "reset" ] && [ "$1" != "update" ]; then
    echo "Unknown command: $1 (use: reset, update, or no argument)"
    exit 1
fi

if [ "$1" = "reset" ]; then
    echo "Removing old virtual environment and creating new one..."
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
fi

if [ "$1" = "update" ]; then
    echo "Updating virtual environment..."
    source venv/bin/activate
    python -m pip install -r requirements.txt
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
fi

source venv/bin/activate
python -m Project.main