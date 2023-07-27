"""
In the previous exercise, we assume that the underlying list is
initially empty. Redo that exercise, this time preallocating an
underlying list with length equal to the stack's maximum capacity.
"""
from enum import Enum
from typing import Any, List, Optional

from ch06.exceptions import Empty, Full


class ConstrainedArrayStack:
    """LIFO Stack implementation using a Python list as storage."""

    class ErrorMessages(Enum):
        EMPTY = "Stack is empty."
        FULL = "Stack is full."

    def __init__(self, maxlen: Optional[int] = None) -> None:
        """Create an empty stack."""
        self._capacity = maxlen or 10  # default to 10.
        self._data: List[Any] = [None] * self._capacity
        self._max = maxlen
        self._n = 0

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return self._n == 0

    def push(self, e) -> None:
        """Add element e to the top of the stack."""
        if self._max is not None and self._n == self._max:
            raise Full(ConstrainedArrayStack.ErrorMessages.FULL.value)

        if self._max is None and self._n == self._capacity:
            self._resize(2 * self._n)

        self._data[self._n] = e
        self._n += 1

    def top(self) -> Any:
        """Return (but do not remove) the element at the top of the stack.

        Raises Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty(ConstrainedArrayStack.ErrorMessages.EMPTY.value)
        return self._data[self._n - 1]

    def pop(self) -> Any:
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raises Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty(ConstrainedArrayStack.ErrorMessages.EMPTY.value)

        element = self._data[self._n - 1]
        self._data[self._n - 1] = None
        self._n -= 1
        return element

    def _resize(self, c: int) -> None:
        """Resize to a new list of new capacity c."""
        old = self._data
        self._data = [None] * c
        for k in range(self._n):
            self._data[k] = old[k]
