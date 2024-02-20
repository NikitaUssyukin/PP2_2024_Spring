def myRange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

nums = list(myRange(5))

print(nums)
