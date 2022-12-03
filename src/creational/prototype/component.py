from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Component(ABC):
    @abstractmethod
    def clone() -> Component: ...


class ConcreteComponent(Component):
    def __init__(self, variable: float = None) -> None:
        self._variable = variable

    @property
    def variable(self) -> float:
        return self._variable

    @variable.setter
    def variable(self, variable: float) -> None:
        self._variable = variable

    def clone(self) -> Component:
        new_component = ConcreteComponent(self.variable)
        return new_component
