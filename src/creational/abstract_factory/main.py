from abstract_factory import AbstractFactory

from abstract_factory import ConcreteFactory1
from abstract_factory import ConcreteFactory2


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
