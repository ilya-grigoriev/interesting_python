class A(list):
    loaded = lambda self: bool(self)


a = A()
assert bool(a) == a.loaded()   # Both expressions are equals
