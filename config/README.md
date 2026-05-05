# config

Camada responsável pela injeção de dependências do bot.  
Layer responsible for dependency injection of the bot.

---

## Responsabilidades / Responsibilities

- Instanciar e fornecer as dependências utilizadas pelo bot (clientes de API, conexões, serviços externos, etc.).  
  Instantiate and provide the dependencies used by the bot (API clients, connections, external services, etc.).
- Centralizar as configurações em uma única classe `BotSettings`, carregando variáveis de ambiente sem dependência externa obrigatória.
  Centralize settings in a single `BotSettings` class, loading environment variables without a required external dependency.
- Servir como ponto único de montagem das dependências, desacoplando os use cases das implementações concretas.  
  Serve as the single assembly point for dependencies, decoupling use cases from concrete implementations.

---

## O que pertence aqui / What belongs here

- `settings.py` — classe `BotSettings` com os campos tipados das variáveis de ambiente. / `BotSettings` class with typed environment variable fields.
- Fábricas ou funções que instanciam clientes e serviços externos (ex: cliente SAP, conexão com banco, cliente de API).  
  Factories or functions that instantiate external clients and services (e.g. SAP client, database connection, API client).

---

## O que NÃO pertence aqui / What does NOT belong here

- Lógica de negócio. / Business logic.
- DTOs ou entidades de domínio (use `entities/`). / DTOs or domain entities (use `entities/`).
- Funções auxiliares genéricas (use `utils/`). / Generic helper functions (use `utils/`).

---

## Exemplo de uso / Usage example

```python
from config.settings import BotSettings

settings = BotSettings.from_env()
# settings carrega automaticamente as variáveis do .env
# settings automatically loads variables from .env
```
