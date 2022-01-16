"""
Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller
than n.
"""


def sum_of_smaller_squares(n: int) -> int:
    """Returns the sum of the squares of all the positive integers
    smaller than n.
    """
    total = 0
    while n:
        n -= 1
        total += n * n

    return total
