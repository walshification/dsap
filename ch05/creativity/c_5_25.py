"""
The syntax data.remove(value) for Python list data removes only the
first occurrence of element value from the list. Give an implementation
of a function, with signature remove_all(data, value), that removes
_all_ occurrences of value from the given list, such that the worst-case
running time of the function is O(n) on a list of _n_ elements. Note
that it is not efficient enough in general to rely on repeated calls to
remove.
"""
from ch05.dynamic_array import DynamicArray

from typing import Any


class SettableDynamicArray(DynamicArray):
    def __setitem__(self, index: int, value: Any):
        if not 0 <= index < self._n:
            raise IndexError("Index out of range")

        self._A[index] = value


def remove_all(data: SettableDynamicArray, value: Any) -> None:
    removed = 0
    for i in range(len(data)):
        if data[i] == value:
            removed += 1
        else:
            data[i - removed] = data[i]

    data._n -= removed
