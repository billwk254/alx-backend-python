#!/usr/bin/env python3
"""
Module containing the measure_time function.
"""


import asyncio
import time
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per execution.
    """
    async def measure():
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        return end_time - start_time

    total_time = asyncio.run(measure())
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
