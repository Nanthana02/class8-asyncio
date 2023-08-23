from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: Done')

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
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:27:21 2023 Consumer: Running
# Wed Aug 23 14:27:21 2023 Producer: Running
# Wed Aug 23 14:27:21 2023 Producer: Running
# Wed Aug 23 14:27:21 2023 Producer: Running
# Wed Aug 23 14:27:21 2023 Producer: Running
# Wed Aug 23 14:27:21 2023 Producer: Running
# Wed Aug 23 14:27:21 2023 > got 0.203092041017645
# Wed Aug 23 14:27:21 2023 > got 0.645971721388975
# Wed Aug 23 14:27:22 2023 > got 0.696641862483762
# Wed Aug 23 14:27:23 2023 > got 0.7027233468419745
# Wed Aug 23 14:27:23 2023 > got 0.01744703885126664
# Wed Aug 23 14:27:23 2023 > got 0.5116825882899855
# Wed Aug 23 14:27:24 2023 > got 0.04256870273273683
# Wed Aug 23 14:27:24 2023 > got 0.9770188152887834
# Wed Aug 23 14:27:25 2023 > got 0.5151828193434461
# Wed Aug 23 14:27:26 2023 > got 0.6628978160383594
# Wed Aug 23 14:27:26 2023 > got 0.07126623458470849
# Wed Aug 23 14:27:26 2023 > got 0.14366584309472263
# Wed Aug 23 14:27:26 2023 > got 0.6996589184374654
# Wed Aug 23 14:27:27 2023 > got 0.44333405966696615
# Wed Aug 23 14:27:28 2023 > got 0.7715317635646962
# Wed Aug 23 14:27:28 2023 > got 0.9944430593497755
# Wed Aug 23 14:27:29 2023 > got 0.740241917213858
# Wed Aug 23 14:27:30 2023 > got 0.4819720301998418
# Wed Aug 23 14:27:31 2023 > got 0.33958900089368027
# Wed Aug 23 14:27:31 2023 > got 0.8908403103456333
# Wed Aug 23 14:27:32 2023 > got 0.12866873500170928
# Wed Aug 23 14:27:32 2023 > got 0.6255710572343236
# Wed Aug 23 14:27:33 2023 > got 0.32300394820820866
# Wed Aug 23 14:27:33 2023 > got 0.7705831498937604
# Wed Aug 23 14:27:34 2023 > got 0.08979274370702306
# Wed Aug 23 14:27:34 2023 > got 0.6265703115405697
# Wed Aug 23 14:27:35 2023 > got 0.5613009601663215
# Wed Aug 23 14:27:35 2023 > got 0.21337842050321554
# Wed Aug 23 14:27:35 2023 > got 0.6297459048117405
# Wed Aug 23 14:27:36 2023 > got 0.6060360309243906
# Wed Aug 23 14:27:37 2023 > got 0.6965189322776802
# Wed Aug 23 14:27:37 2023 > got 0.28425421755561686
# Wed Aug 23 14:27:38 2023 > got 0.5198346209554997
# Wed Aug 23 14:27:38 2023 > got 0.2435055180658886
# Wed Aug 23 14:27:38 2023 > got 0.30853336566042366
# Wed Aug 23 14:27:39 2023 > got 0.559442602825407
# Wed Aug 23 14:27:39 2023 > got 0.41344831392602055
# Wed Aug 23 14:27:40 2023 > got 0.05181512989490411
# Wed Aug 23 14:27:40 2023 > got 0.22738879184890548
# Wed Aug 23 14:27:40 2023 > got 0.5949260868238286
# Wed Aug 23 14:27:41 2023 > got 0.1525361573329853
# Wed Aug 23 14:27:41 2023 > got 0.7395395520340301
# Wed Aug 23 14:27:41 2023 Producer: Done
# Wed Aug 23 14:27:41 2023 > got 0.9036124813971153
# Wed Aug 23 14:27:41 2023 Producer: Done
# Wed Aug 23 14:27:42 2023 > got 0.3569255891777364
# Wed Aug 23 14:27:43 2023 > got 0.9303125248884396
# Wed Aug 23 14:27:43 2023 Producer: Done
# Wed Aug 23 14:27:44 2023 > got 0.8245533757598419
# Wed Aug 23 14:27:45 2023 > got 0.7260212196829734
# Wed Aug 23 14:27:45 2023 Producer: Done
# Wed Aug 23 14:27:45 2023 > got 0.8442229852309022
# Wed Aug 23 14:27:45 2023 Producer: Done
# Wed Aug 23 14:27:46 2023 > got 0.7948785976719026
# Wed Aug 23 14:27:47 2023 > got 0.3162954072235753