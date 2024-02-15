def num_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start
        start += 1

print(list(num_sequence(1, 10)))