# Lambda functions
def add1(a, b):
    return a + b

print(add1(2, 5))

# lambda parameters : expression
add2 = lambda a, b : a + b

print(add2(8, 5))

print((lambda a, b : a + b)(5, 3))

