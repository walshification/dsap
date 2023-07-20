"""
The constructor for the CaesarCipher class in Code Fragment 5.11 can be
implemented with a two-line body by building the forward and backward
strings using a combination of the join method and an appropriate
comprehension syntax. Give such an implementation.
"""
from ch05.caesar_cipher import CaesarCipher


class RefactoredCaesarCipher(CaesarCipher):
    def __init__(self, shift):
        self._forward = "".join(chr((k + shift) % 26 + ord("A")) for k in range(26))
        self._backward = "".join(chr((k - shift) % 26 + ord("A")) for k in range(26))
