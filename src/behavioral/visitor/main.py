from __future__ import annotations

from visitor import Visitor
from visitor import ConcreteVisitor1
from visitor import ConcreteVisitor2

from component import Component
from component import ConcreteComponentB
from component import ConcreteComponentA


def visit(components: list(Component), visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("Visitor 1:")
    visitor1 = ConcreteVisitor1()
    visit(components, visitor1)

    print("Visitor 2:")
    visitor2 = ConcreteVisitor2()
    visit(components, visitor2)
