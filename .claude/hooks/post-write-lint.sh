#!/usr/bin/env bash
# post-write-lint.sh
# Runs black + isort on the written file, then flake8 (non-blocking warnings).
# Called by Claude Code's PostToolUse hook after Write or Edit on a .py file.
#
# Usage: bash hooks/post-write-lint.sh <file_path>

set -euo pipefail

FILE="${1:-}"

if [[ -z "$FILE" ]]; then
  echo "[post-write-lint] No file path provided, skipping." >&2
  exit 0
fi

# Only run on Python files
if [[ "$FILE" != *.py ]]; then
  exit 0
fi

# Verify the file exists
if [[ ! -f "$FILE" ]]; then
  echo "[post-write-lint] File not found: $FILE" >&2
  exit 0
fi

echo "[post-write-lint] Linting $FILE"

# --- black ---
if command -v black &>/dev/null; then
  black --quiet "$FILE" && echo "[post-write-lint] black: ok" || {
    echo "[post-write-lint] black: failed (check syntax)" >&2
    exit 1
  }
else
  echo "[post-write-lint] black not found, skipping formatting" >&2
fi

# --- isort ---
if command -v isort &>/dev/null; then
  isort --quiet "$FILE" && echo "[post-write-lint] isort: ok" || {
    echo "[post-write-lint] isort: failed" >&2
    exit 1
  }
else
  echo "[post-write-lint] isort not found, skipping import sorting" >&2
fi

# --- flake8 (non-blocking — warnings only) ---
if command -v flake8 &>/dev/null; then
  flake8 --max-line-length=88 --extend-ignore=E203,W503 "$FILE" \
    && echo "[post-write-lint] flake8: clean" \
    || echo "[post-write-lint] flake8: warnings above (non-blocking)" >&2
else
  echo "[post-write-lint] flake8 not found, skipping style check" >&2
fi

exit 0
