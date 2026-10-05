def high_and_low(numbers: str):
    nums = list(map(int, numbers.split()))
    numbers = f"{max(nums)} {min(nums)}"
    return numbers



print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
