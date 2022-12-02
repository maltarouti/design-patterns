

class Component:
    def operation(self) -> str: ...


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"
