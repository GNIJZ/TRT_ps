import asyncio

async def delayed_print():
    print("开始延迟执行 (从 delayed_print 函数)")
    await asyncio.sleep(2)  # 延迟 2 秒
    print("2 秒后执行 (从 delayed_print 函数)")

async def repeated_print():
    while True:
        await asyncio.sleep(1)  # 每隔 1 秒执行一次
        print("每隔 1 秒执行一次 (从 repeated_print 函数)")

async def main():
    # 创建并发执行的异步任务
    task1 = asyncio.create_task(delayed_print())
    task2 = asyncio.create_task(repeated_print())

    print("开始延迟执行 (从 main 函数)")

    # 等待 delayed_print 完成
    await task1
    # await asyncio.gather(task1, task2)   #异步等待2个任务执行

if __name__ == "__main__":
    asyncio.run(main())
    print("主程序执行完成")
