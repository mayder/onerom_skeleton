from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from config.settings import BotSettings
from runtime.context import RuntimeContext
from runtime.evidence import EvidenceRecorder
from use_cases.example import ExampleUseCase


class FakeExecution:
    params = SimpleNamespace(as_dict=lambda: {})

    def __init__(self) -> None:
        self.success_items = 0

    def add_success_item(self) -> None:
        self.success_items += 1


def test_runtime_prepares_workspace(tmp_path: Path) -> None:
    settings = BotSettings(
        project_root=tmp_path,
        inputs_dir=tmp_path / "inputs",
        outputs_dir=tmp_path / "outputs",
        evidence_dir=tmp_path / "evidence",
        artifacts_dir=tmp_path / "artifacts",
        logs_dir=tmp_path / "logs",
        local_mode=True,
        log_level="INFO",
    )
    runtime = RuntimeContext(settings=settings, parameters={"customer_id": 123})

    runtime.prepare_workspace()

    assert settings.outputs_dir.is_dir()
    assert settings.evidence_dir.is_dir()


def test_example_use_case_writes_summary(tmp_path: Path) -> None:
    settings = BotSettings(
        project_root=tmp_path,
        inputs_dir=tmp_path / "inputs",
        outputs_dir=tmp_path / "outputs",
        evidence_dir=tmp_path / "evidence",
        artifacts_dir=tmp_path / "artifacts",
        logs_dir=tmp_path / "logs",
        local_mode=True,
        log_level="INFO",
    )
    runtime = RuntimeContext(settings=settings, parameters={"customer_id": 123})
    runtime.prepare_workspace()
    execution = FakeExecution()

    result = ExampleUseCase(runtime=runtime, execution=execution).execute()  # type: ignore[arg-type]

    assert result == settings.outputs_dir / "summary.json"
    assert result.is_file()
    assert execution.success_items == 1


def test_runtime_context_reads_runner_contract(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("ONEROM_EXECUTION_ID", "42")
    monkeypatch.setenv("ONEROM_API_URL", "https://example.com/api/v1")
    monkeypatch.setenv("ONEROM_RUNNER_KEY", "runner-key")
    monkeypatch.setenv("ONEROM_RUNNER_ID", "7")
    monkeypatch.setenv("ONEROM_BOT_NAME", "bot-example")
    monkeypatch.setenv("ONEROM_METRICS_FILE", str(tmp_path / "metrics.json"))
    monkeypatch.setenv("ONEROM_CONTEXT", '{"parameters":{"customer_id":123}}')

    runtime = RuntimeContext.from_env(parameters={"customer_id": 123})

    assert runtime.execution_id == "42"
    assert runtime.can_upload_evidence is True
    assert runtime.is_offline is False
    assert runtime.metrics_file == tmp_path / "metrics.json"
    assert runtime.onerom_context["parameters"]["customer_id"] == 123


def test_evidence_recorder_keeps_local_fallback(tmp_path: Path) -> None:
    settings = BotSettings(
        project_root=tmp_path,
        inputs_dir=tmp_path / "inputs",
        outputs_dir=tmp_path / "outputs",
        evidence_dir=tmp_path / "evidence",
        artifacts_dir=tmp_path / "artifacts",
        logs_dir=tmp_path / "logs",
        local_mode=True,
        log_level="INFO",
    )
    runtime = RuntimeContext(settings=settings, parameters={})

    evidence_path = EvidenceRecorder(runtime).record_text(
        stage="start",
        label="Smoke local",
        metadata={"offline": True},
    )

    assert evidence_path is not None
    assert evidence_path.is_file()
