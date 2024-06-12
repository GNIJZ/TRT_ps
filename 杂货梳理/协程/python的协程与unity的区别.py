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

    print("主程序继续执行")  # 立即打印，不等待任务完成

    # 等待 delayed_print 完成
    await task1
    # Note: task2 will keep running indefinitely

if __name__ == "__main__":
    asyncio.run(main())
    print("主程序执行完成")  # 事件循环结束后立即执行



#unity的区别

# using UnityEngine;
# using System.Collections;
#
# public class CoroutineExample : MonoBehaviour
# {
#     void Start()
#     {
#         // 启动协程
#         StartCoroutine(DelayedPrint());
#         StartCoroutine(RepeatedPrint());
#         Debug.Log("主程序继续执行");  // 立即执行，不等待协程完成
#     }
#
#     IEnumerator DelayedPrint()
#     {
#         Debug.Log("开始延迟执行");
#         yield return new WaitForSeconds(2); // 延迟 2 秒
#         Debug.Log("2 秒后执行");
#     }
#
#     IEnumerator RepeatedPrint()
#     {
#         while (true)
#         {
#             yield return new WaitForSeconds(1); // 每隔 1 秒执行一次
#             Debug.Log("每隔 1 秒执行一次");
#         }
#     }
# }
