"""
Describe a recursive function for computing the nth Harmonic number:

H sub n = The sum from i = 1 to n of 1/i.
"""


def harmonic_number(n: int) -> float:
    """
    Algorithm HarmonicNumber(n):
        Input: An integer n
        Output: The harmonic number of n.

    if i is 1 do
        return 1
    else
        find the harmonic number of i by dividing 1 by i
        add harmonic number to HarmonicNumber(n-1)
    """
    if n == 1:
        return n
    return (1 / n) + harmonic_number(n - 1)
