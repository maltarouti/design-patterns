from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

if TYPE_CHECKING:
    from visitor import Visitor


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    def __str__(self) -> str:
        return "Component A"

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)


class ConcreteComponentB(Component):
    def __str__(self) -> str:
        return "Component B"

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)
