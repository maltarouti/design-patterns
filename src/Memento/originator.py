from memento import Memento


class Originator:
    def __init__(self, state: str) -> None:
        self.state = state

    def write(self, content: str) -> None:
        self.state += content

    def save(self) -> Memento:
        return Memento(self.state)

    def undo(self, memento: Memento) -> None:
        self.state = memento.state
