def to_weird_case(words):
    removed_whitespace = words.strip()
    separated_words = removed_whitespace.split(" ")
    sentence = []
    for word in separated_words:
        case_generator = []
        for i, letter in enumerate(word):
            if i % 2 == 0:
                case_generator.append(letter.upper())
            else:
                case_generator.append(letter)
        sentence.append(("").join(case_generator))
    return (" ").join(sentence)


print(to_weird_case("Weird string case"))
