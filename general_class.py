from typing import Generic, TypeVar

T = TypeVar('T')


class Wow(Generic[T]):
    def __init__(self, msg: T):
        self.msg = msg

    def hello(self):
        return self.msg


wow = Wow[int]('man')   # there is type error
