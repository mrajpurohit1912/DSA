import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)  # Simulate a delay

async def main():
    await asyncio.gather(print_numbers(), print_numbers())

asyncio.run(main())
