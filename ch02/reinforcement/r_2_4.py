"""
Write a Python class, Flower, that has three instance variables of type
str, int, and float, that respectively represent the name of the
flower, its number of petals, and its price. Your class must include a
constructor method that initializes each variable to an appropriate
value, and your class should include methods for setting the value of
each type, and retrieving the value of each type.
"""


class Flower:
    """Pretty fleur."""

    def __init__(self, name: str, petal_count: int, price: float) -> None:
        """Create a new flower.

        name    the name of the species (e.g., "rose")
        petals  the number of petals
        price   the current cost in dollars (e.g., 5.0 for $5.00)
        """
        self._name = name
        self._petal_count = petal_count
        self._price = price

    def get_name(self) -> str:
        """Return the name of the flower."""
        return self._name

    def set_name(self, new_name: str) -> bool:
        """Set the flower's name.

        Return True if successful; otherwise return False.
        """
        self._name = new_name
        return self._name == new_name

    def get_petal_count(self) -> int:
        """Return the flower's number of petals."""
        return self._petal_count

    def set_petal_count(self, new_count: int) -> bool:
        """Set the flower's petal count. Cannot be negative.

        Return True if successful; otherwise return False.
        """
        if new_count >= 0:
            self._petal_count = new_count
        return self._petal_count == new_count

    def get_price(self) -> float:
        """Return the flower's price."""
        return self._price

    def set_price(self, new_price: float) -> bool:
        """Set the flower's price. Cannot be negative or zero.

        Return True if successful; otherwise return False.
        """
        if new_price > 0.0:
            self._price = new_price
        return self._price == new_price
