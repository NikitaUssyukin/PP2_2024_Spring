# Lambda Functions

def power(n):
    return lambda a : a ** n

square = power(2) # lambda a : a ** 2
cube = power(3) # lambda a : a ** 3

a = int(input())
b = int(input())

print(square(a))
print(cube(b))

