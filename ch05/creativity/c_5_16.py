"""
Implement a pop method for the DynamicArray class, given in Code
Fragment 5.3, that removes the last element of the array, and that
shrinks the capacity, _N_, of the array by half any time the number of
elements in the array goes below N/4.
"""
from typing import Optional

from ch05.dynamic_array import DynamicArray


class PoppableDynamicArray(DynamicArray):
    def pop(self, k: Optional[int] = None):
        k = k or self._n - 1  # Default to last index
        item = self._A[k]
        self._n -= 1

        if self._n < self._capacity / 4:
            self._resize(self._capacity // 2)

        return item
