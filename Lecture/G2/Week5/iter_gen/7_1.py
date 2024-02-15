def square_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

for square in square_sequence(1, 10):
    print(square, end=' ')