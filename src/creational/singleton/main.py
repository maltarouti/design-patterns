
from singleton import SingletonClass


if __name__ == "__main__":
    singleton = SingletonClass()
    singleton.variable = "Singleton Variable"

    new_singleton = SingletonClass()
    print(new_singleton.variable)
