def square_gen(start, stop):
    while start < stop:
        yield start ** 2 
        start += 1

square_nums = list(square_gen(1, 20))

print(square_nums)