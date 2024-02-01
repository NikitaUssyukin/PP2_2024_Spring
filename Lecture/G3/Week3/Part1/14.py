def power(n):
    return lambda a : a ** n

square = power(2) # return lambda a : a ** 2

cube = power(3)

print(square(9))
print(cube(5))