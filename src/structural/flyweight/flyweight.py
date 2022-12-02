from typing import Any


class Flyweight:
    def __init__(self, resolution: str, image: Any) -> None:
        self.class_type = resolution
        self.image = image
