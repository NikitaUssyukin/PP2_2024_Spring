# Built-in functions

# filter()

nums = range(1, 50)

nums_odd = list(filter(lambda x : x % 2 != 0, nums))

print(nums_odd)

import math

def isPrime(n):
    if n == 1:
        return False
    root = round(math.sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            return False
    return True

nums_prime = list(filter(isPrime, nums))

print(nums_prime)
