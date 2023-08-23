import asyncio
import time
from random import random

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)  

    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consum work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal  
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:07:22 2023 Producer: Running
# Wed Aug 23 14:07:22 2023 Consumer: Running
# Wed Aug 23 14:07:22 2023 > got 0.28277947616170296
# Wed Aug 23 14:07:22 2023 > got 0.11484816936026032
# Wed Aug 23 14:07:23 2023 > got 0.6807288546841007
# Wed Aug 23 14:07:24 2023 > got 0.512626161757214
# Wed Aug 23 14:07:25 2023 > got 0.9841593468586798
# Wed Aug 23 14:07:25 2023 > got 0.7853609643492281
# Wed Aug 23 14:07:26 2023 > got 0.7501569507714931
# Wed Aug 23 14:07:26 2023 > got 0.20254018769757476
# Wed Aug 23 14:07:27 2023 > got 0.998871804370783
# Wed Aug 23 14:07:28 2023 Producer: Done
# Wed Aug 23 14:07:28 2023 > got 0.5098843717295878
# Wed Aug 23 14:07:28 2023 Consumer: Done
