import concurrent.futures
import random
import time
import threading


def run_dp_task(count):
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
        results.append(f"{num}:{dp[num]}")

    print("D", sep="", end="", flush=True)
    return results


def run_all_dp_tasks(task_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(run_dp_task, task_list))
    return results


if __name__ == "__main__":
    tasks = [5] * 1000

    print("Starting Threaded DP tasks...")
    start = time.time()

    all_results = run_all_dp_tasks(tasks)

    duration = time.time() - start
    print(f"\nCompleted {len(tasks)} tasks using Threading in {duration:.4f} seconds")
