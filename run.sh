#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "=========================================="
echo "       OS RESOURCE MANAGER"
echo "=========================================="
mkdir -p logs reports screenshots
PYTHON_BIN="${PYTHON:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "Python 3 is required. Set PYTHON to its executable if it is not named python3."
  exit 1
fi
"$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 9) else "Python 3.9 or newer is required.")'

case "${1:-}" in
  "")
    "$PYTHON_BIN" main.py
    ;;
  --test)
    "$PYTHON_BIN" -m unittest discover -s tests -v
    ;;
  --help|-h)
    echo "Usage: ./run.sh [--test|--help]"
    echo "  (no option)  Start the interactive simulator"
    echo "  --test       Run the automated unittest suite"
    ;;
  *)
    echo "Unknown option: $1"
    echo "Usage: ./run.sh [--test|--help]"
    exit 2
    ;;
esac
