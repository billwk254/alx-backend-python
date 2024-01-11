#!/usr/bin/env python3


"""
Module: 5-sum_list

This module provides a function for calculating the sum of a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_list([3.14, 1.11, 2.22])
        6.47
    """
    return sum(input_list)
