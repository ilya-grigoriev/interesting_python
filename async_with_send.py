import asyncio


async def func():
    await asyncio.sleep(3)


async def main():
    await func()


async def func2():
    print('Hello')


async def main2():
    await func2()


loop = asyncio.get_event_loop()

loop.run_until_complete(main())

# main().send(None)   # There is error: no running loop
main2().send(None)
