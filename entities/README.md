# entities

Camada responsável pela definição das estruturas de dados do bot.  
Layer responsible for defining the bot's data structures.

---

## Responsabilidades / Responsibilities

- Declarar os DTOs (Data Transfer Objects) utilizados para trafegar dados entre as camadas.  
  Declare DTOs (Data Transfer Objects) used to transfer data between layers.
- Garantir tipagem e validação dos dados via `Pydantic`.  
  Ensure typing and data validation via `Pydantic`.
- Representar entidades de domínio e de sistemas externos (ex: SAP, planilhas, APIs).  
  Represent domain entities and external system entities (e.g. SAP, spreadsheets, APIs).

---

## O que pertence aqui / What belongs here

- DTOs de entrada e saída de use cases. / Input and output DTOs for use cases.
- Modelos de credenciais de sistemas (ex: `CredentialSap`). / System credential models (e.g. `CredentialSap`).
- Qualquer estrutura de dado que precise ser validada ou tipada. / Any data structure that needs to be validated or typed.

---

## O que NÃO pertence aqui / What does NOT belong here

- Lógica de negócio ou processamento. / Business logic or processing.
- Chamadas a sistemas externos. / Calls to external systems.
- Configurações de ambiente. / Environment configurations.

---

## Exemplo de uso / Usage example

```python
from entities.dto_example import ClienteDTO

cliente = ClienteDTO(id=1, nome="João", email="joao@email.com", telefone="11999999999")
```
