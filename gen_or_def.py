import collections.abc


def func(lst: collections.abc.Sized):
    if len(lst) > 10:
        for i in lst:
            yield i
    return 1


print(func([2]))   # print that it is generator

for i in func([2]):
    print(i)   # we don't enter in here

try:
    next(func([2]))
except StopIteration as e:
    print(e.value)   # print 1
