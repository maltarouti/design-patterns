
from component import Component


class Context:
    def duplicate(self, component: Component) -> None:
        component.clone()
