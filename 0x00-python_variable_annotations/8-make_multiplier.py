#!/usr/bin/env python3
""" Module contains:
    - methods: make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create function that multiplies any float by given multiplier.
    """
    def foo(x: float) -> float:
        """Multiply numbers by specified multiplier
        """
        return multiplier * x
    return foo
