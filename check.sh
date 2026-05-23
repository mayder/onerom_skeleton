#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

run_model_validations() {
  local script
  for script in     scripts/validate-required-files.sh     scripts/validate-paths.sh     scripts/validate-docs.sh     scripts/validate-rules.sh     scripts/validate-no-secrets.sh     scripts/validate-file-size.sh     scripts/validate-no-runtime-pkg-names.sh     scripts/validate-fixtures.sh     scripts/validate-layering.sh     scripts/validate-stack.sh; do
    [[ -x "$script" ]] || { echo "[check:modelo] ERROR: script obrigatório ausente ou sem execução: $script" >&2; exit 1; }
    "$script"
  done
}

run_model_validations

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
