"""
Python's `random` module includes a function `choice(data` that returns a
random element from a non-empty sequence. The random module
includes a more basic function `randrange`, with parametrerization similar to
the built-in `range` function, that return [sic] a random choice from the given
range. Using only the `randrange` function, implement your own version
of the `choice` function.
"""
from random import randrange, seed
from typing import List, Optional


def my_choice(data: List[int], seed_key: Optional[int] = None) -> int:
    """Implements a random choice function using randrange."""
    seed(seed_key)
    return data[randrange(len(data))]
