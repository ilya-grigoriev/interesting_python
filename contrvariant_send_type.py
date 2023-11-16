from typing import Any, Generator


def func() -> Generator[Any, int, Any]:
    i = 0.0
    i_2 = yield i


a = func()
next(a)
a.send(1.0)
