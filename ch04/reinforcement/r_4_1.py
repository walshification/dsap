"""
Describe a recursive algorithm for finding the maximum element in a
sequence, `S`, of `n` elements. What is your running time and space
usage?
"""
from typing import List


def find_max(S: List[int], n: int) -> int:
    """Return the maximum element of S with n elements.

    S (List[int]): A list of ints.
    n (int): The total size of S.

    Return (int)
    """
    if n == 0:
        return S[n]

    return max(S[n - 1], find_max(S, n - 1))


# Running time: O(n), worst case n recursive calls
# Space usage: O(n), one call per element of S
