import asyncio

# 定义一个异步函数
async def async_operation(name):
    print(f"{name}: 开始执行异步操作")
    await asyncio.sleep(5)
    print(f"{name}: 异步操作执行完成")

# 定义主函数
async def main():
    # 创建并发执行的异步任务列表
    tasks = [
        async_operation("任务A"),
        async_operation("任务B")
    ]
    # 等待所有任务完成

    print(111111111111111111111111111)


    await asyncio.gather(*tasks)
# 运行异步主函数
asyncio.run(main())
