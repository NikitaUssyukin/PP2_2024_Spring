# Lambda functions
def power(n):
    return lambda a : a ** n

square = power(2)

cube = power(3)

print(square(5))
print(cube(4))