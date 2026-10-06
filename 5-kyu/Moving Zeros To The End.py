def move_zeros(lst):
    zeros = lst.count(0)
    non_zeros = [item for item in lst if item != 0]
    return non_zeros + [0] * zeros


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
