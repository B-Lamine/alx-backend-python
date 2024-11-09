#!/usr/bin/env python3
"""Module contains:
    - coroutines: wait_random.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Delay execution for a random duration.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
