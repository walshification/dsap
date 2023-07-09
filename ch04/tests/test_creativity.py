import pytest

from ch04.creativity import min_max


@pytest.mark.parametrize(
    ("sequence", "result"),
    (
        ((1, 9), (1, 9)),
        ((9, 1), (1, 9)),
        ((2, 4, 17, -6, 9, 1), (-6, 17)),
    ),
)
def test_min_max(sequence, result):
    assert min_max(sequence) == result
