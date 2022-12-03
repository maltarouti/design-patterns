from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from product import Product
from product import ConcreteProduct1
from product import ConcreteProduct2


class Creator(ABC):
    @abstractmethod
    def factory_method(self): ...

    def operation(self) -> str:
        product = self.factory_method()
        return f"Creator worked with {product.operation()}"


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
