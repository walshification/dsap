"""
Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the odd positive integers
smaller than n.
"""


def sum_smaller_odd_squares(n: int) -> int:
    """Returns the sum of the squares of all the odd positive integers
    smaller than n.
    """
    total = 0
    while n:
        n -= 1
        if n % 2 == 1:
            total += n * n

    return total
