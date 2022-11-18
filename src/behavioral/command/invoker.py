from command import Command


class Invoker:
    def __init__(self) -> None:
        self.command: Command | None = None

    def set_command(self, command: Command) -> None:
        self.command = command

    def execute(self) -> None:
        self.command.process()
