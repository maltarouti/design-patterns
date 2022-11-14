from abc import ABC
from abc import abstractmethod


class State(ABC):
    @property
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None: ...

    @abstractmethod
    def handle2(self) -> None: ...
