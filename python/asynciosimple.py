import asyncio
import time
async def say(delay, msg):
    print(f"before: {msg}")
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(say(1, "Good"))
    task2 = asyncio.create_task(say(2, "Morning"))

    print("Started at ", time.strftime("%X"))
    await asyncio.gather(task1, task2)
    print("Stopped at ", time.strftime("%X"))

asyncio.run(main())
