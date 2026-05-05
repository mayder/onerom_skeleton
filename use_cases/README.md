# use_cases

Camada responsável pela lógica de negócio do bot.  
Layer responsible for the bot's business logic.

---

## Responsabilidades / Responsibilities

- Implementar cada ação ou processo de negócio do bot como uma função isolada.  
  Implement each bot action or business process as an isolated function.
- Orquestrar o fluxo de dados entre entidades, utilitários e integrações.  
  Orchestrate the data flow between entities, utilities, and integrations.
- Receber DTOs como entrada e retornar resultados tipados.  
  Receive DTOs as input and return typed results.
- Registrar logs relevantes sobre o processamento.  
  Record relevant logs about the processing.

---

## O que pertence aqui / What belongs here

- Funções que representam um caso de uso específico do bot (ex: processar item, validar registro, enviar dados).  
  Functions that represent a specific bot use case (e.g. process item, validate record, send data).
- Regras de negócio e decisões de fluxo. / Business rules and flow decisions.

---

## O que NÃO pertence aqui / What does NOT belong here

- Configurações de ambiente (use `config/`). / Environment configurations (use `config/`).
- Definição de estruturas de dados (use `entities/`). / Data structure definitions (use `entities/`).
- Utilitários genéricos sem relação com negócio (use `utils/`). / Generic utilities unrelated to business logic (use `utils/`).
- Inicialização do bot ou chamadas ao framework (use `main.py`). / Bot initialization or framework calls (use `main.py`).

---

## Exemplo de uso / Usage example

```python
from use_cases.exemplo_use_case import processar_item
from entities.dto_example import ItemDTO

resultado = processar_item(item=ItemDTO(...), settings=settings)
```
