from typing import Dict, Optional

from ch06.array_stack import ArrayStack


def does_match(
    expression: str,
    open_delimiters: str,
    close_delimiters: str,
    close_to_open_map: Dict[str, str],
    S: Optional[ArrayStack] = None,
) -> bool:
    """Return True if expression is properly grouped."""
    if S is None:
        S = ArrayStack()

    if not expression:
        return S.is_empty()

    character = expression[0]
    remainder = expression[1:]

    if character in open_delimiters:
        S.push(character)

    if character in close_delimiters:
        if S.is_empty():
            return False

        if close_to_open_map[character] != S.pop():
            return False

    return does_match(
        "".join(remainder),
        open_delimiters,
        close_delimiters,
        close_to_open_map,
        S,
    )
