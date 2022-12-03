
from Creator import ConcreteCreator1
from Creator import ConcreteCreator2


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    c1 = ConcreteCreator1()
    print(c1.operation())

    print("App: Launched with the ConcreteCreator2.")
    c2 = ConcreteCreator2()
    print(c2.operation())
