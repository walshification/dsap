"""
Use the techniques of Section 1.7 to revise the charge and make_payment
methods of the CreditCard class to ensure that the caller sends a
number as a parameter.
"""
from ch02.src.credit_card import CreditCard


class CarefulCreditCard(CreditCard):
    """A credit card that cares about its data types."""

    def charge(self, price: float) -> bool:
        """Charge given price to card, assuming sufficient limit.

        Raise TypeError if price is the wrong type.

        Return True if charge was processed; otherwise, False.
        """
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number")

        if price + self._balance > self._limit:
            # Charge exceeds limit. Can't accept it.
            return False
        else:
            self._balance += price
            return True
