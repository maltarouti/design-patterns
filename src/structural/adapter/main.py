from target import Target
from adaptee import Adaptee
from adapter import Adapter


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    # State 1: Working with home-made target object
    target = Target()
    print(target.request(), end="\n\n")

    # State 2: Working with external object
    adaptee = Adaptee()
    adaptee.specific_request()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    # State 3: Using the adapter so we're able to understand it
    adapter = Adapter()
    print(adapter.request())
