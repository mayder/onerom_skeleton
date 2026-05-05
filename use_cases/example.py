"""Exemplo minimo de caso de uso gerado."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path

from use_cases.base import UseCase

logger = logging.getLogger(__name__)


class ExampleUseCase(UseCase):
    """Smoke funcional que prova entradas, saidas, logs e metricas."""

    def execute(self) -> Path:
        logger.info("Iniciando caso de uso exemplo")

        summary = {
            "generated_at": datetime.now(UTC).isoformat(),
            "offline": self.runtime.is_offline,
            "bot_name": self.runtime.bot_name,
            "parameters": self.runtime.parameters,
            "conventions": {
                "inputs": str(self.runtime.settings.inputs_dir),
                "outputs": str(self.runtime.settings.outputs_dir),
                "evidence": str(self.runtime.settings.evidence_dir),
                "artifacts": str(self.runtime.settings.artifacts_dir),
                "logs": str(self.runtime.settings.logs_dir),
            },
        }
        output_path = self.runtime.settings.outputs_dir / "summary.json"
        output_path.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        logger.info("Resumo escrito em %s", output_path)
        self.execution.add_success_item()
        return output_path
