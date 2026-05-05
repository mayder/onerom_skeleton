# Versioning and releases

The public skeleton must be consumed by version, not by branch.

## Tag format

Use semantic version tags:

```text
vMAJOR.MINOR.PATCH
```

Examples:

- `v0.1.0`: first public skeleton.
- `v0.2.0`: backward-compatible new structure or optional helpers.
- `v1.0.0`: stable contract for AI Builder Runner consumption.

## Release rule

Before creating a tag:

1. Run `./check.sh`.
2. Confirm `.env` and generated folders are not tracked.
3. Confirm `README.md`, `QUALITY_ROADMAP.md`, `GOVERNANCA.md`, and `DEMANDAS.md` match the runtime contract.
4. Confirm no local paths, customer names, credentials, or private URLs are present.

## Builder consumption

The AI Builder Runner must receive one of:

- a tag, for example `v0.1.0`;
- a commit SHA;
- a release artifact generated from a tag.

It must not clone `main` or another moving branch as the default source for generated robots.

## Repository identity

The public repository name and Python project name are both `onerom_skeleton`.

Generated robot projects may replace this name after cloning or unpacking the skeleton, but the public skeleton itself must keep the `onerom_skeleton` identity.
