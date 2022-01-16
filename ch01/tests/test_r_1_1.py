from ch01.reinforcement.r_1_1 import is_multiple


def test_is_multiple():
    assert is_multiple(10, 5) is True
    assert is_multiple(10, 3) is False
