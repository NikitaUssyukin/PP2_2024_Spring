def SquaresRange(stop):
    start = 0
    while start < stop:
        yield str(start ** 2)
        start += 1

nums = list(SquaresRange(5))

nums_str = ', '.join(nums)

print(nums_str)