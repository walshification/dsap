"""
Give a single command that computes the sum from Exercise R-1.6,
relying on Python's comprehension syntax and the built-in sum function.
"""


def sum_smaller_odd_squares(n: int) -> int:
    """Returns the sum of the squares of all the odd positive integers
    smaller than n.
    """
    return sum(num * num for num in range(n, 0, -1) if num % 2 == 1)
