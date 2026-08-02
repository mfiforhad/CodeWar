# %%


def no_repeat(string:str)-> str:
    first_letter = ''
    for letter in string:
        if string.islower() and string.count(letter) < 2:
            first_letter = letter
            break

    return first_letter


print(no_repeat("aabbccdde"))
# %%
