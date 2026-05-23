# Demandas do Robo Onerom

Este arquivo e o backlog executavel do robo gerado. Ele deve ser preenchido pelo AI Builder Runner a partir do workflow aprovado antes da implementacao dos lotes.

## Precedencia

1. `CODEX_PATHS.toml`
2. `QUALITY_ROADMAP.md`
3. `GOVERNANCA.md`
4. `DEMANDAS.md`

## Regras de uso

- Cada pacote deve ter objetivo, escopo, criterios de aceite e validacao.
- Cada lote deve ser pequeno o suficiente para implementar, testar e revisar.
- Marcar `- [x]` somente depois de validar o lote.
- Registrar evidencia objetiva no proprio pacote quando houver execucao, artefato ou decisao relevante.
- Nao duplicar regras de governanca ja definidas em `GOVERNANCA.md`.
- `./check.sh` falha se um lote concluido nao tiver `evidencia:` ou `validacao:`.
- `./check.sh` falha se um pacote com `Status atual: concluido.` ainda tiver checkbox pendente.

## Template de pacote

### [PKG-001] Titulo do pacote

Contexto: descreva o problema, o fluxo aprovado e o resultado esperado.

Status atual: planejado.

- [ ] [exec] **Lote 1 - Titulo do lote**
  - objetivo: descreva o objetivo do lote.
  - escopo:
    - [ ] item implementavel;
    - [ ] item implementavel;
  - validacao:
    - [ ] comando ou roteiro de validacao.

- [ ] [validacao] **Criterios de aceite do pacote**
  - [ ] `./check.sh` verde;
  - [ ] fluxo principal validado;
  - [ ] evidencias registradas quando aplicavel.

---

## Modelo de trabalho IA - 2026-05-22

Projeto: `onerom_skeleton`. Stack: Template Onerom, pytest, ruff. Este arquivo segue o modelo oficial em `PATHS.toml` e deve ser atualizado ao iniciar ou alterar o projeto.

## Quando criar pacote

Criar pacote quando houver varias demandas relacionadas, risco transversal, mudanca em mais de um modulo ou necessidade de dividir entrega em lotes. Um lote pode resolver uma ou mais demandas, mas o pacote so fecha apos check completo e review de fechamento.
