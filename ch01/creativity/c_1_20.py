"""
Python's random module includes a function shuffle(data) that acceprs a
list of elements and randomly reorders the elements so that each
possible order occurs with equal probability. The random module
includes a more basic function randint(a, b) that returns a uniformly
random integer from a to b (including both endpoints). Using only the
randint function, implement your own version of the shuffle function.
"""
from random import randint
from typing import List


def my_shuffle(data: List[int]) -> List[int]:
    """Given a list of numbers, returns that list in a random order."""
    ordered = data.copy()
    shuffled = data.copy()
    for idx in range(len(ordered)):
        shuffled[idx] = ordered.pop(randint(0, len(ordered) - 1))

    return shuffled
