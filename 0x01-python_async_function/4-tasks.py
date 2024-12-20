#!/usr/bin/env python3
"""Module contains:
    - coroutines: task_wait_n.
"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays_list = [await task for task in asyncio.as_completed(tasks)]
    return delays_list
