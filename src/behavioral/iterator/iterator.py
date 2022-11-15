

class Aggregate:
    def __init__(self) -> None:
        self.history = list(range(10))

    def __iter__(self) -> None:
        return iter(self.history)
