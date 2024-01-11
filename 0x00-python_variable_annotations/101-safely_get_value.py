#!/usr/bin/env python3


"""
Module: 101-safely_get_value

This module provides a function for safely retrieving a value
"""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve from the dictionary.
        default (Union[T, None], optional): The default value to return

    Returns:
        Union[Any, T]: The value associated with the key

    Example:
        >>> safely_get_value({'a': 1, 'b': 2}, 'a', default='Not found')
        1
        >>> safely_get_value({'a': 1, 'b': 2}, 'c', default='Not found')
        'Not found'
    """
    if key in dct:
        return dct[key]
    else:
        return default
