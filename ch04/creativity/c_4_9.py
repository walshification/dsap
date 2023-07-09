"""
Write a short recersive Python function that finds the minimum and
maximum values in a sequence without using any loops.
"""
from typing import Sequence, Tuple


def min_max(sequence: Sequence[int]) -> Tuple[int, int]:
    if not sequence:
        raise Exception("Sequence must be a list of integers")

    return _find_min_max(sequence, sequence[0], sequence[0], 1)


def _find_min_max(
    sequence: Sequence[int], min: int, max: int, idx: int
) -> Tuple[int, int]:
    if idx == len(sequence):
        return min, max

    integer = sequence[idx]
    if integer < min:
        min = integer
    if integer > max:
        max = integer

    return _find_min_max(sequence, min, max, idx + 1)
