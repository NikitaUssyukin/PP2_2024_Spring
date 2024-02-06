# Lambda Functions

def sum1(a, b):
    return a + b 

a = int(input())
b = int(input())

print(sum1(a, b))
print((lambda a, b : a + b)(a, b))

