from subject import ConcreteSubject
from observer import ConcreteObserverA
from observer import ConcreteObserverB


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    # State 1:
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.notify()

    # State 2
    subject.deatach(observer_b)
    subject.notify()
