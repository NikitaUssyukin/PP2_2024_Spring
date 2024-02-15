def myRange(start, stop):
    while start < stop:
        yield start
        start += 1

print(list(myRange(1, 20)))