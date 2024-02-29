# Built-in functions

# map()

nums = [1, 2, 3, 4, 5]

nums_doubled = list(map(lambda x : x * 2, nums))

print(str(nums_doubled))
print(', '.join(map(str, nums_doubled)))

