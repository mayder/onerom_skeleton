# Contributing

This repository is a base skeleton for generated Onerom bots.

## Minimum rules

1. Read `CODEX_PATHS.toml`, then `QUALITY_ROADMAP.md`, then `GOVERNANCA.md`, then `DEMANDAS.md`.
2. Keep changes small and scoped to the active demand.
3. Do not commit secrets, real credentials, customer data, screenshots with sensitive data, cookies, local paths, or private URLs.
4. Use `uv` for dependency management.
5. Run `./check.sh` before opening a change.
6. Mark a demand item as done only after validation evidence exists.

## Local setup

```bash
uv sync --group dev
cp .env.example .env
./check.sh
```

## Release changes

Every release must use a versioned tag. The AI Builder Runner should clone a tag, not a moving branch.
