"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in
the form of a tuple of length two. Do not use the built-in functions
min or max in implementing your solution.
"""
from typing import List, Tuple


def minmax(data: List[int]) -> Tuple[int, int]:
    """Returns the smallest and largest numbers as a tuple."""
    smallest = data[0]
    largest = data[0]
    for k in data:
        if k < smallest:
            smallest = k
        if k > largest:
            largest = k
    return (smallest, largest)
