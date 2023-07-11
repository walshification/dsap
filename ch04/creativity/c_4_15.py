"""
Write a recursive function that will output all the subsets of a set of
_n_ elements (without repeating any subsets).
"""
from typing import List, Set


def puzzle_solve(k: int, sequence: List[str], U: Set[str]) -> List[str]:
    """
    Algorithm PuzzleSolve(k, S, U):
        Input: An integer k, sequence S, and set U
        Output: An enumeration of all k-length extensions to S using elements in U
            without repetitions.

        for each e in U do
            Add e to the end of S
            Remove e from U
            if k == 1 then
                Test whether S is a configuration that solves the puzzle
                If S solves the puzzle then
                    return "Solution found: " S
            else
                PuzzleSolve(k - 1, S, U)
            Remove e from the end of S
            Add e back to U
    """
    answers = []
    universe = U.copy()  # Avoid altering the set during iteration. O(n) unfortunately.
    for element in U:
        sequence.append(element)
        universe.remove(element)

        if k == 1:
            answers.append("".join(sequence))
        else:
            answers += puzzle_solve(k - 1, sequence, universe)

        universe.add(sequence.pop())

    return answers
