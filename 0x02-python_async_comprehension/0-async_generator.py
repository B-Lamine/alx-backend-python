#!/usr/bin/env python3
"""Module contains:
    - coroutines: async_generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate a random number from 0 to 10.
    """
    count = 0
    while (count < 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        count += 1
