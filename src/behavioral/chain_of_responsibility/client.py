from typing import Any

from handler import Handler


class Client():
    def __init__(self, handler: Handler) -> None:
        self.handler = handler

    def start_handling(self, request: Any) -> None:
        while self.handler:
            self.handler = self.handler.handle(request)
