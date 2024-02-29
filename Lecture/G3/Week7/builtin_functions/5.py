# built-in functions

# filter()

nums = list(range(1, 51))

nums_even = list(filter(lambda x : x % 2 == 0, nums))

print(nums_even)
