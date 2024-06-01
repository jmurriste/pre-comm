from typing import Any


class Duck:
    def __init__(self): ...

    def __getattribute__(self, name: str) -> Any:
        if name == "quack":
            return lambda: print("quack")

        elif name == "swim":
            return lambda: print("splash")

        else:
            raise (AttributeError)


duck = Duck()
duck.quack()
duck.swim()
