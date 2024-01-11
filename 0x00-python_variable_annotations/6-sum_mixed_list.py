#!/usr/bin/env python3


"""
Module: 6-sum_mixed_list

This module provides a function for calculating the sum
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input list

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        679.13
    """
    return sum(mxd_lst)
