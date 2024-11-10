#!/usr/bin/env python3
"""Module contains:
    - async_comprehension.
"""
import asyncio
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Get list of random numbers generated asynchronously.
    """
    return [x async for x in async_generator()]
