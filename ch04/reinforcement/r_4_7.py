"""
Describe a recursive function for converting a string of digits into the
integer it represents. For example, "13531" represents the integer
13,531.
"""


def cast_to_int(digits: str, index: int = 0) -> int:
    length = len(digits)
    if length == 1:
        return int(digits)

    return int(digits[index]) * 10 ** (length - index - 1) + cast_to_int(
        digits, index + 1
    )
