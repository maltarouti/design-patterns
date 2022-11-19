from __future__ import annotations

from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod

if TYPE_CHECKING:
    from observer import Observer


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None: ...

    @abstractmethod
    def deatach(self, observer: Observer) -> None: ...

    @abstractmethod
    def notify(self) -> None: ...


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self._observers: list(Observer) = list()

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def deatach(self, observer: Observer) -> None:
        return self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
