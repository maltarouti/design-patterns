from abc import ABC
from abc import abstractmethod

from receiver import Receiver


class Command(ABC):
    def __init__(self, receiver: Receiver) -> None:
        self.receiver = receiver

    @abstractmethod
    def process(self) -> None: ...


class SimpleCommand(Command):
    def process(self) -> None:
        self.receiver.simple_action()


class ComplexCommand(Command):
    def process(self) -> None:
        self.receiver.complex_action()
