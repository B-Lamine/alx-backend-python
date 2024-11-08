#!/usr/bin/env python3
"""Module contains:
    - methods: sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sum up numbers of given list.
    """
    sum: float = 0
    for value in mxd_list:
        sum += value
    return sum
