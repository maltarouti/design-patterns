from context import Context
from strategy import ConcreteStrategyA
from strategy import ConcreteStrategyB


if __name__ == "__main__":
    context = Context(strategy=ConcreteStrategyA())

    print("State #1:")
    context.apply_strategy()

    print("State #2:")
    context.strategy = ConcreteStrategyB()
    context.apply_strategy()
