"""Contrato base para casos de uso gerados."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from onerom_core import OneromExecution

from runtime.context import RuntimeContext


@dataclass
class UseCase(ABC):
    runtime: RuntimeContext
    execution: OneromExecution

    @abstractmethod
    def execute(self):
        """Executa o caso de uso e retorna artefato principal opcional."""
