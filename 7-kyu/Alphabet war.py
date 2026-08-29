def alphabet_war(fight:str):
    # your code here
    left_words = "".join(charecter for charecter in fight if charecter in "wpbs")
    letf_table= left_words.maketrans("wpbs", "4321")
    converted_left = left_words.translate(letf_table)
    left_points =  sum([int(n) for n in converted_left])

    right_words: str = "".join(c for c in fight if c in "mqdz")
    right_tabel = fight.maketrans("mqdz", "4321")
    converted_right = right_words.translate(right_tabel)
    right_point:int = sum([int(n) for n in converted_right])

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
