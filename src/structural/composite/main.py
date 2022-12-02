from composite import Composite
from leaf import Leaf


if __name__ == "__main__":
    # State 1:
    simple = Leaf()
    print(simple.operation())

    # State 2:
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print(tree.operation())
