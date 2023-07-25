from typing import Any

from ch06.empty_exception import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._data = []

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e) -> None:
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self) -> Any:
        """Return (but do not remove) the element at the top of the stack.

        Raises Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self) -> Any:
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raises Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
