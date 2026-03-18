import asyncio
import random
 
FUZZ = True
counter = 0
lock = asyncio.Lock()
 
async def fuzz():
    if FUZZ:
        await asyncio.sleep(random.random())
 
async def worker():
    global counter

    await fuzz()
    oldcnt = counter
    await fuzz()
    counter = oldcnt + 1
    await fuzz()
    print(f'The count is {counter}\n--------------------\n')
    await fuzz()
 

async def main():
    print('Starting up')
    tasks = [asyncio.create_task(worker()) for _ in range(10)]
    await asyncio.gather(*tasks)
    print('Finishing up')
 
asyncio.run(main())
 
