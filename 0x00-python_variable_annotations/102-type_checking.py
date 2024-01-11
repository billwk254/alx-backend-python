#!/usr/bin/env python3


"""
Module: 102-type_checking

This module provides a function for zooming in an array.
"""


from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Zooms in an array by repeating each element by a given factor.

    Args:
        lst (List): The input list.
        factor (int, optional): The factor to repeat

    Returns:
        List: The zoomed-in list.

    Example:
        >>> zoom_array([1, 2, 3], 3)
        [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
