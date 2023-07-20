import pytest

from ch05.caesar_cipher import CaesarCipher
from ch05.dynamic_array import DynamicArray
from ch05.reinforcement import (
    BetterDynamicArray,
    EfficientInsertDynamicArray,
    RefactoredCaesarCipher,
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


def test_caesar_cipher_new_init_works():
    shift = 3
    old_cipher = CaesarCipher(shift)
    new_cipher = RefactoredCaesarCipher(shift)

    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    old_coded = old_cipher.encrypt(message)
    new_coded = new_cipher.encrypt(message)

    assert old_coded == new_coded
    assert old_coded != message

    old_decoded = old_cipher.decrypt(old_coded)
    new_decoded = new_cipher.decrypt(new_coded)

    assert old_decoded == new_decoded == message
