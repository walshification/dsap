"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than
they were before, and compare this method to an equivalent Python
function for doing the same thing.
"""
from typing import List


def reverse(data: List[int]) -> List[int]:
    """Given a list of integers, returns the same list in reverse
    order.

    Initialize empty List Reversed
    While there are Numbers in Data:
        Remove last Number in Data
        Append Number to Reversed
    Return Reversed
    """
    _reversed = []
    while data:
        current = data.pop()
        _reversed.append(current)

    return _reversed
