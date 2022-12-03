from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from product import AbstractProductA
from product import AbstractProductB

from product import ConcreteProductA1
from product import ConcreteProductA2
from product import ConcreteProductB1
from product import ConcreteProductB2


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA: ...

    @abstractmethod
    def create_product_b(self) -> AbstractProductB: ...


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
