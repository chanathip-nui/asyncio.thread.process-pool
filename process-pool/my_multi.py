import multiprocessing
import random
import time

MAX_NUM = 100
COINS = [4, 3, 1]


def build_dp_table(max_val, coins):
    dp = [float("inf")] * (max_val + 1)
    dp[0] = 0
    for i in range(1, max_val + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp


def run_dp_task(task_id, count, dp_table):
    results = []
    for _ in range(count):
        num = random.randint(10, MAX_NUM)
        results.append(f"{num}:{dp_table[num]}")

    indicator = multiprocessing.current_process().name.split("-")[-1]
    print(indicator, end="", flush=True)
    return results


def run_parallel_tasks(num_tasks, items_per_task):
    dp_table = build_dp_table(MAX_NUM, COINS)

    tasks = [(i, items_per_task, dp_table) for i in range(num_tasks)]

    with multiprocessing.Pool() as pool:
        final_results = pool.starmap(run_dp_task, tasks)

    print()
    return final_results


if __name__ == "__main__":
    NUM_TASKS = 1000
    ITEMS_PER_TASK = 1000

    print(f"Starting {NUM_TASKS} tasks in parallel...")
    start_time = time.time()

    results = run_parallel_tasks(NUM_TASKS, ITEMS_PER_TASK)

    duration = time.time() - start_time
    total_processed = NUM_TASKS * ITEMS_PER_TASK
    print(f"Completed {NUM_TASKS} tasks using Threading in {duration:.4f} seconds")
