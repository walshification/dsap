"""
Describe an efficient recursive function for solving the element
uniqueness problem, which runs in time that is at most O(n2) in the
worst case without using sorting.
"""
from typing import Sequence


def are_unique(S: Sequence, i: int = 0) -> bool:
    """
    Algorithm UniqueSequence(S, i):
        Input: A sequence S and an optional index i (default 0).
        Output: A boolean whether or not the elements are unique.

        if len(S) == i do
            return True

        for index in the range from i + 1 to the length of S do
            if S[i] == S[index]:
                return False

        return UniqueSequence(S, i + 1)
    """
    if len(S) == i:
        return True

    for j in range(i + 1, len(S)):
        if S[i] == S[j]:
            return False

    return are_unique(S, i + 1)
