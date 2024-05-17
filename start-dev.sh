#!/bin/sh

# Create venv and install requirements if not exist
if [ ! -e '.venv/' ]; then
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
fi

# Start flask server
.venv/bin/flask --app "app:create_app()" run -h 0.0.0.0 -p 5002 --debug --reload