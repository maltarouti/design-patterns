from caretaker import Caretaker
from originator import Originator


if __name__ == "__main__":
    originator = Originator("Default State")
    caretaker = Caretaker(originator)

    print("State #1:")
    caretaker.save()
    print(originator.state)

    print("State #2:")
    originator.write("\n")
    originator.write("New content")
    caretaker.save()
    print(originator.state)

    print("State #3:")
    caretaker.undo()
    print(originator.state)
