"""Contrato runtime entre robo, runner e execucao local."""

from .context import RuntimeContext
from .evidence import EvidenceRecorder

__all__ = ["EvidenceRecorder", "RuntimeContext"]
