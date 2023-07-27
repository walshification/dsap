"""
Implement a function with signature transfer(S, T) that transfers all
elements from stack S onto stack T, so that the element that starts at
the top of S is the first to be inserted onto T, and the element at the
bottom of S ends up at the top of T.
"""
from ch06.array_stack import ArrayStack


def transfer(S: ArrayStack, T: ArrayStack) -> None:
    """Move elements from S to T, reversing their order."""
    for _ in range(len(S)):
        T.push(S.pop())
