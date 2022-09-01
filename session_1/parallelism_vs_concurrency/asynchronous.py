import asyncio
import time

async def wait_for_10_sec(start):
    await asyncio.sleep(10)
    end = time.time()
    print(f"Normal   ==> {end - start}")


async def main():
    start = time.time()
    a1 = asyncio.create_task(wait_for_10_sec(start))
    a2 = asyncio.create_task(wait_for_10_sec(start))
    a3 = asyncio.create_task(wait_for_10_sec(start))

    await a1
    await a2
    await a3

if __name__ == "__main__":
    asyncio.run(main())

