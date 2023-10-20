from typing import Protocol, runtime_checkable


class A(Protocol):
    def wow(self, boo: int) -> None:
        ...


@runtime_checkable
class B(A, Protocol):
    def omg(self, goo: str) -> None:
        ...


class B2(A):
    def omg(self, goo: str) -> None:
        ...


class Face:
    def wow(self, boo: int) -> None:
        print(f'wow: {boo}')

    def omg(self, goo: str) -> None:
        print(f'googoma: {goo}')


def func_with_B(cls: B):
    cls.wow(1)


def func_with_B2(cls: B2):
    cls.wow(1)


func_with_B(Face())
func_with_B2(Face())   # Pyright says that there is error
print(isinstance(Face, B))   # True
print(isinstance(Face, B2))   # False
