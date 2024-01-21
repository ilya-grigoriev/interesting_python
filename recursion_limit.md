- Write simple program with recursion:

```python
def func(n):
    if n == 0:
        return 0
    return func(n - 1)


func(10)
```

- If we run this, then it will work.
- But let's add recursion limit of less than 1000:

```python
import sys

sys.setrecursionlimit(10)

def func(n):
    if n == 0:
        return 0
    return func(n - 1)


func(10)
```

- It will work.
- Let's add `print` line:

```python

import sys

sys.setrecursionlimit(10)

def func(n):
    print(n)
    if n == 0:
        return 0
    return func(n - 1)


func(10)
```

- And now we can see error:

```python
10
9
8
7
6
5
Traceback (most recent call last):
...
RecursionError: maximum recursion depth exceeded while calling a Python object
```

- Question arises: why? We can add `print` line. How does this affect function recursion?
- Python counts not only function recursion, but also other functions. For example, this is `print` function. This function calls other functions in itself, and Python counts this as recursion.
- That is why we only see six numbers.

- Sources:
    - [StackOverflow](https://stackoverflow.com/questions/55560258/why-python-raises-recursionerror-before-it-exceeds-the-real-recursion-limit)
    - [Reddit](https://www.reddit.com/r/learnpython/s/eggFvYRLOG)
