def myRange(start, stop):
    while start < stop:
        yield start
        start += 1

print(set(myRange(1, 20)))

res = set()

start = 1
stop = 20

while start < stop:
    res.add(start)
    start += 1

print(res)