"""
Give a recursive method for removing all the elements from a stack.
"""
from typing import Any, List

from ch06.array_stack import ArrayStack


def clear(S: ArrayStack) -> List[Any]:
    if len(S) == 0:
        return []

    if len(S) == 1:
        return [S.pop()]

    return [S.pop()] + clear(S)
