# built-in functions

# all(), any()

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

nums_isprime = list(map(is_prime, nums))

print(nums_isprime)

amount_of_primes = sum(nums_isprime)

print(amount_of_primes)