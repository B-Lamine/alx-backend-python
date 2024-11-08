#!/usr/bin/env python3
"""Module contains:
    - methods: sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum up numbers of given list.
    """
    sum: float = 0
    for value in input_list:
        sum += value
    return sum
