

from context import Context
from component import ConcreteComponent


if __name__ == "__main__":
    context = Context()
    circle = ConcreteComponent(3.14)
    context.duplicate(circle)
