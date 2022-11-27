from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediator import Mediator


class Component:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class CheckBox(Component):
    def enable_button(self) -> None:
        print("Component CheckBox is enabling the Button")
        self.mediator.notify("E")


class Button(Component):
    def enable_event(self) -> None:
        print("The button is enabled")
