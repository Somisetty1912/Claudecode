#!/usr/bin/env bash
# pre-commit-check.sh
# Runs flake8 + mypy type check before commit.
# Called by .pre-commit-config.yaml or manually before git commit.
#
# Usage: bash hooks/pre-commit-check.sh [file_or_dir]
# If no argument is given, checks the entire project.

set -euo pipefail

TARGET="${1:-.}"
FAILED=0

echo "[pre-commit-check] Running pre-commit checks on: $TARGET"

# --- flake8 ---
if command -v flake8 &>/dev/null; then
  echo "[pre-commit-check] Running flake8..."
  if flake8 --max-line-length=88 --extend-ignore=E203,W503 "$TARGET"; then
    echo "[pre-commit-check] flake8: passed"
  else
    echo "[pre-commit-check] flake8: FAILED" >&2
    FAILED=1
  fi
else
  echo "[pre-commit-check] flake8 not found, skipping" >&2
fi

# --- mypy ---
if command -v mypy &>/dev/null; then
  echo "[pre-commit-check] Running mypy..."
  MYPY_ARGS=(
    --ignore-missing-imports
    --disallow-untyped-defs
    --disallow-any-generics
    --warn-return-any
    --no-error-summary
  )
  if mypy "${MYPY_ARGS[@]}" "$TARGET"; then
    echo "[pre-commit-check] mypy: passed"
  else
    echo "[pre-commit-check] mypy: FAILED" >&2
    FAILED=1
  fi
else
  echo "[pre-commit-check] mypy not found, skipping" >&2
fi

# --- Summary ---
if [[ $FAILED -eq 0 ]]; then
  echo "[pre-commit-check] All checks passed."
  exit 0
else
  echo "[pre-commit-check] One or more checks FAILED. Fix the issues above before committing." >&2
  exit 1
fi
