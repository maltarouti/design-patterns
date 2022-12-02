from system import System1
from system import System2


class Facade:
    def __init__(self, system1: System1, system2: System2) -> None:
        self.system1 = system1
        self.system2 = system2

    def operation(self) -> str:
        results = []

        results.append(self.system1.operation1())
        results.append(self.system1.operation2())
        results.append(self.system1.operation3())

        results.append(self.system2.operation1())
        results.append(self.system2.operation2())
        results.append(self.system2.operation3())
        
        print(f"processed {len(results)} operations")

        return "\n".join(results)
