from random import shuffle

import pytest

from ch06.array_stack import ArrayStack
from ch06.creativity import (
    ConstrainedArrayStack,
    generate_subsets,
    is_matched_html,
    pick_largest,
)
from ch06.exceptions import Empty, Full


def test_pick_largest():
    n_tests = 1000
    correct = []
    numbers = [1, 2, 3]
    for _ in range(n_tests):
        shuffle(numbers)
        S = ArrayStack()
        for i in numbers:
            S.push(i)

        largest = pick_largest(S)
        if largest == 3:
            correct.append(1)

    # Probability of correctness should be at least ~66.6%.
    assert 66 > sum(correct) / n_tests < 67


def test_c_6_16():
    """
    Modify the ArrayStack implementation so that the stack's capacity is
    limited to maxlen elements, where maxlen is an optional parameter to
    the constructor (that defaults to None). If push is called when the
    stack is at full capacity, throw a Full exception (defined similarly
    to Empty).
    """
    S = ArrayStack(maxlen=0)

    with pytest.raises(Full) as e:
        S.push(None)

    assert e.value.args[0] == ConstrainedArrayStack.ErrorMessages.FULL.value


def test_contrained_array_stack():
    # Behaves like a normal stack.
    S = ConstrainedArrayStack()
    assert S.is_empty()

    with pytest.raises(Empty):
        S.top()

    for i in range(3):
        S.push(i)

    assert S.top() == 2
    assert S.pop() == 2
    assert len(S) == 2
    assert not S.is_empty()

    # Adds new contrained functionality.
    S = ConstrainedArrayStack(maxlen=1)
    S.push(1)

    with pytest.raises(Full):
        S.push(2)


@pytest.mark.parametrize(
    ["html", "expected_result"],
    (
        ("<body><p>Hello, World</p></body>", True),
        ("<body><p>Hello, World</></body>", False),
        ("<body><p style='whatever' blah='sure ok'>Hello, World</p></body>", True),
    ),
)
def test_is_matched_html(html, expected_result):
    assert is_matched_html(html) == expected_result


@pytest.mark.parametrize(
    ["initial_set", "expected_subsets"],
    (
        (
            {1, 2, 3},
            {
                frozenset(),
                frozenset({1}),
                frozenset({2}),
                frozenset({3}),
                frozenset({1, 2}),
                frozenset({1, 3}),
                frozenset({2, 3}),
                frozenset({1, 2, 3}),
            },
        ),
    ),
)
def test_generate_subsets(initial_set, expected_subsets):
    assert generate_subsets(initial_set) == expected_subsets
