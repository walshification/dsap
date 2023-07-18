from ch05.reinforcement import determine_size_memory_increases


def test_determine_size_memory_increases():
    assert determine_size_memory_increases() == [0, 4, 8, 16, 24]
