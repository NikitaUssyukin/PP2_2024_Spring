# built-in functions

# filter()

from math import sqrt

nums = list(range(1, 51))

def is_prime(x):
    if(x == 1):
        return False
    root = round(sqrt(x))
    for i in range(2, root + 1):
        if x % i == 0:
            return False
    return True

nums_prime = list(filter(is_prime, nums))

print(nums_prime)
