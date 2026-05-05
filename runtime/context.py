"""Contexto runtime normalizado para uso pelos casos de uso."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from config.settings import BotSettings


def _load_context() -> dict[str, Any]:
    raw = os.environ.get("ONEROM_CONTEXT", "")
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {"_invalid_context": raw}
    return data if isinstance(data, dict) else {"_raw_context": data}


@dataclass(frozen=True)
class RuntimeContext:
    """Dados normalizados que use cases podem consumir sem ler env diretamente."""

    settings: BotSettings
    parameters: dict[str, Any]
    onerom_context: dict[str, Any] = field(default_factory=dict)
    execution_id: str | None = None
    api_url: str | None = None
    runner_key: str | None = None
    runner_id: str | None = None
    bot_name: str | None = None
    metrics_file: Path | None = None
    env_file: Path | None = None

    @classmethod
    def from_env(
        cls,
        parameters: dict[str, Any] | None = None,
        settings: BotSettings | None = None,
    ) -> "RuntimeContext":
        metrics_file = os.environ.get("ONEROM_METRICS_FILE")
        env_file = os.environ.get("ONEROM_ENV_FILE")
        return cls(
            settings=settings or BotSettings.from_env(),
            parameters=parameters or {},
            onerom_context=_load_context(),
            execution_id=os.environ.get("ONEROM_EXECUTION_ID"),
            api_url=os.environ.get("ONEROM_API_URL"),
            runner_key=os.environ.get("ONEROM_RUNNER_KEY"),
            runner_id=os.environ.get("ONEROM_RUNNER_ID"),
            bot_name=os.environ.get("ONEROM_BOT_NAME"),
            metrics_file=Path(metrics_file) if metrics_file else None,
            env_file=Path(env_file) if env_file else None,
        )

    @property
    def is_offline(self) -> bool:
        return not self.execution_id

    @property
    def can_upload_evidence(self) -> bool:
        return bool(self.execution_id and self.api_url and self.runner_key)

    def prepare_workspace(self) -> None:
        for path in self.settings.managed_dirs():
            Path(path).mkdir(parents=True, exist_ok=True)
