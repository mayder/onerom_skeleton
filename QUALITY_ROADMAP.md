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

---

## Modelo de trabalho IA - 2026-05-22

Projeto: `onerom_skeleton`. Stack: Template Onerom, pytest, ruff. Este arquivo segue o modelo oficial em `PATHS.toml` e deve ser atualizado ao iniciar ou alterar o projeto.

## Regras essenciais do modelo

- SOLID e separacao de responsabilidades sao obrigatorios para qualquer implementacao.
- Leitura mínima por tipo de tarefa: seguir `PATHS.toml` e abrir somente os arquivos necessarios para pacote, bug, UI, arquitetura ou docs.
- Resposta final curta: informar o que foi feito, bloqueios e como validar.
- Se a branch atual for `main` ou `hml`, confirmar com o usuario antes de alterar, exceto quando ja houver autorizacao explicita para o lote.
- Nunca usar migrations. Mudancas de banco devem ser scripts `.sql`, preferencialmente idempotentes, com ordem e rollback.
- Observabilidade mínima da aplicação: logs estruturados, correlacao quando aplicavel, metricas/auditoria proporcionais ao risco e sem criar tabelas desnecessarias.
- Toda observabilidade persistida precisa de retenção e limpeza documentadas.
- Review de fechamento de pacote: revisar bugs, regressao, arquitetura, testes, docs, riscos e rollback antes de encerrar.
- Contrato de módulo: cada modulo deve declarar responsabilidade, entrada, saida, erros, dependencias e limites de camada.
- Nomenclatura oficial do projeto: registrar nomes aprovados para service, use case, repository, adapter, DTO/schema, controller/route e evitar sinonimos sem decisao.
- Adaptação à arquitetura real: ao aplicar este modelo em projeto real, a IA deve inspecionar linguagem, framework, pastas, comandos, testes e convencoes antes de editar.
- Decisoes arquiteturais devem ser registradas em `DECISOES.md` usando o formato `DEC-YYYYMMDD-01`.
- Check adaptável por stack: `check.sh` deve chamar validacoes do modelo e os comandos reais da linguagem/framework do projeto.
