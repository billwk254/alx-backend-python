#!/usr/bin/env python3


"""
Module: 100-safe_first_element

This module provides a function for safely retrieving
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a list.

    Args:
        lst (Sequence[Any]): The input list.

    Returns:
        Union[Any, None]:

    Example:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element([])
        None
    """
    if lst:
        return lst[0]
    else:
        return None
