from typing import Any
from flyweight import Flyweight


class FlyweightFactory:
    def __init__(self, initial_flyweights: dict = dict()) -> None:
        self.flyweights = initial_flyweights

    def create_flyweight(self,
                         *args,
                         resolution: str,
                         image: Any) -> Flyweight:

        key = self.flyweights.get(resolution, None)

        if not key:
            print("Creating a new flyweight object")
            self.flyweights[resolution] = Flyweight(resolution, image)
        else:
            print("Reusing existing object")

        return self.flyweights.get(resolution)
