from random import random 
import time
import asyncio

# coroutine to generate work 
async def producer (queue): 
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
    await queue.put (None) 
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print('Consumer: Running')
    #consume work
    while True:
        # get a unit of work without blocking 
        try:
            item = queue.get_nowait() 
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...') 
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print (f'{time.ctime()} >got {item}')
    # all done
    print (f'{time.ctime()} Consumer: Done')

# entry point coroutine 
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers 
    await asyncio.gather (producer(queue), consumer(queue))
# start the asyncio program 
asyncio.run(main())

# Producer: Running
# Consumer: Running
# Wed Aug 23 14:16:20 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:21 2023 >got 0.3167761730241837
# Wed Aug 23 14:16:21 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:21 2023 >got 0.35801772252859454
# Wed Aug 23 14:16:21 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:22 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:22 2023 >got 0.8323732845536296
# Wed Aug 23 14:16:22 2023 >got 0.41820193891572544
# Wed Aug 23 14:16:22 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:23 2023 >got 0.5325764729799739
# Wed Aug 23 14:16:23 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:23 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:24 2023 >got 0.9364428768758994
# Wed Aug 23 14:16:24 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:24 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:25 2023 >got 0.9608064294374102
# Wed Aug 23 14:16:25 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:25 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:26 2023 >got 0.6700742728922362
# Wed Aug 23 14:16:26 2023 >got 0.38709833419478257
# Wed Aug 23 14:16:26 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:26 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:26 2023 Producer: Done
# Wed Aug 23 14:16:27 2023 >got 0.8637004087227641
# Wed Aug 23 14:16:27 2023 Consumer: Done