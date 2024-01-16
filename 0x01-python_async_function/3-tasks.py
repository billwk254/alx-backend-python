#!/usr/bin/env python3
"""
Module containing the task_wait_random function.
"""


import asyncio
from typing import Generator


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Generator[asyncio.Task, None, None]:
    """
    Takes an integer max_delay and returns an asyncio.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        Generator[asyncio.Task, None, None]
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
