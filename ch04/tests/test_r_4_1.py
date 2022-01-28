from ch04.reinforcement import find_max


def test_find_max():
    assert find_max([0, 1, 2, 3, 4, 5], 6) == 5
    assert find_max([5, 4, 3, 2, 1, 0], 6) == 5
    assert find_max([1, 2, 3, 9, 4, 5, 6], 7) == 9
