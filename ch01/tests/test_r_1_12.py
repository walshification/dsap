from ch01.reinforcement.r_1_12 import my_choice


def test_my_choice():
    seq = [5, 10, 32, 89, 4, 72]
    # Use the seed key for predictable results.
    assert [89, 10, 5, 10, 10, 4] == [my_choice(seq, seed_key=n) for n in range(6)]
