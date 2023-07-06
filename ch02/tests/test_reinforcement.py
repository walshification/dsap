import pytest

from ch02.reinforcement import CarefulCreditCard, Flower


def test_flower_creation():
    """Flowers can be created."""
    flower = Flower("rose", 8, 5.0)
    assert flower.get_name() == "rose"
    assert flower.get_petal_count() == 8
    assert flower.get_price() == 5.0


def test_flower_updates():
    """A flower's attributes can be updated."""
    flower = Flower("violet", 10, 3.0)
    assert flower.get_name() == "violet"
    assert flower.get_petal_count() == 10
    assert flower.get_price() == 3.0


def test_careful_credit_card():
    """
    Careful credit card raises TypeError if charge is not numeric.
    """
    card = CarefulCreditCard("Bob Doobis", "Chase", "1234", 5000)
    with pytest.raises(TypeError):
        card.charge("bogus")
