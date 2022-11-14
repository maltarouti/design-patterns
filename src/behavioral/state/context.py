from state import State


class Context:
    def __init__(self) -> None:
        self._current_state: State | None = None

    def change_state(self, state: State) -> None:
        self._current_state = state

    def handle1(self) -> None:
        self._current_state.handle1()

    def handle2(self) -> None:
        self._current_state.handle2()
