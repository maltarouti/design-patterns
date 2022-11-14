from context import Context


if __name__ == "__main__":
    context = Context()
    context.change_state(context.state_a)

    print("State #1:")
    context.handle1()
    context.handle2()

    print("State #2:")
    context.handle1()
    context.handle2()

    print("State #3:")
    context.handle1()
