from ch01 import reinforcement


def test_is_multiple():
    assert reinforcement.is_multiple(10, 5) is True
    assert reinforcement.is_multiple(10, 3) is False


def test_is_even():
    assert reinforcement.is_even(17) is False
    assert reinforcement.is_even(36) is True


def test_minmax():
    assert reinforcement.minmax([3, 4, 5, 6, 7]) == (3, 7)
    assert reinforcement.minmax([7, 6, 5, 4, 3]) == (3, 7)
    assert reinforcement.minmax([4, 5, 7, 3, 6]) == (3, 7)
    assert reinforcement.minmax([3]) == (3, 3)


def test_sum_of_small_squares():
    assert reinforcement.sum_of_smaller_squares(6) == 55


def test_sum_of_small_squares_5():
    assert reinforcement.sum_of_smaller_squares_5(6) == 55


def test_sum_smaller_odd_squares():
    assert reinforcement.sum_smaller_odd_squares(6) == 25 + 9 + 1


def test_sum_smaller_odd_squares_7():
    assert reinforcement.sum_smaller_odd_squares_7(6) == 25 + 9 + 1


def test_my_choice():
    seq = [5, 10, 32, 89, 4, 72]
    # Use the seed key for predictable results.
    assert [89, 10, 5, 10, 10, 4] == [
        reinforcement.my_choice(seq, seed_key=n) for n in range(6)
    ]
