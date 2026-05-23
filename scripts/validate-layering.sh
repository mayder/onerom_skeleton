#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
log "validando arquitetura por camadas"
enabled="$(toml_string_value quality.layering enabled)"
if [[ "$enabled" != "true" ]]; then log "quality.layering.enabled=false; pulando validação de camadas no modelo"; exit 0; fi
if [[ "${STRICT_PYTHON_LAYERING:-0}" != "1" ]]; then
  log "modo legado: layering Python estrito desativado; use STRICT_PYTHON_LAYERING=1"
  exit 0
fi
runtime_dirs=()
while IFS= read -r dir; do [[ -n "$dir" ]] && runtime_dirs+=("$dir"); done < <(toml_array_values quality runtime_dirs)
for dir in "${runtime_dirs[@]}"; do [[ -d "$dir" ]] || fail "runtime_dir inexistente: $dir"; done
if grep -RInE 'from (fastapi|sqlalchemy|sqlmodel|pydantic_settings)|import (fastapi|sqlalchemy|sqlmodel)' "${runtime_dirs[@]}"   --include='*.py' --exclude-dir=.venv --exclude-dir=venv --exclude-dir=dist --exclude-dir=build --exclude-dir=__pycache__ | grep -E '/(domain|entities|use_cases)/'; then
  fail "camada de domínio/use_case não deve depender diretamente de framework/infra"
fi
