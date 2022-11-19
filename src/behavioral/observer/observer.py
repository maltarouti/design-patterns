from __future__ import annotations

from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

if TYPE_CHECKING:
    from subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None: ...


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverA is updating")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB is updating")
