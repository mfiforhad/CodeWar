def multiples(a: int, b: int, limit: int) -> list[int]:
    return [num for num in range(1, limit + 1) if num % a == 0 and num % b == 0]


print(multiples(2, 4, 40))
