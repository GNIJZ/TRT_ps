import asyncio

# 异步生成器，模拟从异步数据源中生成数据
async def async_data_generator():
    for i in range(1, 6):
        # 模拟异步操作，例如从网络请求数据或从文件读取数据
        await asyncio.sleep(1)
        yield i

# 异步任务，处理异步数据集
async def process_async_data():
    async for data in async_data_generator():
        # 在这里处理异步数据，例如计算、转换等操作
        print(f"处理异步数据：{data}")
        # 模拟异步操作
        await asyncio.sleep(0.5)
    async_data_generator()

async def main():
    # 创建并发执行的异步任务
    task = asyncio.create_task(process_async_data())
    # while True:
    #     print(111)
    # 等待异步任务完成
    await task

# 运行异步主函数
asyncio.run(main())
