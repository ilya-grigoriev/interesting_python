async def func():
    for i in range(10):
        yield i


a = func()
while True:
    try:
        next(a.__anext__())
    except StopAsyncIteration:
        break
    except Exception as e:
        print(e.args[0])
