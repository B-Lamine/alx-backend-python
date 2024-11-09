#!/usr/bin/env python3
"""Module contains:
    - coroutines: wait_n.
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays_list = [await task for task in asyncio.as_completed(tasks)]
    return delays_list
