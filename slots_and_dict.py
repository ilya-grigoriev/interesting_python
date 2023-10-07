class A:
    __slots__ = ('__dict__', 'x', 'y')


a = A()
a.x = 8
print(a.__dict__) # there is no `x`
a.z = 9
print(a.__dict__) # there is `z`
