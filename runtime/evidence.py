"""Registro de evidencias com upload online e fallback local."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from runtime.context import RuntimeContext

logger = logging.getLogger(__name__)

EvidenceStage = Literal["start", "checkpoint", "error", "finish"]


def _normalize_runner_agent_base(raw_url: str | None) -> str:
    base = (raw_url or "").rstrip("/")
    if not base:
        return ""
    if base.endswith("/runner-agent"):
        return base
    if base.endswith("/api/v1"):
        return f"{base}/runner-agent"
    return f"{base}/api/v1/runner-agent"


class EvidenceRecorder:
    """Envia evidencias ao runner-agent quando possivel e sempre preserva fallback local."""

    def __init__(self, runtime: RuntimeContext) -> None:
        self.runtime = runtime
        self.local_dir = runtime.settings.evidence_dir

    def record_text(
        self,
        *,
        stage: EvidenceStage,
        label: str,
        metadata: dict[str, Any] | None = None,
    ) -> Path | None:
        payload = self._payload(stage=stage, label=label, metadata=metadata)
        local_path = self._write_local(payload=payload)
        self._send(stage=stage, label=label, metadata=payload["metadata"], attachment=None)
        return local_path

    def record_file(
        self,
        *,
        stage: EvidenceStage,
        label: str,
        path: Path,
        metadata: dict[str, Any] | None = None,
    ) -> Path | None:
        payload = self._payload(
            stage=stage,
            label=label,
            metadata={
                **(metadata or {}),
                "attachment_name": path.name,
                "attachment_size_bytes": path.stat().st_size if path.exists() else None,
            },
        )
        local_path = self._write_local(payload=payload)
        self._send(stage=stage, label=label, metadata=payload["metadata"], attachment=path)
        return local_path

    def _payload(
        self,
        *,
        stage: EvidenceStage,
        label: str,
        metadata: dict[str, Any] | None,
    ) -> dict[str, Any]:
        return {
            "created_at": datetime.now(UTC).isoformat(),
            "stage": stage,
            "label": label,
            "execution_id": self.runtime.execution_id,
            "runner_id": self.runtime.runner_id,
            "bot_name": self.runtime.bot_name,
            "offline": self.runtime.is_offline,
            "metadata": metadata or {},
        }

    def _write_local(self, *, payload: dict[str, Any]) -> Path | None:
        try:
            self.local_dir.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%f")
            target = self.local_dir / f"{stamp}_{payload['stage']}.json"
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return target
        except OSError as exc:
            logger.warning("Falha ao registrar evidencia local: %s", exc)
            return None

    def _send(
        self,
        *,
        stage: EvidenceStage,
        label: str,
        metadata: dict[str, Any],
        attachment: Path | None,
    ) -> None:
        if not self.runtime.can_upload_evidence:
            logger.debug("Upload de evidencia desabilitado em modo local/passivo")
            return

        api_base = _normalize_runner_agent_base(self.runtime.api_url)
        if not api_base:
            return

        try:
            import requests

            data = {
                "stage": stage,
                "label": label,
                "metadata_json": json.dumps(metadata, ensure_ascii=False),
            }
            headers = {"X-Runner-Key": self.runtime.runner_key or ""}

            if attachment and attachment.exists():
                with attachment.open("rb") as file_handle:
                    response = requests.post(
                        f"{api_base}/executions/{self.runtime.execution_id}/evidences",
                        headers=headers,
                        data=data,
                        files={"attachment": (attachment.name, file_handle)},
                        timeout=15,
                    )
            else:
                response = requests.post(
                    f"{api_base}/executions/{self.runtime.execution_id}/evidences",
                    headers=headers,
                    data=data,
                    timeout=10,
                )

            if response.status_code not in (200, 201):
                logger.warning("Upload de evidencia retornou HTTP %s", response.status_code)
        except Exception as exc:
            logger.warning("Upload de evidencia falhou; fallback local preservado: %s", exc)
