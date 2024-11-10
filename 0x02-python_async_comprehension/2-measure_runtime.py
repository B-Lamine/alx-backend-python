#!/usr/bin/env python3
"""Module contains:
    - coroutines: measure_runtime.
"""
import asyncio
import time


async_comprehension = __import__("1-async_comprehension")\
        .async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of async execution of async_comprehension.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
