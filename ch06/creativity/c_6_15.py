"""
Suppose Alice has picked three distinct integers and placed them into a
stack S in random order. Write a short, straight-line piece of
pseudo-code (with no loops or recursion) that uses only one comparison
and only one variable x, yet that results in variable x storing the
largest of Alice's three integers with probability 2/3. Argue why your
method is correct.
"""
from ch06.array_stack import ArrayStack


def pick_largest(S: ArrayStack) -> int:
    """
    Case 1: Largest on top.
        x = 3
        x > S.top()
        return x

        Output: Success

    Case 2: Largest in the middle.
        x = 1 (or 2)
        x < S.top()
        switch x to greater value.

        Output: Success

    Case 3: Largest is last.
        x = 1 (or 2)
        x is compared to 1 or 2
        Largest remains in stack.

        Output: Failure
    """
    x = S.pop()
    if x < S.top():
        x = S.pop()
    return x
