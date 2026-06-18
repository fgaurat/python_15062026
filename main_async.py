import asyncio
import time




async def add(a,b): # coroutine
    await asyncio.sleep(1)
    return a+b


async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    start = time.perf_counter()
    # r = await add(1,3)
    # print(r)
    # r = await add(2,4)
    # print(r)

    coroutines = [add(1,3),add(2,4)]

    r = await asyncio.gather(*coroutines)
    print(r)
    end = time.perf_counter()
    print(f"{end-start:.3}s")


if __name__=='__main__':
    asyncio.run(main())




