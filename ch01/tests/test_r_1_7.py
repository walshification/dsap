from ch01.reinforcement.r_1_7 import sum_smaller_odd_squares


def test_sum_smaller_odd_squares():
    assert sum_smaller_odd_squares(6) == 25 + 9 + 1
