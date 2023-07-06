from ch04.reinforcement import puzzle_solve


def test_puzzle_solve():
    answers = puzzle_solve(3, [], {"a", "b", "c", "d"})
    expected_answers = [
        "abc",
        "abd",
        "acb",
        "acd",
        "adb",
        "adc",
        "bcd",
        "bca",
        "bdc",
        "bda",
        "bac",
        "bad",
        "cda",
        "cdb",
        "cad",
        "cab",
        "cbd",
        "cba",
        "dab",
        "dac",
        "dba",
        "dbc",
        "dca",
        "dcb",
    ]
    assert all(answer in expected_answers for answer in answers)
    assert all(expected_answer in answers for expected_answer in expected_answers)
