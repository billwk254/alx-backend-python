#!/usr/bin/env python3


"""
Module: 2-floor

This module provides a function for getting the floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.

    Example:
        >>> floor(3.14)
        3
    """
    return math.floor(n)
