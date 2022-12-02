from component import ConcreteComponent
from decorator import ConcreteDecoratorA
from decorator import ConcreteDecoratorB


if __name__ == "__main__":
    # State 1:
    simple = ConcreteComponent()
    print(simple.operation())

    # State 2:
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print(decorator2.operation())
