#!/usr/bin/env python3
"""Module contains:
    - coroutine: measure_time.
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure performance time of wait_n method.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
