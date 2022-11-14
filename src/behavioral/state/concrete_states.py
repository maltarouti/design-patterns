from state import State


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request 1")

    def handle2(self) -> None:
        print("ConcreteStateA handles request 2")
        print("ConcreteStateA is changing to ConcreteStateB")
        self.context.change_state(self.context.state_b)


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request 1")

    def handle2(self) -> None:
        print("ConcreteStateB handles request 2")
        print("ConcreteStateB is changing to ConcreteStateA")
        self.context.change_state(self.context.state_a)
