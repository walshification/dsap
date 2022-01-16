"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are
distinct).
"""
from typing import List


def are_distinct(data: List[int]) -> bool:
    """Returns True if all numbers in data are different from each
    other; otherwise, False.

    Naive implementation.
    """
    checked = []
    for k in data:
        if k in checked:
            return False
        checked.append(k)
    return True
