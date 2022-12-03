from director import Director
from builder import ConcreteBuilder


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard basic product:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product:")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Using the builder directly
    print("Custom product:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
    print("\n")
