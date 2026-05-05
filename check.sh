#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv nao encontrado. Instale o uv antes de validar o robo." >&2
  exit 1
fi

uv sync --group dev

uv run ruff format --check .
uv run ruff check .

uv run python - <<'PY'
import importlib

modules = (
    "main",
    "abstract",
    "abstract.elements",
    "use_cases",
    "use_cases.base",
    "use_cases.example",
    "runtime",
    "runtime.context",
    "runtime.evidence",
)

for module in modules:
    importlib.import_module(module)

print("Import smoke ok")
PY

uv run pytest tests
uv run python scripts/validate_demands.py
