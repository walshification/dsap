import pytest

from ch05.dynamic_array import DynamicArray
from ch05.reinforcement import (
    BetterDynamicArray,
    EfficientInsertDynamicArray,
    determine_size_memory_increases,
)


def test_determine_size_memory_increases():
    assert determine_size_memory_increases() == [0, 4, 8, 16, 24]


def test_better_dynamic_array_supports_negative_indices():
    dynamic_array = BetterDynamicArray()
    for i in range(5):
        dynamic_array.append(i)

    assert all(
        dynamic_array[i] == dynamic_array[j] for i, j in zip(range(5), range(-5, 0))
    )


@pytest.mark.parametrize("initial_size", (5, 7))
def test_efficient_insert_dynamic_array_allows_correct_insert(initial_size):
    efficient_array = EfficientInsertDynamicArray()
    inefficient_array = DynamicArray()
    for i in range(initial_size):
        efficient_array.append(i)
        inefficient_array.append(i)

    test_index = 2
    test_value = 42
    efficient_array.insert(test_index, test_value)
    inefficient_array.insert(test_index, test_value)

    for i in range(initial_size + 1):
        assert efficient_array[i] == inefficient_array[i]

    assert efficient_array[test_index] == test_value
