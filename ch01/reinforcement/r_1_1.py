"""
Write a short Python function, is_multiple(n, m), that takes two
integer values and returns True if n is a multiple of m, that is n = mi
for some integer i, and False otherwise.
"""


def is_multiple(n: int, m: int) -> bool:
    """Returns True if n is a multiple of m and False otherwise."""
    if n % m == 0:
        return True
    return False
