"""Catalogo oficial de elementos para automacoes geradas por IA."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

LocatorStrategy = Literal[
    "css",
    "xpath",
    "text",
    "image",
    "coordinate",
    "desktop",
    "sap_id",
]


@dataclass(frozen=True)
class Locator:
    """Representa um seletor, imagem, coordenada ou identificador capturado pelo Spy."""

    strategy: LocatorStrategy
    value: str
    confidence: float | None = None
    source: str = "manual"


@dataclass(frozen=True)
class ElementDefinition:
    """Elemento de automacao com nome estavel e locators alternativos."""

    name: str
    description: str
    locators: tuple[Locator, ...]
    required: bool = True
    tags: tuple[str, ...] = field(default_factory=tuple)


class ElementRegistry:
    """Registro simples para evitar locators soltos em use cases."""

    def __init__(self, elements: list[ElementDefinition] | None = None) -> None:
        self._elements: dict[str, ElementDefinition] = {}
        for element in elements or []:
            self.register(element)

    def register(self, element: ElementDefinition) -> None:
        if element.name in self._elements:
            raise ValueError(f"Elemento duplicado: {element.name}")
        self._elements[element.name] = element

    def get(self, name: str) -> ElementDefinition:
        try:
            return self._elements[name]
        except KeyError as exc:
            raise KeyError(f"Elemento nao registrado: {name}") from exc

    def list(self) -> list[ElementDefinition]:
        return list(self._elements.values())


DEFAULT_ELEMENTS = ElementRegistry()
