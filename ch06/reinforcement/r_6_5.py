"""
Implement a function that reverses a list of elements by pushing them
onto a stack in one order, and writing them back to the list in reversed
order.
"""
from typing import List

from ch06.array_stack import ArrayStack


def reverse(L: List) -> None:
    """Reverse a list of elements."""
    if len(L) == 0 or len(L) == 1:
        return

    stack = ArrayStack()
    for i in range(len(L)):
        stack.push(L[i])

    for i in range(len(stack)):
        L[i] = stack.pop()
