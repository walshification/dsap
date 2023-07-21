from collections import defaultdict
from copy import deepcopy

from ch05.creativity import (
    PoppableDynamicArray,
    SettableDynamicArray,
    remove_all,
    shuffle,
)


def test_shuffle():
    original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffled = deepcopy(original)
    shuffle(shuffled)
    assert len(original) == len(shuffled)
    assert all(element in original for element in shuffled)


def test_shuffle_distribution():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    index_to_value_map = defaultdict(list)
    n_tests = 10000
    for _ in range(n_tests):
        shuffle(sequence)
        for i in range(len(sequence)):
            index_to_value_map[i].append(sequence[i])

    # Given 10 values, each value should appear at each index ~10% of the time.
    assert all(
        9 > (counts.count(i) / n_tests * 100) < 11
        for i in range(len(index_to_value_map))
        for counts in index_to_value_map.items()
    )


def test_poppable_dynamic_array():
    array = PoppableDynamicArray()

    array.append(None)  # capacity 1
    array.append(None)  # capacity 2
    array.append(None)  # capacity 4
    array.append(None)
    array.append(None)  # capacity 8

    assert len(array) == 5
    assert array._capacity == 8

    array.pop()
    array.pop()
    array.pop()

    assert len(array) == 2
    assert array._capacity == 8

    array.pop()

    assert len(array) == 1
    assert array._capacity == 4

    array.pop()

    assert len(array) == 0
    assert array._capacity == 2


def test_remove_all():
    data = SettableDynamicArray()
    for i in [1, 2, 3, 4, 5, 1]:
        data.append(i)

    remove_all(data, 1)

    assert 1 not in data
