
from originator import Originator


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = list()
        self._originator = originator

    def save(self) -> None:
        memento = self._originator.save()
        self._mementos.append(memento)

    def undo(self) -> None:
        memento = self._mementos.pop(0)
        self._originator.undo(memento)
