"""
Give a recursive algorithm to compute the product of two positive
integers, _m_ and _n_, using only addition and subtraction.
"""


def multiply(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0

    if m == 1:
        return n

    if n == 1:
        return m

    return n + multiply(n, m - 1)
