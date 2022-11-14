from typing import TYPE_CHECKING

from abc import ABC
from abc import abstractmethod


if TYPE_CHECKING:
    from context import Context


class State(ABC):
    def __init__(self, context: 'Context'):
        self.context = context

    @abstractmethod
    def handle1(self) -> None: ...

    @abstractmethod
    def handle2(self) -> None: ...
