# Validacao final do skeleton

## Resultado

Status: aprovado para uso como base publica inicial.

Data: 2026-05-05.

## Checks executados

```bash
./check.sh
```

Resultado esperado:

- `uv sync --group dev`: verde;
- `ruff format --check .`: verde;
- `ruff check .`: verde;
- import smoke de `main.py`, `abstract`, `use_cases` e `runtime`: verde;
- `pytest tests`: verde;
- `scripts/validate_demands.py`: verde.

## Estrutura obrigatoria confirmada

- `abstract/`
- `use_cases/`
- `resources/`
- `tests/`
- `main.py`
- `CODEX_PATHS.toml`
- `QUALITY_ROADMAP.md`
- `GOVERNANCA.md`
- `DEMANDAS.md`

## Banco de dados

Nao ha banco envolvido no skeleton.

Verificacao recomendada antes de publicar:

```bash
find . -maxdepth 3 \( -iname '*migration*' -o -iname '*alembic*' -o -path '*/sql/*' -o -name '*.sql' \) -print
```

Resultado esperado: nenhum arquivo encontrado.

## Simulacao de consumo pelo Builder

O AI Builder Runner deve consumir o skeleton por tag, SHA ou release artifact e criar um workspace isolado para o robo gerado.

Validacao recomendada no workspace gerado:

```bash
BOT_PROJECT_ROOT="$(mktemp -d)" uv run python main.py
./check.sh
```

Resultado esperado:

- `./check.sh` verde;
- `outputs/summary.json` gerado;
- evidencia local JSON gerada em `evidence/`;
- skeleton pronto para receber demandas geradas pelo AI Builder Runner.

## Publicacao

O repositorio publico deve ser criado como `onerom_skeleton`.

Regra de publicacao:

1. Copiar o estado atual limpo para o repositorio publico.
2. Nao preservar historico de outro repositorio.
3. Rodar `./check.sh`.
4. Criar a tag inicial `v0.1.0`.
5. Configurar consumidores para usar tag, SHA ou release artifact.
