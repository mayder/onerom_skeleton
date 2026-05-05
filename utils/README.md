# utils

Camada responsável por utilitários genéricos e reutilizáveis do projeto.  
Layer responsible for generic, reusable project utilities.

---

## Responsabilidades / Responsibilities

- Prover funções auxiliares sem vínculo com o domínio de negócio do bot.  
  Provide helper functions with no ties to the bot's business domain.
- Centralizar operações repetitivas de infraestrutura (ex: manipulação de arquivos, leitura de metadados do projeto, atualização de dependências internas).  
  Centralize repetitive infrastructure operations (e.g. file manipulation, reading project metadata, updating internal dependencies).
- Isolar código de suporte para evitar duplicação entre use cases.  
  Isolate support code to avoid duplication across use cases.

---

## O que pertence aqui / What belongs here

- Helpers de manipulação de arquivos e caminhos. / File and path manipulation helpers.
- Funções de leitura de configurações do projeto (`pyproject.toml`). / Functions for reading project settings (`pyproject.toml`).
- Utilitários de ambiente de desenvolvimento (ex: `ensure_libs_updated`). / Development environment utilities (e.g. `ensure_libs_updated`).
- Qualquer função genérica reutilizável em múltiplos contextos. / Any generic function reusable across multiple contexts.

---

## O que NÃO pertence aqui / What does NOT belong here

- Lógica de negócio do bot. / Bot business logic.
- DTOs ou entidades de domínio. / DTOs or domain entities.
- Configurações de ambiente (use `config/`). / Environment configurations (use `config/`).

---

## Exemplo de uso / Usage example

```python
from utils.py_utils import obter_nome_arquivo

nome = obter_nome_arquivo("/caminho/para/arquivo.xlsx")
# retorna / returns: "arquivo"
```
