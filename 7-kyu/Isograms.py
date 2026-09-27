def is_isogram(string) -> bool:
    return True if len(string) == len(set(string.lower())) else False



print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
