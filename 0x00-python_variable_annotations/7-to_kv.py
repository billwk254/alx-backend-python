#!/usr/bin/env python3


"""
Module: 7-to_kv

This module provides a function for creating a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple with the input string

    Example:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)
        >>> to_kv("school", 0.02)
        ('school', 0.0004)
    """
    return k, v ** 2.0
