from ch05.reinforcement import BetterDynamicArray, determine_size_memory_increases


def test_determine_size_memory_increases():
    assert determine_size_memory_increases() == [0, 4, 8, 16, 24]


def test_better_dynamic_array_supports_negative_indices():
    dynamic_array = BetterDynamicArray()
    for i in range(5):
        dynamic_array.append(i)

    assert all(
        dynamic_array[i] == dynamic_array[j]
        for i, j in zip(range(5), range(-5, 0))
    )
