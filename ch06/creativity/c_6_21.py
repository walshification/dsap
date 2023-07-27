"""
Show how to use a stack S and a queue Q to generate all possible subsets
of an n-element set T nonrecursively.
"""
from typing import FrozenSet, Set

from ch06.array_queue import ArrayQueue
from ch06.array_stack import ArrayStack


def generate_subsets(T: Set[int]) -> Set[FrozenSet[int]]:
    """Return a set of all subsets of set T."""
    # The stack is merely temp storage to ensure we use all the elements.
    S = ArrayStack()
    for i in T:
        S.push(i)

    # The queue is how we cycle through subsets, building them as we go.
    Q = ArrayQueue()
    Q.enqueue(set())  # Add our zero point.

    while not S.is_empty():
        current = S.pop()
        subset = None

        # We've exhausted all iterations when we hit the empty set.
        while subset != set():
            subset = Q.dequeue()

            # Create two versions of existing subset:
            # one with the current element, one without.
            containing_subset = subset.copy()
            containing_subset.add(current)

            # Repopulate the queue keeping the emptier one last.
            Q.enqueue(containing_subset)
            Q.enqueue(subset)

    return {frozenset(Q.dequeue()) for _ in range(len(Q))}
