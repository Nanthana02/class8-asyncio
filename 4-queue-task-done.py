from random import random
import asyncio 
import time

# coroutine to generate work
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
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running') 
    # consume work 
    while True:
        # get a unit of work.
        item = await queue.get()
        # report 
        print (f'{time.ctime()} >got {item}') 
        # block while processing
        if item:
            await asyncio.sleep(item) 
        # mark the task as done 
        queue.task_done()
# entry point coroutine 
async def main():
    # create the shared queue 
    queue =asyncio.Queue()
    #  start the consumer
    _ = asyncio.create_task(consumer(queue)) 
    # start the producer and wait for it to finish 
    await asyncio.create_task(producer(queue)) 
    #wait for all items to be processed 
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:39:37 2023 Consumer: Running
# Producer: Running
# Wed Aug 23 14:39:38 2023 >got 0.6123203973774164
# Wed Aug 23 14:39:38 2023 >got 0.6240850373405479
# Wed Aug 23 14:39:39 2023 >got 0.15254426577068092
# Wed Aug 23 14:39:39 2023 >got 0.2722876235571775
# Wed Aug 23 14:39:39 2023 >got 0.34173225970345733
# Wed Aug 23 14:39:40 2023 >got 0.051679845761560816
# Wed Aug 23 14:39:40 2023 >got 0.7610377288536793
# Wed Aug 23 14:39:41 2023 >got 0.1686148983807132
# Wed Aug 23 14:39:41 2023 >got 0.8164599333011912
# Wed Aug 23 14:39:42 2023 Producer: Done
# Wed Aug 23 14:39:42 2023 >got 0.7652587172439563