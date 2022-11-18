from abc import ABC
from abc import abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.first()
        self.second()

    @abstractmethod
    def first(self) -> None: ...

    @abstractmethod
    def second(self) -> None: ...


class ConcreteClassA(AbstractClass):
    def first(self) -> None:
        print("ConcreteClassA is calling the first method")

    def second(self) -> None:
        print("ConcreteClassA is calling the second method")


class ConcreteClassB(AbstractClass):
    def first(self) -> None:
        print("ConcreteClassB is calling the first method")

    def second(self) -> None:
        print("ConcreteClassB is calling the second method")
