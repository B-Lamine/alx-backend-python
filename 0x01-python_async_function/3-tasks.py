#!/usr/bin/env python3
"""Module contains:
    - functions: task_wait_random.
"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Wrap waint_random into a task.
    """
    return asyncio.create_task(wait_random(max_delay))
