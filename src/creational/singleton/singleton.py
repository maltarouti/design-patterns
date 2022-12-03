from __future__ import annotations


class SingletonClass:
    def __new__(cls) -> SingletonClass:
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance
