import asyncio


async def hello1():
    print("start hello1")
    await asyncio.sleep(2)
    print("end hello1")


async def hello2():
    print("start hello2")
    await asyncio.sleep(2)
    print("hello2 end")


async def hello3():
    print("start hello3")
    for i in range(10):
        await asyncio.sleep(1)
        print(i)


# task = Task(hello1())
# task2 = Task(hello2())
# task3 = Task(hello3())

loop = asyncio.get_event_loop()


async def main():
    # 创建任务
    task = loop.create_task(hello1())
    task2 = loop.create_task(hello2())
    task3 = loop.create_task(hello3())

    # 等待任务完成
    await task
    await task2
    await task3


# 执行任务直到所有任务完成
loop.run_until_complete(main())