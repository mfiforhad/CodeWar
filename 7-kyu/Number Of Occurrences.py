# manual approach


def number_of_occurrence(element, sample):
    counter = 0
    for e in sample:
        if e == element:
            counter += 1
    return counter


# Built-in approach


def number_of_occurrences(element, sample):
    return sample.count(element)


# Note: This built-in approach still has a time complexity of O(N) and space complexity of O(1), but it runs significantly faster in practice.

sample = [0, 1, 2, 2, 3]
print(number_of_occurrences(0, sample))
print(number_of_occurrences(4, sample))
print(number_of_occurrences(2, sample))
print(number_of_occurrences(3, sample))
