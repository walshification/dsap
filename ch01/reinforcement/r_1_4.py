"""
Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller
than n.
"""


def sum_of_smaller_squares(n: int) -> int:
    """Returns the sum of the squares of all the positive integers
    smaller than n.
    """
    return sum(num * num for num in range(n - 1, 0, -1))
