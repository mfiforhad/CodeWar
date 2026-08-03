"""
If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice as strong as love :-)

Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.

The input will always be made of only lowercase letters and will never be empty.
"""
# Solution: 01

import string

alphabets = [alphabet for alphabet in string.ascii_lowercase]


def words_to_marks(s):
    s_list = [letter.lower() for letter in s]
    total = 0
    for i, letter in enumerate(alphabets, start=1):
        for item in s_list:
            if item == letter:
                total += i
    return total

print(words_to_marks("love"))
print(words_to_marks("friendship"))

# Solution: 02

def total_of_words(word):
    return sum(ord(letter.lower()) - ord("a") + 1 for letter in word)


total_of_words("love")
total_of_words("friendship")
