import pytest

from ch04.creativity import are_unique, min_max, multiply, puzzle_solve, towers_of_hanoi


@pytest.mark.parametrize(
    ("sequence", "result"),
    (
        ((1, 9), (1, 9)),
        ((9, 1), (1, 9)),
        ((2, 4, 17, -6, 9, 1), (-6, 17)),
    ),
)
def test_min_max(sequence, result):
    assert min_max(sequence) == result


@pytest.mark.parametrize(
    ("sequence", "result"),
    (
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), True),
        ((1, 0), True),
        ((1, 1), False),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 4), False),
    ),
)
def test_are_unique(sequence, result):
    assert are_unique(sequence) == result


@pytest.mark.parametrize(
    ("m", "n", "product"),
    (
        (2, 3, 6),
        (1, 0, 0),
        (0, 5, 0),
        (1, 3, 3),
        (3, 1, 3),
        (6, 12, 72),
    ),
)
def test_multiply(m, n, product):
    assert multiply(m, n) == product


def test_towers_of_hanoi():
    start, spare, destination = towers_of_hanoi(len([3, 2, 1]), [3, 2, 1], [], [])
    assert start == []
    assert spare == []
    assert destination == [3, 2, 1]


def test_puzzle_solve():
    answers = puzzle_solve(3, [], {"a", "b", "c", "d"})
    expected_answers = [
        "abc",
        "abd",
        "acb",
        "acd",
        "adb",
        "adc",
        "bcd",
        "bca",
        "bdc",
        "bda",
        "bac",
        "bad",
        "cda",
        "cdb",
        "cad",
        "cab",
        "cbd",
        "cba",
        "dab",
        "dac",
        "dba",
        "dbc",
        "dca",
        "dcb",
    ]
    assert all(answer in expected_answers for answer in answers)
    assert all(expected_answer in answers for expected_answer in expected_answers)
