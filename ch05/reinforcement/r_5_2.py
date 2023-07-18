"""
In Code Fragment 5.1, we perform an experiment to compare the length of
a Python list to its underlying memory usage. Determining the sequence
of attay sizes requires a manual inspection of the outpu of that
program. Redesign the experiment so that the program outputs only those
values of _k_ at which the existing capacity is exhausted.

For example, on a system consistent with the results of Code Fragment
5.2, your program should output that the sequence of array capacities
are 0, 4, 8, 16, 25, ....
"""
import sys

from typing import List


def determine_size_memory_increases(n: int = 27) -> List[int]:
    """Returns number of elements at which list memory is increased."""
    data: List[None] = []
    increase_indexes: List[int] = []
    capacity = sys.getsizeof(data)

    for k in range(n):
        current_mem_size = sys.getsizeof(data)

        if current_mem_size > capacity:
            increase_indexes.append(k - 1)  # The previous index was at capacity
            capacity = current_mem_size

        data.append(None)

    return increase_indexes
