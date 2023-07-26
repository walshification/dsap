from collections import deque
from enum import Enum

from typing import Any, Deque

from ch06.exceptions import Empty


class DequeMessages(Enum):
    EMPTY = "Deque is empty."


class DequeDeque:
    """A deque ADT using a Python deque as internal storage."""

    def __init__(self) -> None:
        """Create an empty deque."""
        self._data: Deque[Any] = deque()

    def __len__(self) -> int:
        """Return the number of elements in the deque."""
        return len(self._data)

    def is_empty(self) -> bool:
        """Return True if the deque is empty."""
        return len(self._data) == 0

    def add_first(self, e: Any) -> None:
        """Add an element to the front of the deque."""
        self._data.appendleft(e)

    def add_last(self, e: Any) -> None:
        """Add an element to the back of the deque."""
        self._data.append(e)

    def delete_first(self) -> Any:
        """Remove and return the first element of the deque.

        Raise Empty exception if the deque is empty.
        """
        self._check_empty()
        return self._data.popleft()

    def delete_last(self) -> Any:
        """Remove and return the last element of the deque.

        Raise Empty exception if the deque is empty.
        """
        self._check_empty()
        return self._data.pop()

    def first(self) -> Any:
        """Return (but do not remove) the first element of the deque.

        Raise Empty exception if the deque is empty.
        """
        self._check_empty()
        return self._data[0]

    def last(self) -> Any:
        """Return (but do not remove) the last element of the deque.

        Raise Empty exception if the deque is empty.
        """
        self._check_empty()
        return self._data[-1]

    def _check_empty(self) -> None:
        """Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty(DequeMessages.EMPTY.value)
