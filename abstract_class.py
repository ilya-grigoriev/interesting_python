from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def wow(self, goo: str) -> None:
        ...


class B(A):
    def hello(self, name: str):
        print(f'Hello, {name}')


# b = B()   # There is error


class B2(A):
    def wow(self):
        pass

    def hello(self, name: str):
        print(f'Hello, {name}')


b2 = B2()   # There is no error
b2.wow()
