"""
Write a Python program that repeatedly reads lines from standard
input until an EOFError is raised, and then outputs those lines in
reverse order (a user can indicate end of input by typing ctrl-D.
"""


def reverse_read() -> None:
    """Reads lines from input until an EOFError is raised, then prints
    the lines in reverse order.
    """
    lines = []
    while True:
        try:
            lines.append(input("Enter a line (Press ctrl-D to stop): "))
        except EOFError:
            break

    print("")
    for idx in range(1, len(lines) + 1):
        print(lines[-idx])


if __name__ == "__main__":
    reverse_read()
