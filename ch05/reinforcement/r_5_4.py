"""
Our DynamicArray class, as given in Code Fragment 5.3, does not support
use of negative indicies with __getitem__. Update that method to better
match the semantics of a Python list.
"""
from ch05.dynamic_array import DynamicArray


class BetterDynamicArray(DynamicArray):
    """A dynamic array class with support for negative indices."""

    def __getitem__(self, k: int):
        """Return item at index k."""
        if not -self._n <= k < self._n:
            raise IndexError("invalid index")
        if k < 0:
            k += self._n  # Convert negative index to positive index.
        return self._A[k]
