from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from typing import Any


class Handler(ABC):
    def __init__(self) -> None:
        self._next_handler: Handler | None = None

    def set_next(self, handler: Handler) -> None:
        self._next_handler = handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Handler1(Handler):
    def handle(self, request: Any) -> str:

        if request.get("password", None) != 1234:
            return None

        print("Handler 1 is handling the request")
        return super().handle(request)


class Handler2(Handler):
    def handle(self, request: Any) -> str:
        print("Handler 2 is handling the request")
        return super().handle(request)


class Handler3(Handler):
    def handle(self, request: Any) -> str:
        print("Handler 3 is handling the request")
        return super().handle(request)
