"""
Asyncio ist gut für Input-Outputprozsse, läuft nur in einem Thread!
nicht geeignet für CPU-Bound
"""

import asyncio


async def count():
    print("enter count")
    await asyncio.sleep(1)
    print("leave count")


async def main():
    """Asynchrone"""
    # await count()
    await asyncio.gather(
        count(),
        count(),
        count(),
    )


if __name__ == "__main__":
    asyncio.run(main())
