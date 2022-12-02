from __future__ import annotations

from abc import ABC


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def is_composite(self) -> bool:
        return False

    def add(self, component: Component) -> None: ...
    def remove(self, component: Component) -> None: ...
    def operation(self) -> str: ...
