# Governanca do Robo Onerom

Este arquivo define gates, riscos, evidencias e rollback para um robo gerado a partir do skeleton.

## Gates de pronto

### Qualidade

- `./check.sh` verde.
- Fluxo principal validado em modo local/smoke.
- Codigo simples, explicito e compativel com Python 3.11.
- `main.py` apenas orquestra entrada e saida; regra de negocio fica em `use_cases/`.

### Seguranca

- Nenhum segredo, token, credencial, cookie, print sensivel ou dado real de cliente versionado.
- Entradas externas validadas antes de uso.
- Logs nao devem expor credenciais, documentos, dados pessoais ou payloads sensiveis completos.
- Arquivos em `resources/` devem ser exemplos publicaveis ou fixtures anonimizadas.

### Operacao

- Falhas devem retornar erro objetivo e exit code compativel com o runner.
- Execucao local sem backend real deve continuar disponivel para smoke.
- Evidencias e artefatos devem ser salvos/uploadados apenas quando permitido pelo contrato do robo.

### Suporte

- Setup e comandos locais documentados.
- Mudancas de parametro, entrada, saida ou dependencia devem atualizar `README.md` e `DEMANDAS.md`.

## Evidencias minimas

- Comando executado.
- Resultado do `./check.sh`.
- Resumo do fluxo validado.
- Risco residual, quando existir.

## Riscos principais

| Area | Risco | Mitigacao | Rollback |
|---|---|---|---|
| Runtime | Quebrar contrato com o runner | Smoke local e uso de `onerom_core` | Reverter mudanca do contrato |
| Dados | Vazar segredo ou dado real | `.env.example`, fixtures anonimas e revisao antes de publicar | Remover arquivo, rotacionar segredo e republicar |
| Automacao | Usar locator fragil ou sem rastreio | Registrar elementos em `abstract/` | Voltar para locator anterior |
| IA Builder | Marcar demanda como pronta sem validacao | `./check.sh` e evidencia no lote | Reabrir item no `DEMANDAS.md` |

## Priorizacao

1. P0: seguranca, segredos, credenciais, isolamento e contrato runtime.
2. P1: confiabilidade do fluxo principal e checks.
3. P2: refino de estrutura, documentacao e cobertura adicional.

## Relacao com outros arquivos

- `CODEX_PATHS.toml`: paths e check oficial.
- `QUALITY_ROADMAP.md`: workflow tecnico e Definition of Done.
- `DEMANDAS.md`: backlog executavel do robo.

---

## Modelo de trabalho IA - 2026-05-22

Projeto: `onerom_skeleton`. Stack: Template Onerom, pytest, ruff. Este arquivo segue o modelo oficial em `PATHS.toml` e deve ser atualizado ao iniciar ou alterar o projeto.

## Banco e governanca tecnica

- Migrations são proibidas. Alteracoes de banco devem ser entregues como scripts `.sql`, preferencialmente idempotentes.
- Mudancas com risco transversal exigem rollback, evidencia de teste e registro em `DECISOES.md` quando criarem padrao duradouro.
