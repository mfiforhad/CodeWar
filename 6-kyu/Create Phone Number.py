def create_phone_number(n):
    converted = [str(i) for i in n]
    area_code = "".join(converted[:3])
    mid_number = "".join(converted[3:6])
    rest_number = "".join(converted[6:])

    return f"({area_code}) {mid_number}-{rest_number}"


# more pythonic way:


def create_phn_number(num: list[int]):
    n = "".join(map(str, num))
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"


print(
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
)  # => returns "(123) 456-7890"
print(create_phn_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # => returns "(123) 456-7890"
