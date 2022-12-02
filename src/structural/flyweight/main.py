from flyweight_factory import FlyweightFactory


if __name__ == "__main__":
    flyweight_factory = FlyweightFactory()

    # State 1: Creating an object with new resolution
    f1 = flyweight_factory.create_flyweight(
        resolution="1080p", image="2073600px")

    print("Image ID: ", id(f1.image))

    # State 2: Creating an object with new resolution
    f2 = flyweight_factory.create_flyweight(resolution="240p", image="76800px")

    print("Image ID: ", id(f2.image))

    # State 3: Creating an object with existing resolution
    f3 = flyweight_factory.create_flyweight(
        resolution="1080p", image="2073600px")

    print("Image ID: ", id(f3.image))
