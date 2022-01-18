"""
Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.
"""


def sum_of_smaller_squares_5(n: int) -> int:
    """Returns the sum of the squares of all the positive integers
    smaller than n.
    """
    return sum(num * num for num in range(n - 1, 0, -1))
