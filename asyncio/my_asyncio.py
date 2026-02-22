import asyncio
import time
import random
import concurrent.futures


def dynamic_programming(count):
    max_num = 100
    coins = [4, 3, 1]

    dp = [float("inf")] * (max_num + 1)
    dp[0] = 0

    for i in range(1, max_num + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    results = []
    for _ in range(count):
        num = random.randint(10, max_num)
        results.append(f"{num}{dp[num]}")

    return "".join(results)


async def main():
    total_calculations = 10000
    num_tasks = 10
    chunk_size = total_calculations // num_tasks

    print(f"Starting {total_calculations} calculations...")
    start = time.time()

    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        tasks = []
        for _ in range(num_tasks):
            task = loop.run_in_executor(pool, dynamic_programming, chunk_size)
            tasks.append(task)

        results = await asyncio.gather(*tasks)

    final_output = "".join(results)

    duration = time.time() - start
    print(f"Executed total {total_calculations} operations in {duration:.6f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
