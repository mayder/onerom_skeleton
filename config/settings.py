"""Settings locais do robo gerado."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _bool_from_env(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "sim", "on"}


@dataclass(frozen=True)
class BotSettings:
    """Configuracao minima, sem dependencia externa alem da stdlib."""

    project_root: Path
    inputs_dir: Path
    outputs_dir: Path
    evidence_dir: Path
    artifacts_dir: Path
    logs_dir: Path
    local_mode: bool
    log_level: str

    @classmethod
    def from_env(cls) -> "BotSettings":
        root = Path(os.environ.get("BOT_PROJECT_ROOT", ".")).resolve()
        return cls(
            project_root=root,
            inputs_dir=Path(os.environ.get("BOT_INPUTS_DIR", root / "inputs")),
            outputs_dir=Path(os.environ.get("BOT_OUTPUTS_DIR", root / "outputs")),
            evidence_dir=Path(os.environ.get("BOT_EVIDENCE_DIR", root / "evidence")),
            artifacts_dir=Path(os.environ.get("BOT_ARTIFACTS_DIR", root / "artifacts")),
            logs_dir=Path(os.environ.get("BOT_LOGS_DIR", root / "logs")),
            local_mode=_bool_from_env(os.environ.get("BOT_LOCAL_MODE"), default=True),
            log_level=os.environ.get("BOT_LOG_LEVEL", "INFO").upper(),
        )

    def managed_dirs(self) -> tuple[Path, ...]:
        return (
            self.inputs_dir,
            self.outputs_dir,
            self.evidence_dir,
            self.artifacts_dir,
            self.logs_dir,
        )
