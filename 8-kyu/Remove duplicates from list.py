def distinct(seq) -> list[int]:
    return [num for num in {}.fromkeys(seq, 0).keys()]


print(distinct([1, 2, 1, 1, 3, 2]))
