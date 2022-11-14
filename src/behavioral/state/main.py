from context import Context
from concrete_states import ConcreteStateA
from concrete_states import ConcreteStateB


if __name__ == "__main__":
    context = Context()
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()

    print("State #1:")
    context.change_state(state_a)
    context.handle1()

    print("State #2:")
    context.change_state(state_b)
    context.handle1()
    context.handle2()
