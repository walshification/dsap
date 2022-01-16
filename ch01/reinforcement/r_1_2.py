"""
Write a short Python function, is_even(k), that takes an integer value
and returns True if k is even, and False otherwise. However, your
function cannot use the multiplication, modulo, or division operators.
"""


def is_even(k: int) -> bool:
    """Returns True if k is even, and False otherwise."""
    # Reduces any number to its rightmost bit. If it is odd, that will
    # complement then 1 and return 1 as a result of the bitwise AND. If
    # it is even, it will return 0.
    return k & 1 == 0
