def square_digits(num):
    output = ""
    for n in str(abs(num)):
        output += str(int(n) ** 2)
    return int(output)

# Pythonic Way:
def square_digit(num):
    return int("".join(str(int(n) ** 2) for n in str(abs(num))))

print(square_digit(-2345))
