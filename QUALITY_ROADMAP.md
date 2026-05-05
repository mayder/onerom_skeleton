# Qualidade, Arquitetura e Roadmap do Robo Onerom

Este arquivo define o padrao tecnico do robo gerado a partir do skeleton.

## Precedencia obrigatoria

1. `CODEX_PATHS.toml`: paths, arquivos oficiais e comando de check.
2. `QUALITY_ROADMAP.md`: workflow tecnico, arquitetura e Definition of Done.
3. `GOVERNANCA.md`: gates, riscos, rollback e operacao.
4. `DEMANDAS.md`: backlog executavel do robo.

## Regras tecnicas

1. Manter mudancas pequenas, isoladas e revisaveis.
2. Separar entrada (`main.py`), casos de uso (`use_cases/`), entidades (`entities/`), runtime/config e utilitarios.
3. Nao acoplar regra de negocio diretamente em `main.py`.
4. Validar entradas antes de processar arquivos, telas, APIs, credenciais ou sistemas externos.
5. Usar `onerom_core` para status, logs, metricas, progresso e artefatos quando o robo rodar pelo Onerom.
6. Manter modo local/smoke sem backend real para desenvolvimento e testes.
7. Nao versionar segredos, dados reais de cliente, evidencias sensiveis ou arquivos temporarios.

## Baseline

- Python: `>=3.11`.
- Gerenciador: `uv`.
- Runtime Onerom: `onerom-core`.
- Gate minimo: `ruff` e `pytest` pelo `check.sh`.

## Estrutura esperada

- `main.py`: entrada unica do robo.
- `config/`: settings e montagem de dependencias.
- `runtime/`: contrato com env/contexto do Onerom.
- `entities/`: DTOs e estruturas tipadas.
- `use_cases/`: regras e fluxos de negocio.
- `abstract/`: catalogo de elementos e locators.
- `resources/`: imagens, fixtures e artefatos locais publicaveis.
- `tests/`: smoke e testes unitarios essenciais.

## Definition of Done

1. Demanda implementada no menor escopo possivel.
2. Contrato runtime preservado.
3. Entradas e falhas tratadas com mensagens objetivas.
4. Evidencias, logs e artefatos sensiveis protegidos.
5. Documentacao atualizada quando houver mudanca de contrato, setup ou operacao.
6. `./check.sh` verde.
7. Item correspondente marcado em `DEMANDAS.md` somente depois da validacao.

## Banco de dados

Robos gerados nao devem criar migrations. Se algum robo precisar de banco local ou externo, a decisao precisa estar documentada em `DEMANDAS.md` e em `GOVERNANCA.md`, com rollback explicito.
