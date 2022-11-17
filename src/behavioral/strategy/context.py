
from strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def apply_strategy(self):
        self.strategy.apply_strategy()
