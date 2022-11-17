from abc import ABC
from abc import abstractmethod


class Strategy(ABC):
    @abstractmethod
    def apply_strategy(self) -> None: ...


class ConcreteStrategyA(Strategy):
    def apply_strategy(self) -> None:
        print("Strategy A applied")


class ConcreteStrategyB(Strategy):
    def apply_strategy(self) -> None:
        print("Strategy B applied")
