#!/usr/bin/env bash
set -euo pipefail

# start.sh — installs deps (if needed) and runs the Flask app on $PORT (default 8000)
cd "$(dirname "$0")"

# Optional: activate .venv if present
if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

echo "Installing Python dependencies from requirements.txt (if any)..."
pip install -r requirements.txt

: ${PORT:=5000}
echo "Starting app on port $PORT"
export FLASK_ENV=development
export FLASK_RUN_PORT="$PORT"

python3 app.py
