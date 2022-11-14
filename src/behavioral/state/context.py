from state import State

from concrete_states import ConcreteStateA
from concrete_states import ConcreteStateB


class Context:
    def __init__(self) -> None:
        self._current_state: State | None = None
        self.state_a = ConcreteStateA(self)
        self.state_b = ConcreteStateB(self)

    def change_state(self, state: State) -> None:
        self._current_state = state

    def handle1(self) -> None:
        self._current_state.handle1()

    def handle2(self) -> None:
        self._current_state.handle2()
