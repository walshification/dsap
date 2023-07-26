import pytest

from ch06.array_stack import ArrayStack
from ch06.reinforcement import DequeQueue, clear, does_match, reverse, transfer


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
