"""Entrada unica do robo gerado pelo skeleton Onerom."""

from __future__ import annotations

import logging
from typing import Any

from onerom_core import OneromExecution

from config.settings import BotSettings
from runtime.context import RuntimeContext
from runtime.evidence import EvidenceRecorder
from use_cases.example import ExampleUseCase

logger = logging.getLogger("onerom_skeleton")


def _params_as_dict(params: Any) -> dict[str, Any]:
    if hasattr(params, "as_dict"):
        data = params.as_dict()
        return data if isinstance(data, dict) else {}
    if isinstance(params, dict):
        return params
    return {key: value for key, value in vars(params).items() if not key.startswith("_") and key != "as_dict"}


def run_bot(execution: OneromExecution | None = None) -> None:
    """Executa o fluxo principal preservando o ciclo de vida do `onerom_core`."""
    exec_ctx = execution or OneromExecution()
    exec_ctx.attach_logger(logger)

    settings = BotSettings.from_env()
    runtime = RuntimeContext.from_env(
        parameters=_params_as_dict(exec_ctx.params),
        settings=settings,
    )
    runtime.prepare_workspace()
    evidence = EvidenceRecorder(runtime)

    evidence.record_text(
        stage="start",
        label="Execucao iniciada",
        metadata={
            "offline": runtime.is_offline,
            "has_api_url": bool(runtime.api_url),
            "has_context": bool(runtime.onerom_context),
            "parameters_keys": sorted(runtime.parameters.keys()),
        },
    )

    try:
        use_case = ExampleUseCase(runtime=runtime, execution=exec_ctx)
        result = use_case.execute()
        if result is not None and result.exists():
            evidence.record_file(
                stage="finish",
                label="Resumo final",
                path=result,
                metadata={"kind": "summary", "relative_path": str(result.name)},
            )
        else:
            evidence.record_text(stage="finish", label="Execucao concluida")
    except Exception as exc:
        evidence.record_text(
            stage="error",
            label="Falha na execucao",
            metadata={"error_type": type(exc).__name__, "error": str(exc)},
        )
        raise


def main() -> None:
    execution = OneromExecution()
    execution.run(lambda: run_bot(execution))


if __name__ == "__main__":
    main()
