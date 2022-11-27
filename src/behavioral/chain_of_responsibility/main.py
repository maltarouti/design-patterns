from client import Client

from handler import Handler1
from handler import Handler2
from handler import Handler3


if __name__ == "__main__":
    handler1 = Handler1()
    handler2 = Handler2()
    handler3 = Handler3()

    handler1.set_next(handler2)
    handler2.set_next(handler3)

    client = Client(handler1)
    client.start_handling(dict(username="Murtada", password=1234))
