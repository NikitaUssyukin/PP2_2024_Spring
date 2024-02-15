def square_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

squares = list(square_sequence(1, 10))

print(', '.join(map(str, squares)))
    