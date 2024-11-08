#!/usr/bin/env python3
"""Module contains:
    - element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Input: iterable item (list, tuple, etc).
    Return: list of tuple with the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
