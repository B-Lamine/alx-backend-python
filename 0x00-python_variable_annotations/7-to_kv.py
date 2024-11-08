#!/usr/bin/env python3
"""Module contains:
    - methods : to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of input.
    """
    v_sqrd: float = v**2
    return (k, v_sqrd)
