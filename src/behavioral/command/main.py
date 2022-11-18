from receiver import Receiver
from command import SimpleCommand
from command import ComplexCommand
from invoker import Invoker


if __name__ == "__main__":
    receiver = Receiver()
    invoker = Invoker()

    simple_command = SimpleCommand(receiver=receiver)
    complex_command = ComplexCommand(receiver=receiver)

    invoker.set_command(simple_command)
    invoker.execute()

    invoker.set_command(complex_command)
    invoker.execute()
