from abc import ABC

from component import CheckBox
from component import Button


class Mediator(ABC):
    def notify(self, event: str) -> None: ...


class ConcreteMediator(Mediator):
    def __init__(self, checkbox: CheckBox, Button: Button) -> None:
        self._CheckBox = checkbox
        self._CheckBox.mediator = self

        self._Button = Button
        self._Button.mediator = self

    def notify(self, event: str) -> None:
        if event == "E":
            self._Button.enable_event()
