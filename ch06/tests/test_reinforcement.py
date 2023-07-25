from ch06.array_stack import ArrayStack
from ch06.reinforcement import transfer


def test_transfer():
    S = ArrayStack()
    for i in range(10):
        S.push(i)

    T = ArrayStack()

    transfer(S, T)

    assert len(S) == 0
    assert T._data == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
