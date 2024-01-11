#!/usr/bin/env python3


"""
Module: 8-make_multiplier

This module provides a function for creating a multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]:

    Example:
        >>> fun = make_multiplier(2.22)
        >>> fun(2.22)
        4.9284
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
