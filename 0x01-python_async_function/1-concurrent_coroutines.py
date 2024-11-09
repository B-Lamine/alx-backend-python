#!/ussr/bin/env python3
"""Module contains:
    - coroutines: wait_n.
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times.
    """
    delays_list = [await wait_random(max_delay) for _ in range(n)]
    return delays_list
