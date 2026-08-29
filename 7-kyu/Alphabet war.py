# initial solution
def alphabet_war(fight: str):
    # your code here
    left_words = "".join(charecter for charecter in fight if charecter in "wpbs")
    letf_table = left_words.maketrans("wpbs", "4321")
    converted_left = left_words.translate(letf_table)
    left_points = sum([int(n) for n in converted_left])

    right_words: str = "".join(c for c in fight if c in "mqdz")
    right_tabel = fight.maketrans("mqdz", "4321")
    converted_right = right_words.translate(right_tabel)
    right_point: int = sum([int(n) for n in converted_right])

    if left_points > right_point:
        return "Left side wins!"
    elif left_points < right_point:
        return "Right side wins!"
    else:
        return "Let's fight again!"


print(alphabet_war("z"))
print(alphabet_war("zdqmwpbs"))
print(alphabet_war("zzzzs"))
print(alphabet_war("wwwwwwz"))


# pro solution
def alphabet_war_2(fight: str):
    left: dict[str, int] = {"w": 4, "p": 3, "b": 2, "s": 1}
    right: dict[str, int] = {"m": 4, "q": 3, "d": 2, "z": 1}

    left_point: int = sum(left.get(c, 0) for c in fight)
    right_point: int = sum(right.get(c, 0) for c in fight)

    if left_point > right_point:
        return "Left side wins!"
    if left_point < right_point:
        return "Right side wins!"

    return "Let's fight again!"


print(alphabet_war_2("wwwwwwz"))
