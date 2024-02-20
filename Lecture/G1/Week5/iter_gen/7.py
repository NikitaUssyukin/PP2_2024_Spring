def SquaresRange(stop):
    start = 0
    while start < stop:
        yield start ** 2
        start += 1

nums = list(SquaresRange(5))

print(nums)
