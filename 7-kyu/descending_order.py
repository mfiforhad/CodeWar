def descending_order(num) -> int:
    """Return an integer with the digits of num sorted in descending order."""
    if num < 0:
        raise ValueError("num must be non-negative")
    return int("".join(sorted(str(num), reverse=True)))
