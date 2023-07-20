from ch05.caesar_cipher import CaesarCipher


class RefactoredCaesarCipher(CaesarCipher):
    def __init__(self, shift):
        self._forward = "".join(chr((k + shift) % 26 + ord("A")) for k in range(26))
        self._backward = "".join(chr((k - shift) % 26 + ord("A")) for k in range(26))
