from abc import ABC, abstractmethod


class Start(ABC):
    @abstractmethod
    def hello(self):
        pass


@Start.register
class Wow:
    def bye(self):
        pass


class Yeah(Start):
    def bye(self):
        pass


wow = Wow()
# yeah = Yeah()   # There is TypeError exception
