# Public repository preparation

Date: 2026-05-05

## Goal

Prepare the current skeleton content to be copied into the public `onerom_skeleton` repository without depending on a local source-repository path.

## Final identity

- Repository name: `onerom_skeleton`
- Repository URL: `https://github.com/mayder/onerom_skeleton`
- Python project name: `onerom_skeleton`
- Initial version: `0.1.0`
- License: MIT
- Runtime baseline: Python `>=3.11`
- Package manager: `uv`

## Files aligned

- `pyproject.toml`: renamed from `template_onerom` to `onerom_skeleton` and filled with license, keywords, classifiers and public URLs.
- `README.md`: describes the public skeleton, bootstrap, runtime contract, AI Builder Runner usage and publication flow.
- `main.py`: logger renamed to `onerom_skeleton`.
- `docs/VERSIONING.md`: public identity updated to `onerom_skeleton`.
- `docs/DIAGNOSTICO_TEMPLATE.md`: historical diagnostics updated to the current public-ready state.

## Publication rule

Publish by copying the current clean tree into a new `onerom_skeleton` repository. Do not preserve source-repository history, because old commits included a deprecated `onerom.env` placeholder file.

## Validation

Run before creating the first tag:

```bash
./check.sh
```

The first public tag should be created only after the check is green in the standalone repository.
