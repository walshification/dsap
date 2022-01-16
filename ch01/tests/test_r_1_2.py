from ch01.reinforcement.r_1_2 import is_even


def test_is_even():
    assert is_even(17) is False
    assert is_even(36) is True
