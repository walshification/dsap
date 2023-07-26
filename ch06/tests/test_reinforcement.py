import pytest

from ch06.array_queue import ArrayQueue
from ch06.array_stack import ArrayStack
from ch06.empty_exception import Empty
from ch06.reinforcement import DequeDeque, DequeQueue, clear, does_match, reverse, transfer


def test_transfer():
    S = ArrayStack()
    for i in range(10):
        S.push(i)

    T = ArrayStack()

    transfer(S, T)

    assert len(S) == 0
    assert T._data == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_clear():
    S = ArrayStack()
    for i in range(10):
        S.push(i)

    clear(S)

    assert len(S) == 0


def test_reverse():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    reverse(sequence)

    assert sequence == expected


@pytest.mark.parametrize(
    [
        "expression",
        "open_delimiters",
        "close_delimiters",
        "close_to_open_map",
        "expected_result",
    ],
    (
        ("(([]))", "([", ")]", {")": "(", "]": "["}, True),
        ("(([])", "([", ")]", {")": "(", "]": "["}, False),
        ("(5 + 3 * (2 + (1 + 1)) * 1)", "([", ")]", {")": "(", "]": "["}, True),
    ),
)
def test_does_match(
    expression, open_delimiters, close_delimiters, close_to_open_map, expected_result
):
    assert (
        does_match(expression, open_delimiters, close_delimiters, close_to_open_map)
        == expected_result
    )


def test_deque_queue():
    dq = DequeQueue()
    for i in range(10):
        dq.enqueue(i)

    assert dq.first() == 0
    assert len(dq) == 10
    assert dq.dequeue() == 0

    for i in range(10, 15):
        dq.enqueue(i)

    assert dq.first() == 1
    assert len(dq) == 14


def test_deque_deque():
    d = DequeDeque()

    assert len(d) == 0

    d.add_first(0)
    d.add_first(1)
    d.add_last(2)

    assert len(d) == 3
    assert d.first() == 1
    assert d.last() == 2

    assert d.delete_first() == 1

    d.add_first(3)

    assert d.delete_last() == 2

    for _ in range(len(d)):
        d.delete_last()

    with pytest.raises(Empty):
        d.delete_first()

    with pytest.raises(Empty):
        d.delete_last()

    with pytest.raises(Empty):
        d.first()

    with pytest.raises(Empty):
        d.last()

    assert d.is_empty()


def test_r_6_13():
    """
    Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6,
    7, 8), in this order. Suppose further that you have an initially
    empty queue Q.

    Give a code fragment that uses only D and Q (and no other variables)
    and results in D storing the elements in the order (1, 2, 3, 5, 4,
    6, 7, 8).
    """
    D = DequeDeque()
    # Initialize deque state as (1, 2, 3, 4, 5, 6, 7, 8).
    for i in range(1, 9):
        D.add_last(i)

    # Initialize empty queue.
    Q = ArrayQueue()

    Q.enqueue(D.delete_first())  # [1], (2, 3, 4, 5, 6, 7, 8)
    Q.enqueue(D.delete_first())  # [1, 2], (3, 4, 5, 6, 7, 8)
    Q.enqueue(D.delete_first())  # [1, 2, 3], (4, 5, 6, 7, 8)
    Q.enqueue(D.delete_first())  # [1, 2, 3, 4], (5, 6, 7, 8)
    Q.enqueue(D.delete_first())  # [1, 2, 3, 4, 5], (6, 7, 8)

    D.add_last(Q.dequeue())  # [2, 3, 4, 5], (6, 7, 8, 1)
    D.add_last(Q.dequeue())  # [3, 4, 5], (6, 7, 8, 1, 2)
    D.add_last(Q.dequeue())  # [4, 5], (6, 7, 8, 1, 2, 3)

    D.add_first(Q.dequeue())  # [5], (4, 6, 7, 8, 1, 2, 3)
    D.add_first(Q.dequeue())  # [], (5, 4, 6, 7, 8, 1, 2, 3)

    Q.enqueue(D.delete_last())  # [3], (5, 4, 6, 7, 8, 1, 2)
    D.add_first(Q.dequeue())  # [], (3, 5, 4, 6, 7, 8, 1, 2)

    Q.enqueue(D.delete_last())  # [2], (3, 5, 4, 6, 7, 8, 1)
    D.add_first(Q.dequeue())  # [], (2, 3, 5, 4, 6, 7, 8, 1)

    Q.enqueue(D.delete_last())  # [1], (2, 3, 5, 4, 6, 7, 8)
    D.add_first(Q.dequeue())  # [], (1, 2, 3, 5, 4, 6, 7, 8)

    assert Q.is_empty()
    assert [D.delete_first() for _ in range(len(D))] == [1, 2, 3, 5, 4, 6, 7, 8]


def test_r_6_14():
    """
    Repeat the previous problem using the deque D and an initially empty
    stack S.
    """
    D = DequeDeque()
    # Initialize deque state as (1, 2, 3, 4, 5, 6, 7, 8).
    for i in range(1, 9):
        D.add_last(i)

    # Initialize empty stack.
    S = ArrayStack()

    S.push(D.delete_first())  # [1], (2, 3, 4, 5, 6, 7, 8)
    S.push(D.delete_first())  # [1, 2], (3, 4, 5, 6, 7, 8)
    S.push(D.delete_first())  # [1, 2, 3], (4, 5, 6, 7, 8)
    S.push(D.delete_first())  # [1, 2, 3, 4], (5, 6, 7, 8)
    S.push(D.delete_first())  # [1, 2, 3, 4, 5], (6, 7, 8)

    D.add_last(S.pop())  # [1, 2, 3, 4], (6, 7, 8, 5)
    D.add_first(S.pop())  # [1, 2, 3], (4, 6, 7, 8, 5)

    S.push(D.delete_last())  # [1, 2, 3, 5], (4, 6, 7, 8)
    D.add_first(S.pop())  # [1, 2, 3], (5, 4, 6, 7, 8)
    D.add_first(S.pop())  # [1, 2], (3, 5, 4, 6, 7, 8)
    D.add_first(S.pop())  # [1], (2, 3, 5, 4, 6, 7, 8)
    D.add_first(S.pop())  # [], (1, 2, 3, 5, 4, 6, 7, 8)

    assert S.is_empty()
    assert [D.delete_first() for _ in range(len(D))] == [1, 2, 3, 5, 4, 6, 7, 8]
