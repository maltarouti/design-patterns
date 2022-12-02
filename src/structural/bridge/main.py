from abstruction import Abstraction
from abstruction import ExtendedAbstraction

from implementation import ConcreteImplementationA
from implementation import ConcreteImplementationB


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    print(abstraction.operation())

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    print(abstraction.operation())
