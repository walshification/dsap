"""
The shuffle method, supported by the random module, takes a Python list
and rearranges it so that every possible ordering is equally likely.
Implement your own version of such a function. You may rely on the
randrange(n) function of the random module, which returns a random
number between 0 and n - 1 inclusive.
"""
from random import randrange

from typing import List


def shuffle(S: List[int]) -> List[int]:
    """Return a given list with element-order randomized."""
    swapped = set()
    for i in range(len(S)):
        random_i = randrange(len(S))
        if random_i not in swapped:
            S[i], S[random_i] = S[random_i], S[i]
            swapped.add(random_i)
    return S
