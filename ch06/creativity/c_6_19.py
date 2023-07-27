from ch06.array_stack import ArrayStack


def is_matched_html(raw: str) -> bool:
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1 : k]
        tag = tag.split()[0]  # I added this.
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return S.is_empty()
