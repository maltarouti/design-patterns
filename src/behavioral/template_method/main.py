from template_method import ConcreteClassA
from template_method import ConcreteClassB


if __name__ == "__main__":
    A = ConcreteClassA()
    A.template_method()

    B = ConcreteClassB()
    B.template_method()
