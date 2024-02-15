def myRange(start, stop):
    while start < stop:
        yield str(start)
        start += 1

nums = list(myRange(1, 20))

print(', '.join(nums))