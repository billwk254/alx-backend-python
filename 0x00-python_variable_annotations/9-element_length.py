#!/usr/bin/env python3


"""
Module: 9-element_length

This module provides a function for returning the length of each element
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the original element and its length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the original

    Example:
        >>> element_length(['apple', 'banana', 'kiwi'])
        [('apple', 5), ('banana', 6), ('kiwi', 4)]
    """
    return [(i, len(i)) for i in lst]
