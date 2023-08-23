from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep((id+1)*0.1)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: {id} Done')

# coroutine to 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
            # mark as completed
            queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:19:09 2023 Consumer: Running
# Wed Aug 23 15:19:09 2023 Producer: Running
# Wed Aug 23 15:19:09 2023 Producer: Running
# Wed Aug 23 15:19:09 2023 Producer: Running
# Wed Aug 23 15:19:09 2023 Producer: Running
# Wed Aug 23 15:19:09 2023 Producer: Running
# Wed Aug 23 15:19:09 2023 > got 0.955349273545056
# Wed Aug 23 15:19:10 2023 > got 0.17531314444648616
# Wed Aug 23 15:19:10 2023 > got 0.9239886415732594
# Wed Aug 23 15:19:11 2023 > got 0.4532219423667926
# Wed Aug 23 15:19:12 2023 > got 0.6923729082845623
# Wed Aug 23 15:19:12 2023 > got 0.31113026589266657
# Wed Aug 23 15:19:13 2023 > got 0.06265171033690686
# Wed Aug 23 15:19:13 2023 > got 0.6533434576593313
# Wed Aug 23 15:19:13 2023 > got 0.6072438649916957
# Wed Aug 23 15:19:14 2023 > got 0.5809743191076865
# Wed Aug 23 15:19:15 2023 > got 0.038114741538757047
# Wed Aug 23 15:19:15 2023 > got 0.22218460388714156
# Wed Aug 23 15:19:15 2023 > got 0.7861412875341423
# Wed Aug 23 15:19:16 2023 > got 0.686113766583905
# Wed Aug 23 15:19:16 2023 > got 0.9871047639575513
# Wed Aug 23 15:19:17 2023 > got 0.1396878883135747
# Wed Aug 23 15:19:17 2023 > got 0.5309550848800489
# Wed Aug 23 15:19:18 2023 > got 0.5022518209501057
# Wed Aug 23 15:19:19 2023 > got 0.1753477357700739
# Wed Aug 23 15:19:19 2023 > got 0.12405334279484814
# Wed Aug 23 15:19:19 2023 > got 0.34949923471661537
# Wed Aug 23 15:19:19 2023 > got 0.012780235770729731
# Wed Aug 23 15:19:19 2023 > got 0.3132146131968737
# Wed Aug 23 15:19:20 2023 > got 0.29129193619293026
# Wed Aug 23 15:19:20 2023 > got 0.3919536133165029
# Wed Aug 23 15:19:20 2023 > got 0.27695738996189345
# Wed Aug 23 15:19:21 2023 > got 0.33991866264637394
# Wed Aug 23 15:19:21 2023 > got 0.6534217749420483
# Wed Aug 23 15:19:22 2023 > got 0.41348677705639025
# Wed Aug 23 15:19:22 2023 > got 0.440244514885342
# Wed Aug 23 15:19:22 2023 > got 0.6856718555630487
# Wed Aug 23 15:19:23 2023 > got 0.2506997797725392
# Wed Aug 23 15:19:23 2023 > got 0.42188237845159016
# Wed Aug 23 15:19:24 2023 > got 0.508854569369051
# Wed Aug 23 15:19:24 2023 > got 0.09286987563658622
# Wed Aug 23 15:19:24 2023 > got 0.2951391443432214
# Wed Aug 23 15:19:24 2023 Producer: 0 Done
# Wed Aug 23 15:19:25 2023 > got 0.9916533738929504
# Wed Aug 23 15:19:26 2023 > got 0.12319495113005419
# Wed Aug 23 15:19:26 2023 > got 0.7856565796033635
# Wed Aug 23 15:19:27 2023 > got 0.2050263051496053
# Wed Aug 23 15:19:27 2023 > got 0.4787986896340728
# Wed Aug 23 15:19:27 2023 > got 0.1577292324957631
# Wed Aug 23 15:19:27 2023 Producer: 1 Done
# Wed Aug 23 15:19:27 2023 > got 0.9844178033273528
# Wed Aug 23 15:19:28 2023 > got 0.0841711468450479
# Wed Aug 23 15:19:29 2023 > got 0.9576283921260363
# Wed Aug 23 15:19:29 2023 Producer: 2 Done
# Wed Aug 23 15:19:30 2023 > got 0.2074172722080414
# Wed Aug 23 15:19:30 2023 > got 0.6817111443299763
# Wed Aug 23 15:19:30 2023 Producer: 3 Done
# Wed Aug 23 15:19:30 2023 > got 0.15473160942975484
# Wed Aug 23 15:19:30 2023 Producer: 4 Done
# Wed Aug 23 15:19:31 2023 > got 0.8748024668552635
# Wed Aug 23 15:19:31 2023 > got 0.6016611987638087