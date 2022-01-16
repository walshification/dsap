from ch01.reinforcement.r_1_3 import minmax


def test_minmax():
    assert minmax([3, 4, 5, 6, 7]) == (3, 7)
    assert minmax([7, 6, 5, 4, 3]) == (3, 7)
    assert minmax([4, 5, 7, 3, 6]) == (3, 7)
    assert minmax([3]) == (3, 3)
