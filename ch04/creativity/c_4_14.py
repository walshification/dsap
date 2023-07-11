from typing import List, Tuple


def towers_of_hanoi(
    n: int, start: List[int], spare: List[int], destination: List[int]
) -> Tuple[List, List, List]:
    """
    Algorithm TowersOfHanoi(n, a, b, c):
        Input: A number of plates n of decreasing size from the bottom, a seqence
            that holds the plates, an empty sequence b as a spare tower, and an empty
            sequence c as the destination.
        Output: Empty sequences a and b and sequence c containing n integers of
            decreasing size.

        if len(a) == 0 do
            return a, b, c

        # Recursively move all but the last plate to the spare tower.
        TowersOfHanoi(n - 1, a, c, b)

        Move the bottom disk from a to the destination c.

        # Recursively complete the puzzle.
        TowersofHanoi(n - 1, b, a, c)
    """
    if n == 0:
        return start, spare, destination

    if n == 1:
        # move bottom disk to destination
        destination.append(start.pop())
        return start, spare, destination

    # Move all but last disk to spare
    start, destination, spare = towers_of_hanoi(n - 1, start, destination, spare)
    print(f"{start}\n{spare}\n{destination}\n")

    # Move target disk to destination
    destination.append(start.pop())
    print(f"{start}\n{spare}\n{destination}\n")

    # Move disks from spare to destination
    spare, start, destination = towers_of_hanoi(n - 1, spare, start, destination)
    return start, spare, destination


if __name__ == "__main__":
    original_start = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"{original_start}\n{[]}\n{[]}\n")
    start, spare, destination = towers_of_hanoi(
        len(original_start), original_start, [], []
    )
    print(f"{start}\n{spare}\n{destination}\n")
