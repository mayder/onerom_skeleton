# Diagnostico do skeleton atual

## Estado validado

- `pyproject.toml`: projeto Python publico `onerom_skeleton` com `onerom-core>=0.2.5`, `pytest` e `ruff`.
- `.python-version`: alinhado para Python 3.11, baseline publico do skeleton.
- `main.py`: entrada unica do robo, com logger `onerom_skeleton` e orquestracao do runtime local/Onerom.
- `config/`: possui README e `settings.py` com leitura defensiva de ambiente.
- `entities/`, `use_cases/`, `utils/`: possuem estrutura minima para expansao pelo AI Builder Runner.
- `resources/`, `abstract/`, `runtime/`, `tests`, `check.sh`, `CODEX_PATHS.toml`, `QUALITY_ROADMAP.md`, `GOVERNANCA.md`, `DEMANDAS.md` e `.env.example`: presentes no estado atual do skeleton.
- `onerom.env`: removido do estado atual; nao deve existir no repositorio publico.

## Decisao de Python

O template original estava em Python `>=3.12`, mas o runner operacional e o skeleton publico usam Python 3.11 como baseline.

Decisao: o skeleton deve usar Python `>=3.11` para manter compatibilidade com o runner operacional, checks locais e ambientes de desenvolvimento.

## Dependencias

### Mantidas

- `onerom-core>=0.2.5`: dependencia essencial para contrato com runner, status, logs, metricas e artefatos.
- `pytest`: necessario para o smoke minimo do skeleton.
- `ruff`: necessario para lint/format no gate oficial.

### Removidas

- `ipykernel`: nao e necessario para robos gerados em runtime operacional.
- `taskipy`: nao existe uso atual no template e adiciona comando indireto desnecessario.
- `pytest-cov`: cobertura ainda nao e gate do skeleton; pode voltar quando houver politica objetiva de cobertura.

## Estado para publicacao

- Governanca local presente: `CODEX_PATHS.toml`, `QUALITY_ROADMAP.md`, `GOVERNANCA.md` e `DEMANDAS.md`.
- Estrutura oficial presente: `abstract/`, `resources/`, `tests/`, `runtime/` e `use_cases/`.
- `main.py` mantem entrada unica.
- `check.sh` executavel valida `uv`, `ruff`, imports, `pytest` e backlog.
- `.env.example` e publicavel e nao contem token operacional.
- Contrato runtime documentado em `README.md`.
