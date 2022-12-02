
from facade import Facade
from system import System1
from system import System2

2
if __name__ == "__main__":
    system1 = System1()
    system2 = System2()
    facade = Facade(system1, system2)
    print(facade.operation())
