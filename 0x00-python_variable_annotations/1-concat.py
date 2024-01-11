#!/usr/bin/env python3


"""
Module: 1-concat

This module provides a function for concatenating two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat("egg", "shell")
        'eggshell'
    """
    return str1 + str2
