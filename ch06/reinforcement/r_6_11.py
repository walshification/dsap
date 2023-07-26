"""
Give a simple adapter that implements our queue ADT while using a
collections.deque instance for storage.
"""
from collections import deque

from typing import Any, Deque

from ch06.exceptions import Empty


class DequeQueue:
    """FIFO queue implementation using a Python deque as storage."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self._data: Deque[Any] = deque()

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._data)

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def first(self) -> Any:
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[0]

    def dequeue(self) -> Any:
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data.popleft()

    def enqueue(self, e: Any) -> None:
        """Add an element to the back of the queue."""
        self._data.append(e)
