"""Valida regras minimas do DEMANDAS.md do robo."""

from __future__ import annotations

from pathlib import Path


BACKLOG = Path("DEMANDAS.md")


def _line_number(lines: list[str], index: int) -> int:
    return index + 1


def _has_pending_checkbox(lines: list[str], start: int, end: int) -> bool:
    return any("- [ ]" in line for line in lines[start:end])


def _block_has_evidence_or_validation(lines: list[str], start: int, end: int) -> bool:
    block = "\n".join(lines[start:end]).lower()
    return "evidencia:" in block or "validacao:" in block or "validação:" in block


def validate_backlog(path: Path = BACKLOG) -> list[str]:
    if not path.exists():
        return [f"{path} nao encontrado"]

    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    for index, line in enumerate(lines):
        normalized = line.strip().lower()
        if normalized == "status atual: concluido.":
            next_pkg = next(
                (i for i in range(index + 1, len(lines)) if lines[i].startswith("### [PKG-")),
                len(lines),
            )
            if _has_pending_checkbox(lines, index + 1, next_pkg):
                errors.append(f"linha {_line_number(lines, index)}: pacote concluido ainda contem checkbox pendente")

        if "- [x]" in line and "**lote" in normalized:
            next_lot = next(
                (
                    i
                    for i in range(index + 1, len(lines))
                    if ("- [ ]" in lines[i] or "- [x]" in lines[i]) and "**lote" in lines[i].lower()
                ),
                len(lines),
            )
            if not _block_has_evidence_or_validation(lines, index + 1, next_lot):
                errors.append(
                    f"linha {_line_number(lines, index)}: lote marcado como concluido sem evidencia ou validacao"
                )

    return errors


def main() -> int:
    errors = validate_backlog()
    if errors:
        print("DEMANDAS.md invalido:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DEMANDAS.md ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
