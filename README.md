# onerom_skeleton

Base publica para robos Python executados pelo Onerom Runner e para robos gerados pelo AI Builder Runner.

## Metadados

- Projeto Python: `onerom_skeleton`
- Versao inicial: `0.1.0`
- Licenca: MIT
- Runtime: Python `>=3.11`
- Gerenciador: `uv`
- Dependencia principal: `onerom-core`

## Publico alvo

- Desenvolvedores humanos que precisam criar um robo Onerom com estrutura previsivel.
- AI Builder Runner, que clona uma versao do skeleton e implementa demandas lote a lote.
- Spy, que fornece locators, imagens, coordenadas e contexto real para preencher `abstract/elements.py`.

## Requisitos

- Python >= 3.11
- `uv`

O Onerom usa `pyproject.toml` e `uv` como contrato de ambiente. Nao use `pip`, `venv`, `poetry` ou arquivos locais para instalar dependencias fora desse contrato.

## Bootstrap local

```bash
uv sync --group dev
cp .env.example .env
./check.sh
```

## Validacao oficial

```bash
./check.sh
```

O gate oficial executa:

- `uv sync --group dev`;
- `ruff format --check`;
- `ruff check`;
- import smoke de `main.py`, `abstract`, `use_cases` e `runtime`;
- `pytest tests`;
- validacao do `DEMANDAS.md` para impedir lote concluido sem evidencia/validacao e pacote concluido com pendencias abertas.

## Execucao local de smoke

```bash
uv run python main.py
```

Smoke local isolado:

```bash
BOT_PROJECT_ROOT="$(mktemp -d)" uv run python main.py
```

Sem `ONEROM_EXECUTION_ID`, o robo opera em modo local fake/smoke, sem backend real e sem exigir URL publica.

## Contrato runtime

Variaveis oficiais consumidas pelo skeleton:

- `ONEROM_CONTEXT`: contexto completo da execucao, incluindo execution, bot, runner e parameters.
- `ONEROM_PARAMETERS`: parametros diretos da execucao.
- `ONEROM_API_URL`: base da API usada pelo `onerom_core` e pelo upload de evidencias.
- `ONEROM_RUNNER_KEY`: chave do runner para chamadas ao runner-agent.
- `ONEROM_EXECUTION_ID`: id da execucao atual.
- `ONEROM_BOT_NAME`: nome do robo.
- `ONEROM_RUNNER_ID`: id do runner.
- `ONEROM_METRICS_FILE`: arquivo de metricas lido pelo runner.
- `ONEROM_ENV_FILE`: caminho do `.env` injetado pelo runner, quando existir.

## Convencoes de arquivos

- `inputs/`: arquivos de entrada locais.
- `outputs/`: resultados gerados.
- `evidence/`: evidencias de execucao e fallback local.
- `artifacts/`: arquivos publicaveis ou uploadaveis.
- `logs/`: logs locais quando necessario.
- `resources/`: imagens e fixtures publicaveis usadas pela automacao.

Esses diretorios de runtime sao ignorados pelo Git.

## Estrutura

```text
onerom_skeleton/
├── abstract/        # Catalogo de elementos e locators
├── config/          # Configuracoes do robo
├── entities/        # Entidades de dominio e DTOs
├── resources/       # Imagens e fixtures publicaveis
├── runtime/         # Contrato com runner/env/evidencias
├── scripts/         # Validadores locais
├── tests/           # Smoke e testes minimos
├── use_cases/       # Regras de negocio
├── utils/           # Utilitarios
├── main.py          # Entrada unica
├── pyproject.toml   # Configuracao do projeto e dependencias
└── uv.lock          # Lock file gerado pelo uv
```

## Uso pelo AI Builder Runner

1. Clonar uma tag, release artifact ou SHA fixo do repositorio `onerom_skeleton`.
2. Preencher `DEMANDAS.md` a partir do workflow aprovado.
3. Implementar um lote por vez.
4. Registrar locators capturados pelo Spy em `abstract/elements.py`.
5. Rodar `./check.sh`.
6. Marcar lotes como concluidos somente com evidencia ou validacao.

## Uso pelo Spy

O Spy nao executa desenvolvimento pesado. Ele deve produzir contexto para o Builder:

- seletores CSS/XPath;
- texto visivel;
- imagens de referencia;
- coordenadas;
- desktop locators;
- ids de sistemas como SAP.

Esses dados devem virar entradas rastreaveis em `abstract/elements.py` e arquivos publicaveis em `resources/`, nunca dados sensiveis reais.

## Versionamento

O Builder deve consumir o skeleton por tag, commit SHA ou release artifact. Nao use branch movel como fonte padrao.

Formato de tag:

```text
vMAJOR.MINOR.PATCH
```

Mais detalhes em `docs/VERSIONING.md`.

## Publicacao

Para publicar este skeleton em um repositorio separado:

1. Copie o estado atual limpo para o repositorio `onerom_skeleton`.
2. Nao preserve historico local de outro repositorio.
3. Execute `./check.sh` no repositorio novo.
4. Crie a tag inicial `v0.1.0` somente depois do gate verde.
5. Configure o AI Builder Runner para consumir tag, SHA ou release artifact.
