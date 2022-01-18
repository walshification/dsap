"""
Write a short Python function that takes a sequence of integer values
and determines if there is a distinct pair of numbers in the sequence
whose product is odd.
"""
from typing import List


def has_odd_product_pair(data: List[int]) -> bool:
    """Returns True if data contains a distinct pair of numbers whose
    product is odd.
    """
    data_length = len(data)
    # End at data_length - 1 because the last index gets checked by all the others.
    for k in range(data_length - 1):
        for j in range(k + 1, data_length):
            if (data[k] * data[j]) % 2 == 1 and data[k] != data[j]:
                return True

    return False
