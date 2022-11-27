from mediator import ConcreteMediator
from component import CheckBox
from component import Button


if __name__ == "__main__":
    checkbox = CheckBox()
    button = Button()
    mediator = ConcreteMediator(checkbox, button)

    checkbox.enable_button()
