import asyncio
import time
from random import random

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue  
        await queue.put(value)  
    # send an all done signal
    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # Check for stop
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())

# Producer: Running
# Wed Aug 23 14:14:50 2023 Consumer: Running
# Wed Aug 23 14:14:50 2023 Consumer: gave up waiting...
# Wed Aug 23 14:14:51 2023 > got 0.9847371243042988
# Wed Aug 23 14:14:51 2023 Consumer: gave up waiting...
# Wed Aug 23 14:14:52 2023 > got 0.6767213082934963
# Wed Aug 23 14:14:52 2023 > got 0.3066842845726643
# Wed Aug 23 14:14:52 2023 > got 0.14685423332855818
# Wed Aug 23 14:14:53 2023 Consumer: gave up waiting...
# Wed Aug 23 14:14:53 2023 > got 0.5382139316643456
# Wed Aug 23 14:14:53 2023 Consumer: gave up waiting...
# Wed Aug 23 14:14:53 2023 > got 0.6018189029744104
# Wed Aug 23 14:14:54 2023 > got 0.43243137142082533
# Wed Aug 23 14:14:54 2023 Consumer: gave up waiting...
# Wed Aug 23 14:14:54 2023 > got 0.5823039499063221
# Wed Aug 23 14:14:55 2023 > got 0.28757010803676064
# Wed Aug 23 14:14:55 2023 Producer: Done
# Wed Aug 23 14:14:55 2023 > got 0.25596283332351644
# Consumer: Done