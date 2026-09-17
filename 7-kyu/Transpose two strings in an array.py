# Beginer version

def transpose_two_strings(arr):
    max_len = max(map(len, arr))

    letter_container = {}

    for item in arr:
        equal_item = (item + " " * (max_len - len(item)))
        for index, letter in enumerate(equal_item):
            if index not in letter_container.keys():
                letter_container.setdefault(index, letter)
            else:
                letter_container[index] = letter_container.get(index, "") + " " + letter

    return "\n".join(letter_container.values())


test_arr = ["Hello", "World"]

p = ["I", "Love", "Python", "as", "Language"]

print(transpose_two_strings(p))

# print(max(test_arr, key=len))

# Pro version

def transpose_strings(strings):
    max_length = max(map(len, strings))

    padded = (s.ljust(max_length) for s in strings)

    return "\n".join(" ".join(row) for row in zip(*padded))


print(transpose_strings(p))
