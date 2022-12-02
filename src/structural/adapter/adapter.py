from target import Target
from adaptee import Adaptee


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: {self.specific_request()[::-1]}"
