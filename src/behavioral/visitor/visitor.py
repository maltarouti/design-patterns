from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

if TYPE_CHECKING:
    from component import ConcreteComponentA
    from component import ConcreteComponentB


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print("Visiting:", element)

    def visit_concrete_component_b(self, element) -> None:
        print("Visiting:", element)


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print("Visiting:", element)

    def visit_concrete_component_b(self, element) -> None:
        print("Visiting:", element)
