from ch01 import creativity


def test_reverse():
    assert creativity.reverse([3, 4, 5, 6]) == [6, 5, 4, 3]


def test_has_odd_product_pair():
    assert creativity.has_odd_product_pair([3, 5]) is True
    assert creativity.has_odd_product_pair([3, 2]) is False
    assert creativity.has_odd_product_pair([3, 2, 7]) is True
    assert creativity.has_odd_product_pair([3, 2, 4, 5, 6]) is True
